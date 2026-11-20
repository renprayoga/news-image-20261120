#!/usr/bin/env python3
"""Render entry.png (1024x1024) for news-image-20261120.

Deterministic one-page newspaper front page summing up Friday
20 November 2026: the ICJ Rohingya genocide verdict (hero), Trump
holding off new Iran strikes, Cyclone Akvan hitting Odisha, and
GTA 6 passing $1.8 billion in launch-week sales, plus an ALSO strip.

Only Pillow is used. No network, no randomness, no timestamps:
the same code always produces the same bytes.
"""

import os

from PIL import Image, ImageDraw, ImageFont

W = 1024
H = 1024
MARGIN = 36

# Palette (fixed constants).
PAPER = (251, 247, 238)      # warm newsprint
INK = (17, 24, 39)           # near-black
NAVY = (22, 50, 79)          # hero panel
NAVY_DARK = (14, 34, 56)
GOLD = (232, 184, 75)        # hero accent
RED = (185, 28, 28)          # kicker red
GREY = (90, 96, 110)         # footer grey
ROW_TINT_1 = (253, 230, 222)  # pale red tint
ROW_TINT_2 = (219, 234, 254)  # pale blue tint
ROW_TINT_3 = (237, 233, 254)  # pale violet tint
WHITE = (255, 255, 255)
SOFT = (226, 232, 240)       # light subtext on navy

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_BOLD = font("DejaVuSerif-Bold.ttf", 62)
SANS_BOLD = font("DejaVuSans-Bold.ttf", 26)
SANS = font("DejaVuSans.ttf", 23)
SANS_SM = font("DejaVuSans.ttf", 21)
SANS_BOLD_SM = font("DejaVuSans-Bold.ttf", 19)
SANS_BOLD_XS = font("DejaVuSans-Bold.ttf", 17)
SANS_BOLD_MD = font("DejaVuSans-Bold.ttf", 29)
SANS_BOLD_LG = font("DejaVuSans-Bold.ttf", 56)
KICKER = font("DejaVuSans-Bold.ttf", 22)
KICKER_SM = font("DejaVuSans-Bold.ttf", 17)
FOOTER = font("DejaVuSans.ttf", 15)
ALSO_FONT = font("DejaVuSans.ttf", 20)
ALSO_BOLD = font("DejaVuSans-Bold.ttf", 20)


def wrap(draw, text, fnt, max_width):
    """Greedy word wrap; returns a list of lines that fit max_width."""
    lines = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        cur = words[0]
        for word in words[1:]:
            trial = cur + " " + word
            if draw.textlength(trial, font=fnt) <= max_width:
                cur = trial
            else:
                lines.append(cur)
                cur = word
        lines.append(cur)
    return lines


def draw_centered(draw, cx, y, text, fnt, fill):
    draw.text((cx - draw.textlength(text, font=fnt) / 2, y), text,
              font=fnt, fill=fill)


def draw_scales(draw, cx, top, size, beam_color, pan_color):
    """Geometric scales of justice, drawn from primitives."""
    half = size // 2
    base_y = top + size
    # Base.
    draw.polygon([(cx - 70, base_y), (cx + 70, base_y),
                  (cx + 52, base_y - 22), (cx - 52, base_y - 22)],
                 fill=beam_color)
    # Pillar.
    draw.rectangle([cx - 7, top + 34, cx + 7, base_y - 22], fill=beam_color)
    # Finial.
    draw.ellipse([cx - 12, top + 8, cx + 12, top + 32], fill=pan_color)
    # Crossbeam.
    draw.rectangle([cx - half, top + 34, cx + half, top + 46], fill=beam_color)
    # Beam end knobs.
    draw.ellipse([cx - half - 8, top + 30, cx - half + 8, top + 50],
                 fill=pan_color)
    draw.ellipse([cx + half - 8, top + 30, cx + half + 8, top + 50],
                 fill=pan_color)
    # Hanging pans.
    for sx in (cx - half, cx + half):
        draw.line([(sx, top + 46), (sx - 34, top + 118)], fill=pan_color,
                  width=3)
        draw.line([(sx, top + 46), (sx + 34, top + 118)], fill=pan_color,
                  width=3)
        draw.line([(sx, top + 46), (sx, top + 118)], fill=pan_color, width=3)
        draw.pieslice([sx - 42, top + 112, sx + 42, top + 176], 0, 180,
                      fill=pan_color)
        draw.line([(sx - 42, top + 118), (sx + 42, top + 118)],
                  fill=pan_color, width=3)


