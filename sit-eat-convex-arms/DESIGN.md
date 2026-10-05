# Shape constraints before animation

Owner direction, 2026-10-05: extend the original mathematical arm constraints;
avoid mechanical fitting and local optima. The previous fair-arm candidate is
reopened after a residual wavy/tapered oblique outline at frame1061 (17.67s).
Feet, seated mechanics, face and the complete meal remain protected.

Current implementation is r03: the convex shape below, an analytic body-space
shoulder ceiling, and C1 body-facet containment of the complete proximal cap.
See ATTACHMENT.md for the derivation and rejected intermediate prototypes.
r01 and r02 passed their shape checks but failed assembled appearance. They
remain preserved. The unchanged body-bound point is an upper guide; the new
internal joint is solved below it and inside the body, with the grip held exact.

## What the previous implementations actually guarantee

Arm124/126 uses a fixed round-capped club profile and constant-curvature arc.
`scripts/research/arm124_20260918/model.py` defines the profile and public domain;
`verify.py` checks the curvature-radius factor. Its documented guarantee is
local sweep regularity, not every projected silhouette or inter-part clearance.
The original smoothstep radius transition itself is not a convexity proof.

The SE212 articulated extension composes another localized elbow curvature.
The current meal's kGirth/kPaw are both1; local width animation is not the
observed cause. The subsequent fair layer preserves those section radii but
replaces the centerline with a shallow quadratic and blends surfaces near rest.
Positive volume, monotone stations and smooth centerlines do not constrain the
whole solid's contour class. The earlier review therefore overstated resolution.

## Construction, without an image objective

Use the convex hull of two balls as a round-capped club. In an axial coordinate
q, the first center is a, the second L-b, with radii a and b. The common tangent
joins the two circular caps. Set d=L-a-b>|b-a|, n=-(b-a)/d, c=sqrt(1-n*n).
The joins are q0=a*(1+n), q1=L-b+b*n; the middle radius has slope -n/c.
Both radius and first derivative agree at the joins. The radius is concave;
there is no radius valley or alternating local swelling. The surface has a
continuous tangent, with a curvature change at the cap/cone joins (C1, not C2).

Dimensions originate in motion126/model.json: length0.78328305, proximal radius
0.11998972, distal radius0.14386844, depth ratio0.85. The old global Thickness
remains a uniform scale. No frame-specific taper, image residual or optimizer
is involved. The original65 material rings/32 azimuth samples remain the scaffold.

The template's shoulder is an internal attachment reference, rather than a
zero-radius surface pole. Shoulder seat e in[0,1] adds e*a to the template's
total length and places the internal reference at q=e*a. At e=1 the shoulder
lies at the proximal cap center. This provides a nonzero proximal section and
extends the closed end behind the joint. Vertex0 therefore intentionally moves.
In r03 the internal joint is solved below the unchanged body-bound upper guide,
so the proximal ellipsoid's upper support touches that guide in the live body's
up direction. Default e=1 is a geometric convention, not a fitted frame parameter.

The original shoulder guide and food-grip trajectories define a single affine map
of the whole template. The map sends the template origin to the solved shoulder
and material vertex1937 to the original grip. One evaluated material section
defines a transverse frame; there is no camera input. Its determinant
is explicitly checked after both analytic shoulder corrections. The proximal
support quadratic must also have a positive leading coefficient and real root.
Each of the unchanged body's73728 facet planes supplies an analytic inward
entry bound. A C1 upper positive-part and an L32 aggregate dominate those
bounds without a hard maximum or iterative fitting. The body-axis endpoint
must be feasible, and the selected fraction stays strictly below0.9.
Every pose remains in the same convex shape family. No local post-deformation,
elbow-band correction or blend with a nonconvex surface is allowed in the
qualified mode. An explicit diagnostic bypass remains separate from that domain.

