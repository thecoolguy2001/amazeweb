# -*- coding: utf-8 -*-
"""Generates the static site into the repo root. Run: python3 build/build.py"""
import html, pathlib, shutil, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from content import *

ROOT = pathlib.Path(__file__).resolve().parent.parent
E = lambda s: html.escape(s, quote=True)

# ---------------------------------------------------------------- asset hashes
# GitHub Pages serves everything with cache-control: max-age=600, so a browser
# can hold a ten-minute-old style.css while already running today's HTML — the
# markup arrives, the rules that size it do not, and the page renders gutted.
# Fingerprinting the URL makes a changed file a different file, so that skew
# cannot happen: the browser either has this exact build's CSS or fetches it.
def _v(relpath):
    f = ROOT / relpath.lstrip("/")
    if not f.exists():
        return relpath
    import hashlib
    return f"{relpath}?v={hashlib.sha1(f.read_bytes()).hexdigest()[:10]}"

# ---------------------------------------------------------------- icons
ARROW = ('<svg class="arrow" viewBox="0 0 16 16" fill="none" aria-hidden="true">'
         '<path d="M4 12L12 4M12 4H5.5M12 4v6.5" stroke="currentColor" stroke-width="1.6" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')
CHEV = ('<svg class="chev" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
        '<path d="M12 4v15m0 0 6-6m-6 6-6-6" stroke="currentColor" stroke-width="1.7" '
        'stroke-linecap="round" stroke-linejoin="round"/></svg>')
CARET = ('<svg class="caret" viewBox="0 0 24 24" fill="none" aria-hidden="true">'
         '<path d="m6 9 6 6 6-6" stroke="currentColor" stroke-width="1.8" '
         'stroke-linecap="round" stroke-linejoin="round"/></svg>')
CARET_L = ('<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
           '<path d="m15 5-7 7 7 7" stroke="currentColor" stroke-width="1.8" '
           'stroke-linecap="round" stroke-linejoin="round"/></svg>')
CARET_R = ('<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
           '<path d="m9 5 7 7-7 7" stroke="currentColor" stroke-width="1.8" '
           'stroke-linecap="round" stroke-linejoin="round"/></svg>')
SVC_ICONS = {
 "scan": '<svg viewBox="0 0 24 24" fill="none" stroke="#17A34A" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8V5a2 2 0 0 1 2-2h3M16 3h3a2 2 0 0 1 2 2v3M21 16v3a2 2 0 0 1-2 2h-3M8 21H5a2 2 0 0 1-2-2v-3"/><circle cx="12" cy="12" r="3.2"/></svg>',
 "code": '<svg viewBox="0 0 24 24" fill="none" stroke="#17A34A" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><path d="m8.5 8.5-4 3.5 4 3.5M15.5 8.5l4 3.5-4 3.5M13.5 5.5l-3 13"/></svg>',
 "monitor": '<svg viewBox="0 0 24 24" fill="none" stroke="#17A34A" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"><rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8.5 21h7M12 17v4"/></svg>',
}
SOCIAL_SVG = {
 "TikTok": '<path d="M16.5 2h-3v13.1a2.6 2.6 0 1 1-2.1-2.55V9.5a5.7 5.7 0 1 0 5.1 5.67V8.9a6.6 6.6 0 0 0 3.9 1.26V7.1a3.75 3.75 0 0 1-3.9-3.6V2z"/>',
 "Instagram": '<path d="M12 2.2c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9-.42-.42-.68-.82-.9-1.38-.16-.42-.36-1.06-.41-2.23C2.21 15.58 2.2 15.2 2.2 12s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41C8.42 2.21 8.8 2.2 12 2.2zm0 3.08A6.72 6.72 0 1 0 18.72 12 6.72 6.72 0 0 0 12 5.28zm0 11.08A4.36 4.36 0 1 1 16.36 12 4.36 4.36 0 0 1 12 16.36zm6.99-11.3a1.57 1.57 0 1 1-1.57-1.57 1.57 1.57 0 0 1 1.57 1.57z"/>',
 "X": '<path d="M17.53 3h3.04l-6.64 7.59L21.75 21h-5.9l-4.62-6.04L5.94 21H2.9l7.1-8.12L2.4 3h6.05l4.18 5.52L17.53 3zm-1.07 16.2h1.68L7.62 4.71H5.82l10.64 14.49z"/>',
 "Facebook": '<path d="M6.821 20v-9h2.733L10 7H6.821V5.052C6.821 4.022 6.848 3 8.287 3h1.458V.14c0-.043-1.253-.14-2.52-.14C4.58 0 2.924 1.657 2.924 4.7V7H0v4h2.923v9z" transform="translate(2 2)"/>',
 "LinkedIn": '<path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM10 9h3.8v1.71h.05a4.17 4.17 0 0 1 3.75-2.06C21.3 8.65 22 11 22 14.1V21h-4v-6.1c0-1.46-.03-3.33-2.03-3.33s-2.34 1.59-2.34 3.23V21h-4z"/>',
}

