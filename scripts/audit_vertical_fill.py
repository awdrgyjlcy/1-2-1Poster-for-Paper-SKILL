#!/usr/bin/env python3
"""Audit whether poster card content reaches and balances across cards.

This script is intentionally simple and layout-agnostic. Render the poster to a
PNG, pass the normalized or pixel coordinates of the three cards, and fail if
content inside any card ends too far above the bottom or if card content stacks
have visibly different vertical spans. With three cards it also checks that
inter-card gutters stay narrow and close to the sample-like spacing.
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
    content_top_ratio: float
    content_bottom_ratio: float
    content_span_ratio: float
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
            content_top_ratio=0.0,
            content_bottom_ratio=0.0,
            content_span_ratio=0.0,
            bottom_blank_ratio=1.0,
            has_lower_half_content=False,
            passes=False,
            reason="no content detected inside card",
        )

    content_top_ratio = min(content_rows) / max(1, inner_height - 1)
    content_bottom_ratio = max(content_rows) / max(1, inner_height - 1)
    content_span_ratio = content_bottom_ratio - content_top_ratio
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
        content_top_ratio=round(content_top_ratio, 4),
        content_bottom_ratio=round(content_bottom_ratio, 4),
        content_span_ratio=round(content_span_ratio, 4),
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
    parser.add_argument(
        "--max-content-bottom-spread",
        type=float,
        default=0.04,
        help="Maximum allowed spread between card content-bottom ratios.",
    )
    parser.add_argument(
        "--max-content-span-spread",
        type=float,
        default=0.08,
        help="Maximum allowed spread between card content-span ratios.",
    )
    parser.add_argument(
        "--min-content-span",
        type=float,
        default=0.82,
        help="Minimum allowed content span ratio for each card.",
    )
    parser.add_argument(
        "--min-gutter-ratio",
        type=float,
        default=0.008,
        help="Minimum allowed inter-card gutter as a fraction of image width.",
    )
    parser.add_argument(
        "--max-gutter-ratio",
        type=float,
        default=0.025,
        help="Maximum allowed inter-card gutter as a fraction of image width.",
    )
    parser.add_argument(
        "--max-gutter-spread",
        type=float,
        default=0.006,
        help="Maximum allowed difference between the two inter-card gutters.",
    )
    parser.add_argument(
        "--max-side-width-spread",
        type=float,
        default=0.008,
        help="Maximum allowed difference between left and right card widths.",
    )
    parser.add_argument(
        "--max-center-ratio-error",
        type=float,
        default=0.015,
        help="Maximum allowed error for center_width / average_side_width from 2.0.",
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

    bottom_values = [item.content_bottom_ratio for item in audits]
    span_values = [item.content_span_ratio for item in audits]
    content_bottom_spread = max(bottom_values) - min(bottom_values)
    content_span_spread = max(span_values) - min(span_values)
    min_content_span = min(span_values)

    balance_reasons: list[str] = []
    if content_bottom_spread > args.max_content_bottom_spread:
        balance_reasons.append(
            f"content bottom spread {content_bottom_spread:.3f} exceeds threshold "
            f"{args.max_content_bottom_spread:.3f}"
        )
    if content_span_spread > args.max_content_span_spread:
        balance_reasons.append(
            f"content span spread {content_span_spread:.3f} exceeds threshold "
            f"{args.max_content_span_spread:.3f}"
        )
    if min_content_span < args.min_content_span:
        balance_reasons.append(
            f"minimum content span {min_content_span:.3f} below threshold {args.min_content_span:.3f}"
        )
    balance_passes = not balance_reasons

    geometry = {"passes": True, "reason": "not checked; expected exactly three cards"}
    sorted_boxes = sorted([item.box_px for item in audits], key=lambda box: box[0])
    if len(sorted_boxes) == 3:
        left_box, center_box, right_box = sorted_boxes
        left_width = (left_box[2] - left_box[0]) / width
        center_width = (center_box[2] - center_box[0]) / width
        right_width = (right_box[2] - right_box[0]) / width
        left_gutter = (center_box[0] - left_box[2]) / width
        right_gutter = (right_box[0] - center_box[2]) / width
        gutter_spread = abs(left_gutter - right_gutter)
        side_width_spread = abs(left_width - right_width)
        average_side_width = (left_width + right_width) / 2
        center_to_side_ratio = center_width / average_side_width if average_side_width else 0.0
        center_ratio_error = abs(center_to_side_ratio - 2.0)

        geometry_reasons: list[str] = []
        if side_width_spread > args.max_side_width_spread:
            geometry_reasons.append(
                f"side width spread {side_width_spread:.3f} exceeds threshold "
                f"{args.max_side_width_spread:.3f}"
            )
        if center_ratio_error > args.max_center_ratio_error:
            geometry_reasons.append(
                f"center/side ratio error {center_ratio_error:.3f} exceeds threshold "
                f"{args.max_center_ratio_error:.3f}"
            )
        for label, value in (("left gutter", left_gutter), ("right gutter", right_gutter)):
            if value < args.min_gutter_ratio:
                geometry_reasons.append(
                    f"{label} {value:.3f} below threshold {args.min_gutter_ratio:.3f}"
                )
            if value > args.max_gutter_ratio:
                geometry_reasons.append(
                    f"{label} {value:.3f} exceeds threshold {args.max_gutter_ratio:.3f}"
                )
        if gutter_spread > args.max_gutter_spread:
            geometry_reasons.append(
                f"gutter spread {gutter_spread:.3f} exceeds threshold {args.max_gutter_spread:.3f}"
            )

        geometry_passes = not geometry_reasons
        geometry = {
            "left_width_ratio": round(left_width, 4),
            "center_width_ratio": round(center_width, 4),
            "right_width_ratio": round(right_width, 4),
            "center_to_side_ratio": round(center_to_side_ratio, 4),
            "side_width_spread": round(side_width_spread, 4),
            "center_ratio_error": round(center_ratio_error, 4),
            "left_gutter_ratio": round(left_gutter, 4),
            "right_gutter_ratio": round(right_gutter, 4),
            "gutter_spread": round(gutter_spread, 4),
            "min_gutter_ratio": args.min_gutter_ratio,
            "max_gutter_ratio": args.max_gutter_ratio,
            "max_gutter_spread": args.max_gutter_spread,
            "max_side_width_spread": args.max_side_width_spread,
            "max_center_ratio_error": args.max_center_ratio_error,
            "passes": geometry_passes,
            "reason": "; ".join(geometry_reasons) if geometry_reasons else "ok",
        }

    payload = {
        "image": str(image_path),
        "image_size": [width, height],
        "max_bottom_blank": args.max_bottom_blank,
        "max_content_bottom_spread": args.max_content_bottom_spread,
        "max_content_span_spread": args.max_content_span_spread,
        "min_content_span": args.min_content_span,
        "passes": all(item.passes for item in audits) and balance_passes and geometry["passes"],
        "balance": {
            "content_bottom_spread": round(content_bottom_spread, 4),
            "content_span_spread": round(content_span_spread, 4),
            "min_content_span": round(min_content_span, 4),
            "passes": balance_passes,
            "reason": "; ".join(balance_reasons) if balance_reasons else "ok",
        },
        "geometry": geometry,
        "cards": [asdict(item) for item in audits],
    }
    print(json.dumps(payload, indent=2))
    return 0 if payload["passes"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
