# Sweep31: the missing support-relative body motion

## Conclusion

The owner's reading is a better next design hypothesis than making the torso twist more. Sweep29 primarily reads as a broad, coordinated turn and inclination of the trunk, with the body carried toward the non-holding side and a sweep reaching that side's foot. Strong internal chest-versus-pelvis torsion is not established by the images. Sweep30 adds a controllable torsion field, but its chosen motion suppresses lower-body presentation and retains a much smaller working reach.

The next experiment should first reproduce common trunk/pelvis transport relative to the planted feet, with internal torso twist set to zero. Test the non-holding-foot pivot explicitly. Add only the residual differential turn that improves the observed performance. This is a revised mechanism proposal, not a claim that the hidden pivot or weight distribution has been recovered.

Scope: read-only analysis. Sweep29's original video and Sweep30's complete native and A/B movies are unchanged. No new native, generated source, adopted release, or independent-model review is claimed.

## Evidence and measurement

All120 source frames at30fps were inspected in chronological full-image and enlarged foot/trunk sheets. Seven full-resolution overlays and14 annotated keys expose feature ownership. Both exact Sweep30 front movies were decoded at60fps,240frames each; A/B key sheets and the prior complete continuous review are retained. Source and native measurements use their original960px and480px resolutions.

Measurements are image observables. The gray head-envelope midpoint is not a center of mass or rigid-body translation; the nose's offset inside it is a face-presentation cue, not a yaw angle. Cream-belly edges are fixed-height image contours, not tracked material particles, joints or section headings. Broom movement uses its clearly visible green binding, not the bristle tip or contact patch. Comparisons use range over the complete clip, normalized by the initial gray-head-envelope width (source443px; native221px). No video retiming or geometric fit was performed.

| Observable range, in percent of initial head width | Source29 | Sweep30 A | Sweep30 B | B / source |
| --- | ---: | ---: | ---: | ---: |
| Gray head-envelope midpoint X | 9.03 | 4.52 | 4.52 | 50% |
| Nose offset inside head envelope X | 11.94 | 13.52 | 13.50 | 113% |
| Nose X | 19.97 | 17.60 | 17.57 | 88% |
| Nose Y | 12.36 | 10.39 | 10.40 | 84% |
| Green broom binding X | 51.76 | 26.05 | 25.93 | 50% |
| Left cream-belly edge at image height67.5% | 7.67 | 5.66 | 4.52 | 59% |
| Left cream-belly edge at image height71.5% | 7.67 | 6.33 | 2.71 | 35% |
| Left cream-belly edge at image height76.5% | 10.38 | 8.14 | 3.62 | 35% |

Small A/B head/tool pixel differences come from independent compressed renders; native geometry checks established equal upper tasks. These ranges are diagnostics, not a composite quality score or calibrated motion amplitudes. In particular, do not read the head midpoint range as proof that root translation must be exactly doubled.

At the inward extreme, the source binding crosses the initial head-midpoint image axis by0.131head widths toward image-left. B remains0.160head widths on the holding side. In the images, the source broom reaches the non-holding foot region while B remains near the holding foot. This categorical missed sweep zone matters more than a small angle adjustment.

## What the source supports

- Image-left is the non-holding foot. Its sampled exposed outside edge is atx309 and sampled sole aty846 in all120frames. Both are unchanged when the dark-mask cutoff is90,100 or110.
- The holding-side sampled sole is also aty846 in all108unoccluded frames, across those cutoffs. The12obstructed samples are omitted. No step or sole lift is visible in the reviewed sequence.
- The holding-side inner edge ranges2px at cutoffs90/100 but11px at110. This is threshold-sensitive, so it is not accepted as a precise bound on foot movement. The previous global rightmost dark boundary is likewise not a paw marker.
- Both visible contacts stay in place. This supports planted-foot animation but does not prove that only the non-holding foot bears weight. Normal force, pressure distribution and the concealed contact patch are unavailable.
- From roughly1.4 to2.1s, the face presentation, cream belly and holding arm turn together into the sweep. The lower cream edge travels while the exposed outer gray lower-body boundary changes very little. A stable outside outline does not mean the pelvis orientation is fixed.
- The torso keeps a broad, simple shape; a pronounced wrung waist is not a dominant visible feature. Small internal torsion remains possible. Its magnitude and sign cannot be separated reliably from projection, inclination, occlusion and generated-image changes.
- The return reopens the belly and face while the tool returns. It should be treated as a coordinated action phase, not merely the same body amplitude scaled down.

The source is generated imagery from one uncalibrated frontal view. Its changing tail is not appearance authority. It does not provide anatomically consistent hidden joints or a mechanically exact rigid model.

## Where Sweep30 goes wrong

### 1. The mechanism was assumed before it was distinguished

The implementation authors chest yaw toward-15degrees and pelvis yaw toward-3degrees. Its sampled maximum relative yaw is-12.137degrees at2.067s. Those numbers were design choices, not source measurements. The earlier Sweep27 report explicitly called independent chest/pelvis torsion a testable choice; Sweep30 implemented it without first demonstrating that common supported body transport was insufficient.