# ---------------------------------------------------------------- partials
def nav(prefix=""):
    links = "".join(f'<a href="{h}">{E(t)}</a>' for t, h in NAV)
    # .nav-row and .nav-links are display:contents on desktop, so the logo and the
    # three links are direct flex children of the pill. Under 810px the pill turns
    # into a column: the row keeps the logo + burger, the links stack below it and
    # the pill's height animates 51px -> 267px with overflow:hidden.
    return (f'<header class="nav"><nav class="nav-pill" aria-label="Main">'
            f'<div class="nav-row">'
            f'<a href="/" aria-label="Amazé Web — home">'
            f'<img class="nav-logo" src="{LOGO}" alt="Amazé Web" width="158" height="49"></a>'
            f'<button class="nav-toggle" type="button" aria-label="Menu" '
            f'aria-expanded="false" aria-controls="nav-menu">'
            f'<span class="bar b1"></span><span class="bar b2"></span></button>'
            f'</div>'
            f'<div class="nav-links" id="nav-menu">{links}</div></nav></header>')

def footer():
    cols = ""
    for title, items in FOOTER["cols"]:
        ls = "".join(f'<a href="{h}">{E(t)}</a>' for t, h in items)
        cols += f'<div class="footer-col"><h3>{E(title)}</h3>{ls}</div>'
    socs = "".join(
        f'<a href="{u}" target="_blank" rel="noopener" aria-label="{E(n)}">'
        f'<svg viewBox="0 0 24 24" aria-hidden="true">{SOCIAL_SVG[n]}</svg></a>'
        for n, u in SOCIALS)
    return (f'<footer class="footer"><div class="footer-top">'
            f'<div><p class="t-stmt footer-stmt">{E(FOOTER["stmt"])}</p>'
            f'<div class="socials">{socs}</div></div>{cols}</div>'
            f'<div class="footer-bar">{E(SITE["copyright"])}</div></footer>')

def faq_block():
    groups = ""
    for i, (title, qs) in enumerate(FAQ):
        items = "".join(
            f'<div class="faq-item"><p class="faq-q">{E(q)}</p><p class="faq-a">{E(a)}</p></div>'
            for q, a in qs)
        op = ""   # the published site renders every group collapsed
        groups += (f'<details class="faq-group"{op}><summary class="faq-head">'
                   f'<span class="t-faq-h">{E(title)}</span>{CHEV}</summary>'
                   f'<div class="faq-panel">{items}</div></details>')
    return (f'<section class="wrap s-faq" id="faqss"><p class="t-label tag" style="margin-bottom:49px">FAQ</p>'
            f'<div class="faq">{groups}</div></section>')

def hero(black, grey):
    return (f'<section class="wrap hero"><h1 class="t-hero">{E(black)} '
            f'<span class="muted">{E(grey)}</span></h1>')

