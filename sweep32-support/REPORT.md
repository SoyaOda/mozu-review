# Sweep32 supported whole-body sweep

Sweep32 replaces the previous separated chest/pelvis turn with one common trunk frame over two planted paws. It carries both shoulders, the tail and the neck attachment; an inward/front shoulder action brings the original arm and broom across the body to the opposite foot. The four-second native candidate is editable and has been reviewed in front, oblique, side and top views.

This is a scoped candidate delivery, not owner adoption or complete motion-release qualification. Native SHA256: `d3cac1880009f3b27aa3da18116b209af38885ab6ed672384455221176867694` (221011694 bytes).

## What changed and why

The Sweep31 audit found that Sweep30 produced about half the source head-envelope and broom excursion, and missed the opposite-foot work zone. Its internal twist did not establish whole-body transport. Sweep32 declares the non-holding sole centroid as an authoring reference, rotates the trunk together, then accommodates the movement through lower body sections while preserving both paw contacts. The source front video does not uniquely identify this 3D pivot or physical load distribution.

Each original-height section of the lower body receives a rigid rotation. A quintic height weight connects the fixed gray ankle band to the common trunk; it preserves same-height distances and has C2 joins. The first native pilot passed geometry correspondence but was rejected for a visible rear-leg bulge and excessive head inclination. The corrected uniform section field removes that local bulge; gentle rigid-head leveling reduces the tilt. The original head, face, paw dimensions and appearance remain intact.

The arm retains its original material length and uses shoulder articulation plus a soft elbow. Its actual holding-paw centroid supplies the grip. Broom inclination follows the preserved broom dimensions, hand height and floor/return-lift constraint. No separate world-space hand animation or reach-through-lengthening is used. A small gradual return at the work end avoids freezing every part together.

The central-reference ablation keeps identical local arm/head curves and changes the body reference only. World-space transport consequently differs. Its frontal difference is modest; depth movement is more apparent from oblique and side views. The contact reference is the chosen authoring hypothesis, not an inferred physical truth.

## Observed performance

All1200 rendered view frames were inspected on20complete sheets, in addition to56color and8shaded pilot images. The active transition, crossing, work and recovery remain continuous. The working arm is readable, its grip stays connected, and no new visible ankle gap, sharp fold or local rear-leg bulge was observed. The original shoulder-root embedding remains. Side views retain the original forward broom reach; the overhead view naturally hides much of the torso under the head.

| Image excursion / source excursion | Previous Sweep30 | Sweep32 |
| --- | ---: | ---: |
| Head-envelope midpoint X | 50.1% | 90.2% |
| Broom binding X | 50.1% | 106.1% |
| Nose offset inside head | 113.0% | 118.9% |
| Lower cream-belly edge at normalized height0.765 | 34.9% | 61.0% |

These are ranges normalized by initial head width, measured from the unchanged source and actual encoded front movies. They are image features, not joints, material-point paths or contact forces. No time retiming was applied. The new reach and common transport improve substantially, but the source is not matched exactly: head presentation still turns somewhat farther, middle belly-edge excursions are about141% of source, while the lowest sampled belly edge moves less. Arm occlusion also affects belly measurements. The source's generated tail and changing anatomy are not adopted as shape authority. See the four feature plots and full measurement JSON for timing and missing observations.

## Native and media evidence

- 55native sample times check the exact procedural body field, both shoulder frames, tail transport, rigid head/neck carrier, original arm FK, hand/tool connection and floor branch. Maximum body-field error4.81e-7, arm error1.08e-6 and prop error8.35e-7 in model units.
- 9988displayed paw vertices are unchanged.22344lower gray vertices are fixed; all240continuous time samples in both reference cases pass, with paw error0, gray-band error at most1.50e-8 and floor/lift error at most1.50e-7.
- 18full-scene comparisons bind the faster capture representation to actual native geometry (maximum6.26e-7). No linked libraries or unpacked file images are required for playback.
- Rest and quiet endpoint match the source within1.20e-7. Save/reopen geometry error is0. Five control edits/restorations pass before saving and five more after reopening with scripts disabled.
- Finite-difference diagnostics at12396actual body-surface points over55control times give minimum determinant0.91664 and maximum principal stretch2.25517. This excludes sampled local inversion, but it is not volume preservation, an all-control collision certificate or proof of physical anatomy.
- Five480px movies each decode all240frames at60fps without blank or cropped frames. All25transferred movies/sheets match the host SHA256 records; source and previous comparison movies remain unchanged.

The completed FIFO job is `20261004-091722-96a7b095` (return code0). An earlier capture stopped before rendering on a record-initialization bug; it was fixed without changing the native. The failed attempt is not a motion-quality RED result. The earlier motion's failure to cross into the opposite-foot work zone is recorded separately in the pilot's baseline measurement.

## Reuse and limits

Open the complete `.blend` directly in Blender5.2; no custom Python driver namespace or external cache is needed. Use `RIG_GUIDE.md` for the actual controls and tested range. The extension sources rebuild within the Mozu repository; the included native itself is self-contained.

The whole-motion ledger retains all15architecture issues and11release gates, with individual scoped evidence and exclusions. General stepping, force balance, arbitrary control combinations, volume preservation, independent critic sign-off and skeletal runtime export are unqualified. This work delivers the requested supported sweep design and comparison; it does not replace an adopted asset or certify unrelated motion families.
