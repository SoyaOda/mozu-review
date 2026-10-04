# Sweep27: feet, support, pelvis and trunk audit

Completed source analysis, 2026-10-04. This pass specifically examines the questions left open by Sweep26: paw rotation, heel/toe pivots, ankle/hip accommodation, pelvis/chest separation and their timing. No native rig was changed. Source measurements do not drive native controls.

## Main finding

The source strongly supports a stable ground contact with a changing lower-body overlap and coordinated upper-body presentation. It does not establish a visible heel/toe rocking action, a measurable paw yaw, a foot-first impulse, or separately identifiable pelvis and chest yaw angles.

The distinction is important. The upper boundary of the black foot changes, but it is mostly the boundary where the gray lower body covers the foot. Tracking that line as an ankle bone would invent anatomy. The exposed foot/background boundary is much steadier. A stationary foot with changing body coverage remains a viable explanation; subtle foot rotation or compliance is also not ruled out.

The engineering consequence is to separate the contact constraint from the gray leg/hip/body accommodation and from chest/arm/head presentation. The evidence supports testing that design; it does not prove a unique internal skeleton or mandate a large new foot motion.

## Exact source and inspected coverage

Primary: the owner-liked oblique original, `output/ssot_candidates/sweep23_fixedshoulder_20261003/r01/original/output.mp4`.
SHA256 `21f8a76609d8bbaa3a100592d7f38ece48f469d622f0130e4532f635bd318fd4`.
All180 frames, 960x960, 30fps, 6s were decoded and measured. This pass visually inspects every frame again in six enlarged foot sheets and six torso sheets,17 lower-body keys, and boundary-classified work/recovery poses. Original frame pixels are retained; magnified sheets add no recovered detail.

Independent front-r03, side-r02 and top-r03 were inspected at six times each as supplemental evidence, with their hashes recorded. They were generated separately: they are not synchronized cameras of this oblique action. Front shows a changing torso presentation over a largely stable base; side supports small trunk inclination and stronger head attention; top occludes the hips and feet and cannot identify their rotation. None resolves the oblique source's hidden joints.

## Methods and quality controls

1. Measure exposed front and rear foot endpoints, flat sole strips, crown profiles and the dark/gray interface separately. These names refer to image regions, not proven anatomical left/right paws or heel/toe landmarks.
2. Mark tool occlusion and remove those observations. The front endpoint/sole has120 valid frames; the more conservative whole rear patch has101. The rear outer curve also has full-clip feature tracks. Missing samples are not treated as zero motion.
3. Inspect back contours at image heights675/700/725/750/775/790. These are visible surface slices, not vertebrae, hips or a spine centerline.
4. Track actual image features with Shi-Tomasi and pyramidal Lucas-Kanade, rejecting failed status, forward/backward error >=0.5px, patch error >=12 and tool-occluded patches. Nine of11 rear-region features survive all180 frames; no initial front, lower-trunk or mid-trunk feature survives the entire clip. Failed tracks are retained as missing evidence, not filled with an assumed skeleton.
5. Compare the common visible foot/background pixels to a fixed frame61 reference, excluding gray body/tool boundaries and a4px margin. This tests a stationary screen-space foot appearance without warping the source or fitting a native rig.
6. Repeat the dark-foot segmentation with thresholds90/100/110. The rear-edge range remains2px and the outer upper-boundary range remains6px. The front-edge range varies0–1px, showing the scale of raster-threshold sensitivity.

