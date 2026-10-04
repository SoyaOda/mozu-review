# Editable eating arm rig

Use a new copy of `mozu-siteat212-fair-arms-r01.blend` from
`output/rig_candidates/siteat212_20260925/arm_fairness_20261005/`.
Byte-identical copies are retained on the Mac and Windows verification host. The compact sit, head and complete
six-mouthful action remain upstream. The saved native contains no render
caches or Python runtime handlers. Native identity and current verification
status are recorded in REPORT.md.

## Artist controls

Select `SE212A | Grip-preserving arm shape`.

| Control | Selected value | Effect |
| --- | --- | --- |
| Shape fairness | 1 | Applies the shoulder/grip constrained silhouette. Zero restores the exact incoming arm. |
| Bow retention | 0.20 | Spreads this fraction of the original middle-arm bow over one quadratic curve. Tested range: 0–0.4. |

The original shoulder/elbow action remains on each arm's `SE212F` modifier.
The final `SE212A | Fair material sweep` modifier remains unapplied and reads
the evaluated incoming arm, rather than stored per-frame meshes. Existing
animation keys therefore continue to own hand placement.

The new section frame changes hand orientation while preserving the actual
food-contact vertex. At fairness 1, upstream articulation supplies the shoulder
and grip tasks without prescribing every local bend of the visible arm.
Individual distal twist is not preserved by this unified frame. Fairness 0
restores the original articulated sweep. This shape layer is qualified for
the existing eating action; new wrist/roll combinations need new evidence.

## Native construction

The unchanged source club has 2,018 vertices and 65 material stations: two
poles and 63 rings of 32 vertices. `c12_material` and `c12_ring` retain source
material coordinates and ring ownership. Opposite section vertices recover
the center. The midpoint section establishes a frame around the shoulder-to-
grip direction. Each ring retains its inherited elliptical x/y radii.

The task constraints use vertex 0 and the prop's actual recorded grip index,
1937, on both sides. The grip lies at material fraction 0.99458821, rather than
at the terminal pole. A quadratic bow has zero offset at the shoulder and grip.
The two anchor vertices are returned directly from the input, preserving bit
identity. Downstream rice placement and orientation therefore use the same
anchors as before.

Original elbow activity enables the shape through a quintic fade over 0–18
degrees. Canonical rest is exact. Original-arm blending and use/mode gates
remain upstream. A zero fairness weight switches the entire geometry through
unchanged. No camera-dependent corrections, target-image fitting or food
compensation are present.

Do not change source topology, vertex order, material stations or the grip
index without rebuilding the adapter and renewing its evidence. The installer
checks the 65-station, 32-vertex ring family. Control values are live; a changed
scaffold requires rerunning the installer on a new parent copy. Five labeled
node stages separate material coordinates, section recovery, task frame, bow
construction and protected output.

## Verified scope

The pilot passed 19 native poses and 42 matched whole/isolated image reviews.
Root/grip points, protected body/feet/head/food fields and inherited arm
material/topology fields are exact; four bypass/reset probes are exact.
All 60 mathematical pose/control cases pass task constraints, rigid-transform
covariance and forward section order. Maximum native/prototype coordinate
difference is 2.43e-7.

Saved-native reopens, four control edit/reset probes, three other-mode bypasses,
216 native times and 18 shaded comparisons also pass. All 1,329 native frames
per camera (three views, 60 fps) pass capture checks and complete visual review.
All three movies fully decode; see REPORT.md and full-visual-review.json.

Side-view food occlusion and late-bite front-view foreshortening remain. This
candidate does not claim owner adoption, broad 15-issue/11-gate qualification,
physical grasp/friction or verified export to another runtime.