def draw_hourglass(draw, box, color, sand):
    """Geometric hourglass: a decision delayed."""
    x0, y0, x1, y1 = box
    cx = (x0 + x1) // 2
    w = (x1 - x0) // 2 - 14
    # Frame bars.
    draw.rectangle([x0 + 8, y0 + 4, x1 - 8, y0 + 12], fill=color)
    draw.rectangle([x0 + 8, y1 - 12, x1 - 8, y1 - 4], fill=color)
    # Glass: two triangles meeting in the middle.
    draw.polygon([(cx - w, y0 + 14), (cx + w, y0 + 14), (cx, (y0 + y1) // 2)],
                 outline=color, width=4)
    draw.polygon([(cx - w, y1 - 14), (cx + w, y1 - 14), (cx, (y0 + y1) // 2)],
                 outline=color, width=4)
    # Sand in the lower half.
    my = (y0 + y1) // 2
    draw.polygon([(cx - w + 10, y1 - 18), (cx + w - 10, y1 - 18),
                  (cx, my + 8)], fill=sand)


def draw_cyclone(draw, box, color):
    """Geometric cyclone: concentric broken arcs spiralling inward."""
    x0, y0, x1, y1 = box
    cx = (x0 + x1) // 2
    cy = (y0 + y1) // 2
    for i, r in enumerate((44, 34, 24, 14)):
        start = 20 + i * 55
        draw.arc([cx - r, cy - r, cx + r, cy + r], start, start + 250,
                 fill=color, width=6)
    draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=color)


def draw_controller(draw, box, color, accent):
    """Geometric game controller."""
    x0, y0, x1, y1 = box
    # Body.
    draw.rounded_rectangle([x0 + 6, y0 + 26, x1 - 6, y1 - 22], radius=18,
                           fill=color)
    # Grips.
    draw.ellipse([x0 + 2, y1 - 44, x0 + 30, y1 - 8], fill=color)
    draw.ellipse([x1 - 30, y1 - 44, x1 - 2, y1 - 8], fill=color)
    # D-pad (left).
    px = x0 + 30
    py = (y0 + y1) // 2 - 4
    draw.rectangle([px - 5, py - 16, px + 5, py + 16], fill=accent)
    draw.rectangle([px - 16, py - 5, px + 16, py + 5], fill=accent)
    # Buttons (right).
    bx = x1 - 32
    by = (y0 + y1) // 2 - 4
    for dx, dy in ((0, -12), (12, 0), (0, 12), (-12, 0)):
        draw.ellipse([bx + dx - 6, by + dy - 6, bx + dx + 6, by + dy + 6],
                     fill=accent)


def draw_row(draw, y, height, tint, icon_fn, kicker, headline, sub):
    """One news row: tinted icon square + kicker + headline + subtext."""
    # Icon square.
    draw.rounded_rectangle([MARGIN, y, MARGIN + 104, y + height], radius=10,
                           fill=tint)
    icon_fn(draw, (MARGIN + 8, y + 4, MARGIN + 96, y + height - 4))
    # Text column.
    tx = MARGIN + 124
    tw = W - MARGIN - tx
    draw.text((tx, y + 6), kicker, font=KICKER_SM, fill=RED)
    draw.text((tx, y + 28), headline, font=SANS_BOLD_MD, fill=INK)
    lines = wrap(draw, sub, SANS_SM, tw)
    ly = y + 66
    for line in lines[:2]:
        draw.text((tx, ly), line, font=SANS_SM, fill=(51, 65, 85))
        ly += 26


def render():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # ---- Masthead -----------------------------------------------------
    draw_centered(draw, W // 2, 26, "THE WORLD IN ONE IMAGE", SERIF_BOLD, INK)
    draw.rectangle([MARGIN, 108, W - MARGIN, 112], fill=RED)
    draw.rectangle([MARGIN, 116, W - MARGIN, 118], fill=INK)

    # ---- Date bar ------------------------------------------------------
    draw.rectangle([MARGIN, 128, W - MARGIN, 168], fill=INK)
    draw_centered(draw, W // 2, 136, "FRIDAY  20  NOVEMBER  2026",
                  SANS_BOLD, WHITE)

    # ---- Hero panel: ICJ Rohingya genocide verdict --------------------
    hy0, hy1 = 182, 548
    draw.rectangle([MARGIN, hy0, W - MARGIN, hy1], fill=NAVY)
    draw.rectangle([MARGIN, hy0, W - MARGIN, hy0 + 6], fill=GOLD)
    # Scales icon on the left.
    draw_scales(draw, 185, 230, 190, (214, 226, 240), GOLD)
    # Text on the right.
    tx = 330
    draw.text((tx, 202), "THE HAGUE  —  WORLD COURT", font=KICKER, fill=GOLD)
    headline = ["MYANMAR GUILTY", "OF ROHINGYA", "GENOCIDE"]
    hy = 234
    for line in headline:
        draw.text((tx, hy), line, font=SANS_BOLD_LG, fill=WHITE)
        hy += 62
    sub = ("The International Court of Justice rules 9–6 — the first "
           "genocide verdict against a state in its 80-year history. "
           "Reparations ordered; a report due within two years.")
    lines = wrap(draw, sub, SANS, W - MARGIN - tx)
    ly = 428
    for line in lines[:3]:
        draw.text((tx, ly), line, font=SANS, fill=SOFT)
        ly += 29
    # Fact chips (measured to fit the 658 px text column at 17 px).
    draw.text((tx, 516), "9–6 VOTE   •   ~10,000 KILLED IN 2017   •   CASE "
              "BY THE GAMBIA", font=SANS_BOLD_XS, fill=GOLD)

    # ---- Three story rows ----------------------------------------------
    rows = [
        (562, ROW_TINT_1,
         lambda d, b: draw_hourglass(d, b, RED, GOLD),
         "WASHINGTON  —  IRAN",
         "TRUMP: NO NEW IRAN STRIKES BEFORE 2027",
         "From Air Force One after his China trip: “I am not rushing into "
         "any decision.” Israel is pressing for new strikes; the decision "
         "is pushed to next year."),
        (680, ROW_TINT_2,
         lambda d, b: draw_cyclone(d, b, NAVY),
         "INDIA  —  CYCLONE AKVAN",
         "CYCLONE AKVAN HITS ODISHA TODAY",
         "Severe storm makes landfall near Gopalpur with winds of "
         "90–100 km/h. 105,304 people evacuated to 1,224 shelters; red "
         "alert in 11 districts."),
        (798, ROW_TINT_3,
         lambda d, b: draw_controller(d, b, NAVY, GOLD),
         "ENTERTAINMENT  —  GAMES",
         "GTA 6 SALES PASS $1.8 BILLION",
         "Launch-week sales top $1.80bn — passing the global box office "
         "of The Odyssey. Out worldwide on 19 November for PS5 and Xbox."),
    ]
    for y, tint, icon_fn, kicker, headline, sub in rows:
        draw_row(draw, y, 108, tint, icon_fn, kicker, headline, sub)

    # ---- ALSO strip ------------------------------------------------------
    ay0, ay1 = 922, 978
    draw.rectangle([MARGIN, ay0, W - MARGIN, ay1], fill=NAVY_DARK)
    also = ("ALSO:  Houthi strike hits Riyadh, damaging the Saudi PIF "
            "tower  •  Russian strikes damage embassies in Kyiv  •  "
            "Europe ready to talk to Russia on ending the Ukraine war")
    lines = wrap(draw, also, ALSO_FONT, W - 2 * MARGIN - 20)
    ly = ay0 + 6
    for line in lines[:2]:
        draw.text((MARGIN + 10, ly), line, font=ALSO_FONT, fill=WHITE)
        ly += 24

    # ---- Footer ----------------------------------------------------------
    draw_centered(draw, W // 2, 990,
                  "Sources: CNN  •  Le Monde  •  Reuters  •  Axios  •  IMD  "
                  "•  The Hindu  •  BBC",
                  FOOTER, GREY)
    return img


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, "entry.png")
    img = render()
    img.save(out, format="PNG")
    print("wrote", out, img.size)


if __name__ == "__main__":
    main()