For fixed positive width and seat, the task map is differentiable while reach
and transverse-frame margin remain nonzero. The current animation never crosses
a mode switch or clamp boundary. Thus the extension does not introduce a new
temporal corner into the inherited smooth task trajectories.

A convex set stays convex under an affine map, including an orthographic
projection. Thus the unoccluded arm cannot develop a concave notch in any view.
This construction uses that preservation result, not an optimization solver.
Reference: Boyd and Vandenberghe, Convex Optimization, section2.3.2,
https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf .

This is a deliberately stricter shape family than the old curved tube. It does
not promise articulated elbow anatomy or exact preservation of the old neutral
arm surface. Shoulder/grip tasks and the non-arm performance stay protected.

## Guarantees and limits must remain separate

Analytic domain: positive radii/depth/width; separated cap centers; positive
shoulder-to-grip reach; transverse material-frame sine margin>=0.5; seat[0,1];
uniform width[0.85,1.15]. The proximal cap must remain inside every body facet,
the axis endpoint must have positive clearance, and active facets must remain
away from the near-parallel denominator guard. The native and validators use
the same equations; validators reject poses outside this domain. UI ranges
alone do not prove that arbitrary combinations or new motions are feasible.
No geometric theorem alone establishes a pleasing full character. Head/body
occlusion can make a visible portion pointed even when the complete arm is
convex. Attachment, cap burial, hand/food contact and full-character views need
their own checks. If current task paths are infeasible, report and revise their
shared motion design; do not add camera-dependent shape compensation.

Before a full render: mathematical boundary/covariance tests, actual-native
RED on the previous solid's supporting-plane violation, GREEN on the new
model, protected-part/grip comparisons, save/reopen/edit/reset, other-mode
bypass, dense subframes, whole/isolated/clay views and predeclared held-out
reach/orientation cases. Full meal review and public delivery follow only when
the small pilot resolves both standalone shape and assembled attachment.

Main-agent review only. No owner adoption, broad15issue/11gate closure or export
to another runtime is implied. Previous natives, evidence and public pages are
preserved. Active implementation/evidence: arm_contract_20261005.

## Finite-precision native certificate

First actual-native run20261005-014727-4bffc2bf reproduced the previous shape's
supporting-plane violation0.0699001. It then stopped on the new float32 mesh:
raw facet violation3.06447e-6, although coordinate parity was below2e-6.
Near-coplanar cone facets amplify tiny coordinate rounding in their normals.
This failed test and its original source are preserved in attempt-r01.

The corrected certificate retains the same2e-6 coordinate-error bound. It checks
the exact float64 affine envelope's convexity, native correspondence to every
vertex, and native vertices against all exact supporting planes. Cauchy-Schwarz
bounds each normal displacement by sqrt(3)*2e-6 plus the exact-plane numerical
bound. Raw native-facet violations remain recorded as diagnostics. We certify
the native surface's bounded proximity to a convex solid; we do not claim exact
convexity of its rounded float32 triangles. A0.005 local perturbation is rejected.
The envelope implementation was not changed to address this measurement issue.

## Verification execution continuation

Run20261005-015511-cb2d6b23 passed24 actual-native/protected poses,6 save/reopen
comparisons,4 edit/reset probes,3 other-mode bypasses and40 dense times. Maximum
native coordinate error was4.36039e-7. The native was saved before these probes.
The raw scene reevaluated unchanged food CSG on arm-control updates, making the
dense section expensive. After1373seconds the harness was deliberately stopped
(rc130); its completed prefix and execution receipt are retained. This was not
a geometry failure or a candidate rebuild.

Continuation20261005-021954-f528d9ae opens the identical saved native, retains
that exact prefix, and first compares15 food states/ingestion transitions with
the disposable six-state food cache. Remaining arm subframes are still live
native evaluations with the same2e-6 gate. Pilot rendering uses the established
pruned review scene. No food cache is saved to the native. Direct/cached pixel
parity is separately required before the full movie capture.
