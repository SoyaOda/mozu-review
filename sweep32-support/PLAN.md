# Sweep32: supported whole-body sweep

Owner requested implementation after the Sweep31 contact analysis, including the complete foot/body/shoulder/arm relationship and natural performance. Preserve all previous candidates and adopted originals. Main-agent work; no new reference generation.

## Design and evidence

Use the complete Sweep29 front source and Sweep31 measurements. Both visible paw contacts stay planted. The source favors common lower/upper trunk participation; its exact physical support load, anatomical angles and 3D axis are not recoverable. The source's tail shape is not an appearance authority.

1. A declared non-holding sole reference governs one common trunk transform. A central-reference ablation keeps the exact same local arm/head score. Do not preserve equal world-space tasks between those cases.
2. Two gray ankle/hip regions accommodate the moving trunk above fixed paws. Their rest-space side assignments and smooth boundary conditions are explicit. Common rotation is exact above the accommodation region; there is no independent chest twist by default.
3. The shoulder-bound original club arms keep their material lengths and girth. The working shoulder swings inward in front of the body. The grip is derived from the actual evaluated hand; tool contact is solved from that grip and the original broom dimensions.
4. Head transport follows the common trunk. Local attention supplements that movement without increasing facial yaw to conceal weak body motion. The timing includes preparation, crossing, a broad working interval and release.

Gauge: fixed chosen contact reference plus authored rotations; no freely optimized pivot and translation. Reference choice is an authoring assumption, not a discovered force axis.

## Verification sequence

Before the queued Blender pilot, inspect offline rest geometry, arm reach/collision feasibility, fold bounds, field Jacobians and temporal continuity. Local checks precede every host run. One queued job at a time; preserve exact job handles. Actual native probes must verify rest identity, common upper-frame rigidity, both displayed contacts, attachment accommodation, arm FK, grip/floor, material attributes, edit/reset and save/reopen. The previous native's observed insufficient spatial reach is the performance RED; missing controls are not a performance test.

Review seven event poses in front/oblique/side/top and isolated shaded gray legs/body. Fix observed defects before a continuous render. Then inspect the full 60fps sequence and compare source/previous/new in real browser playback. Deliver an editable native, evidence and a public review URL. Scope qualification and owner adoption remain distinct from a candidate delivery; inherited 15 architecture issues and 11 gate groups remain tracked.

## Initial implementation record

The actual original sole samples contain513vertices per side. The non-holding centroid is(-0.3765225806,-0.0686235507,-0.2863089144); the declared reference differs by less than0.00000021 model units. Both displayed paws contain4994vertices and stay outside the moving-body selection. The gray ankle band remains fixed separately.

The first common-yaw audition reaches26degrees. This is an authored candidate angle, not an estimated source angle. The head counterturns locally by up to8degrees so that greater trunk participation does not imply exaggerated facial yaw. The working arm's original material length and girth remain fixed; shoulder inward/front articulation replaces the previous outward-limited stroke.

For each gray leg, a smooth rest-space side assignment defines an ankle reference. A C2 weight grows from zero atZ-0.045 to one atZ0.30 on the non-holding side andZ0.39 on the holding side. Intermediate sections rotate about their ankle and receive the corresponding weighted common-frame displacement; the result equals the exact common transform at the top and identity at the bottom. This is a geometric accommodation model, not a force simulation or volume-preserving skin solver.

Actual native rest-surface preflight samples17049points per event pose. At the first work pose its minimum Jacobian determinant is0.8041, but maximum singular stretch is2.5897. The latter is a meaningful surface-strain concern to inspect in the pilot, not a pass for visible anatomy. The original offline G body mesh has164270vertices while this candidate's joined body has168230; offline body assumptions do not certify the current geometry. The actual rest surface is retained in actual-rest-body.npz.

The first host run stopped on a4.04798e-6degree Bezier residual treated as a model-space error. The curve check now records absolute residuals by channel and normalizes degree channels by their authored amplitude. No geometric threshold, shape or performance score changed. That validation stop is not the performance RED; the previous native's measured opposite-side reach failure remains the RED.

## First visual correction

Pilot02 passed55native poses, exact paw retention, arm/prop correspondence, four-view pose coverage, edit/reset and save/reopen. It is rejected for visual refinement before continuous capture. Inspected work-pose front/oblique/side images establish the opposite-foot reach and readable arm; the head is too inclined. Shaded H1 leg images show a local rear-side protrusion associated with the asymmetric ankle-section mixture. The H0 central-reference side is smoother, so the difference must not be dismissed as unchanged anatomy.

Pilot03 removes the per-side interior mixture. Every original rest-height section receives one rigid transform, including combined pitch/roll/yaw; pairwise distances within a section are exactly preserved. A common quintic lower ramp ends atZ0.50. Both fixed ankle boundaries and the fixed displayed paws remain explicit, while the upper trunk is exactly common. The earlier two-ankle design paragraph describes the rejected pilot, not the corrected field. Local tests cover section rigidity and the original boundary/temporal/reach conditions. The same peak trunk/arm/broom reach is retained. A small gradual recovery across the work-end interval replaces the exact0.16second all-part hold; every curve remains C1.

Head leveling adds a3.2degree delayed local counter-inclination with a separate editable gain. The head remains a rigid assembly. New diagnostic clay uses darker neutral material and restrained lights to reveal subtle support-surface defects. No full-render job is admitted until the corrected pilot is visually reviewed.
