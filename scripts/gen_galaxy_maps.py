"""Generate galaxy-shaped GeoJSON maps for the WH40k and Star Wars scenarios.

Coordinates live in lon/lat space (Mercator-friendly: |lat| <= ~55).
The galaxy is an ellipse centred on (0, 0); shapes are polar wedges, rings and
jittered blobs so the result looks like a galactic map, not a grid of boxes.

Exterior rings are wound clockwise (planar, y-up) to match d3-geo rendering,
same as the previous hand-made map.
"""
import json
import math
import os
import random

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "backend", "app", "data", "custom_maps")
WH40K_ID = "a40b0000-c000-4000-b000-000040000001"
STARWARS_ID = "aa570000-c000-4000-b000-000050000001"

# Ellipse squish: r=80 maps to lon ±72 / lat ±50
SX = 0.90
SY = 0.62

rng = random.Random(40000)


def _noise_params():
    return (rng.uniform(0.03, 0.07), rng.uniform(0, 6.28),
            rng.uniform(0.015, 0.035), rng.uniform(0, 6.28))


def _pt(theta_deg: float, r: float) -> list[float]:
    t = math.radians(theta_deg)
    return [round(r * math.cos(t) * SX, 2), round(r * math.sin(t) * SY, 2)]


def wedge(theta0: float, theta1: float, r0: float, r1: float, organic: bool = True) -> list[list[float]]:
    """Partial annulus, outer arc jittered for an organic edge. Clockwise exterior."""
    a1, p1, a2, p2 = _noise_params() if organic else (0, 0, 0, 0)
    step = 3.0
    pts: list[list[float]] = []
    # outer arc, theta decreasing (clockwise)
    t = theta1
    while t >= theta0 - 1e-9:
        rr = r1 * (1 + a1 * math.sin(3 * math.radians(t) + p1) + a2 * math.sin(7 * math.radians(t) + p2))
        pts.append(_pt(t, rr))
        t -= step
    # inner arc, theta increasing
    t = theta0
    while t <= theta1 + 1e-9:
        pts.append(_pt(t, r0))
        t += step
    pts.append(pts[0])
    return pts


def ring(r0: float, r1: float, organic: bool = True) -> list[list[float]]:
    """Full annulus drawn as a wedge with a hair-thin seam at theta=0."""
    return wedge(0.4, 359.6, r0, r1, organic)


def disc(radius: float, cx: float = 0.0, cy: float = 0.0) -> list[list[float]]:
    a1, p1, a2, p2 = _noise_params()
    pts = []
    for i in range(120, -1, -1):  # clockwise
        t = math.radians(i * 3)
        rr = radius * (1 + 1.6 * a1 * math.sin(3 * t + p1) + 1.6 * a2 * math.sin(6 * t + p2))
        pts.append([round(cx + rr * math.cos(t) * SX, 2), round(cy + rr * math.sin(t) * SY, 2)])
    pts.append(pts[0])
    return pts


def blob(theta_deg: float, dist: float, radius: float) -> list[list[float]]:
    """Jittered blob centred at polar (theta, dist) from the galactic core."""
    cx, cy = _pt(theta_deg, dist)
    return disc(radius, cx, cy)


def feature(fid: str, name: str, coords: list[list[float]]) -> dict:
    return {
        "type": "Feature",
        "properties": {"id": fid, "name": name},
        "geometry": {"type": "Polygon", "coordinates": [coords]},
    }


def write_map(map_id: str, features: list[dict]):
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, f"{map_id}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"type": "FeatureCollection", "features": features}, f, ensure_ascii=False)
    print(f"wrote {path} ({len(features)} features)")


# ── Warhammer 40,000 ─────────────────────────────────────────────────────────
# Segmentums as wedges around Terra (Segmentum Solar, galactic centre),
# warp storms and empires as organic pockets drawn on top.
wh40k = [
    feature("segmentum_obscurus", "Segmentum Obscurus", wedge(75, 200, 14, 78)),
    feature("segmentum_pacificus", "Segmentum Pacificus", wedge(200, 256, 14, 78)),
    feature("segmentum_tempestus_w", "Segmentum Tempestus", wedge(256, 302, 14, 76)),
    feature("ultima_segmentum", "Ultima Segmentum", wedge(-58, 75, 14, 80)),
    feature("segmentum_solar", "Segmentum Solar (Terra)", disc(15)),
    # Pockets (drawn on top of the segmentum wedges)
    feature("eye_of_terror", "Œil de la Terreur", blob(152, 46, 12)),
    feature("maelstrom", "Le Maelstrom", blob(-18, 26, 8)),
    feature("ultramar", "Ultramar", blob(14, 47, 8)),
    feature("octarius", "Secteur d'Octarius", blob(44, 44, 8.5)),
    feature("necron_sautekh", "Dynastie Sautekh", blob(-40, 40, 8)),
    feature("ghoul_stars", "Étoiles Goules", blob(60, 64, 9)),
    feature("tau_empire", "Empire T'au", blob(-2, 62, 9)),
    feature("eastern_fringe", "Lisière Orientale", wedge(-32, 30, 70, 82)),
    feature("commorragh", "Commorragh (Webway)", blob(217, 88, 5.5)),
]

# ── Star Wars (an 0 — Bataille de Yavin) ─────────────────────────────────────
# Classic concentric galactic regions + Outer Rim split into sectors.
rng = random.Random(1977)
starwars = [
    feature("unknown_regions", "Régions Inconnues", wedge(110, 250, 45, 82)),
    feature("hutt_space", "Espace Hutt", wedge(-20, 40, 45, 80)),
    feature("corporate_sector", "Secteur Corporatif", wedge(40, 75, 45, 78)),
    feature("mandalore_sector", "Secteur de Mandalore", wedge(75, 110, 45, 78)),
    feature("outer_rim", "Bordure Extérieure (Sud)", wedge(250, 340, 45, 80)),
    feature("mid_rim", "Bordure Médiane", ring(35, 45)),
    feature("expansion_region", "Région d'Expansion", ring(28, 35)),
    feature("inner_rim", "Bordure Intérieure", ring(21, 28)),
    feature("colonies", "Les Colonies", ring(15, 21)),
    feature("core_worlds", "Mondes du Noyau", ring(7, 15)),
    feature("deep_core", "Noyau Profond (Coruscant)", disc(7)),
]

if __name__ == "__main__":
    write_map(WH40K_ID, wh40k)
    write_map(STARWARS_ID, starwars)
