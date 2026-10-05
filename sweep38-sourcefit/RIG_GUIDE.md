# Sweep38 cleaning animation

Open `sweep38-cleaning.blend` in Blender 5.2. The file contains the complete native
character, original procedural geometry, materials, broom, drivers and action.
Playback needs no Python handler, external model file or geometry cache.

The eight-second action uses frames 1–480 at 60 fps. Frame 481 is the closed endpoint.
It starts holding the broom, prepares, sweeps three times, then returns to holding.
There is no walking, tool pickup or tool release.

## Action editing

The selected object is `Sweep33 | Supported action and world attention`.
Its new action is `Sweep38 | Three inward pulls from source r03`. Historical object
names are retained so existing driver references and the construction lineage stay
clear. Open the Dope Sheet or Graph Editor to edit the ten custom-property curves:
Work posture, Stroke, Common yaw, Unloaded lift, Bristle drag, Look task, Nod task,
Attention, Head response and Balance.

Each curve uses a single shared tangent at each knot, stored in Bezier handles.
The native curves match the independent C1 Hermite score. Work posture remains
engaged across both lifted returns. Loaded inward pulls are0.82–2.08,3.02–4.28
and5.28–6.55seconds; each moves Stroke1 to0.08. The final settle6.55..8s is authored. Both endpoints are stationary holds.

Select `Sweep36 | Constructive supported action` to adjust `Body contribution`
from 0 to 1. This one coupled control scales body turn, forward movement, lowering
and inclination together. Its six driven output values should not be disconnected
or edited independently. Default 1 is the authored performance.

## Construction

The original Body core moves rigidly. Each thigh is independently reconstructed
from the retained 180 upper ellipsoid and 198 lower ellipse/quadratic taper with
its moved hip and fixed current G ankle task. The source parts are built before
bounded hip composition. There is no height-weighted post-composition body warp.
The original analytic arm sections and material length remain; the F2 broom keeps
its dimensions and distal grip. Both feet stay planted.

The inherited world-attention constraint directs the head while the neck follows
the rigid body frame. The tail, shoulders and arms share that body transport.
The broom's fan is supported at the floor during working strokes and raised0.075units
for each return. Balance drives the unchanged left arm through18degrees Swing and
6degrees dRaise. New property bounds permit the reviewed lift and negative bristle
drag; native geometry parity checks the actual evaluated result. Existing medial arm embedding is inherited and measured
for depth increase; the rig is not certified as globally collision-free.

## Scope of verification

See REPORT.md and the included evidence for actual sample counts and results.
The coupled Body contribution 0..1 family is sampled along this authored action.
Free changes to curves or independent controls require fresh checks for shape,
attachment, floor contact, self-intersection and readable performance.

This is an editable review candidate, not an adopted production motion or a
bone-only runtime export. Earlier accepted releases and provisionally adopted Sweep37 are preserved.
The source extension scripts require the Mozu repository and preserved ancestor
inputs to rebuild; the saved native does not require them for playback.
