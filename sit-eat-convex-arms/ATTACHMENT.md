# Proximal envelope at a body-owned upper guide

The r01 native passed its mathematical, native and editing checks. All84 pilot
images were inspected, including full-size frame1061 oblique. Standalone arms
are smooth and convex; assembled side/oblique raised poses still have a thin
attachment because the head hides the upper proximal envelope. This is a
visual failure. The r01 review does not qualify it for full capture or publication.

The old surface-pole shoulder must not simply become the center of a new rounded
end. Use that same body-bound point as an upper shoulder guide. Position the
entire proximal ellipsoid below the guide in the live body's upward direction.
Keep the original grip exact. The cap dimensions, all non-arm geometry, source
movement keys and food tasks remain protected.

The live body-up vector is the normalized difference of the body's immutable
material poles, indices0 and36865 (36,866 vertices). These are the bottom and
top poles in both default-G.npz and start-mode3.npz, whose body arrays agree.
Their native meaning and evaluated direction must be checked in the pilot.
This is a body-space convention, not a screen-down shift or a selected-frame fit.

Let the r01 map be M=[X,Y,Z], guide R, grip G, normalized body up U and grip
template height z. Let a be the proximal radius, d the template depth ratio,
and c=a*(1-seat) the proximal sphere center's template height. Put the internal
joint at R-delta*U and replace Z by Z+(delta/z)*U. The complete arm remains one
affine image of the same convex template, and its grip is unchanged exactly.
X and Y retain the original material frame; they are not recomputed against the
shifted reach, which makes the clearance equation analytic and covariant.

Set t=Z dot U, k=(X dot U)^2+(d*Y dot U)^2, f=1-c/z and h=c*t.
The proximal ellipsoid's upper support relative to the guide is

    -delta + c*(t+delta/z) + a*sqrt(k+(t+delta/z)^2).

Set that support to zero. With A=f*f-(a/z)^2, B=f*h+a*a*t/z and
C=h*h-a*a*(k+t*t), the nonnegative solution is

    delta = (B + sqrt(B*B-A*C)) / A.

The domain requires A>0 and a nonsingular resulting map. This is a closed-form
support constraint, with no iterative fitting, camera input or per-frame
parameter table. At the default seat1 it places the complete proximal
ellipsoid below the original body shoulder guide. The convex-solid certificate
and the grip task are retained. The internal joint intentionally changes; the
upper guide remains the body-owned invariant and must be tested separately.

This ceiling does not, on its own, certify every head/body intersection or a
pleasing assembled silhouette. The next native pilot must verify both the
analytic support condition and whole-character attachment across views before
another complete movie is rendered. r01 and its failed visual review remain
preserved as causal evidence.

## r02 result and body-contained joint prototype

r02 native885307d6b4a4d7e700efaab6784dae4ad505f3428a9068c185d5aac6d207bb95
passed the ceiling, exact grip, six protected poses, three reopen comparisons
and four edit/reset probes. All36 images were inspected. Whole side/oblique
poses215/1061 still show a narrowed attachment and a small exposed proximal
lobe. The visual review is FAIL, and no full r02 capture is permitted.

Occlusion probe20261005-031935-0688cb50 removes the actual instanced cranial
cage. The lower attachment neck remains without the head; the isolated arm
is convex. Native body-cap support is negative before burial. This identifies
body occlusion as the remaining attachment cause. The probe's `no-body`
variant hid the non-renderable body source instead of the visible A189 joined
assembly; those images are ineffective and are excluded from causal evidence.
The whole, no-head and isolated-arm variants remain useful.

The next prototype moves the internal joint toward the live body's material
axis in the plane perpendicular to body-up. Its fixed halfway position is an
anatomical depth convention; no per-frame optimization drives the animation.
The axial affine column changes by the opposite translation divided by the
grip's template height, so the grip remains exact. The move is perpendicular
to body-up, so the proximal upper support stays unchanged.

For validation, every actual body facet n dot x <= b bounds the complete
proximal ellipsoid: n dot center + a*norm(E transpose*n) <= b-margin, where
E is the affine matrix with its second column multiplied by the depth ratio.
The moving center and axial column are linear in a candidate inward fraction.
Each facet therefore gives a quadratic entry bound. The largest entry bound
certifies the minimum sufficient depth. The runtime uses the fixed depth,
not that nonsmooth maximum. The body is the unchanged C164 closed source;
its73728 triangles and actual pose vertices are read from the native.