# --- card artwork --------------------------------------------------------
# Drawn, not photographed: each scene shows the service its card sells, so it
# stays honest (nothing is a screenshot of work we did not do) and adds no
# binary assets. Decorative, hence aria-hidden.

def _rows(spec):
    """Code lines: (indent, [(class, width%), ...])."""
    out = ""
    for indent, parts in spec:
        bars = "".join(f'<i class="{c}" style="width:{w}%"></i>' for c, w in parts)
        out += f'<span class="row in{indent}"><i class="n"></i>{bars}</span>'
    return out

CHEVRON = ('<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
           '<path d="M12 5v14m0 0 6-6m-6 6-6-6" stroke="currentColor" stroke-width="2.2" '
           'stroke-linecap="round" stroke-linejoin="round"/></svg>')
ENVELOPE = ('<svg viewBox="0 0 24 24" fill="none" aria-hidden="true">'
            '<rect x="2.5" y="5" width="19" height="14" rx="2.5" stroke="currentColor" stroke-width="1.6"/>'
            '<path d="m3.5 7 8.5 6 8.5-6" stroke="currentColor" stroke-width="1.6" '
            'stroke-linecap="round" stroke-linejoin="round"/></svg>')

def _art_setup():
    """A bought template being set up: real domain in the bar, one section
       still snapping into place, and the same page already on a phone."""
    nav = '<span class="l"></span><span class="l"></span><span class="l last"></span>'
    return ('<div class="scard-art art-setup" aria-hidden="true">'
            '<div class="win-bar"><i></i><i></i><i></i>'
            '<span class="url">yourshop.com</span><span class="live">Live</span></div>'
            '<div class="win-body">'
            f'<div class="w-nav"><span class="mark"></span>{nav}</div>'
            '<div class="w-hero"><span class="b1"></span><span class="b2"></span>'
            '<span class="cta"></span></div>'
            '<div class="w-grid"><span class="snap"></span><span></span><span></span></div>'
            '</div>'
            '<div class="w-phone"><span class="nub"></span><span class="s1"></span>'
            '<span class="s2"></span><span class="s3"></span></div></div>')

def _art_custom():
    """Written from scratch, then rendered: the editor above, the page below."""
    code = _rows([(0, [("k", 26), ("s", 34)]),
                  (1, [("p", 18), ("k", 30), ("s", 22)]),
                  (1, [("s", 44), ("p", 16)]),
                  (2, [("k", 22), ("p", 38)]),
                  (2, [("p", 30), ("s", 26), ("p", 14)]),
                  (1, [("k", 18), ("p", 46)]),
                  (0, [("p", 24), ("k", 20)]),
                  (0, [("s", 38), ("p", 18)])])
    return ('<div class="scard-art art-custom" aria-hidden="true">'
            '<div class="code"><span class="tab">index.html</span>'
            f'<div class="rows">{code}</div></div>'
            f'<div class="seam"><span class="badge">{CHEVRON}</span></div>'
            '<div class="out">'
            '<div class="o-nav"><span class="mark"></span><span class="l"></span>'
            '<span class="l"></span><span class="l last"></span></div>'
            '<div class="o-hero"><span class="t1"></span><span class="t2"></span>'
            '<span class="cta"></span></div>'
            '<div class="o-row"><span></span><span></span><span></span></div>'
            '</div></div>')

def _art_tools():
    """Four of the add-ons named in the card copy, each as its own small tool."""
    bars = "".join(f'<i style="height:{h}%"></i>' for h in (34, 58, 46, 76, 92))
    return ('<div class="scard-art art-tools" aria-hidden="true">'
            '<div class="tool t-book"><p class="cap">Booking</p>'
            '<div class="slots"><span></span><span class="on"></span><span></span>'
            '<span></span></div></div>'
            '<div class="tool t-form"><p class="cap">Signup</p>'
            '<div class="field"></div><div class="field short"></div>'
            '<div class="send"></div></div>'
            f'<div class="tool t-mail"><p class="cap">Email</p><div class="env">{ENVELOPE}</div></div>'
            f'<div class="tool t-stat"><p class="cap">Analytics</p><div class="bars">{bars}</div></div>'
            '</div>')

