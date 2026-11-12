#!/usr/bin/env python3
"""Builds the profile README's graphics.

Run from the repository root:  python3 assets/build.py

Every graphic is written twice, `<name>-light.svg` and `<name>-dark.svg`, and the README picks
one with a <picture> element. The SVGs use system fonts only (an SVG shown through <img> cannot
load a web font), so text is laid out with generous margins rather than measured.

Edit the text in PROJECTS, STEPS and the banner below, then rebuild. Counts that go stale
(test totals, version numbers) belong in the README's text, not in a graphic.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent
FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"

THEMES = {
    "light": {
        "card": "#f6f8fa", "border": "#d0d7de", "text": "#1f2328", "muted": "#59636e",
        "accent": "#0f766e", "accent_soft": "#ccfbf1", "agent": "#6639ba", "agent_soft": "#eee7fb",
        "auto": "#9a6700", "auto_soft": "#fff4d1", "line": "#afb8c1",
    },
    "dark": {
        "card": "#161b22", "border": "#30363d", "text": "#e6edf3", "muted": "#9198a1",
        "accent": "#2dd4bf", "accent_soft": "#0f2f2c", "agent": "#b392f0", "agent_soft": "#241b3a",
        "auto": "#e3b341", "auto_soft": "#33290d", "line": "#484f58",
    },
}


def text(x, y, s, size, fill, weight=400, anchor="start", family=FONT, spacing=None):
    extra = f' letter-spacing="{spacing}"' if spacing else ""
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'fill="{fill}" text-anchor="{anchor}"{extra}>{escape(s)}</text>')


def lines(x, y, rows, size, fill, gap, **kw):
    return "".join(text(x, y + i * gap, row, size, fill, **kw) for i, row in enumerate(rows))


def svg(width, height, title, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
            f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">'
            f"<title>{escape(title)}</title>{body}</svg>\n")


def write(name, build):
    for theme, t in THEMES.items():
        (OUT / f"{name}-{theme}.svg").write_text(build(t), encoding="utf-8")


# ---------------------------------------------------------------------------- banner
# Every graphic is 840 units wide, close to the width GitHub gives a README, so text is drawn
# at about the size it is read.

W = 840
WAYPOINTS = ["Physical operations", "Systems of record", "Compliance", "Automation"]


def banner(t):
    h = 200
    xs = [110, 317, 523, 730]
    ys = [150, 136, 150, 136]
    path = f"M 28 {ys[0] + 9} " + " ".join(f"L {x} {y}" for x, y in zip(xs, ys)) + f" L {W - 28} {ys[-1] + 8}"
    body = [
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="12" fill="{t["card"]}" stroke="{t["border"]}"/>',
        text(36, 62, "Joel Abraham", 38, t["text"], 700),
        text(36, 92, "Operations, logistics, compliance, and systems automation", 17, t["muted"]),
        f'<path d="{path}" fill="none" stroke="{t["line"]}" stroke-width="2" stroke-dasharray="2 8" stroke-linecap="round"/>',
    ]
    for x, y, label in zip(xs, ys, WAYPOINTS):
        body.append(f'<circle cx="{x}" cy="{y}" r="11" fill="{t["accent_soft"]}" stroke="{t["accent"]}" stroke-width="2"/>')
        body.append(f'<circle cx="{x}" cy="{y}" r="4" fill="{t["accent"]}"/>')
        body.append(text(x, y + 32, label, 13, t["muted"], 600, "middle"))
    return svg(W, h, "Joel Abraham. Operations, logistics, compliance, and systems automation.", "".join(body))


# ---------------------------------------------------------------------------- process

STEPS = [
    ("human", "1 Define", ["The workflow,", "and how it fails"]),
    ("human", "2 Plan", ["Agreed before", "a large change"]),
    ("agent", "3 Build", ["An agent writes", "the code under", "written rules"]),
    ("auto", "4 Gates", ["Types, lint,", "tests, build"]),
    ("agent", "5 Review", ["Adversarial,", "separate from", "the author"]),
    ("human", "6 Merge", ["I approve once", "every check is", "green"]),
]
ROLES = {"human": ("accent", "Mine to decide"), "agent": ("agent", "Agent"), "auto": ("auto", "Automated")}


def process(t):
    h = 330
    bw, bh, gap, top = 124, 128, 16, 62
    left = (W - (6 * bw + 5 * gap)) / 2
    body = [text(left, 32, "How a change ships", 19, t["text"], 700)]

    lx = W - left
    for role in ("auto", "agent", "human"):
        key, label = ROLES[role]
        lx -= len(label) * 7.0 + 4
        body.append(text(lx, 31, label, 12.5, t["muted"], 600))
        lx -= 19
        body.append(f'<rect x="{lx}" y="20" width="13" height="13" rx="3" fill="{t[key + "_soft"]}" stroke="{t[key]}" stroke-width="1.5"/>')
        lx -= 16

    for i, (role, name, rows) in enumerate(STEPS):
        key = ROLES[role][0]
        x = left + i * (bw + gap)
        body.append(f'<rect x="{x}" y="{top}" width="{bw}" height="{bh}" rx="9" fill="{t[key + "_soft"]}" stroke="{t[key]}" stroke-width="1.5"/>')
        body.append(text(x + 12, top + 30, name, 16, t["text"], 700))
        body.append(lines(x + 12, top + 56, rows, 13, t["muted"], 18))
        if i < 5:
            ax, ay = x + bw + 3, top + bh / 2
            body.append(f'<path d="M {ax} {ay} H {ax + gap - 6} M {ax + gap - 10} {ay - 4} L {ax + gap - 6} {ay} L {ax + gap - 10} {ay + 4}" fill="none" stroke="{t["line"]}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/>')

    def cx(i):
        return left + i * (bw + gap) + bw / 2

    # A failed gate or review sends the change back to the build step.
    y0, y1 = top + bh + 5, top + bh + 38
    for i in (3, 4):
        body.append(f'<path d="M {cx(i)} {y0} V {y1}" stroke="{t["auto"]}" stroke-width="1.75" stroke-dasharray="5 5" stroke-linecap="round"/>')
    body.append(f'<path d="M {cx(4)} {y1} H {cx(2)} V {y0 + 5}" fill="none" stroke="{t["auto"]}" stroke-width="1.75" stroke-dasharray="5 5" stroke-linecap="round" stroke-linejoin="round"/>')
    body.append(f'<path d="M {cx(2) - 5} {y0 + 10} L {cx(2)} {y0 + 3} L {cx(2) + 5} {y0 + 10}" fill="none" stroke="{t["auto"]}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/>')
    body.append(text((cx(2) + cx(4)) / 2, y1 + 19, "A failure goes back to the build step", 12.5, t["auto"], 600, "middle"))

    by = h - 46
    body.append(f'<rect x="{left}" y="{by}" width="{W - 2 * left}" height="38" rx="9" fill="{t["card"]}" stroke="{t["border"]}"/>')
    body.append(text(W / 2, by + 24, "A check is not trusted until it has been shown failing on a planted defect.", 13.5, t["text"], 600, "middle"))
    return svg(W, h, "How a change ships: define, plan, build, gates, review, merge. A failed gate or review "
                     "sends the change back to the build step.", "".join(body))


# ---------------------------------------------------------------------------- project headers
# A header strip per project: name, kind, and up to three short tags. The description is README
# text, so it stays readable on a phone and to a screen reader.

PROJECTS = [
    ("formwaypoint", "FormWaypoint", "Export documentation", ["No backend", "MIT", "Pre-release"]),
    ("ai-advocate", "AI Advocate", "Civic tech", ["Live", "English + Spanish"]),
    ("squadlogic", "SquadLogic", "Scheduling", ["Live", "Admin-only"]),
    ("agent-ready-template", "agent-ready-template", "Process", ["MIT", "Storybook"]),
    ("helmets-clash", "Helmets Clash", "Game prototype", ["Live", "Prototype"]),
]


def card(name, kind, tags):
    def build(t):
        h = 78
        body = [
            f'<rect x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="10" fill="{t["card"]}" stroke="{t["border"]}"/>',
            f'<rect x="0.5" y="0.5" width="6" height="{h - 1}" rx="3" fill="{t["accent"]}"/>',
            text(26, 28, kind.upper(), 11.5, t["accent"], 700, spacing="0.09em"),
            text(26, 58, name, 25, t["text"], 700),
        ]
        x = W - 22
        for tag in reversed(tags):
            tw = round(len(tag) * 7.1 + 26)
            x -= tw
            body.append(f'<rect x="{x}" y="27" width="{tw}" height="25" rx="12.5" fill="none" stroke="{t["border"]}"/>')
            body.append(text(x + tw / 2, 44, tag, 12.5, t["muted"], 600, "middle"))
            x -= 8
        return svg(W, h, f"{name}: {kind.lower()}", "".join(body))
    return build


# ---------------------------------------------------------------------------- FormWaypoint flow

FLOW = [
    ("Invoice and", "packing list"),
    ("Read on the", "machine"),
    ("Checked against", "printed totals"),
    ("Carrier's own", "form filled"),
    ("Completed form,", "unsigned"),
]


def flow(t):
    h = 178
    bw, bh, gap = 136, 62, 22
    left = (W - (5 * bw + 4 * gap)) / 2
    top = 58
    body = [
        f'<rect x="{left - 18}" y="{top - 38}" width="{W - 2 * left + 36}" height="{bh + 84}" rx="12" fill="none" stroke="{t["accent"]}" stroke-width="1.5" stroke-dasharray="6 6"/>',
        text(left - 2, top - 14, "YOUR MACHINE", 11.5, t["accent"], 700, spacing="0.1em"),
        text(W - left + 2, top - 14, "No shipment data leaves it", 12.5, t["muted"], 600, "end"),
    ]
    for i, rows in enumerate(FLOW):
        x = left + i * (bw + gap)
        edge = i in (0, 4)
        body.append(f'<rect x="{x}" y="{top}" width="{bw}" height="{bh}" rx="9" fill="{t["card"]}" stroke="{t["text"] if edge else t["border"]}" stroke-width="{1.5 if edge else 1}"/>')
        body.append(lines(x + bw / 2, top + 27, list(rows), 13, t["text"], 18, weight=600, anchor="middle"))
        if i < 4:
            ax, ay = x + bw + 4, top + bh / 2
            body.append(f'<path d="M {ax} {ay} H {ax + gap - 8} M {ax + gap - 12} {ay - 4} L {ax + gap - 8} {ay} L {ax + gap - 12} {ay + 4}" fill="none" stroke="{t["line"]}" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"/>')
    body.append(text(W / 2, top + bh + 28, "If the figures do not sum back to the totals printed on the document, no form is produced.", 12.5, t["muted"], 400, "middle"))
    return svg(W, h, "FormWaypoint: an invoice and packing list is read on your machine, checked against its printed "
                     "totals, and used to fill the carrier's own blank form. No shipment data leaves the machine.",
               "".join(body))


if __name__ == "__main__":
    for old in OUT.glob("*.svg"):
        old.unlink()
    write("banner", banner)
    write("process", process)
    write("formwaypoint-flow", flow)
    for slug, name, kind, tags in PROJECTS:
        write(f"card-{slug}", card(name, kind, tags))
    print(f"wrote {len(list(OUT.glob('*.svg')))} files to {OUT}")
