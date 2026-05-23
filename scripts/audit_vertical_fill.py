#!/usr/bin/env python3
"""Audit whether poster card content reaches the lower part of each card.

This script is intentionally simple and layout-agnostic. Render the poster to a
PNG, pass the normalized or pixel coordinates of the three cards, and fail if
content inside any card ends too far above the bottom.
"""

from __future__ import annotations

import argparse
import json
import statistics
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

try:
    from PIL import Image
except ImportError:  # pragma: no cover - environment dependent
    print("ERROR: Pillow is required. Install with: python -m pip install pillow", file=sys.stderr)
    raise


@dataclass
class CardAudit:
    name: str
    box_px: tuple[int, int, int, int]
    content_bottom_ratio: float
    bottom_blank_ratio: float
    has_lower_half_content: bool
    passes: bool
    reason: str


def parse_card(value: str) -> tuple[str, tuple[float, float, float, float]]:
    if ":" in value:
        name, raw = value.split(":", 1)
    else:
        name, raw = f"card_{abs(hash(value))}", value
    parts = [float(item.strip()) for item in raw.split(",")]
    if len(parts) != 4:
        raise ValueError(f"Card must be name:left,top,right,bottom, got {value!r}")
    left, top, right, bottom = parts
    if right <= left or bottom <= top:
        raise ValueError(f"Invalid card coordinates: {value!r}")
    return name.strip() or "card", (left, top, right, bottom)


def to_pixels(box: tuple[float, float, float, float], width: int, height: int) -> tuple[int, int, int, int]:
    if all(0 <= item <= 1 for item in box):
        left, top, right, bottom = box
        return (
            round(left * width),
            round(top * height),
            round(right * width),
            round(bottom * height),
        )
    return tuple(round(item) for item in box)  # type: ignore[return-value]


def channel_median(pixels: list[tuple[int, int, int]]) -> tuple[int, int, int]:
    return tuple(round(statistics.median([px[idx] for px in pixels])) for idx in range(3))  # type: ignore[return-value]


def audit_card(
    image: Image.Image,
    name: str,
    box_px: tuple[int, int, int, int],
    threshold: int,
    ignore_edge: float,
    max_bottom_blank: float,
) -> CardAudit:
    left, top, right, bottom = box_px
    crop = image.crop((left, top, right, bottom)).convert("RGB")
    width, height = crop.size

    edge_x = max(2, round(width * ignore_edge))
    edge_y = max(2, round(height * ignore_edge))
    inner_left, inner_top = edge_x, edge_y
    inner_right, inner_bottom = width - edge_x, height - edge_y
    inner_width = max(1, inner_right - inner_left)
    inner_height = max(1, inner_bottom - inner_top)

    inner_pixels = [
        crop.getpixel((x, y))
        for y in range(inner_top, inner_bottom)
        for x in range(inner_left, inner_right)
    ]
    fill = channel_median(inner_pixels)

    row_threshold = max(6, round(inner_width * 0.0015))
    content_rows: list[int] = []
    lower_half_rows = 0
    for y in range(inner_top, inner_bottom):
        row_hits = 0
        for x in range(inner_left, inner_right):
            px = crop.getpixel((x, y))
            diff = max(abs(px[idx] - fill[idx]) for idx in range(3))
            if diff >= threshold:
                row_hits += 1
        if row_hits >= row_threshold:
            y_rel = y - inner_top
            content_rows.append(y_rel)
            if y_rel >= inner_height * 0.5:
                lower_half_rows += 1

    if not content_rows:
        return CardAudit(
            name=name,
            box_px=box_px,
            content_bottom_ratio=0.0,
            bottom_blank_ratio=1.0,
            has_lower_half_content=False,
            passes=False,
            reason="no content detected inside card",
        )

    content_bottom_ratio = max(content_rows) / max(1, inner_height - 1)
    bottom_blank_ratio = 1.0 - content_bottom_ratio
    has_lower_half_content = lower_half_rows >= max(4, round(inner_height * 0.01))
    passes = bottom_blank_ratio <= max_bottom_blank and has_lower_half_content

    reasons: list[str] = []
    if bottom_blank_ratio > max_bottom_blank:
        reasons.append(
            f"bottom blank {bottom_blank_ratio:.3f} exceeds threshold {max_bottom_blank:.3f}"
        )
    if not has_lower_half_content:
        reasons.append("no substantive lower-half content detected")
    return CardAudit(
        name=name,
        box_px=box_px,
        content_bottom_ratio=round(content_bottom_ratio, 4),
        bottom_blank_ratio=round(bottom_blank_ratio, 4),
        has_lower_half_content=has_lower_half_content,
        passes=passes,
        reason="; ".join(reasons) if reasons else "ok",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit vertical fill of poster cards.")
    parser.add_argument("image", help="Rendered poster PNG path.")
    parser.add_argument(
        "--card",
        action="append",
        required=True,
        help="Card box as name:left,top,right,bottom. Coordinates may be normalized 0-1 or pixels.",
    )
    parser.add_argument(
        "--threshold",
        type=int,
        default=18,
        help="RGB max-channel distance from estimated card fill color to count as content.",
    )
    parser.add_argument(
        "--ignore-edge",
        type=float,
        default=0.025,
        help="Ignore this fraction of each card edge to avoid borders/shadows.",
    )
    parser.add_argument(
        "--max-bottom-blank",
        type=float,
        default=0.06,
        help="Maximum allowed blank fraction below final detected content.",
    )
    args = parser.parse_args()

    image_path = Path(args.image)
    image = Image.open(image_path).convert("RGB")
    width, height = image.size

    audits: list[CardAudit] = []
    for raw_card in args.card:
        name, box = parse_card(raw_card)
        box_px = to_pixels(box, width, height)
        audits.append(
            audit_card(
                image=image,
                name=name,
                box_px=box_px,
                threshold=args.threshold,
                ignore_edge=args.ignore_edge,
                max_bottom_blank=args.max_bottom_blank,
            )
        )

    payload = {
        "image": str(image_path),
        "image_size": [width, height],
        "max_bottom_blank": args.max_bottom_blank,
        "passes": all(item.passes for item in audits),
        "cards": [asdict(item) for item in audits],
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["passes"] else 2


if __name__ == "__main__":
    raise SystemExit(main())

