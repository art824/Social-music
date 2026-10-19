"""Parametric badge enclosure (build123d). All sizes in mm.
PLACEHOLDER dimensions: replace with the real board, battery and screen sizes once chosen.
Run: python3 cad/badge.py   -> writes cad/out/badge_front.stl, badge_back.stl, preview.png
"""
import os
from build123d import *

# --- parameters (edit these) ---
W, H = 44.0, 52.0            # outer width, height
D_FRONT = 9.0                # front shell depth (board + battery stack goes here)
D_BACK = 2.4                 # back plate thickness
WALL = 1.6
CORNER_R = 5.0
WINDOW_W, WINDOW_H = 28.0, 33.0   # visible screen area (derived from a 1.69" 240x280 panel; verify on datasheet)
WINDOW_Y = 2.0               # window shift upward, leaves room for a bottom edge
BUTTON_D, BUTTON_Y = 4.2, -10.0   # side button hole
LED_D, LED_X = 2.0, 0.0           # mode light hole on top edge
LIP, TOL = 1.6, 0.25         # back-plate lip depth and fit tolerance
STRAP_SLOT = (14.0, 2.4)     # two slots for a strap / clip bar (grip is still undecided)

def front():
    s = Box(W, H, D_FRONT, align=(Align.CENTER, Align.CENTER, Align.MIN))
    s = fillet(s.edges().filter_by(Axis.Z), CORNER_R)
    cavity = Box(W - 2*WALL, H - 2*WALL, D_FRONT - WALL, align=(Align.CENTER, Align.CENTER, Align.MIN))
    cavity = fillet(cavity.edges().filter_by(Axis.Z), max(CORNER_R - WALL, 0.5))
    s -= cavity
    win = Pos(0, WINDOW_Y, D_FRONT - WALL) * Box(WINDOW_W, WINDOW_H, WALL + 1, align=(Align.CENTER, Align.CENTER, Align.MIN))
    s -= win
    s -= Pos(W/2 - WALL/2, BUTTON_Y, (D_FRONT - WALL)/2) * Rot(0, 90, 0) * Cylinder(BUTTON_D/2, WALL + 2)
    s -= Pos(LED_X, H/2 - WALL/2, (D_FRONT - WALL)/2) * Rot(90, 0, 0) * Cylinder(LED_D/2, WALL + 2)
    return s

def back():
    p = Box(W, H, D_BACK, align=(Align.CENTER, Align.CENTER, Align.MIN))
    p = fillet(p.edges().filter_by(Axis.Z), CORNER_R)
    iw, ih = W - 2*WALL - TOL, H - 2*WALL - TOL
    lip = Pos(0, 0, D_BACK) * Box(iw, ih, LIP, align=(Align.CENTER, Align.CENTER, Align.MIN))
    lip = fillet(lip.edges().filter_by(Axis.Z), max(CORNER_R - WALL, 0.5))
    lip -= Pos(0, 0, D_BACK) * Box(iw - 2*WALL, ih - 2*WALL, LIP + 1, align=(Align.CENTER, Align.CENTER, Align.MIN))
    p += lip
    for y in (-H/4, H/4):
        p -= Pos(0, y, -0.5) * Box(*STRAP_SLOT, D_BACK + 1, align=(Align.CENTER, Align.CENTER, Align.MIN))
    return p

def flat_for_print(part):
    part = part.rotate(Axis.X, 180)
    return Pos(0, 0, -part.bounding_box().min.Z) * part

if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "out"); os.makedirs(out, exist_ok=True)
    f, b = flat_for_print(front()), back()
    export_stl(f, os.path.join(out, "badge_front.stl"))
    export_stl(b, os.path.join(out, "badge_back.stl"))
    print("front volume mm3:", round(f.volume), " back volume mm3:", round(b.volume))
