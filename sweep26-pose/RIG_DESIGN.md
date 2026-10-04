# Sweep26 whole-body rig extension

Status: concrete design for a new candidate; not yet a native implementation. Evidence: REPORT.md. Primary source and accepted-rest identity remain separate authorities. Mechanical fitting is prohibited.

## Responsibility graph

```text
Authored action events / work intention
  -> support/contact state + balance intention
       -> left/right paw contact frames
       -> pelvis frame and bilateral hip/thigh accommodation
            -> broad torso deformation -> chest material frame
                 -> left/right shoulder frames -> local arm articulation
                      -> world grip -> broom orientation/contact
                 -> neck frame -> intact head + local attention
            -> pelvis-bound tail root -> existing tail response
```

This is one acyclic evaluation graph. Source pixels are observation outputs only; they are not inputs to the rig, control drivers or an optimizer. A world grip or shoulder position must not be read back to drive its own ancestor.

## Small public control interface

| Control | Meaning and owner | Initial experiment domain (authored, not measured) |
| --- | --- | --- |
| Work posture | Overall preparation/settling envelope | 0–1 |
| Sweep phase | Three authored reach/recovery events | C1 or smoother curves, separate from posture |
| Balance intention | Direction and small pelvis accommodation over support | Start0; test lateral/forward shifts up to1% of character height |
| Pelvis heading / incline | Lower frame, independent of chest | Heading±4deg; incline±3deg |
| Chest relative heading / incline | Orientation relative to pelvis | Heading±12deg; forward incline0–8deg |
| Support softness | Bilateral hip/thigh response to pelvis task | Start low; test0/0.5/1 at the same end constraints |
| Paw contact mode L/R | Supported surface, optional roll, or explicit release | Both supported for the first sweep pilot |
| Shoulder reach L/R | Local shoulder orientation, broad elbow articulation | Reuse original fixed-length arm controls and their declared domains |
| Attention / head stabilization | Local look direction and compensation on chest-bound neck | Preserve complete rigid head; verify eyes/ears/muzzle together |
| Return relaxation | Chest unwind and arm recovery after work | Separate phase curve; no forced exact phase delay from pixels |
| Tail response | Small pelvis-rooted follow-through | Reuse existing tail controls; no added sway until primary action reads correctly |

These values are a predeclared pilot range, not a proven safe domain. Do not multiply all controls by one Stroke scalar. Preserve a zero-valued neutral state and an explicit bypass to the candidate's exact input geometry. A body-relative shoulder offset is not permitted to drift as an arbitrary world-space path.

## Support and leg mechanics

The constraint is stable **contact**, not an immutable foot object and rigid thigh. Keep each planted contact point and tangent-plane relation coherent while allowing pelvis/hip accommodation. The first source-derived sweep should keep both paws supported; no step or large sole roll is justified by the visible evidence.

Existing P173/W205 stance pitch/roll/yaw and current paw support geometry are reuse candidates, not automatically valid for this action. Establish their actual evaluated owners in the new native, then bind the shown joined paw branch, not only hidden source meshes. A foot rolling mode must pivot about a declared contact anchor and solve height from the current sole; rotating around the object origin is insufficient. Do not introduce roll just because the control exists.

Hip frames receive pelvis motion; ankle/contact frames receive support tasks. Distribute their relative transform across the full connected thigh/hip domain. Do not push all displacement into a narrow ankle strip or turn the rounded leg into a telescoping cylinder. No visible knee needs to be invented for this short-legged mascot. Preserve paw identity and inspect hidden caps when changing the attachment.

## Torso and attachments

Implement a broad pelvis-to-chest deformation, with a stable rest-material coordinate/binding. Compare a centerline/frame field plus limited pose corrections against the existing rigid baseline at equal contact and hand tasks. The chest endpoint frame and pelvis endpoint frame must be independently controllable; a smooth scalar called Twist is not enough if both endpoints still use the same rotation.