ART = {"setup": _art_setup, "custom": _art_custom, "tools": _art_tools}

def card_art(name):
    return ART[name]()

def stack(cards):
    out = '<section class="stack" id="case-study">'
    for c in cards:
        dim = " dim" if c["dim"] else ""
        # Stats are optional. With none, the shot fills the right column instead of
        # leaving the stat pair's height as dead space under it — so no inline
        # aspect-ratio either, since that would fight the flex height.
        pairs = c.get("stats") or []
        stats = "".join(f'<div><p class="k">{E(k)}</p><p class="t-stat v">{E(v)}</p></div>'
                        for k, v in pairs)
        stats = f'<div class="scard-stats">{stats}</div>' if pairs else ""
        shot_style = f' style="aspect-ratio:{c["ratio"]}"' if pairs else ""
        shot = (card_art(c["art"]) if c.get("art") else
                f'<img class="scard-shot"{shot_style} src="{c["img"]}" '
                f'alt="" loading="lazy" decoding="async">')
        label, href = c["cta"]
        out += (f'<div class="stack-item"><article class="scard{dim}">'
                f'<div class="scard-left"><h2 class="t-card-h">{E(c["title"])}</h2>'
                f'<p class="t-18">{E(c["body"])}</p>'
                f'<a class="btn" href="{href}">{E(label)}{ARROW}</a></div>'
                f'<div class="scard-right{"" if pairs else " full"}">'
                f'{shot}{stats}</div></article></div>')
    return out + "</section>"

# --- service-card tiles --------------------------------------------------
# The three squares under each Vision card. Drawn, like the service artwork
# above, and each trio spells out what that card's three tags actually are.
# They render around 88px square, so each tile holds one idea, no more.

def _bars(spec, cls="b"):
    return "".join(f'<i class="{cls}" style="width:{w}%"></i>' for w in spec)

SVC_TILES = {
    # Branding Design — logo, guideline, strategy.
    "branding": (
        '<span class="stile st-logo"><i class="m"></i><i class="w1"></i><i class="w2"></i></span>'
        '<span class="stile st-guide"><span class="chips"><i></i><i></i><i></i></span>'
        '<b>Aa</b><i class="ln"></i><i class="ln s"></i></span>'
        '<span class="stile st-matrix"><i class="ax-v"></i><i class="ax-h"></i>'
        '<i class="dot"></i><i class="dot2"></i></span>'),
    # Web Development — a landing page, the code behind it, a multi-page stack.
    "webdev": (
        '<span class="stile st-land"><i class="bar"></i><i class="hero"></i>'
        '<i class="cta"></i><i class="sec"></i></span>'
        '<span class="stile st-code">'
        + "".join(f'<i class="{c}" style="width:{w}%"></i>'
                  for c, w in (("k", 54), ("s", 72), ("p", 40), ("k", 64), ("s", 48)))
        + '</span>'
        '<span class="stile st-pages"><i class="p3"></i><i class="p2"></i><i class="p1"></i></span>'),
    # UI/UX — an app on a phone, a component set, a prototype flow.
    "uiux": (
        '<span class="stile st-phone"><span class="scr"><i class="nub"></i><i class="hd"></i>'
        '<i class="r"></i><i class="r s"></i></span></span>'
        '<span class="stile st-sys"><i class="btn"></i><i class="tog"></i><i class="sld"></i></span>'
        '<span class="stile st-proto"><i class="f1"></i><i class="arw"></i><i class="f2"></i></span>'),
}

def svc_tiles(name):
    return SVC_TILES[name]

