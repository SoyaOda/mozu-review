# Reach and seated mechanics

Candidate native: `mozu-siteat212-reach-seated-r03.blend` on the Windows SE212
workspace. SHA256: `2ac0328d74c06ae269951326e90e27590282e630a109083647a8f97e790a2472`; see `build-r03.json`.
Prior r01/r02 files remain failed-diagnostic evidence.
This is an editable candidate, not an adopted release. Preserve this file and
make a new version for another change. No character or food render cache is saved
in this native.

## Entry point

Select `SE212M | Reach and seated mechanics`. The native is saved at frame1 with
this controller selected. Locomotion Mode3 activates the seated action. Modes0–2
keep the prior behavior. `Enabled=0` restores the complete parent candidate;
original actions and driver expressions are retained.

| Control | Default | Meaning |
|---|---:|---|
| Enabled | 1 | Select the revised seated mechanics |
| Exact floor support | 1 | Complete signed support correction during seated mode |
| Reach constraint | 1 | Apply the shared floor-support reach correction |
| Stretch allowance | 0.04 | Maximum segment ratio1.04 when vertical reach is feasible |
| Seated paw Y | -0.40 | Requested forward floor position |
| Seated paw spread | 0.12 | Per-paw lateral opening from standing |
| Retreat distance | 0.36 | Distance between standing and seated body locations |
| Body progress | animated | Coupled pelvis descent and backward travel |
| Foot progress | animated | Paw placement and rigid rotation |

Coordinates use the existing native world convention. Both progress curves are
C1-continuous Bezier curves with zero endpoint speed. Feet are ready at frame49
(0.80s), while body progress is0.66. The body finishes at frame73 (1.20s). The
full native is1329frames at60fps. Meal hand/food/face keys are inherited unchanged.

For pose edits to an animated progress property, first detach its action on a
new working copy or edit the corresponding keyframes. Direct property values
will otherwise be replaced by animation evaluation. The verification script
detaches and restores both the action and its slot for edit/reset probes.

## Shared reach ownership

The actual body-mapped material hip and rigid paw-owned ankle define the thigh
segment. The inherited C179 map scales its longitudinal axis by their separation
divided by0.365. The prior seated target produced a1.6652 ratio. A timing change
alone does not fix that final geometry.

The new adapter computes one XY support correction in the actual paw, rigid paw
frame, ankle collar and thigh graph. Their common origin and three orientation
axes and each side's actual rest anchor are recovered and structurally checked
before editing. Accepted right/left support origins differ slightly; the r01
mirrored-origin shortcut was rejected by the independent dense oracle. The XY reach correction keeps paw height, shape and rotation unchanged and
draws excess horizontal reach toward the actual material hip. Before this step,
a shared signed floor correction uses the accepted G hull and current rotation
to close small support gaps that the legacy upward-only clamp ignored. The
paw, rigid frame, collar and thigh share both corrections. `Exact floor support=0`
restores the inherited one-sided clamp; `Enabled=0` restores the whole parent. No separate visible paw-only correction is used.

For requested ratio r, the ceiling follows identity through1, then transitions
smoothly using u=clamp((r-1)/(2a),0,1) and cap=1+a(2u-u²), with a=0.04. The result
cannot resolve a vertically unreachable target without changing floor support;
that condition is exposed by `se212m_vertical_feasible` and must fail validation.
This is a scoped seated reach adapter, not a general joint solver or proof that
every arbitrary slider combination is feasible.

The authored default target is already feasible: final longitudinal ratio is
approximately1.0016 and correction is negligible. The bound is a guard for future
edits, not a mechanism used to drag the selected feet after seating. An overreach
ablation shows why both layers matter: the old far target with the guard is
bounded, but moves the paws during descent. The selected motion brings their
requested placement within reach and completes the visible foot preparation
before final pelvis descent.

## Source-shape edits

The tested editing surface is the controller and its animation curves. It keeps
the accepted source meshes, source material fields, body-mapped hip and paw
support hull intact. Changing those meshes, their topology or the inherited
rest-coordinate fields is a separate rig change. Rebuild the corresponding
material-point/support mapping and repeat the native contact and visual checks;
the reach adapter does not regenerate stale scaffold data. The current repair
does not require rerunning Python for ordinary edits to its saved controls.

## Preserved inputs and verification

Raw accepted geometry, parent files and inherited actions stay unchanged. The
new lower-body seat is intentional and therefore requires a fresh entire meal
capture. Upper-body meal geometry/materials, grip/food and facial behavior are
compared against the parent at seven protected meal times. Save/reopen, control
reset, actual support and render-equivalence evidence live beside the candidate.

Use `make_native.py` only to build a new version with corresponding paths updated;
it refuses to overwrite this native. `audit_native.py` exercises the saved file,
then `capture.py` and `media.py` create the review. Expensive work belongs on the
Windows FIFO. Render-only food CSG caching and fast full-field mesh extraction
must pass candidate-bound native/pixel equivalence before capture. Complete
frames remain native lossless PNGs with compression100. A21-image WebP experiment
is preserved as an inactive alternative; it is not part of the actual capture. Native rig
editing never depends on these disposable render caches.

Historical raw-frame cache retirement preserved natives, source inputs, movies,
keyframes and hash receipts. Regenerate the older captures with
`seated_authored_full_capture.py` and `meal_complete_20261004/capture_fast.py`;
their old capture directories are not complete resume points.

Broader15issue/11gate native-motion qualification, unrestricted control domains,
runtime/skeletal export and owner adoption remain outside this candidate's
verification. Main-agent visual review is recorded as such.

Historical chew previews also retain six complete FFV1/BGRA archives in
`retained-preview-pixels/`. Every decoded frame matches the original RGBA image;
JSON receipts retain source PNG hashes and kept keyframes. Their30fps archive
addressing is not a new motion specification. Other retired old entry PNGs are
regenerable from the preserved parent native and its capture source; the old
entry directory is no longer a complete resume point.

Later shared-host storage pressure required a verified continuation after841.
Exact duplicate review media and39 additional lossless diagnostic archives are
retained onMac, with their Windows cache copies retired. Read RECOVERY.md for
each receipt, archive mapping and restore method. Current r03 native/audit/pilot
inputs and capture PNGs were excluded; native code and thresholds are unchanged.
