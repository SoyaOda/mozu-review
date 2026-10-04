"""Authored torso frames and supported cross-sections; no source-coordinate fit."""
import math

PIVOT = (0.0, 0.03, -0.03)
ANKLE_START, HIP_END = -0.035, 0.30
TWIST_START, CHEST_END = 0.36, 0.90


def smooth5(x):
    x = min(1.0, max(0.0, x))
    return x**3 * (10.0 + x * (-15.0 + 6.0*x))


def weights(z):
    return (smooth5((z-ANKLE_START)/(HIP_END-ANKLE_START)),
            smooth5((z-TWIST_START)/(CHEST_END-TWIST_START)))


def rotation(pitch, roll, yaw):
    x, y, z = map(math.radians, (pitch, roll, yaw))
    cx, sx, cy, sy, cz, sz = math.cos(x), math.sin(x), math.cos(y), math.sin(y), math.cos(z), math.sin(z)
    return ((cz*cy, cz*sy*sx-sz*cx, cz*sy*cx+sz*sx),
            (sz*cy, sz*sy*sx+cz*cx, sz*sy*cx-cz*sx), (-sy, cy*sx, cy*cx))


def rigid(point, angles):
    v = [x-y for x, y in zip(point, PIVOT)]
    return tuple(sum(a*b for a, b in zip(row, v))+p
                 for row, p in zip(rotation(*angles), PIVOT))


def angles_at(z, pitch, roll, chest, pelvis, articulation=1.0, leg=1.0):
    lower, upper = weights(z)
    support = 1.0-articulation*leg*(1.0-lower)
    yaw = chest+articulation*(pelvis-chest)*(1.0-upper)
    return pitch*support, roll*support, yaw*support


def deform(point, pitch, roll, chest, pelvis, articulation=1.0, leg=1.0):
    return rigid(point, angles_at(point[2], pitch, roll, chest, pelvis, articulation, leg))


def score(knots, t):
    if t <= knots[0][0]:
        return knots[0][1]
    if t >= knots[-1][0]:
        return knots[-1][1]
    for (a, x), (b, y) in zip(knots, knots[1:]):
        if a <= t <= b:
            u = (t-a)/(b-a)
            return x+(y-x)*u*u*(3-2*u)
    raise ValueError(t)


SCORES = {
    'Work posture': [(0, 0), (1.30, 0), (1.65, 1), (2.22, 1), (2.85, 0), (4, 0)],
    'Stroke': [(0, 0), (1.42, 0), (2.08, 1), (2.82, 0), (4, 0)],
    'Unloaded lift': [(0, 0), (1.30, 0), (1.45, .018), (1.65, 0), (2.08, 0), (2.40, .024), (2.85, 0), (4, 0)],
    'Bristle drag': [(0, 0), (1.45, 0), (1.83, 1), (2.08, .15), (2.4, -.12), (2.85, 0), (4, 0)],
    'Chest yaw': [(0, 0), (1.33, 0), (1.67, -5), (2.08, -15), (2.37, -8), (2.85, 0), (4, 0)],
    'Pelvis yaw': [(0, 0), (1.42, 0), (1.83, -2), (2.15, -3), (2.49, -1.5), (2.90, 0), (4, 0)],
}
KEYS = [('hold', 0.0), ('prepare', 1.46), ('mid-sweep', 1.78), ('work-end', 2.08),
        ('early-return', 2.38), ('late-return', 2.70), ('settled', 3.20)]


def controls(t):
    out = {key: score(knots, t) for key, knots in SCORES.items()}
    out['Attention'] = score(SCORES['Work posture'], t-.07)
    out['Head response'] = score(SCORES['Stroke'], t-.07)
    return out


def pose(t):
    c = controls(t)
    return dict(pitch=3*c['Work posture']+2*c['Stroke'],
                roll=-c['Work posture']-.8*c['Stroke'],
                chest=c['Chest yaw'], pelvis=c['Pelvis yaw'])
