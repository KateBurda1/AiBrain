from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from PIL import Image
import os, sys

S = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(S, "img")
CROP = os.path.join(S, "crop"); os.makedirs(CROP, exist_ok=True)
OUT = sys.argv[1]

COPPER = RGBColor(0x96, 0x6A, 0x4D)
GREEN = RGBColor(0x34, 0x3B, 0x36)
GRAY = RGBColor(0x5B, 0x52, 0x55)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
BLACK = RGBColor(0, 0, 0)
HEAD = "Avenir"          # brand: Avenir/Calibri in place of Brother 1816
BODY = "Times New Roman"  # brand: Times New Roman in place of Calluna

prs = Presentation()
prs.slide_width, prs.slide_height = Inches(13.333), Inches(7.5)
W, H = 13.333, 7.5
BLANK = prs.slide_layouts[6]

def f(n):
    for x in os.listdir(IMG):
        if x.startswith(n + "_"): return os.path.join(IMG, x)
    raise KeyError(n)

def crop(n, w, h, focus=0.5):
    src = f(n); im = Image.open(src).convert("RGB")
    iw, ih = im.size; tr = w / h
    if iw / ih > tr:
        nw = int(ih * tr); x0 = int((iw - nw) * focus); box = (x0, 0, x0 + nw, ih)
    else:
        nh = int(iw / tr); y0 = int((ih - nh) * focus); box = (0, y0, iw, y0 + nh)
    p = os.path.join(CROP, f"{n}_{w:.2f}x{h:.2f}_{focus}.jpg")
    im.crop(box).save(p, quality=88)
    return p

def pic(s, n, x, y, w, h, focus=0.5):
    return s.shapes.add_picture(crop(n, w, h, focus), Inches(x), Inches(y), Inches(w), Inches(h))

def rect(s, x, y, w, h, color, alpha=None, line=False):
    r = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h))
    r.fill.solid(); r.fill.fore_color.rgb = color
    if not line: r.line.fill.background()
    r.shadow.inherit = False
    if alpha is not None:
        sf = r.fill._xPr.find(qn("a:solidFill"))[0]
        a = sf.makeelement(qn("a:alpha"), {"val": str(int(alpha * 100000))}); sf.append(a)
    return r

def text(s, x, y, w, h, runs, size=14, color=GRAY, font=BODY, bold=False, align=PP_ALIGN.LEFT,
         anchor=MSO_ANCHOR.TOP, spacing=None, italic=False, space_after=0, line_spacing=None):
    """runs: str or list of paragraphs; each paragraph a str or dict overriding style."""
    tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = anchor
    paras = runs if isinstance(runs, list) else [runs]
    for i, p in enumerate(paras):
        d = p if isinstance(p, dict) else {"t": p}
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = d.get("align", align)
        para.space_after = Pt(d.get("after", space_after))
        if d.get("ls", line_spacing): para.line_spacing = d.get("ls", line_spacing)
        r = para.add_run(); r.text = d["t"]
        fo = r.font; fo.size = Pt(d.get("size", size)); fo.name = d.get("font", font)
        fo.bold = d.get("bold", bold); fo.italic = d.get("italic", italic)
        fo.color.rgb = d.get("color", color)
        sp = d.get("spacing", spacing)
        if sp is not None:
            r._r.get_or_add_rPr().set("spc", str(int(sp * 100)))
    return tb

def logo(s, x, y, w, which="logo_horiz_white.png"):
    s.shapes.add_picture(os.path.join(S, which), Inches(x), Inches(y), Inches(w))

def notes(s, t): s.notes_slide.notes_text_frame.text = t

def eyebrow(s, x, y, t, color=COPPER, w=6):
    text(s, x, y, w, 0.3, t.upper(), size=11, color=color, font=HEAD, bold=True, spacing=3)

def footer(s, n, dark=False, x=0.6):
    c = WHITE if dark else GRAY
    text(s, x, 7.05, 6, 0.25, "FLYING HORSE RESORT & CLUB  |  INNOSPEC CHARITY GOLF TOURNAMENT 2027",
         size=8, color=c, font=HEAD, spacing=1.5)
    text(s, W - 1.6, 7.05, 1.0, 0.25, str(n), size=8, color=c, font=HEAD, align=PP_ALIGN.RIGHT)

page = [1]
def new(dark=False, bg=None):
    s = prs.slides.add_slide(BLANK)
    if bg is not None: rect(s, 0, 0, W, H, bg)
    page[0] += 1
    return s

def divider(num, label, title, sub, img, focus=0.5):
    s = new()
    pic(s, img, 0, 0, W, H, focus)
    rect(s, 0, 0, W, H, BLACK, alpha=0.42)
    rect(s, 0.8, 2.45, 0.08, 2.9, COPPER)
    text(s, 1.1, 2.4, 9, 0.4, f"{num}  |  {label.upper()}", size=13, color=WHITE, font=HEAD, bold=True, spacing=4)
    text(s, 1.1, 2.8, 9.5, 1.8, title, size=42, color=WHITE, font=HEAD, bold=True, line_spacing=0.95)
    text(s, 1.1, 4.75, 10, 0.6, sub, size=18, color=WHITE, font=BODY, italic=True)
    logo(s, W - 3.2, 6.55, 2.5)
    return s