def vision_and_services(cards):
    svc = ""
    for c in cards:
        shots = (svc_tiles(c["art"]) if c.get("art") else
                 "".join(f'<img src="{s}" alt="" loading="lazy" decoding="async">'
                         for s in c["shots"]))
        tags = "".join(f'<span>{E(t)}</span>' for t in c["tags"])
        svc += (f'<a class="svc {c["variant"]}" href="/support/#support-message">'
                f'<div class="svc-head"><span class="name">{E(c["name"])}</span>'
                f'<span class="ico">{SVC_ICONS[c["icon"]]}</span></div>'
                f'<div class="svc-body">'
                f'<div class="svc-copy"><p class="t-16">{E(c["body"])}</p>'
                f'<div class="svc-shots{" art" if c.get("art") else ""}" aria-hidden="true">{shots}</div></div>'
                f'<div class="svc-tags">{tags}</div></div></a>')
    return (f'<section class="wrap s-vision" id="ourvision">'
            f'<div class="vision"><p class="t-label tag">{E(VISION["label"])}</p>'
            f'<h2 class="t-stmt vision-stmt"><span class="lead">{E(VISION["lead"])}</span> '
            f'<span class="tail">{E(VISION["tail"])}</span></h2></div>'
            f'<div class="svc-grid">{svc}</div></section>')

