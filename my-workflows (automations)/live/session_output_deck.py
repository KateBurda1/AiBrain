"""
Generates the branded "Session Output" PPTX (Title / Decisions / Outcomes / Next Steps)
used by the session-output skill (my-skills/session-output/instructions.md).

Two brands: "kbco" (Kate Burda & Company, light) and "ignite" (dark). Values sourced from
my-business (context)/brand-standards.md and ignite-brand-standards.md.

Usage: import build_deck and call it once per session. See the bottom of this file for
the backfill calls (S1, S2, S3B-i) run to produce the first three decks.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
import copy

BRANDS = {
    "kbco": {
        "bg": "FFFFFF",
        "ink": "2E2925",       # warm near-black (brand-standards.md)
        "accent": "D51067",    # PMS 214 pink
        "accent2": "B52372",   # PMS 675 magenta
        "muted": "55575A",     # PMS 425 grey
        "card": "F7EEF2",      # very light pink tint for card backgrounds
        "on_accent": "FFFFFF",
        "font": "Calibri",
        "font_title": "Times New Roman",
        "logo": "/Users/kate/Library/CloudStorage/OneDrive-turningpointglobal.net/My-AI-Brain/My AI Brain/my-files (knowledge)/Brand/Kate & Co- Administrative/1. Kate Burda & Co. - Logo Package/PNG/kb_Logo_2.FullColor_Horizontal.png",
        "logo_width": Inches(2.4),
    },
    "ignite": {
        "bg": "1C1112",        # ink / near-black, measured from live logo files
        "ink": "F1F2F2",       # off-white
        "accent": "FF8983",    # pink on dark backgrounds (measured)
        "accent2": "ED536F",   # brand pink (primary)
        "muted": "C9A9AC",     # dimmed warm grey for secondary text on dark bg
        "card": "2A1B1C",      # slightly lighter than bg, for card fills
        "on_accent": "1C1112",
        "font": "Calibri",
        "font_title": "Calibri",
        "logo": "/Users/kate/Library/CloudStorage/OneDrive-turningpointglobal.net/Ignite/Brand-Marketing/logos and colors/IgniteLogo_Emblem-DarkBG.png",
        "logo_width": Inches(0.9),
    },
}

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)


def _rgb(hexstr):
    return RGBColor.from_string(hexstr)


def _set_background(slide, hexstr):
    bg = slide.background
    bg.fill.solid()
    bg.fill.fore_color.rgb = _rgb(hexstr)


def _no_line(shape):
    shape.line.fill.background()


def _textbox(slide, left, top, width, height, anchor=MSO_ANCHOR.TOP):
    tb = slide.shapes.add_textbox(left, top, width, height)
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = 0
    tf.margin_right = 0
    tf.margin_top = 0
    tf.margin_bottom = 0
    return tb, tf


def _add_para(tf, text, size, color, bold=False, italic=False, font="Calibri",
              align=PP_ALIGN.LEFT, space_after=6, first=False, bullet=False):
    p = tf.paragraphs[0] if first and not tf.paragraphs[0].runs else tf.add_paragraph()
    p.alignment = align
    p.space_after = Pt(space_after)
    run = p.add_run()
    run.text = ("•  " + text) if bullet else text
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.name = font
    run.font.color.rgb = _rgb(color)
    return p


def _header(slide, brand, kicker, title):
    b = BRANDS[brand]
    _, tf = _textbox(slide, Inches(0.7), Inches(0.45), Inches(11.9), Inches(0.5))
    _add_para(tf, kicker.upper(), 12, b["accent"], bold=True, font=b["font"], first=True)
    _, tf2 = _textbox(slide, Inches(0.7), Inches(0.85), Inches(11.9), Inches(0.8))
    _add_para(tf2, title, 30, b["ink"], bold=True, font=b["font_title"], first=True)


def _card(slide, left, top, width, height, brand):
    b = BRANDS[brand]
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shp.adjustments[0] = 0.04
    shp.fill.solid()
    shp.fill.fore_color.rgb = _rgb(b["card"])
    _no_line(shp)
    shp.shadow.inherit = False
    return shp


def _title_slide(prs, brand, session_num, session_title, date, attendees):
    b = BRANDS[brand]
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_background(slide, b["bg"])

    try:
        logo_right_margin = Inches(0.7)
        logo_top = Inches(0.35)
        logo_left = Emu(SLIDE_W - logo_right_margin - b["logo_width"])
        slide.shapes.add_picture(b["logo"], logo_left, logo_top, width=b["logo_width"])
    except Exception:
        pass

    _, tf = _textbox(slide, Inches(0.9), Inches(2.5), Inches(11.5), Inches(0.5))
    _add_para(tf, f"SESSION {session_num}", 16, b["accent"], bold=True, font=b["font"], first=True)

    _, tf2 = _textbox(slide, Inches(0.9), Inches(3.0), Inches(11.5), Inches(1.6))
    _add_para(tf2, session_title, 44, b["ink"], bold=True, font=b["font_title"], first=True)

    _, tf3 = _textbox(slide, Inches(0.9), Inches(4.9), Inches(11.5), Inches(0.5))
    _add_para(tf3, date, 16, b["muted"], font=b["font"], first=True)

    _, tf4 = _textbox(slide, Inches(0.9), Inches(5.3), Inches(11.5), Inches(0.5))
    _add_para(tf4, "Attendees: " + attendees, 14, b["muted"], font=b["font"], first=True)

    _, tf5 = _textbox(slide, Inches(0.9), Inches(6.9), Inches(11.5), Inches(0.4))
    _add_para(tf5, "Advisory & Ignite — Session Output", 11, b["muted"], italic=True, font=b["font"], first=True)
    return slide


def _bullet_slide(prs, brand, kicker, title, items):
    b = BRANDS[brand]
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_background(slide, b["bg"])
    _header(slide, brand, kicker, title)

    card = _card(slide, Inches(0.7), Inches(1.6), Inches(11.9), Inches(5.3), brand)
    _, tf = _textbox(slide, Inches(1.1), Inches(1.95), Inches(11.1), Inches(4.7))
    for i, item in enumerate(items):
        _add_para(tf, item, 16, b["ink"], font=b["font"], bullet=True,
                   space_after=12, first=(i == 0))
    return slide


def _next_steps_slide(prs, brand, this_week, later):
    b = BRANDS[brand]
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    _set_background(slide, b["bg"])
    _header(slide, brand, "Next Steps", "What needs to happen")

    col_w = Inches(5.75)
    gap = Inches(0.4)
    left1 = Inches(0.7)
    left2 = Emu(left1 + col_w + gap)
    top = Inches(1.6)
    height = Inches(5.3)

    _card(slide, left1, top, col_w, height, brand)
    _, tfh = _textbox(slide, Emu(left1 + Inches(0.35)), Emu(top + Inches(0.3)), Emu(col_w - Inches(0.7)), Inches(0.5))
    _add_para(tfh, "THIS WEEK  ·  → Weekly Compass", 13, b["accent"], bold=True, font=b["font"], first=True)
    _, tf1 = _textbox(slide, Emu(left1 + Inches(0.35)), Emu(top + Inches(0.85)), Emu(col_w - Inches(0.7)), Emu(height - Inches(1.2)))
    if this_week:
        for i, (item, owner) in enumerate(this_week):
            _add_para(tf1, f"{item}  —  {owner}", 14, b["ink"], font=b["font"], bullet=True,
                       space_after=10, first=(i == 0))
    else:
        _add_para(tf1, "Nothing new this week.", 14, b["muted"], italic=True, font=b["font"], first=True)

    _card(slide, left2, top, col_w, height, brand)
    _, tfh2 = _textbox(slide, Emu(left2 + Inches(0.35)), Emu(top + Inches(0.3)), Emu(col_w - Inches(0.7)), Inches(0.5))
    _add_para(tfh2, "LATER  ·  → Master Plan backlog", 13, b["accent"], bold=True, font=b["font"], first=True)
    _, tf2 = _textbox(slide, Emu(left2 + Inches(0.35)), Emu(top + Inches(0.85)), Emu(col_w - Inches(0.7)), Emu(height - Inches(1.2)))
    if later:
        for i, (item, owner) in enumerate(later):
            _add_para(tf2, f"{item}  —  {owner}", 14, b["ink"], font=b["font"], bullet=True,
                       space_after=10, first=(i == 0))
    else:
        _add_para(tf2, "Nothing outstanding beyond this week.", 14, b["muted"], italic=True, font=b["font"], first=True)

    return slide


def build_deck(brand, session_num, session_title, date, attendees,
                decisions, outcomes, this_week, later, out_path):
    assert brand in BRANDS
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H

    _title_slide(prs, brand, session_num, session_title, date, attendees)
    _bullet_slide(prs, brand, "Decisions", "What was decided", decisions)
    _bullet_slide(prs, brand, "Outcomes", "What this session produced", outcomes)
    _next_steps_slide(prs, brand, this_week, later)

    prs.save(out_path)
    return out_path