def split(img, title, eyebrow_t, body, left=True, focus=0.5, price=None, n=None):
    """Photo on one half, copy on the other."""
    s = new(bg=WHITE)
    px = 0 if left else W / 2
    pic(s, img, px, 0, W / 2, H, focus)
    tx = W / 2 + 0.7 if left else 0.7
    eyebrow(s, tx, 0.85, eyebrow_t)
    text(s, tx, 1.2, W / 2 - 1.4, 1.3, title, size=30, color=GREEN, font=HEAD, bold=True, line_spacing=0.95)
    rect(s, tx, 2.55, 0.9, 0.05, COPPER)
    text(s, tx, 2.85, W / 2 - 1.4, 3.3, body, size=14, color=GRAY, space_after=8, line_spacing=1.1)
    if price:
        rect(s, tx, 5.75, W / 2 - 1.4, 0.95, COPPER)
        text(s, tx + 0.3, 5.75, W / 2 - 2.0, 0.95, price, size=16, color=WHITE, font=HEAD, bold=True,
             anchor=MSO_ANCHOR.MIDDLE)
    footer(s, page[0], x=tx)
    return s

# ---------------------------------------------------------------- 1 COVER
s = prs.slides.add_slide(BLANK)
pic(s, "062", 0, 0, W, H, 0.5)
rect(s, 0, 0, W, H, BLACK, alpha=0.38)
rect(s, 0, 4.35, W, 3.15, GREEN, alpha=0.82)
logo(s, 0.8, 0.7, 3.6)
text(s, 0.8, 4.65, 11.5, 0.4, "A PROPOSAL FOR INNOSPEC FUEL SPECIALTIES", size=13, color=WHITE, font=HEAD, bold=True, spacing=4)
text(s, 0.8, 5.05, 11.5, 1.0, "A Weekend Worthy of Our Heroes", size=44, color=WHITE, font=HEAD, bold=True)
text(s, 0.8, 5.95, 11.5, 0.5, "2027 Charity Golf Tournament benefiting the PenFed Foundation Military Heroes Program",
     size=17, color=WHITE, italic=True)
text(s, 0.8, 6.5, 11.5, 0.4, "SUNDAY, AUGUST 15 + MONDAY, AUGUST 16, 2027   |   COLORADO SPRINGS, COLORADO",
     size=11, color=RGBColor(0xE8, 0xD9, 0xCC), font=HEAD, spacing=2.5)
notes(s, "Anchor dates: Sunday Aug 15 resort buyout + Monday Aug 16 tournament (Mack's Aug 16 Monday option). "
         "Alternate Mondays (Aug 2, 9, 23) shown on the Golf slide.")