Do not attach the head to a raw sheared matrix. Orthonormalize the transported material frame; apply intact head-local attention afterward. Both original arm roots follow the chest material frame; original arm shape/length and local elbow controls remain the source of reach. The tail root follows the pelvis/lower trunk, with later response in its existing angular chain. This removes the current obligation for tail and chest to turn identically.

The body and belly pigment share one deformation/material-coordinate owner. Reuse the original rest-coordinate shading; do not transfer color by nearest body/thigh point. Neutral appearance must return exactly. Any topology change invalidates the old binding and requires a new hash-bound transfer.

Treat recovery as an authored pose with its own presentation: the original exposes more far arm and belly near2.50/3.53s and changes the eye-area relationship. Let the chest unwind while retaining work posture and allow local head stabilization/attention. Do not force the free arm to remain invisible; first obtain the appropriate torso orientation, then adjust only its supported local articulation. Preserve the accepted face geometry even when its projected appearance changes.

## Tool responsibility

Evaluate support, pelvis, chest and arm FK first. Derive world grip from the same material location on the arm. Solve the unchanged broom's orientation/contact from that grip and an authored sweep heading. Reject unreachable combinations; do not shorten the shaft or stretch the arm to hide them. Separate blade contact from relaxed return, but do not claim inferred physical bristle pressure from source pixels.

## Integration boundaries

Create a new candidate from the preserved action basis. Do not add the new field on top of active Sweep25 rigid posture or dormant CD214 lean: choose one body owner in the new candidate. Reuse the original arm generator, world-grip computation, source/media provenance and native capture parity machinery. Replace Sweep25's rigid-body verifier with region-specific invariants for head/paws/arms plus complete body-surface quality checks.

Known native entry points to inspect: `A189 | E final character`, `C164 | Body-owned convex core`, retained180 thighs, parametric separate paws, `S126 | Body-bound shoulders`, `M132 | Neck articulation`, `TAIL101 | Parametric envelope surface`, and `P173 | Contact and planted paw tasks`. The previous source audit identifies these; a new native edit requires fresh owner/effect probes.

## Controlled first experiment

Use six source events: held0, preparation42, first-work61, recovery75, second-work91 and settling142. Keep native camera, accepted shape, material, tool dimensions and hand/contact tasks equal between variants.

- A: existing one-body-frame mechanism, with conservative authored posture and original arms.
- B: pelvis/chest separation, broad torso accommodation, bilateral supported hips; same tool task.
- Ablations: B with chest-relative rotation0; B with pelvis response0; B with local attention0. These identify which layer changes the reading.

Inspect front/oblique/side/top whole views plus shaded torso/hip/ankle views before a complete sequence. Compare whether the work reads as a stable lower base with an engaged, turning upper body. More motion is not automatically better. Do not choose a variant using a pixel-fit score.

## Required native evidence for the later implementation

1. Exact neutral/bypass and protected head/arm/paw material geometry; separate chest/pelvis controls change the intended evaluated domains and restore them.
2. Current sole/contact error, no slipping at planted anchors, floor containment and feasible grip length across work/recovery and support-control boundaries.
3. Complete body/thigh surface, thickness, silhouette and pigment continuity in isolated and joined shaded views. Reject folds, ridges, pinching, local bulges or a moving cuff even when numerical Jacobian tests pass.
4. Shoulder/neck/tail attachment frames follow their declared owner. Reopen, edit each meaningful public control, restore and compare actual geometry; no custom playback callback.
5. Same mechanism handles opposite sweep direction, reduced amplitude and a small asymmetric reach without re-binding. Evaluate60fps and adaptive subframes after the pose pilot; preserve smooth event transitions.
6. Re-review complete output and browser playback. Existing Sweep25 checks cannot certify this new deformation. Track native-development I02/I03/I08/I09/I11/I12/I13/I14/I15; do not mark other open issue groups closed by this scoped experiment.

The next engineering deliverable is this small native A/B phase pilot. Full-loop rendering should follow a visually successful pilot, not precede it. Current task deliverables are the completed source analysis and this design specification.