def shell(title, desc, body, extra_head="", cls=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script>document.documentElement.classList.add('js')</script>
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="icon" href="/assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="icon" href="/assets/img/mark.png" sizes="any" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/favicon-180.png">
<link rel="preload" href="/assets/fonts/inter-400-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/inter-display-700-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{_v("/assets/css/fonts.css")}">
<link rel="stylesheet" href="{_v("/assets/css/style.css")}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:type" content="website">
{extra_head}</head>
<body id="top">
{nav()}
<main class="page"><div class="shell{(" " + cls) if cls else ""}">
{body}
{footer()}
</div></main>
<script src="{_v("/assets/js/app.js")}" defer></script>
</body>
</html>
"""

def write(relpath, text):
    p = ROOT / relpath
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    return p

# ---------------------------------------------------------------- pages
def page_home():
    body = (hero("Built to inspire, made to Amaze.",
                 "Let's shape your brand into a masterpiece together.")
            + f'<a class="btn btn-hero" href="/templates/">Get Started{ARROW}</a></section>'
            + stack(HOME_CARDS) + vision_and_services(HOME_SVC) + faq_block())
    return shell("Amazé Web",
        "Landing Page For Amaze Web, A Modern Web Service Business Selling Website Templates, "
        "AI Assistants, And Email Design Services. Minimalistic, Youthful, And Clean.", body)

def page_services(title, h_black, h_grey, desc):
    body = (hero(h_black, h_grey)
            + f'<a class="btn btn-hero" href="/support/#support-message">Get Started{ARROW}</a></section>'
            + stack(SERVICES_CARDS) + vision_and_services(SERVICES_SVC) + faq_block())
    return shell(title, desc, body, cls="svc-stack")

def svcx_panel(c, lead=False):
    dim = (" dim" if c.get("dim") else "") + (" lead" if lead else "")
    stats = "".join(f'<div><p class="k">{E(k)}</p><p class="v">{E(v)}</p></div>'
                    for k, v in c["stats"])
    label, href = c["cta"]
    return (f'<section class="svcx-panel{dim}">'
            f'<div><h2>{E(c["title"])}</h2><p>{E(c["body"])}</p>'
            f'<a class="btn" href="{href}">{E(label)}{ARROW}</a></div>'
            f'<div class="stats">{stats}</div></section>')

def setup_tiers_block():
    """Setup tiers for /services/setup/. Returns nothing while SETUP_TIERS is
    empty, so the page never shows an empty pricing table."""
    if not SETUP_TIERS:
        return ""
    cards = ""
    for t in SETUP_TIERS:
        items = "".join(f'<li>{E(i)}</li>' for i in t.get("includes", []))
        cards += (f'<article class="tier">'
                  f'<p class="tier-name">{E(t["name"])}</p>'
                  f'<p class="tier-price">{E(t["price"])}</p>'
                  f'<p class="tier-sum">{E(t.get("summary", ""))}</p>'
                  f'<ul class="tier-list">{items}</ul>'
                  f'<a class="btn" href="/support/#support-message">Get started{ARROW}</a>'
                  f'</article>')
    return (f'<section class="wrap tiers-sec">'
            f'<h2 class="t-section tiers-head">Setup tiers</h2>'
            f'<div class="tiers">{cards}</div></section>')

def page_service_sub(key):
    d = SERVICE_PAGES[key]
    secs = ""
    for kick, grey, black in d["sections"]:
        stmt = ""
        if grey or black:
            g = f'<span class="mute">{E(grey)}</span> ' if grey else ""
            stmt = f'<p class="stat">{g}{E(black)}</p>'
        secs += f'<div class="svcx-sec"><p class="kick">{E(kick)}</p>{stmt}</div>'
    body = (hero(d["hero"][0], d["hero"][1])
            + f'<a class="btn btn-hero" href="/support/#support-message">Get Started{ARROW}</a></section>'
            + svcx_panel(d["panel"], lead=True)
            + f'<section class="wrap svcx-secs">{secs}</section>'
            + (setup_tiers_block() if key == "setup" else "")
              + svcx_panel(d["panel2"])
            + vision_and_services(SERVICES_SVC) + faq_block())
    return shell(d["title"], d["desc"], body, cls="svcx-page")

def tpl_card(t):
    """One template card, in the same language as the home-page service cards:
    a surface-coloured shell with a rounded inner panel for the artwork and a
    second inner panel for the name, the category pill and the status."""
    plat = (f'<span class="tpl-plat">{E(t["platform"])}</span>'
            if t.get("platform") else "")
    thumb = (f'<img class="tpl-thumb" src="{t["shots"]}-card.png" alt="" '
             f'width="313" height="240" loading="lazy" decoding="async">'
             if t.get("shots") else '<div class="tpl-thumb ph-stripes"></div>')
    status = ("Demo ready" if t.get("demo") else "Coming Soon")
    return (f'<a class="tpl-card" href="/themes/{t["slug"]}/">'
            f'<div class="tpl-media">{thumb}'
            f'{plat}<span class="tpl-soon">{status}</span></div>'
            f'<div class="tpl-body">'
            f'<p class="tpl-name">{E(t["name"])}</p>'
            f'<span class="tpl-cat">{E(t["kicker"])}</span>'
            f'</div></a>')

def page_templates():
    cards = "".join(tpl_card(t) for t in THEMES)
    body = (hero("Find the perfect website template for your business.",
                 "Designed for conversions, easy to customize, and ready to launch.") + '</section>'
            + f'<section class="wrap tpl-sec">'
              f'<h2 class="t-section tpl-head">Latest Templates</h2>'
              f'<div class="tpl-grid">{cards}</div></section>'
            + vision_and_services(SERVICES_SVC) + faq_block())
    return shell("Templates | Amazé Web",
        "Browse AmazeWeb website templates for Shopify and custom builds — designed for conversions, "
        "easy to customize, and ready to launch.", body)

def page_support():
    # Message is a SELECT on the published site, not a free-text box: the SSR
    # markup is <select name="Message" required> with an empty first option and
    # these four. The three text fields carry placeholders there too.
    topics = ["General Inquiry", "Theme Installation Help",
              "Feature Suggestion", "Partnership & Collaboration"]
    options = '<option value=""></option>' + "".join(
        f'<option value="{E(t)}">{E(t)}</option>' for t in topics)
    form = f"""<section class="wrap s-form" id="support-message"><div class="form-card">
<h2>Write us</h2><p class="sub">We’d love to hear from you!</p>
<form name="support" method="POST" data-netlify="true" action="#">
<div class="form-grid">
<div class="field"><label for="fn">First name</label><input id="fn" name="first-name" type="text" placeholder="Jane" autocomplete="given-name" required></div>
<div class="field"><label for="ln">Last name</label><input id="ln" name="last-name" type="text" placeholder="Smith" autocomplete="family-name" required></div>
<div class="field full"><label for="em">Email</label><input id="em" name="email" type="email" placeholder="janesmith@gmail.com" autocomplete="email" required></div>
<div class="field full"><label for="ms">Message</label><div class="select-wrap"><select id="ms" name="message" required>{options}</select>{CARET}</div></div>
</div>
<button class="btn" type="submit">Submit</button>
</form></div></section>"""
    body = (hero("Get Support.",
                 "Whenever you get stuck or have any questions, check out the FAQs or send a "
                 "message below and we’ll get back to you.") + '</section>'
            + form + faq_block())
    return shell("Support | Amazé Web",
        "Get help with AmazeWeb templates, setup, and launch support. Check the FAQs or send a message.", body)

def page_theme(t):
    # The rail skips the theme you are already on -- the old grid listed it.
    others = "".join(tpl_card(o) for o in THEMES if o["slug"] != t["slug"])
    # Same platform mark the card carries, so the two agree. .theme-head is a
    # 4-child flex column whose children are staggered by the entrance
    # animation -- the meta row keeps that count at 4.
    plat = (f'<span class="theme-plat">{E(t["platform"])}</span>'
            if t.get("platform") else "")
    # Money and demo links come from data and fall back to the honest state:
    # no price set -> "Coming Soon"; no demo URL -> no demo button.
    price = E(t.get("price") or COMMERCE["price"] or "Coming Soon")
    setup_from = COMMERCE.get("setup_from")
    setup_line = (f'<p class="setup-from">Setup from {E(setup_from)}</p>'
                  if setup_from else "")
    terms = " ".join(x for x in (COMMERCE["support"], COMMERCE["license"]) if x)
    demo_btn = (f'<a class="btn btn-light" href="{t["demo"]}">View demo</a>'
                if t.get("demo") else "")
    # Availability, told straight. A theme with a live demo but no price is
    # viewable and not yet purchasable, and saying only "Coming Soon" next to
    # a working demo button reads like the demo is not real.
    if price == "Coming Soon":
        avail = "Demo ready, not yet for sale" if t.get("demo") else "Coming Soon"
    else:
        avail = "Available now"
    buy_url = t.get("buy_url") or COMMERCE.get("buy_url")
    if buy_url:
        label = f'Buy {price}' if price != "Coming Soon" else "Buy"
        demo_btn += (f'<a class="btn btn-buy" href="{buy_url}" rel="noopener">{E(label)}</a>')
    if t.get("shots"):
        frame = (f'<img class="inner" src="{t["shots"]}-hero.png" alt="{E(t["name"])} template, '
                 f'home page" width="1008" height="630" loading="lazy" decoding="async">')
        resp = "".join(
            f'<img class="box" src="{t["shots"]}-{k}.png" alt="{E(t["name"])} on {lbl}" '
            f'width="672" height="520" loading="lazy" decoding="async">'
            for k, lbl in (("desk", "desktop"), ("tab", "a tablet"), ("phone", "a phone")))
    else:
        frame = '<div class="inner ph-stripes"></div>'
        resp = '<div class="box ph-stripes"></div>' * 3
    body = f"""<section class="wrap theme-head">
<p class="theme-kicker">{E(t["kicker"])}</p>
<h1 class="t-page">{E(t["name"])}</h1>
<p class="theme-sub">{E(t["sub"])}</p>
<div class="theme-meta">{plat}<p class="theme-avail">{avail}</p></div>
</section>
<section class="theme-frame">{frame}</section>
<section class="theme-buy">
<div class="buy-left"><p class="note">{E(COMMERCE["note"])}</p>
<p class="price">{price}</p>{setup_line}
<p class="terms">{terms}</p></div>
<div class="buy-actions">{demo_btn}
<a class="btn btn-deep" href="/support/#support-message">Ask about this theme</a></div>
</section>
<section class="wrap"><div class="theme-row">
<h2>Overview</h2>
<div><p class="lead">{E(t["overview"])}</p><p class="who">{E(t["who"])}</p></div>
</div></section>
<section class="wrap"><div class="theme-split">
<div class="theme-note"><h3>What this theme is built to do</h3><p>{E(t["does"])}</p></div>
<div class="theme-note"><h3>Included pages and sections</h3><p>{E(t["includes"])}</p></div>
<div class="theme-note"><h3>{E(COMMERCE["excluded_h"])}</h3><p>{E(COMMERCE["excluded"])}</p></div>
</div></section>
<section class="wrap theme-resp">
<h2>Responsive by design</h2>
<div class="row">{resp}</div>
</section>
<section class="wrap"><div class="theme-mine"><div class="theme-row">
<h2>Make it yours.</h2><p class="lead">{E(MAKE_IT_YOURS)}</p>
</div></div></section>
<section class="wrap"><h2 class="t-page" style="font-size:42px;margin-bottom:32px">More themes to explore</h2>
<div class="rail-wrap"><button class="rail-btn prev" type="button" aria-label="Scroll left" hidden>{CARET_L}</button><div class="rail theme-more" tabindex="0" role="group" aria-label="More themes">{others}</div><button class="rail-btn next" type="button" aria-label="Scroll right" hidden>{CARET_R}</button></div></section>
<section class="theme-cta wrap">
<h2>Need a hand getting this theme ready to launch?</h2>
<a class="btn btn-light" href="/services/setup/">Explore setup support</a>
</section>
{faq_block()}"""
    return shell(f'{t["name"]} | AmazeWeb Template',
                 t["sub"], body, cls="theme")


def page_404():
    body = (hero("Page not found.", "That link does not lead anywhere. Try the templates, "
                 "the services, or send us a message.")
            + f'<a class="btn btn-hero" href="/">Back to home{ARROW}</a></section>')
    return shell("Page not found | Amazé Web",
                 "That page does not exist on amazeweb.shop.", body)

# ---------------------------------------------------------------- run
def main():
    n = 0
    write("index.html", page_home()); n += 1
    write("templates/index.html", page_templates()); n += 1
    write("support/index.html", page_support()); n += 1

    svc_desc = ("AmazeWeb services: template setup and launch support, custom web development, "
                "and business tools built around how your business works.")
    write("services/index.html",
          page_services("Services | Amazé Web", "Discover the essence of Amaze.",
                        "Let's shape your brand into a masterpiece together.", svc_desc)); n += 1
    for key in ("setup", "custom", "tools"):
        write(f"services/{key}/index.html", page_service_sub(key)); n += 1

    for t in THEMES:
        write(f'themes/{t["slug"]}/index.html', page_theme(t)); n += 1

    # /themes -> /templates. _redirects is kept for hosts that read it
    # (Cloudflare/Netlify); GitHub Pages ignores it, so the same redirect is
    # also emitted as a real page. CNAME tells Pages the custom domain.
    write("404.html", page_404())
    write("_redirects", "/themes  /templates/  301\n")
    write("CNAME", "amazeweb.shop\n")
    write(".nojekyll", "")
    write("themes/index.html",
          '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
          '<title>Templates | Amaz\u00e9 Web</title>\n'
          '<link rel="canonical" href="https://amazeweb.shop/templates/">\n'
          '<meta name="robots" content="noindex">\n'
          '<meta http-equiv="refresh" content="0; url=/templates/">\n'
          '</head>\n<body>\n'
          '<p>Redirecting to <a href="/templates/">Templates</a>\u2026</p>\n'
          '</body>\n</html>\n')
    print(f"built {n} pages -> {ROOT}")

if __name__ == "__main__":
    main()