# ---------------------------------------------------------------- 2 WE CREATE CONNECTION
s = new(bg=WHITE)
BAND = RGBColor(0xE9, 0xE2, 0xDC); PANEL = RGBColor(0xF7, 0xF3, 0xEF)
eyebrow(s, 0.6, 0.45, "What we heard")
text(s, 0.6, 0.72, 7.5, 0.7, "We Create Connection", size=34, color=GREEN, font=HEAD, bold=True)
text(s, 6.6, 0.55, 6.15, 1.0, [
    {"t": "Where Belonging & Connection Meet", "size": 17, "bold": True, "color": COPPER, "font": HEAD, "after": 3},
    {"t": "For the heroes you serve, the sponsors who give, and the guests who join them.", "size": 12, "italic": True, "color": GRAY}],
     align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
rect(s, 0, 1.6, W, 5.35, BAND)
heads = ["WHAT YOU WANT...", "WHAT YOU GET...", "SO YOU CAN..."]
cols = [
    ["Honor the military heroes you play for, with 95% of every dollar reaching service members and families",
     "An invitation your sponsors are proud to accept",
     "A weekend spouses and guests enjoy as much as the golfers",
     "Raise the most you can, flawlessly, with a choice your board can stand behind"],
    ["A course that looks out on the U.S. Air Force Academy, in a city with five military installations",
     "The Gazette's Best Golf Course in Colorado Springs three years running, in a AAA Four Diamond resort",
     "The Spa, pools, tennis and pickleball, four restaurants and Colorado Springs next door",
     "A full buyout, one team for golf, rooms and food, and a drive-in location"],
    ["Put the mission in view on every hole, so sponsors feel who they are playing for",
     "Deepen relationships over a round and a fireside evening, and make next year's yes easy",
     "Send every guest home with a story and a reason to come back",
     "Spend less on travel and raise more for heroes"],
]
x0, cwid, gap = 0.35, 4.1, 0.12
for c in range(3):
    x = x0 + c * (cwid + gap)
    shp = s.shapes.add_shape(MSO_SHAPE.PENTAGON if c == 0 else MSO_SHAPE.CHEVRON, Inches(x), Inches(1.75), Inches(cwid + 0.25), Inches(0.62))
    shp.fill.solid(); shp.fill.fore_color.rgb = COPPER if c != 1 else GREEN
    shp.line.color.rgb = BAND; shp.line.width = Pt(2.5); shp.shadow.inherit = False
    if c > 0: shp.adjustments[0] = 0.35
    else: shp.adjustments[0] = 0.35
    text(s, x + (0.3 if c == 0 else 0.45), 1.75, cwid - 0.4, 0.62, heads[c], size=18, color=WHITE, font=HEAD, bold=True,
         anchor=MSO_ANCHOR.MIDDLE, spacing=1)
    pnl = s.shapes.add_shape(MSO_SHAPE.ROUND_2_DIAG_RECTANGLE, Inches(x + 0.1), Inches(2.5), Inches(cwid - 0.15), Inches(4.3))
    pnl.fill.solid(); pnl.fill.fore_color.rgb = PANEL; pnl.line.fill.background(); pnl.shadow.inherit = False
    pnl.adjustments[0] = 0.16; pnl.adjustments[1] = 0.0
    for r, t in enumerate(cols[c]):
        y = 2.72 + r * 1.0
        rect(s, x + 0.35, y + 0.12, 0.09, 0.09, COPPER if c != 1 else GREEN)
        text(s, x + 0.6, y, cwid - 0.85, 0.95, t, size=12.5, color=GREEN if c == 2 else GRAY, font=HEAD,
             bold=(c == 2), line_spacing=1.0)
footer(s, page[0])
notes(s, "Built on the KB&Co 'What you want / What you get / So you can' construct, in Flying Horse colors. "
         "Each row lines up across: 1 veterans (the cause), 2 sponsors (Innospec's customers and suppliers), 3 spouses and guests, 4 Innospec as host. "
         "95% figure is Innospec CEO Patrick Williams' quote on innospecsustainability.com.")

# ---------------------------------------------------------------- 3 WHY HERE (USAFA / MILITARY)
s = new(bg=GREEN)
pic(s, "140", 0, 0, 5.6, H, 0.5)
eyebrow(s, 6.3, 0.8, "Why Flying Horse", color=RGBColor(0xD9, 0xB8, 0x9C))
text(s, 6.3, 1.15, 6.4, 1.4, "Home turf for the heroes you play for", size=32, color=WHITE, font=HEAD, bold=True, line_spacing=0.95)
rect(s, 6.3, 2.6, 0.9, 0.05, COPPER)
text(s, 6.3, 2.9, 6.3, 2.2, [
    "For 18 years, Innospec's tournaments have raised more than $2.68 million for the PenFed Foundation Military Heroes Program. "
    "The setting should honor that.",
    "Our Weiskopf Course looks out over the United States Air Force Academy, and Colorado Springs is home to five military "
    "installations. Your sponsors tee off in the heart of one of America's proudest military communities."],
    size=14, color=WHITE, space_after=10, line_spacing=1.1)
stats = [("15 MIN", "to the U.S. Air Force\nAcademy (approx.)"), ("5", "military installations\nin Colorado Springs"),
         ("102", "rooms, all yours\nin a full buyout")]
for i, (big, small) in enumerate(stats):
    x = 6.3 + i * 2.2
    rect(s, x, 5.35, 2.0, 1.35, COPPER)
    text(s, x, 5.45, 2.0, 0.6, big, size=26, color=WHITE, font=HEAD, bold=True, align=PP_ALIGN.CENTER)
    text(s, x + 0.1, 6.02, 1.8, 0.6, small, size=10.5, color=WHITE, font=HEAD, align=PP_ALIGN.CENTER)
footer(s, page[0], dark=True, x=6.3)
notes(s, "Five installations: Fort Carson, Peterson SFB, Schriever SFB, Cheyenne Mountain SFS, USAFA. "
         "Drive time to USAFA is approximate. $2.68M / 18 years from innospecsustainability.com.")

# ---------------------------------------------------------------- 3 WEEKEND AT A GLANCE
s = new(bg=WHITE)
eyebrow(s, 0.8, 0.7, "The Weekend at a Glance")
text(s, 0.8, 1.05, 11.5, 0.8, "Arrive Sunday. Play Monday. Leave inspired.", size=32, color=GREEN, font=HEAD, bold=True)
rect(s, 0.8, 1.9, 0.9, 0.05, COPPER)
cols = [
    ("SATURDAY, AUG 14", "Early Arrivals", "042", ["Optional guestroom pickup for early arrivals", "Dinner at The Steakhouse", "Sunset on a private balcony"], "093"),
    ("SUNDAY, AUG 15", "The Resort Is Yours", "", ["Full Lodge buyout for sponsors and spouses", "Afternoon at The Spa, pool and Athletic Club",
                                                    "Welcome reception with Pikes Peak views"], "121"),
    ("MONDAY, AUG 16", "Tournament Day", "", ["Breakfast and warm-up on the practice range", "Charity tournament on the Weiskopf Course",
                                                "Lunch and awards, then safe travels home"], "030"),
]
for i, (day, head, _, items, img) in enumerate(cols):
    x = 0.8 + i * 4.0
    pic(s, img, x, 2.3, 3.7, 2.1, 0.5)
    text(s, x, 4.6, 3.7, 0.3, day, size=11, color=COPPER, font=HEAD, bold=True, spacing=2.5)
    text(s, x, 4.9, 3.7, 0.5, head, size=20, color=GREEN, font=HEAD, bold=True)
    text(s, x, 5.45, 3.7, 1.5, ["•  " + t for t in items], size=13, color=GRAY, space_after=4)
footer(s, page[0])
notes(s, "Saturday pickup per Sarah's email. Itinerary is a suggested flow; final timing set with Innospec.")

# ---------------------------------------------------------------- GOLF
divider("01", "The Golf", "Championship golf, framed by Pikes Peak", "Where the legend of Flying Horse was born", "001", 0.5)

split("030", "The Weiskopf Course", "Your tournament course", [
    "Designed by legendary architect Tom Weiskopf, our Club Course has hosted golfers from around the world since 2005.",
    "•  Voted Best Golf Course in Colorado Springs by The Gazette, 2024, 2025 and 2026",
    "•  Picture-perfect views of Pikes Peak and the U.S. Air Force Academy",
    "•  A links feel with a signature 16-17-18 finish that makes or breaks a round",
    "•  Certified Audubon Cooperative Sanctuary, so expect Colorado wildlife"],
    left=True, focus=0.5)

s = new(bg=WHITE)
pic(s, "018", W / 2, 0, W / 2, H / 2, 0.5)
pic(s, "111", W / 2, H / 2, W / 2, H / 2, 0.4)
eyebrow(s, 0.7, 0.85, "Tournament day + golf pricing")
text(s, 0.7, 1.2, 5.3, 1.2, "Run by our PGA team, start to finish", size=30, color=GREEN, font=HEAD, bold=True, line_spacing=0.95)
rect(s, 0.7, 2.55, 0.9, 0.05, COPPER)
text(s, 0.7, 2.85, 5.3, 2.0, [
    "Head Golf Professional Mack Borowicz, PGA, and our team handle the details. Your sponsors simply play.",
    "•  Shotgun start; range opens 90 minutes before",
    "•  Fields of 72 to 120 golfers, more with added carts",
    "•  Scoring and hole contests set up by our team"],
    size=14, color=GRAY, space_after=7, line_spacing=1.1)
rect(s, 0.7, 5.0, 5.3, 1.1, COPPER)
text(s, 1.0, 5.0, 2.3, 1.1, "$130", size=40, color=WHITE, font=HEAD, bold=True, anchor=MSO_ANCHOR.MIDDLE)
text(s, 2.9, 5.0, 3.0, 1.1, "per golfer, including green fees,\ncart and practice range", size=13, color=WHITE, font=HEAD, anchor=MSO_ANCHOR.MIDDLE)
text(s, 0.7, 6.25, 5.3, 0.6, [{"t": "AVAILABLE MONDAYS", "size": 10, "bold": True, "color": COPPER, "font": HEAD, "spacing": 2},
                              {"t": "August 2   •   August 9   •   August 16   •   August 23", "size": 13, "color": GREEN, "font": HEAD, "bold": True}])
footer(s, page[0])
notes(s, "$130 per golfer per Mack's email, for any of the August Mondays listed. "
         "Per the 2026 Golf Events Packet: rate includes green fees, cart fees, practice range, inclusive of RSF. Min 72 players, max 120 with cart fleet "
         "(more needs 45 days' notice for rental carts, cost split 50/50). Lunch for all players required; $750 Golf Shop retail minimum; "
         "scoring/hole contest setup $100 per day. Innospec's page says 'hundreds of golfers' across events: confirm their field size.")

# ---------------------------------------------------------------- RESORT
divider("02", "The Resort", "A AAA Four Diamond resort, all to yourselves", "Tuscan warmth meets the Rocky Mountains", "023", 0.5)

split("150", "Your own private resort", "The Lodge at Flying Horse", [
    "Small enough to know your story. Big enough to deliver your vision. With a full buyout, all 102 rooms, suites and villas belong to your sponsors and their guests.",
    "•  AAA Four Diamond designation",
    "•  Every guestroom is 500+ square feet with a private balcony or patio",
    "•  Views of the golf course or the Front Range",
    "•  Oversized showers, Nespresso and work desks in every room"],
    left=False, focus=0.5)

# Room rates
s = new(bg=WHITE)
pic(s, "109", 0, 0, 4.6, H / 2, 0.5)
pic(s, "134", 0, H / 2, 4.6, H / 2, 0.5)
eyebrow(s, 5.3, 0.7, "Accommodations + group rates")
text(s, 5.3, 1.05, 7.5, 0.7, "Rooms, suites and villas", size=30, color=GREEN, font=HEAD, bold=True)
rect(s, 5.3, 1.8, 0.9, 0.05, COPPER)
rows = [("Room type", "Size", "Sleeps", "Rate / night"),
        ("King or Double Queen", "500+ sq ft", "2 or 4", "$340"),
        ("Academy Suite", "700 sq ft", "2", "$390"),
        ("Deluxe Suite", "725 sq ft", "2", "$440"),
        ("Executive Suite", "930 sq ft", "2", "$490"),
        ("Presidential Suite", "1,114 sq ft", "2", "$640"),
        ("Tuscan Villa, one bedroom", "1,650 sq ft villa", "2", "$640"),
        ("Tuscan Villa, two bedroom", "1,650 sq ft villa", "4", "$1,080")]
tx, ty, cw = 5.3, 2.1, [3.0, 1.7, 1.2, 1.5]
rh = 0.46
for r, row in enumerate(rows):
    y = ty + r * rh
    if r == 0: rect(s, tx, y, sum(cw), rh, GREEN)
    elif r % 2 == 0: rect(s, tx, y, sum(cw), rh, RGBColor(0xF4, 0xEE, 0xE9))
    cx = tx
    for c, val in enumerate(row):
        hdr = r == 0
        text(s, cx + 0.15, y, cw[c] - 0.2, rh, val, size=11 if hdr else 13,
             color=WHITE if hdr else (COPPER if c == 3 else GRAY), font=HEAD, bold=hdr or c == 3,
             anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.RIGHT if c == 3 else PP_ALIGN.LEFT, spacing=1 if hdr else None)
        cx += cw[c]
text(s, 5.3, 5.9, 7.5, 0.9, [
    {"t": "A significantly reduced group rate for your buyout, per room, per night.", "italic": True, "size": 13, "color": GREEN},
    {"t": "Rates do not include the $35 nightly resort amenity fee, 2.95% retail sales fee, or state and city occupancy taxes (currently 10.2% combined). "
          "Final room block and counts will be confirmed in your formal agreement.", "size": 10.5}], size=11, color=GRAY, space_after=4)
footer(s, page[0], x=5.3)
notes(s, "Rates from Sarah Leach's email. Villa sizes: each villa 1,650 sq ft with two king bedrooms; booked as one- or two-bedroom. "
         "Open question from Sarah: master billing or individual?")

# ---------------------------------------------------------------- EXPERIENCE
divider("03", "The Experience", "Something for every guest, golfer or not", "Spa, club and resort life for sponsors and spouses", "028", 0.4)

s = new(bg=WHITE)
pic(s, "098", 0, 0, W / 2, H, 0.5)
tx = W / 2 + 0.6; tw = W / 2 - 1.2
eyebrow(s, tx, 0.6, "While the golfers play")
text(s, tx, 0.95, tw, 0.7, "The Spa at Flying Horse", size=30, color=GREEN, font=HEAD, bold=True)
rect(s, tx, 1.7, 0.9, 0.05, COPPER)
text(s, tx, 1.9, tw, 0.9, "Spouses and guests trade the fairway for a serene haven of renewal. Every service includes access to the whirlpool and steam room.",
     size=13.5, color=GRAY, line_spacing=1.08)
menu = [("Flying Horse Signature Experience", "80 / 100 min", "$230 / $285"),
        ("Serenity Massage", "50 / 80 min", "$155 / $210"),
        ("Signature Facial", "50 / 80 min", "$155 / $210"),
        ("Couples Celebration Package", "110 min, per couple", "$560"),
        ("A Taste of The Spa", "mini spa day", "$270"),
        ("Head to Toe", "massage, facial, mani, pedi", "$450"),
        ("Ultimate Spa Day", "the full indulgence", "$615")]
rect(s, tx, 2.95, tw, 0.42, COPPER)
text(s, tx + 0.2, 2.95, tw - 0.4, 0.42, "SPA MENU  |  GUEST RATES", size=10.5, color=WHITE, font=HEAD, bold=True, spacing=2, anchor=MSO_ANCHOR.MIDDLE)
for k, (nm, d, pr) in enumerate(menu):
    y = 3.42 + k * 0.45
    if k % 2 == 1: rect(s, tx, y, tw, 0.45, RGBColor(0xF4, 0xEE, 0xE9))
    text(s, tx + 0.2, y, 3.3, 0.45, [{"t": nm, "size": 12.5, "bold": True, "color": GREEN}], font=HEAD, anchor=MSO_ANCHOR.MIDDLE)
    text(s, tx + 3.45, y, 1.75, 0.45, d, size=10, color=GRAY, font=HEAD, italic=True, anchor=MSO_ANCHOR.MIDDLE)
    text(s, tx + tw - 1.45, y, 1.25, 0.45, pr, size=12.5, color=COPPER, font=HEAD, bold=True, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.RIGHT)
text(s, tx, 6.62, tw, 0.35, "Per person unless noted. Gratuity not included; 2.95% retail sales fee applies. Private spa mornings can be arranged for your group.",
     size=9.5, color=GRAY, italic=True)
footer(s, page[0], x=tx)
notes(s, "Guest rates from the Spa Booklet dated 1 June 2026 (flyinghorseresort.com/s/Spa-Booklet-1JUN2026-WEB.pdf). "
         "Confirm 2027 rates and any group spa pricing with the Spa team (719-487-2614).")

s = new(bg=WHITE)
eyebrow(s, 0.8, 0.7, "Resort life")
text(s, 0.8, 1.05, 11.5, 0.8, "The Athletic Club and beyond", size=32, color=GREEN, font=HEAD, bold=True)
rect(s, 0.8, 1.9, 0.9, 0.05, COPPER)
tiles = [("124", "Pools + Hot Tubs", "Heated 25-yard lap pool, indoor and outdoor hot tubs, plus the seasonal adult pool in August."),
         ("101", "Tennis + Pickleball", "8 tennis courts, including 4 indoor red clay courts, and 4 pickleball courts with pro-led clinics."),
         ("055", "The Clubhouse", "A European-style clubhouse with fireside lounges, The Steakhouse and sweeping mountain views."),
         ("103", "Fitness + Wellness", "Mountain-view fitness center with group fitness and Pilates classes for guests.")]
for i, (img, h, b) in enumerate(tiles):
    x = 0.8 + i * 3.0
    pic(s, img, x, 2.3, 2.75, 2.3, 0.5)
    text(s, x, 4.8, 2.75, 0.45, h, size=17, color=GREEN, font=HEAD, bold=True)
    text(s, x, 5.25, 2.75, 1.5, b, size=12.5, color=GRAY, line_spacing=1.05)
footer(s, page[0])
notes(s, 
         "Amenity access for buyout guests and any fees to confirm with Sarah.")

# ---------------------------------------------------------------- FOOD
divider("04", "The Food", "World-class dining, steps from your room", "From a welcome toast to the awards lunch", "017", 0.5)

s = new(bg=WHITE)
eyebrow(s, 0.8, 0.7, "Dining at Flying Horse")
text(s, 0.8, 1.05, 11.5, 0.8, "Four ways to feed a winning weekend", size=32, color=GREEN, font=HEAD, bold=True)
rect(s, 0.8, 1.9, 0.9, 0.05, COPPER)
tiles = [("020", "The Steakhouse", "Award-winning prime steaks in a Tuscan-style villa. Wine Spectator Best of Award of Excellence since 2023, with a three-story wine tower."),
         ("169", "Fortezza Italiana", "Our newest restaurant, in the hotel lobby. Italian-inspired breakfast, lunch, dinner and daily happy hour."),
         ("045", "The Tack Room", "Rustic elegance overlooking Hole 15. Perfect for a post-round lunch and a toast to the winners."),
         ("079", "The Pavilion", "On the Weiskopf Course near the range, for grab-and-go fuel on tournament day.")]
for i, (img, h, b) in enumerate(tiles):
    x = 0.8 + i * 3.0
    pic(s, img, x, 2.3, 2.75, 2.3, 0.5)
    text(s, x, 4.8, 2.75, 0.45, h, size=17, color=GREEN, font=HEAD, bold=True)
    text(s, x, 5.25, 2.75, 1.6, b, size=12.5, color=GRAY, line_spacing=1.05)
footer(s, page[0])

split("107", "Intimate rooms for top sponsors", "More private spaces", [
    "When you want a smaller moment for your title sponsors or board, we have rooms made for it.",
    "•  The Rotunda: a private room inside The Steakhouse with 300-degree views of the Front Range. Banquet 40, reception 50",
    "•  Thomas Blake Ballroom: Pikes Peak views and two patios with a fire pit. Banquet 140, reception 200",
    "•  Sienna: an intimate room in the Clubhouse wine tunnel. Dinner for 12 to 18"],
    left=False, focus=0.5)

# F&B minimums (Shanna)
s = new(bg=WHITE)
eyebrow(s, 0.8, 0.55, "Event spaces + food and beverage minimums")
text(s, 0.8, 0.88, 11.5, 0.7, "Three stages for your weekend", size=30, color=GREEN, font=HEAD, bold=True)
rect(s, 0.8, 1.62, 0.9, 0.05, COPPER)
spaces = [
    ("256", "Clubhouse Courtyard", "$10,000", "Sunday welcome reception",
     ["Outdoor fireplaces, fountains, mountain and golf course views",
      "Beside the three-story wine tower and The Steakhouse",
      "Capacity: [to confirm]",
      "Weather backup: [to confirm]"]),
    ("236", "Barolo Ballroom", "$15,000", "Tournament lunch + awards",
     ["3,700 sq ft, 56' x 67', 15' ceilings",
      "Banquet 240  |  Reception 300  |  Theater 240",
      "Floor-to-ceiling windows, full A/V",
      "Adjoining Fortezza pre-function space"]),
    ("259", "Fortezza Dining Room", "$3,000", "Sponsor breakfast or dinner",
     ["Our newest restaurant, in the hotel lobby",
      "Italian-inspired menus and a curated wine list",
      "Capacity: [to confirm]",
      "Steps from every guestroom"]),
]
for i, (img, name, mn, use, facts) in enumerate(spaces):
    x = 0.8 + i * 4.0
    pic(s, img, x, 1.95, 3.7, 1.9, 0.5)
    rect(s, x, 3.85, 3.7, 0.72, COPPER)
    text(s, x + 0.2, 3.85, 2.2, 0.72, [{"t": "F&B MINIMUM", "size": 9, "bold": True, "spacing": 2},
                                       {"t": mn, "size": 22, "bold": True}], color=WHITE, font=HEAD, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x + 2.0, 3.85, 1.55, 0.72, use, size=10, color=WHITE, font=HEAD, italic=True, align=PP_ALIGN.RIGHT, anchor=MSO_ANCHOR.MIDDLE)
    text(s, x, 4.72, 3.7, 0.4, name, size=17, color=GREEN, font=HEAD, bold=True)
    text(s, x, 5.12, 3.7, 1.7, ["•  " + t for t in facts], size=11.5, color=GRAY, space_after=3)
text(s, 0.8, 6.72, 11.7, 0.3, "Minimums are food and beverage spend before service charge and tax. Menus by our culinary team, with steaks cut in our on-site butcher shop.",
     size=10, color=GRAY, italic=True)
footer(s, page[0])
notes(s, "Minimums from Shanna Hughes: Clubhouse Courtyard $10k, Barolo Ballroom $15k, Fortezza dining room $3k. "
         "Barolo specs from FH capacity chart (Oct 2025). Courtyard and Fortezza capacities are NOT on the chart: get from Shanna. "
         "Confirm the minimums exclude service charge and tax, and whether any room rental applies. Suggested use of each space is ours.")

# ---------------------------------------------------------------- BEYOND
divider("05", "Beyond the Resort", "Colorado Springs, at your doorstep", "Attractions for guests and nearby hotels for your team", "065", 0.5)

s = new(bg=WHITE)
eyebrow(s, 0.8, 0.7, "Nearby attractions")
text(s, 0.8, 1.05, 11.5, 0.8, "Make a weekend of it", size=32, color=GREEN, font=HEAD, bold=True)
rect(s, 0.8, 1.9, 0.9, 0.05, COPPER)
attr = [("U.S. Air Force Academy", "About 15 min", "Cadet Chapel, the visitor center and the Honor Court. A fitting stop for this group."),
        ("Garden of the Gods", "About 25 min", "Towering red rock formations and easy walking trails. Free to visit."),
        ("U.S. Olympic & Paralympic Museum", "About 25 min", "Downtown Colorado Springs, in America's Olympic City."),
        ("Pikes Peak", "About 35 min", "America's Mountain, by the Cog Railway or the scenic highway."),
        ("Manitou Springs", "About 30 min", "Historic mountain town with shops, galleries and natural mineral springs."),
        ("Cheyenne Mountain Zoo", "About 35 min", "America's only mountain zoo, famous for its giraffe herd.")]
for i, (h, t, b) in enumerate(attr):
    col, row = i % 3, i // 3
    x, y = 0.8 + col * 4.0, 2.3 + row * 2.3
    rect(s, x, y, 3.7, 2.05, RGBColor(0xF4, 0xEE, 0xE9))
    rect(s, x, y, 0.07, 2.05, COPPER)
    text(s, x + 0.3, y + 0.2, 3.25, 0.3, t.upper(), size=10, color=COPPER, font=HEAD, bold=True, spacing=2)
    text(s, x + 0.3, y + 0.5, 3.25, 0.7, h, size=16, color=GREEN, font=HEAD, bold=True)
    text(s, x + 0.3, y + 1.15, 3.25, 0.85, b, size=12, color=GRAY, line_spacing=1.05)
footer(s, page[0])
notes(s, "Drive times are approximate from Flying Horse Resort; verify before sending.")

s = new(bg=WHITE)
pic(s, "114", 0, 0, 4.6, H, 0.5)
eyebrow(s, 5.3, 0.7, "Overflow lodging")
text(s, 5.3, 1.05, 7.5, 0.7, "Nearby hotels for staff", size=30, color=GREEN, font=HEAD, bold=True)
rect(s, 5.3, 1.8, 0.9, 0.05, COPPER)
text(s, 5.3, 2.05, 7.4, 0.7, "Sponsors stay with us. For staff and any overflow, these hotels sit about 10 minutes away near InterQuest Parkway and the Air Force Academy. "
     "We're happy to introduce you to our local hotel partners.", size=13, color=GRAY, line_spacing=1.05)
hotels = [("Hotel Polaris", "At the U.S. Air Force Academy Visitor Center"),
          ("Courtyard Colorado Springs North / Air Force Academy", "1130 InterQuest Parkway"),
          ("Drury Plaza Hotel Near the Air Force Academy", "1170 InterQuest Parkway"),
          ("Residence Inn Colorado Springs North / Air Force Academy", "InterQuest area"),
          ("SpringHill Suites Colorado Springs North / Air Force Academy", "1320 Republic Drive"),
          ("Hampton Inn & Suites Colorado Springs Air Force Academy / I-25 North", "1307 Republic Drive")]
for i, (h, a) in enumerate(hotels):
    y = 3.0 + i * 0.62
    rect(s, 5.3, y + 0.58, 7.4, 0.01, RGBColor(0xD8, 0xCF, 0xC8))
    text(s, 5.3, y, 7.4, 0.3, h, size=13.5, color=GREEN, font=HEAD, bold=True)
    text(s, 5.3, y + 0.3, 7.4, 0.25, a, size=11, color=GRAY)
footer(s, page[0], x=5.3)
notes(s, "Addresses from hotel listings (Marriott, Hilton, Visit COS). Sarah mentioned local hotel partners; swap in her preferred partners if different.")

# ---------------------------------------------------------------- INVESTMENT IN PERSPECTIVE
s = new(bg=WHITE)
pic(s, "034", 0, 0, 4.4, H, 0.5)
rect(s, 0, 0, 4.4, H, GREEN, alpha=0.55)
text(s, 0.5, 2.3, 3.5, 3.0, [
    {"t": "THE BEST RETURN", "size": 11, "bold": True, "font": HEAD, "color": RGBColor(0xD9, 0xB8, 0x9C), "spacing": 3, "after": 8},
    {"t": "95¢", "size": 72, "bold": True, "font": HEAD, "color": WHITE, "after": 2},
    {"t": "of every dollar raised goes directly to service members and their families.", "size": 15, "color": WHITE, "italic": True}],
    anchor=MSO_ANCHOR.MIDDLE)
eyebrow(s, 5.0, 0.6, "Your investment, in perspective")
text(s, 5.0, 0.95, 7.8, 0.8, "Spend it where it counts", size=30, color=GREEN, font=HEAD, bold=True)
rect(s, 5.0, 1.72, 0.9, 0.05, COPPER)
stops = [("PLAY", "$130", "per golfer", "Championship golf, cart and practice range on the Best Golf Course in Colorado Springs"),
         ("STAY", "$340", "per room, per night", "A AAA Four Diamond resort, all to yourselves, at a significantly reduced group rate"),
         ("GATHER", "$3,000", "F&B minimums from", "Three stages for your weekend, from Fortezza to the Barolo Ballroom")]
for k, (lab, big, unit, desc) in enumerate(stops):
    y = 2.0 + k * 1.2
    rect(s, 5.0, y, 7.8, 1.05, RGBColor(0xF4, 0xEE, 0xE9))
    rect(s, 5.0, y, 0.07, 1.05, COPPER)
    text(s, 5.3, y, 1.1, 1.05, lab, size=11, color=COPPER, font=HEAD, bold=True, spacing=3, anchor=MSO_ANCHOR.MIDDLE)
    text(s, 6.4, y + 0.08, 2.2, 0.6, big, size=26, color=GREEN, font=HEAD, bold=True)
    text(s, 6.4, y + 0.62, 2.2, 0.35, unit, size=10, color=GRAY, font=HEAD, italic=True)
    text(s, 8.7, y, 3.9, 1.05, desc, size=12, color=GRAY, anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
rect(s, 5.0, 5.7, 7.8, 1.05, GREEN)
text(s, 5.3, 5.7, 7.3, 1.05, [
    {"t": "PRICELESS, AND ON THE HOUSE", "size": 10, "bold": True, "font": HEAD, "color": RGBColor(0xD9, 0xB8, 0x9C), "spacing": 2, "after": 3},
    {"t": "Pikes Peak at sunrise, 300 days of Colorado sunshine, and the U.S. Air Force Academy just down the road.", "size": 13, "color": WHITE, "italic": True}],
    anchor=MSO_ANCHOR.MIDDLE)
text(s, 5.0, 6.8, 7.8, 0.22, "Room rates exclude the $35 nightly resort amenity fee, 2.95% retail sales fee and occupancy taxes. F&B minimums exclude service charge and tax.",
     size=8.5, color=GRAY, italic=True)
footer(s, page[0], x=5.0)
notes(s, "Closing value slide: per-person investment at each stop, framed against Innospec's 95-cents-to-heroes promise. No totals, per Kate. "
         "'300 days of sunshine' is Flying Horse's own website claim.")

# ---------------------------------------------------------------- NEXT STEPS
s = new()
pic(s, "034", 0, 0, W, H, 0.5)
rect(s, 0, 0, W, H, BLACK, alpha=0.45)
rect(s, 0.8, 1.2, 6.4, 5.2, GREEN, alpha=0.88)
eyebrow(s, 1.2, 1.55, "Where Belonging & Connection Meet", color=RGBColor(0xD9, 0xB8, 0x9C))
text(s, 1.2, 1.9, 5.7, 1.2, "Let's make 2027 the most memorable tournament yet", size=26, color=WHITE, font=HEAD, bold=True, line_spacing=0.95)
text(s, 1.2, 3.25, 5.7, 1.6, [
    "1.  Hold your preferred August date",
    "2.  Join us for a site visit or group call",
    "3.  Receive your full catering and room proposal"], size=15, color=WHITE, space_after=6)
text(s, 1.2, 4.75, 5.7, 1.5, [
    {"t": "YOUR FLYING HORSE TEAM", "size": 10, "bold": True, "font": HEAD, "color": RGBColor(0xD9, 0xB8, 0x9C), "spacing": 2, "after": 6},
    {"t": "Mack Borowicz, PGA, Head Golf Professional  |  mborowicz@flyinghorseclub.com"},
    {"t": "Sarah Leach, Sales Manager  |  SLeach@flyinghorseclub.com"},
    {"t": "JoDee McGinnis, Director of Catering  |  JMcGinnis@flyinghorseclub.com"},
    {"t": "Shanna Hughes, Catering Sales Manager  |  SHughes@flyinghorseclub.com"}], size=11, color=WHITE, font=HEAD, space_after=3)
logo(s, W - 4.4, 6.2, 3.6)
footer(s, page[0], dark=True)
notes(s, "Golf Shop 719-487-2620. 1880 Weiskopf Point, Colorado Springs, CO 80921.")

prs.save(OUT)
print("saved", OUT, len(prs.slides), "slides")