Optical flow is apparent 2D image motion, not a 3D bone or force measurement. Its brightness/local-motion assumptions and corner-based implementation are described in [OpenCV's official tutorial](https://docs.opencv.org/4.13.0/d4/dee/tutorial_optical_flow.html) and [tracking API](https://docs.opencv.org/4.13.0/dc/d6b/group__video__track.html). Here it is used only where its image evidence survives the checks.

During method development, a broad warm-color classifier incorrectly included cream belly pixels in the tool mask. It was corrected to exclude high-blue cream pixels and checked against actual shaft/belly pixels. Sparse antialias pixels from the adjacent brown tail were also removed from the foot/background comparison by retaining only dark components connected to the sole. These corrected methods generated the delivered receipts.

## Feet: translation, rotation, rocking and overlap

| Observation | Measured result | What it supports |
| --- | --- | --- |
| Image-front exposed endpoint | X340 at threshold100 in120 valid frames;0–1px range across thresholds | No resolved large front-tip translation in the exposed intervals |
| Image-rear exposed endpoint | X553–555 in101 conservative patch observations | Stable rear extent; not proof of zero paw yaw |
| Flat sole strips | Median Y846 for both exposed strips | No resolved lift of those contact strips |
| A full-clip sole feature initially at535,846 | X range0.154px, Y range0.140px | A stable image contact feature; subpixel precision is not physical accuracy |
| Mid rear upper boundary atX520 | Y797–799 over180 frames | Small change at the gray-leg/black-foot boundary |
| Outer rear upper boundary atX552 | Y808–814 over180 frames | Larger change near a curved junction; not a bone angle |
| Tracked upper junction initially555,810 | X range3.54px, Y range8.09px | A changing surface intersection/occlusion feature |
| Common foot/background appearance versus frame61 | At most20 changed class pixels; maximum change distance3.60px; at least7,673 common pixels | Fixed screen-space support remains plausible after occluders are excluded |

The fixed-foot comparison's maximum changed fraction is0.245% of the common classifiable pixels. It is not a whole-foot IoU or a bound on hidden geometry. Small differences include the central sole notch and the outer rounded edge. A small yaw or local deformation can leave nearly the same silhouette, so this comparison cannot certify zero rotation.

The upper-junction excursion must not be labeled8px of ankle lift. At the work pose, the gray lower body shifts against the black foot; during recovery, that covering boundary changes again. The colored boundary views distinguish external silhouette in green, gray-body coverage in orange and tool occlusion in magenta. The red tracked point lies near their junction, not inside a visible joint.

The flat exposed sole and stable ends do not support a large heel-up/toe-up rocker. The image does not expose anatomical heel/toe landmarks or distinguish the two paws reliably where their black silhouettes merge. A vertical-axis paw swivel on a small contact patch, or internal leg twist above a planted paw, remains possible but unmeasured. No angle or left/right weight ratio should be assigned from these images.

## Lower body, pelvis and trunk

The back contour changes increasingly toward the upper measured region. Whole-clip screen-X ranges are12px atY675,10px at700,8px at725,6px at750/775 and4px at790. At frame61 the upper sample moves11px image-left from rest while the lower sample moves4px; at75 they recover to5px and0px image-left, respectively.

This demonstrates differential projected motion above the contact base. It is compatible with inclination, orientation change and local shape/coverage changes. A single rigid body inclination can also produce different displacements at different heights, so this observation alone does not prove internal torso torsion. The recorded back-contour chord varies by4.93 projected degrees; it is explicitly not a spine pitch or chest/pelvis yaw angle.

There is no stable visual marker for each hip joint, no separate visible thigh axis, and no reliable bilateral pelvis line in the oblique clip. Gray body and short legs merge into one smooth region. Accordingly:

- Hip/ankle accommodation above the supported feet is a reasonable mechanism to test, not a measured joint trajectory.
- Pelvis rotation cannot be separated uniquely from torso inclination or shape drift.
- Chest turning during work/recovery is supported by the combined arm, belly and face presentation, but the split between chest yaw, shoulder articulation, local head yaw and occlusion is not uniquely observable.
- Counter-rotation of pelvis versus chest, or an ordered foot-to-hip-to-spine torque transfer, is not demonstrated.

## Corrected belly evidence and recovery

Sweep26 retained only the largest cream component. An arm or shaft can split the visible belly into disconnected regions; the older number then drops visible lower cream. Its area must not be read as total belly exposure or converted to torso yaw. This is a correction to the earlier interpretation, not new motion in the source.

This pass retains all cream components inside the same fixed lower-body ROI, X320–460/Y650–780, below the face. The total varies2,344–9,400px squared. At work61 it is2,528; at recovery75 it is9,356; at work90 it is2,357; at recovery106 it is9,197. The ROI and definition differ from Sweep26, so those numbers must not be mixed.

Even the corrected area is affected by arm/tool occlusion and cannot by itself prove a yaw angle. A more useful pose reading combines the reappearance of the far arm, the belly presentation, the back profile and the previously measured change in the two-eye visibility ratio. The recovery poses at2.50/3.53s are more open toward the viewer while a working posture remains. This is a real performance cue to reproduce semantically, rather than treating recovery as merely the reverse hand path.

## Timing and sequence

| Phase | Source frames / time | Supported interpretation |
| --- | --- | --- |
| Held | 0–33 /0–1.10s | Stable support and held tool |
| Preparation | 34–49 /1.13–1.63s | Tool and arm begin; upper-body presentation and lower covering contour change within the preparation |
| First work region | 50–63 /1.67–2.10s | Reach is held/slowed; contact stays stable and upper foot/body junction is displaced |
| First recovery | 64–80 /2.13–2.67s | Torso/arm/face presentation opens; foot remains supported |
| Second work/recovery | 86–92 then94–109 /2.87–3.07 then3.13–3.63s | The same supported organization repeats |
| Third work | 116–125 /3.87–4.17s | Similar reach and lower support relationship |
| Settle | 126–143 /4.20–4.77s | Working presentation releases toward rest without a step |

For a reproducible diagnostic, three consecutive samples cross the declared thresholds at collarX5px:frame34, upper-backX3px:40, upper-foot-junctionY3px:43, lower-backX3px:46. The sole track never crosses1px. These are different image features with different amplitudes and thresholds. They do not establish causal joint onset order or a measured0.2/0.4-second body delay. In particular, there is no measured foot-first impulse here.

## Competing explanations

| Hypothesis | Current evidence |
| --- | --- |
| Stable paw shapes with changing gray-body coverage, body inclination and arm/head articulation | Viable; the common external foot silhouette test does not reject it |
| Small paw swivel or compliant ankle/hip response above stable contact | Also possible; lacks an identifiable paw axis or joint marker |
| Pronounced heel/toe rocking or alternating lifted feet | Not supported by the exposed sole and endpoint observations |
| Independent pelvis/chest torsion | Useful rig capability to test; its exact amount and even unique necessity are not proven by this monocular source |

The earlier statement that a single body frame is necessarily insufficient was too categorical as a claim about the source's hidden mechanism. Sweep25 visibly misses part of the recovery presentation, and it lacks independent chest/pelvis controls by construction. Those are separate facts. A controlled native comparison should decide which extra freedom improves the performance without inventing foot motion.

## Completion and practical limit

The requested foot/leg/pelvis/trunk questions have been examined at visible-boundary, feature-track, phase and observability levels. Detailed records, all180-frame foot/torso sheets, boundary overlays and an interactive full/crop viewer are delivered. No hidden-joint estimate is claimed where the clip cannot identify one.

See RIG_IMPLICATIONS.md for the revised design experiment. This is main-agent analysis, not independent motion approval. No new .blend, generated video, adopted release or mechanical fitting was produced.
