# Sweep31: a contact-relative experiment, before more torso deformation

Status: proposed next implementation only. No new native is built by this audit.

## Responsibilities

Ground contacts -> independently declared sole tasks.
Contact-relative body transport -> mostly common pelvis/trunk rotation and displacement.
Gray legs and hips -> connect the moving trunk to the planted contacts.
Residual torso twist -> small optional chest-versus-pelvis correction.
Shoulders and rigid head -> carried by the trunk, with local arm and attention tasks.
Grip and broom -> retain grip/floor consistency while reaching the intended sweep zone.

A stationary foot is a boundary condition. A stationary pelvis is a separate choice and is not implied. A smoothly tapered displacement field can still be the wrong action model.

## Controlled mechanism pilot

Use a fresh copy of Sweep30 and preserve its exact zero/bypass appearance, original model, paw shape, arm dimensions and existing grip/contact infrastructure. Work at the small set of source events first: hold0s, preparation1.467s, crossing1.733s, inward sweep2.000s, recovery2.267s, late return2.600s, settled3.200s. Timings are observation checkpoints, not an anatomical lag fit.

1. H0: central pivot, common trunk/pelvis rotation, supported gray legs, zero relative torso yaw. Sweep30 C is a useful starting ablation, but needs the support-chain inspection below.
2. H1: same common rotation score, but an explicit non-holding-contact pivot/reference. Keep the local arm/head scores equal to H0. Transport shoulders/head/tool through the resulting body frame; do not force their world-space tasks to match H0, since that would erase the effect being tested.
3. H2: H1 plus a small independent chest correction, initially0. Sweep only a few clearly labeled authored values if H1 leaves a visible residual. Any extra freedom must improve the performance, not merely pass its own deformation formula.

Keep support-side choice and common-body orientation separate. Both sole tasks stay fixed initially. The supporting gray leg/hip and the opposite leg may require different accommodation, but unilateral physical load is not asserted. Inspect attachment sections and volume in front, oblique, side and top, including shaded surfaces hidden by the large head.

Changing pivot and adding free translation can be redundant. Choose one gauge: either pivot-based rotation plus a small explicitly named residual displacement, or a pelvis rigid transform expressed relative to a declared contact. Do not optimize both unconstrained and then claim to have discovered the support point.

## Performance pass after selecting the mechanism

The current local arm stroke is intentionally too small. After the pilot identifies a plausible mechanism, adjust the local stroke and hand/tool orientation so the broom reaches the non-holding foot region and returns with a readable broad action. Preserve the original arm lengths and geometry; avoid stretching an arm or adding world-space hand teleportation to cover the deficit.

Use the source's spatial relationships and event order:

- Both exposed sole tasks stay planted; no invented step or rocker.
- The body and cream-belly presentation participate below the chest.
- The head travels with the body while local attention remains independently adjustable; do not use stronger face turning to mask weak body transport.
- The tool crosses the neutral frontal reference and reaches the opposite foot region.
- The return opens the face, belly and free-arm presentation coherently.
- Grip and floor contact remain consistent without an excessive bristle rotation or abrupt reset.

Do not directly fit the fixed-height belly edge or head-envelope midpoint as if it were a 3D anatomical landmark. Use them as diagnostics alongside the actual silhouettes, occlusion order and full images. Generated-source shape changes and tail details are not to be copied into the model.

## What counts as progress

Technical checks remain necessary: actual evaluated contacts, attachments, grip/floor, surface quality, original appearance, edit/reset and save/reopen. Separate them from performance checks.

The performance comparison must ask whether the body now reads as one supported action, whether the lower belly participates, and whether the broom reaches the correct side. Report the added mechanism's isolated visible effect. Reject a more complex H2 if H1 is equally convincing or cleaner. Do not use the existence of a new controller as the performance RED.

A successful small multi-view pilot precedes any full continuous render. If H1 cannot preserve both contacts without ugly gray-leg strain, first inspect contact geometry and common-body displacement. Do not hide the incompatibility with more chest twist. Owner judgment and any later production adoption remain separate from this analysis.
