# Smoother eating arms

The owner accepted the compact seated feet and identified an unnatural near-arm
outline in the oblique camera. The isolated arm reproduces the same scallop:
the localized elbow bend, inherited base arc and rounded end sections combine
into an inner notch and a terminal bulge. It is a surface-shape issue, not just
an overlap with the body. Three causal native ablations support this diagnosis.
See ROOT_CAUSE.md for the measurements and rejected prototype.

## Rig change

A final, unapplied Geometry Nodes layer reconstructs the existing elliptical
arm sections along one shallow, continuous bow. Upstream action keys still
place the shoulder and actual food-contact vertex; the new layer constrains
these two points exactly and controls the silhouette separately. The source
mesh, material coordinates, topology and original animation remain intact.

`SE212A | Grip-preserving arm shape` exposes `Shape fairness` (selected: 1) and
`Bow retention` (selected: 0.20). Fairness zero restores the exact incoming
geometry. A quintic elbow-activity fade preserves canonical rest; the existing
mode and original-arm blend gates retain their prior behavior. This is live
native geometry, with no per-frame arm cache or camera-specific deformation.

The editable native is `mozu-siteat212-fair-arms-r01.blend`, 222,298,685 bytes,
SHA256 `5b365a2825e85e2914f89b67275cd2cb1f1adf86dbe57577cf84fd46edcb8b10`.
Byte-identical copies are available on the Mac at
`output/rig_candidates/siteat212_20260925/arm_fairness_20261005/` and on the
Windows verification host under the same path inside `C:/mozu/se212/repo/`.
The Mac transfer was checked against the native SHA256.
The original seated r03 native and previous published pages are preserved.
See EDITING.md for control ownership, construction and reuse constraints.

## Completed native evidence

- 60 mathematical pose/control cases: shoulder/grip constraints, exact zero
  bypass, rigid-transform covariance and positive forward station order.
- 19 live native pilot poses and 42 matched whole/isolated review images.
  Maximum native/prototype coordinate difference: 2.43e-7.
- Protected body, head, feet, food, arm topology and material/scaffold fields
  exact; both shoulder and actual grip vertices bit-identical.
- Six saved/reopened visible states exact. Inherited actions and source meshes
  exact; all new drivers valid. The saved native has no capture caches.
- Four control edits and resets: live shape changes, exact anchor retention and
  zero reset error. Three other locomotion modes: exact adapter bypass.
- 216 native times: positive signed volume and forward section order. Minimum
  section-frame quality: 0.9989476; minimum forward station: 0.00047818.
- 15 food-state comparisons exact; 15 direct-native versus cached-capture image
  comparisons pixel-identical. Only the six static food CSG inputs are cached.
- All 18 shaded isolated-arm comparisons and 15 unique whole-character audit
  images inspected. No visible fold, pinch or alternating elbow scallop in the
  reviewed revised poses.

At matched oblique poses, the concavity descriptor decreases by approximately
77–83% for the holding, first-mouthful and final-mouthful outlines. This is a
measured silhouette descriptor, not an independent artistic score or proof
about arbitrary poses. The image review is the primary appearance evidence.

## Complete meal review

All 1,329 native frames in each of three cameras were rendered at 560px and
60 fps (22.15 seconds). Every arm/character field remained live. All frames
passed positive arm volume/forward-section and paw-floor checks; maximum
floor error is 5.96e-8 and settled-paw drift is zero. Fifteen direct-native
image probes are pixel-identical to the capture. Native and parent hashes
remain unchanged. The three movies fully decode with uniform timestamps.

All 3,987 view-frames were visually inspected on 111 chronological sheets.
The revised outline remains continuous through entry, six mouthfuls, empty
hand release and final rest, including both capture continuation boundaries.
The matched close-ups and shaded checks show the reduced inner notch and
terminal bulge. This is the main agent's scoped appearance assessment.

The browser comparison is published separately at
https://soyaoda.github.io/mozu-review/sit-eat-fair-arms/ .
It provides synchronized old/new movies, three cameras, slow playback, frame
stepping, a seated-entry loop, isolated-arm close-ups and every-frame sheets.
Publication and actual browser verification have separate evidence receipts.
The previous public page and six comparison media payloads remain unchanged.

`full-visual-review.json` binds observations to the native, capture, media and
all 111 sheet hashes. `review/media.json` records complete decoding. Render
continuations and verified backup/replica retirement are recorded in RECOVERY.md.
The new raw capture remains on Windows; the previous seated-r03 raw capture
has a complete hash-verified Mac copy. No original native was retired.

## Qualification limits

This is a candidate for the current six-mouthful eating action. The unified
section frame changes hand orientation; arbitrary distal wrist twists and new
roll combinations require renewed qualification. Physical grasp/friction,
other-runtime export, broad 15-issue/11-gate closure, independent critic scores
and owner adoption are not claimed. The original side-view food occlusion and
late-bite front-view foreshortening remain.

No new source video was generated. No accepted registry or adopted release was
replaced. The main agent performed the review.
