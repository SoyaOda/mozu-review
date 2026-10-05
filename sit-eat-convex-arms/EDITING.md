# Convex eating-arm candidate

Native: `mozu-siteat212-convex-arms-r03.blend` in the matching output folder.
Qualification is recorded by `pilot-r03/report.json`, `pilot-r03-review.json`,
`audit-r03/report.json` and `full-visual-review.json`; an absent or incomplete
record is not a pass. This candidate does not replace an adopted release.

Select `SE212C | Convex arm envelope`. The final Geometry Nodes modifier on
each arm is unapplied and operates during native playback. The original
SE212F action channels and their keyframes still own the movement.

| Control | Default | Meaning |
| --- | --- | --- |
| Width | 1 | One uniform transverse multiplier, bounded to0.85–1.15 |
| Shoulder seat | 1 | Put the shoulder reference at the proximal cap center;0 puts it at the pole |
| Attachment clearance | 1 | Solve the complete proximal cap below the body-owned upper guide;0 is a diagnostic bypass |
| Attachment burial | 1 | Solve the complete proximal cap inside the actual body facets;0 is a diagnostic bypass |
| Enabled | 1 | Whole-construction diagnostic bypass;0 restores the inherited arm |

The original A126 Thickness is inherited as a uniform base multiplier. There
are no per-frame outline controls, local radius edits or camera-dependent
deformations. Do not blend a separately deformed surface into this envelope.
Non-meal locomotion modes bypass this modifier exactly.

The inherited surface-pole point is the unchanged body-bound upper guide.
The internal shoulder is solved below that guide and toward the body's live
axis, keeping the whole proximal ellipsoid inside the body. Surface vertex0
is the closed cap's pole and intentionally moves. The grip remains the
original material vertex1937, including its exact position. Tests must compare
the internal shoulder reference, not require the moved surface pole to stay
fixed. The named final fields `se212c_guide`, `se212c_shoulder`, `se212c_grip`,
`se212c_body_up`, `se212c_drop`, `se212c_support`, `se212c_burial_fraction`,
`se212c_frame_margin` and `se212c_determinant` expose the live task contract.

Keep shoulder-to-grip reach nonzero and the material transverse-frame margin
at least0.5. Recheck edited movement over its whole duration, not only the
pose where a control was changed. Width and seat edits preserve the analytic
convex family; they can still alter visible overlap with the head/body or the
hand's appearance against the food. Those are separate visual requirements.
Both attachment controls must stay at1 for the attachment qualification.
The body-axis endpoint must contain the cap with positive clearance; the
smooth inward fraction must stay below0.9 and the map determinant above0.1.
The current body has36866 source vertices and73728 triangles. A topology
change requires rebuilding and revalidating its material-axis/facet contract.

The current meal's input trajectories are retained. This does not qualify
arbitrary wrist rolls, other performances, a skeletal runtime export or the
project's broader15-issue/11-gate release program. There is no anatomical
two-link elbow in the new shape family. It is a single rounded stylized arm.

The saved native contains neither evaluated character meshes nor food caches
for playback. Review rendering may reuse six verified static food CSG states
in memory only; shoulder, arm, grip and character deformation remain live.
Opening the native requires no external Python playback handler.
