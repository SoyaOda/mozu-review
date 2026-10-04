# Sweep26: oblique source pose audit

Status: source analysis and expanded rig design, 2026-10-04. No new native motion has been built in this pass. Sweep25, its movie bytes, the accepted character and every adopted release remain unchanged.

## Finding

The performance reads as a supported upper-body sweep. The visible foot contact stays nearly stationary while the visible upper-arm root region travels, the belly presentation changes and the head attends to the tool. The feet provide the stable base against which the upper-body action reads. Large steps, alternating lifted feet or a measured left/right weight exchange are not established by this oblique video.

This supports an articulated support/pelvis/chest design. It does not uniquely identify a hidden skeleton or prove a particular spine angle. The important design change is to allow the chest to orient and incline relative to the pelvis, while the hips/thighs accommodate that task and the paw contact remains coherent. Increasing Sweep25's one common rigid-body rotation cannot introduce chest-versus-pelvis articulation.

## Exact evidence and method

Primary: owner-liked Sweep23 r01, `output/ssot_candidates/sweep23_fixedshoulder_20261003/r01/original/output.mp4`. SHA256 `21f8a76609d8bbaa3a100592d7f38ece48f469d622f0130e4532f635bd318fd4`. Decoded 180/180 frames, 960x960, 30 fps, 6 seconds. Original five chronological sheets were re-read, followed by six new 30-frame pose sheets and enlarged lower-body key frames.

`analyze.py` independently extracts visible color components in every frame: belly, near arm, broom collar, nose, exposed foot and the visible rear lower-body edge. The arm's upper/lower visible endpoints are observation proxies. They are **not** anatomical shoulder/wrist joints. The lower-body edge is **not** a reconstructed pelvis center. The two feet partly merge and the broom occludes their forward portions; side identity and hidden heel/toe position are intentionally not invented.

The first attempted lower-body centroid varied with belly visibility and broom occlusion. A second full-width lower silhouette measurement also split under the broom. Both were rejected as translation evidence. The final lower-body observation is the unobscured gray back edge in a fixed rear strip. This correction is important: apparent region-centroid motion must not be converted into a pelvis trajectory.

