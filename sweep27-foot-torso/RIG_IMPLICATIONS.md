# Sweep27: revised rig implications

This document refines the design-only Sweep26 proposal after the foot and trunk audit. It does not authorize an unobserved gait, prescribe measured joint angles, or report a new native implementation.

## What must be represented separately

| Layer | Responsibility | Evidence versus authorship |
| --- | --- | --- |
| Ground contact | Preserve declared sole anchors and floor relation | Strong visible support evidence; hidden full contact patch remains unknown |
| Paw appearance/orientation | Preserve original paw shape; allow explicit optional orientation/compliance controls | No source-measured yaw/rocker trajectory; start with both planted and no added rocker |
| Gray ankle/leg/hip accommodation | Connect a supported paw to a moving lower body without a cuff, gap or pinch | Moving coverage boundary observed; actual joints/deformation split is authored |
| Pelvis/lower trunk | Small balance and orientation task independent of upper presentation | Lower contour shifts modestly; exact pelvis heading/load split unobserved |
| Chest/torso | Working inclination, turning presentation and distinct recovery opening | Qualitative turning/inclination evidence; independent chest/pelvis torsion is a testable design choice |
| Shoulders/arms and neck/head | Original attachment locations carried by the chosen body frame, with local articulation/attention | Preserve accepted geometry; avoid solving recovery by arbitrary root translations |

Do not freeze all gray leg/body points because the sole is stationary. Equally, do not animate paw yaw merely to make a feet-twist control nonzero. The contact task and the visible covering surface are separate concerns.

The head must remain a rigid accepted assembly transported by an orthonormal attachment frame. Torso deformation and belly pigment must share rest-coordinate ownership. Tail-root responsibility should be declared explicitly instead of automatically inheriting every chest angle. Existing original arm dimensions, local articulation and world-grip/tool contact remain in force.

## Small controlled experiment

Use rest0, preparation42, work61, recovery75, work90 and recovery106, then settling142. Recovery106 is added because the supported opening should repeat consistently. Keep the same native cameras, shape, materials, tool dimensions and authored hand/contact tasks between cases.

1. Baseline A: common body-frame inclination/orientation, original local arms/head, planted paws. Improve recovery presentation within these existing freedoms first.
2. Candidate B: independently controllable lower frame and chest, with a broad torso field and coherent gray-leg/hip accommodation. Keep paw orientation equal to A initially.
3. B-minus-relative-chest: zero only relative chest rotation. Compare which visible effect actually depends on it.
4. B-minus-leg-accommodation: hold the gray lower attachment response while preserving the contact task. Inspect whether the mismatch appears in the overlapping leg/paw boundary.
5. Optional foot study only if a visible mismatch remains: a very small explicitly authored paw-orientation/compliance change around a declared support anchor. Do not infer an angle from the8px moving junction or the back-contour chord. No stepping or large rocker by default.

The equal task comparison must examine all four native views plus shaded torso/hip/ankle surfaces. The oblique source is the rhythm authority; independently generated front/side/top sources remain qualitative supplements, not synchronized targets.

## Review criteria that follow from the audit

- Both sole anchors remain supported; no whole-foot translation, accidental pivot about an object origin or heel/toe lift used to hide a body mismatch.
- The gray leg/paw boundary responds continuously to the chosen body/hip mechanism. Classify external silhouette separately from covering boundaries during review.
- Working reach has a modest coordinated body inclination; recovery opens the arm/belly/head presentation while retaining the working posture.
- Do not multiply pelvis, chest, ankle and attention by one scalar. Give recovery its own authored event shape, but do not copy threshold-crossing delays as anatomical timing.
- Retain the exact zero/bypass appearance and verify evaluated edit/reset and save/reopen behavior for each new control.
- Reuse actual contact, grip, attachment and surface checks. Sweep25 rigid-body invariants cannot certify a new deformation field, and a new field must not be assumed necessary merely because it has more controls.

The first comparison can decide whether A already conveys the intended supported sweep or B adds useful natural articulation. Existing source evidence does not predetermine the winner. Full-loop rendering follows a successful phase pilot. No native implementation or additional work is claimed in this analysis delivery.
