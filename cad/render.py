"""Quick preview picture of the STL files. Run after badge.py: python3 cad/render.py"""
import os, numpy as np, trimesh, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
out = os.path.join(os.path.dirname(__file__), "out")
fig = plt.figure(figsize=(11, 5.5))
for i, (name, title) in enumerate([("badge_front.stl", "Front shell (screen window up, as seen from behind)"), ("badge_back.stl", "Back plate (two strap slots)")]):
    m = trimesh.load(os.path.join(out, name))
    ax = fig.add_subplot(1, 2, i + 1, projection="3d")
    tri = m.vertices[m.faces]
    n = m.face_normals
    light = np.array([0.4, -0.5, 0.8]); light /= np.linalg.norm(light)
    shade = 0.35 + 0.65 * np.clip(n @ light, 0, 1)
    ax.add_collection3d(Poly3DCollection(tri, facecolors=[(s, s, s, 1) for s in shade], edgecolor="none"))
    lo, hi = m.bounds
    c, r = (lo + hi) / 2, (hi - lo).max() / 2
    ax.set_xlim(c[0] - r, c[0] + r); ax.set_ylim(c[1] - r, c[1] + r); ax.set_zlim(c[2] - r, c[2] + r)
    ax.view_init(elev=35, azim=-60); ax.set_axis_off(); ax.set_title(title, fontsize=9)
    print(name, "watertight:", m.is_watertight, "size mm:", np.round(hi - lo, 1))
plt.tight_layout(); plt.savefig(os.path.join(out, "preview.png"), dpi=110)