Human Pose Landmarker estimates human bodies and human landmark locations. No human model was installed or run here. The decision to use mascot-specific visible evidence is based on that documented scope, not a claim that every human model necessarily fails on this mascot. See [Google's model description](https://developers.google.com/edge/mediapipe/solutions/vision/pose_landmarker?hl=en). OpenCV supplies local image/component operations; no external model, upload, optical-flow skeleton or monocular 3D reconstruction is claimed.

## Measurements

All distances below are raw screen pixels, not world units, native control values, forces or 3D angles. Approximate clean-edge uncertainty is several pixels; occluded features are substantially less certain. The visible arm endpoint may also move as the arm changes orientation or passes under the head.

| Observable | Whole-clip excursion | Interpretation |
| --- | ---: | --- |
| Rear exposed foot right edge | 2 px | Stable support evidence, not a detectable step |
| Visible foot bottom | 1 px | No supported large foot lift in the visible region |
| Lower gray back edge | 6 px | Lower silhouette is much steadier than the upper action |
| Upper visible near-arm endpoint, X | 94.9 px | Large upper action; includes articulation and visibility effects |
| Broom green collar, X | 178.3 px | Large tool sweep relative to the contact base |
| Nose, X / Y | 51.6 / 67.6 px | Head changes position/presentation with the action |
| Visible belly area | 2,332–12,577 px squared | Strong presentation/occlusion change; not a body-volume measurement |

The rear-foot result stays 553–555 px when the dark-color cutoff is changed from 90 to 100 to 110 across all180 frames. That sensitivity check supports the stable visible edge, but does not establish unobserved contacts, depth or force.

Recovery provides an additional useful orientation cue. At frame61 the separate far-arm visible component is543px squared and the belly is2,633px squared. At frame75 they are2,385 and12,537px squared; at91 they fall to484 and2,550px squared. The image-left/image-right black-eye area ratio changes from0.179 at61 to0.275 at75, then0.182 at91. Both eye components are detected in all180 frames. These measurements, checked against the actual poses, support a changing presentation during recovery. They do not measure changing arm volume or a unique head/body yaw angle.

The actual same-time browser comparison at2.50s also shows the source's far arm and broader belly/face presentation while Sweep25 remains more oblique and its far arm is hidden. Camera differences prevent using that pair as a calibrated geometric error. It is a practical performance-reading difference to test in the native A/B pilot. Recovery should have its own chest unwind and head-attention behavior.

During frames0–33 the figure is close to still. Collar movement crosses a5px threshold at34, visible upper-arm endpoint crosses3px at35, and nose coordinates cross3px at36. These thresholds suggest closely coordinated preparation within roughly two source frames. They do **not** support claiming a measured foot-first force impulse or a precise universal70ms delay.

## Event reading

| Source interval | Observed event | Design implication |
| --- | --- | --- |
| 0–1.1 s | Stable held tool and posture | Preserve a readable supported rest |
| 1.13–1.63 s | Tool moves inward/forward, upper arm changes direction, head lowers/turns, belly presentation narrows | Coordinate chest preparation, local arm articulation and attention; no isolated hand translation |
| 1.67–2.10 s, frames50–63 | First broad reach extremum, collar within8px of its local minimum | Treat this as a held/slow work region, not one frame-exact target |
| 2.13–2.60 s | Tool returns near the feet and belly becomes more exposed; working posture persists | Separate recovery from complete return to rest |
| 2.87–3.07 s, frames86–92 | Second reach region | Reuse the same body/support mechanism |
| 3.10–3.63 s | Second recovery | Chest unwinds while the contact base stays coherent |
| 3.87–4.17 s, frames116–125 | Third reach region | Preserve the original three-stroke rhythm |
| 4.20–4.77 s | Tool and body settle toward initial presentation | Coordinate release of the work posture and attention |
| 4.8–5.97 s | Stable closing pose | Return without a hidden snap |

The collar's individual minima occur at frames56/90/122 (1.867/3.000/4.067 s), but they sit in broad near-extreme intervals. Earlier Sweep25 markers2.03/3.03/4.03 s were reasonable comparison poses, not measured instantaneous extrema. Keep that distinction. Bristle floor contact/loading is uncertain from this flat image; do not derive physical pressure from the fan's image Y alone.

## What is observed, inferred and authored

- **Observed, high confidence:** stable visible rear foot and floor line, three tool excursions, changing near-arm presentation, changing belly exposure, head movement.
- **Inferred, moderate confidence:** upper-body rotation/inclination relative to a stable support base, with lower-body accommodation; the coordinated change of upper arm, belly and head supports this reading. Arm occlusion and generated shape drift can explain some of each isolated feature.
- **Unresolved:** exact pelvis/chest yaw split, hidden hip/knee locations, forward paw contact during broom occlusion, left/right load ratio, true center of mass, sole roll and floor friction.
- **Authored for a future native pilot:** the amount of chest/pelvis separation, support softness, small balance displacement, local head compensation and delayed tail response. These are semantic performance choices, not source-coordinate fits.

A larger rigid body turn plus local arms/head is still a competing explanation for part of the image. A phase pilot should compare that baseline with the articulated design at the same hand/contact tasks. The independent front/side/top generations are supplemental qualitative evidence only; they cannot resolve exact hidden coordinates or synchronize this clip's contacts.

## Sweep25 architecture audit

Source inspection, not a fresh Blender probe: `sweep25/native.py`, `motion.py`, `body_frame.py`, and the underlying `chores214/build_base.py`.

1. Sweep25 rigidly rotates the joined body/thigh branch by one `Rz Ry Rx` around `(0, .03, -.03)`; the displayed paw branch is explicitly excluded. Relative chest-to-pelvis rotation is zero by construction.
2. The same body frame carries shoulder roots, articulated arms, the neck carrier and tail. Head-local attention is separate, but tail/root and pelvis/chest ownership are not separate in this layer.
3. Every main body angle is driven by the same `Work posture` and `Stroke` values. There is no independently timed balance/support response or torso unwind channel.
4. Sweep25 sets the old action channels to neutral. The foundation already has upper-body lean/roll/sway and stance controls, but the existence of those dormant properties does not establish usable chest twist or coherent combined support. The old body field operates on the body core and shoulder copy, not a newly qualified coupled torso/pelvis/thigh domain.
5. The current tool is derived from the world hand and floor contact. This is useful and should be retained, but the hand must be recomputed after any chest/support revision; otherwise the former grip solution becomes stale.

The earlier rigid/foot invariants prove correct implementation of Sweep25's restricted design. They do not prove source-performance completeness. The blanket rule that every body/thigh point must undergo one rigid transform must be replaced for the expanded candidate; face/rest identity and grip/contact checks remain required.

## Deliverables and limits

The pose evidence JSON, trace plot,17 key overlays, six complete chronological sheets, enlarged lower-body board and interactive comparison expose the observations. `RIG_DESIGN.md` and `rig-design.json` define the expanded responsibilities and a controlled native experiment. No new .blend, motion acceptance, physical simulation, full15-issue certification or production runtime is claimed.

This is main-agent analysis. It is not independent animation-reviewer sign-off. New native evaluation is deliberately not represented by the existing Sweep25 receipts.