### 2. Its support is vertical masking, not a side-specific support relationship

`torso_math.py` uses the same central pivot(0,0.03,-0.03) for every section. Support weights depend only on rest height. The lower fade and the independent yaw field can produce smooth deformation, but there is no selected support foot, no contact-relative root displacement, and no asymmetric hip/leg response tied to the non-holding side. A controller named Leg anchoring is not evidence of a load-bearing chain.

The paws are excluded from the moved body mask. Zero paw drift therefore validates preservation of those vertices; it does not validate the causal relationship from a support foot through a leg into the pelvis.

### 3. Quiet pelvis suppresses an observable part of the action

At the middle and lower sampled belly edges, B preserves only about35% of the source's normalized contour excursion. A has about83% and78%, respectively. This does not prove A's hidden mechanism, but it shows that the more articulated B is worse on these useful visible cues. Freezing the lower presentation to make chest torsion visible is not justified by the source.

### 4. Face turning substitutes for whole-character transport

B's nose-within-head presentation cue is already113% of the source range, while its head-envelope midpoint range is50%. Simply increasing the chest/head yaw is unlikely to address the missing spatial motion and could over-turn the face. Common trunk transport, inclination, and local neck attention need distinct responsibilities.

### 5. The inherited working stroke misses the action's destination

The green binding travels only half the source's normalized distance and never reaches the opposite foot region. Sweep30 deliberately retained the old local arm stroke to isolate the new field; that was a controlled implementation experiment, but it left a central performance failure untouched. Changing the torso field beneath identical shoulder/hand/tool tasks cannot fix this missing reach. The feature curves also expose a timing difference: the source retains its leftward head/belly presentation across a broader part of the inward/early-return phase, while the native response peaks and recovers more narrowly. Amplitude gains alone cannot correct that coordination.

### 6. A/B and the gates answered narrower questions

A and B share the central pivot and have equal chest, head, shoulder, arm, grip and broom tasks. A/B measures the lower field's effect under those fixed tasks. Neither case tests the owner's alternative pivot/body-transport hypothesis.

There is an additional attribution problem: A sets Torso articulation to0, which removes both differential yaw and the gray-leg anchoring fade; B enables both. A/B therefore does not isolate torso torsion alone. The existing C-no-relative-turn pilot is the closer yaw-only ablation because it retains leg anchoring. Even C keeps the same central pivot and shared upper motion, so it still cannot test support-relative transport.

The old RED establishes that the pre-extension native lacked four newly named controls. The GREEN checks establish that the chosen field, attachments, contacts, serialization and capture work as implemented. They are valid engineering evidence, but do not establish that the chosen mechanism improves the source performance. The prior report's disclosed full-release gaps remain open.

## Pivot versus translation: what can be concluded

For a common rigid transform, x' = P + R(x-P) + t. Changing the authoring pivot fromP toQ yields the same geometry when t is changed to t + (I-R)(P-Q). A pivot label alone is therefore not an independently observable physical fact if translation is also free. A single front projection is more ambiguous still.

The useful claim is operational: choose the non-holding contact as a reference, keep its contact task fixed, and coordinate common trunk motion and the connecting leg around it. That is a plausible compact authoring model for the owner's intended reading. It must beat the current central model in the visible performance and multi-view native checks. It must not be described as a uniquely recovered source pivot or measured weight transfer.

Both feet staying planted also prevents treating the entire character, including both paws, as one rotating rigid object. The trunk/pelvis can move mostly together while the gray legs/hips accommodate the fixed contacts. Internal torso torsion and leg accommodation are different deformations.

## Decision

Reframe the next native experiment around contact-relative common trunk transport, a source-sized working reach, and separately controlled head attention. Keep independent chest/pelvis controls as an available residual correction, with zero relative yaw in the first trial. Do not delete the functioning Sweep30 controls or broaden deformation merely to make them visibly active.

Read `RIG_RETHINK.md` for the falsifiable comparison and the order of work. This audit changes the interpretation and next design, not any accepted asset.

## Reproduction and bindings

Run `.venv/bin/python scripts/research/chores214_20260925/sweep31_support_audit/analyze.py`.
Data and all feature points: `v2/sweep31_support_audit/image-evidence.json`.
Actual controller audit: `rig-audit.json`. Source/script/native SHA256 bindings are included.

- Source29 original: f47916172a0d827d3e68527cfdd167d2dea7b3a357f5cca19f0ae804b861cd6a.
- Sweep30 native: 81f0a7904bc861989eb894c2be5aeca347b9aeec3ca5447870a24cd30eb7d793.
- Mechanism anchors: Sweep30 `torso_math.py` lines4-6,34-43,65-66; `native.py` lines70-89,109-110,119-125,154-170,383-392,410-424.
- Prior caution: Sweep27 `RIG_IMPLICATIONS.md`, especially the final instruction that a new field must not be assumed necessary because it has more controls.
