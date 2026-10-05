# Preserve the original arm; author a feasible meal

This is an unadopted native-motion experiment. The rejected convex prototype is
not its geometric authority. Original Arm124/126 material sections, rounded ends,
constant base arc and the existing shoulder attachment are the authority.

## A shape-preserving motion family

Let V0 be the actual evaluated original default arm and v0 its first material
vertex. For every current motion pose the intended surface is

`V(t) = Q(t) (V0 - v0) + r(t)`.

Q is one proper rotation. For the right arm it is
`Rx(Swing) Rz(-dForward) Ry(-dRaise)` relative to the original default.
For the left arm, insert the existing X reflection on both sides of the last
two rotations. Its two reflections cancel in the determinant; Q is still proper.
This preserves every within-arm distance, section, cap and volume. It adds no
localized elbow, length change, radius warp or different neutral silhouette.

The native is not a baked surface behind a pass-through modifier. The existing
unapplied material-frame Geometry Nodes reconstruct the original profile;
dBend/Elbow/Wrist/Wrist side/Paw roll are zero and kStretch/kGirth/kPaw are1.
The artist edits three shoulder-orientation curves. Editing deformation controls
outside this family requires a new qualification; it is not automatically safe.

## Preserve the actual shoulder, including transitions

The original body point is `s = sum(w_i B_i(t)) + offset`, with the unchanged
material triangle, barycentric weights and signed offset. Let g be the incoming
legacy shoulder and f the unchanged Surface follow curve. Its authored root is
`r0 = g + f (s - g)`. Original blend, alpha, previously mixed whole shapes and
therefore also mixed their roots. The actual original root was

`r = r0 + alpha (g - r0)`.

The new final node uses that same root formula and leaves f and alpha unchanged.
Only the old *shape* interpolation is removed. Replacing alpha by zero outright
would move the shoulder during the handoff; that shortcut is not used here.
No lower/inward replacement shoulder, hidden cap extension or body change is made.

## Reach and held food belong to one action

The original material grip lies about0.8184units from its shoulder. The previous
meal requested approximately0.94–1.00 through arm stretch and added curvature.
Retaining that old trajectory is incompatible with this fixed-shape family.
The new sparse C1 keys therefore author a lift/hold/lower gesture within the
original reach. Six mouthful times, head expressions and the liked feet remain.

R01 kept the old food-depth relation and failed: food entered the closed head
too deeply, and one final grip separated. R02 tests a centered cradle: cancel
the old0.1depth offset so food lies on the live paw-tip line, and gather both
original arms3.5degrees after the fourth bite for the smaller remaining piece.
This is a change of holding relationship, not a camera-specific arm deformation.
R02 improved depth but failed the fourth contact and final grip. Read-only20/35degree
edge-presentation trials improved the lower-remnant direction but did not solve every
contact. R03 tests staged pitch and a narrower, slightly deeper final-piece cradle;
see PLAN and the output ledger. R04 then completes the fifth-cut regrip while
withdrawing, uses the gentler35degree lower-edge pose and spreads food turns over
the lowered holds. Its27-image pilot is visually qualified for the next audit,
with the recorded small contact/head-overlap limits. It is not a full meal pass.

## Evidence and limits

R01: original-source meshes and all other actions remain exact. Ten native poses
have zero shoulder error and at most1.311e-7 surface error from the original rigid
family. Three saved/reopened poses and six control edits/reset checks pass. All60
initial pilot images were inspected. At standing frame1, decoded matching
Front/Oblique/Side images equal the original predecessor pixel-for-pixel.

The original arm can be foreshortened or partly hidden by the head/body in a
projection. Preserving its3D surface does not make every assembled visible mask
convex, certify arbitrary controls, prove a physical mouth cavity, or provide a
runtime export. Owner adoption and broader native-release qualification remain open.