The prototype preserves the single affine convex arm family, uses no frame
number or camera in its shape construction, and rejects a pose/control setting
if its proximal ellipsoid cannot fit at the chosen depth. Full validation must
also retain the actual visible A189 assembled body/paws, not just the hidden
source parts. The new shape is not accepted until whole-character pilot views
and live Geometry Nodes parity pass.

## C1 conservative facet aggregation

The fixed-halfway prototype passes full cap containment but visually hides too
much of the neutral arm. It is rejected as a performance candidate; its18
images and direct-math geometry are preserved. No r03 native was saved from it.

The revised depth is an explicit smooth bound, not a fitted pose table or a
search. Let V be the inward vector toward the body axis, z the grip coordinate,
f=1-c/z, q=n dot Z, v=n dot V, k=(n dot X)^2+(d*n dot Y)^2 and
D=b-margin-n dot center. Put A=f*f-(a/z)^2. A facet's inward entry fraction is

    r = (f*D - a*a*q/z - a*sqrt((D/z-f*q)^2 + A*k)) / (A*v),

for planes opposing the inward move. The body-axis endpoint must strictly
contain the cap; the domain excludes an active near-parallel facet. A guarded
denominator only affects planes whose contribution is already flat zero.

Use a C1 upper positive-part with tau=.01:

    u = clamp(r+tau, 0, 2*tau)
    h(r) = u*u/(4*tau) + max(r-tau, 0).

It is at least max(r,0), equals it outside[-tau,tau], and its value and first
derivative match at both joins. Combine all body facets using

    depth = (0.025^32 + sum(h(r_i)^32))^(1/32).

This depth dominates every required entry fraction. An L32 norm bounds its
worst-case relative conservatism by(73728+1)^(1/32)<1.5 against the largest
entry/floor term. Scaling by4 inside the power is only a floating-point range
normalization. The positive floor keeps the aggregate differentiable even when
no plane needs additional burial. No maximum-over-facets drives the animation.
The resulting depth must remain below0.9 and the task map nonsingular.

Because the body half-space constraints are convex in depth and the body-axis
endpoint is feasible, any depth between the largest entry and1 contains the
cap. The upper-support ceiling and exact grip are unchanged by this in-plane
shift. Every pose remains a single affine image of the same convex envelope.
The method has no image objective, camera term, iteration or local minimum.

54 actual-body pose/control/covariance tests pass. Default R-arm depths for
frames1/215/1061 are0.154907/0.121893/0.126572, with cap-to-body-plane clearances
0.007065/0.006063/0.006335. All18 smooth-burial prototype images passed the
initial appearance review. This qualified the construction for a native pilot.

## Actual r03 native pilot

FIFO20261005-035123-e1e02973 completed successfully. The frozen native is
`mozu-siteat212-convex-arms-r03.blend`, SHA256
`eb2936306a35d9c5554626494e2f6cf8fa5a0bb6b766bdc2b059a59676d0033e`.
Each live arm uses257 Geometry Nodes; no playback handler or evaluated mesh
cache is saved. Six protected poses agree with the mathematical construction
within4.300e-7. The minimum whole-cap body-plane clearance is0.006063.
The previous r02 actual arm reproduces a negative clearance of-0.037499.
Three saved/reopened visible-scene comparisons and six control edit/resets
pass. Preservation includes the actual A189 joined body and paws.

All36 actual-native pilot views were inspected: six poses, three cameras,
whole character and isolated near arm. The former shoulder lobe and neck are
absent in these samples. The initial review permits dense verification and
additional views; it is not full-motion acceptance. Candidate-bound receipts
are `pilot-r03/report.json` and `pilot-r03-review.json` in the output folder.

FIFO20261005-040411-c4c32717 completed the next audit successfully:262 live
times,24 protected visible-scene comparisons,3 other-mode bypasses,15 food
geometry states and15 direct/cache raster pairs. Maximum native/math error is
4.324e-7; minimum proximal-cap body-plane clearance is0.005896. Maximum inward
fraction is0.173852 and minimum transverse-frame margin is0.9989476.
All36 supplemental whole/isolated and12 shaded images were inspected and
passed this scoped appearance review, bringing the pilot total to84 images.
The initial36-image review remains as `pilot-r03-review-initial.json`;
the expanded review binds the completed audit hash. Full capture is now
permitted, but full-motion review is still a separate requirement.
