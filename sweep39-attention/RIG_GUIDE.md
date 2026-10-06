# Sweep39 editing guide

Open `sweep39-attention.blend` in Blender5.2. Frames1-480 play the8-second
action at60fps. Frame481 is the exact closed endpoint. The complete native is
self-contained; playback needs no custom Python handlers or external geometry cache.

Select `Sweep39 | Floor-work attention`:

- `Alignment`:0 restores Sweep38 horizontal attention,0.5 is the intermediate
  study, and1 is the selected floor-work attention correction.
- `Work yaw`: world yaw in degrees, authored as a C1 Bezier action. The target is
  75% of the unchanged Sweep38 work-area center plus25% of the moving broom-tip center.

The action gate uses the original `Look task` timing. Existing head pitch/roll,
face geometry/materials, body construction and all arm/paw/broom motion are retained.
The gaze curve is authored for this particular broom path; changing the broom or
body path requires retargeting it. It is horizontal attention, not a certified
eye-ray/floor intersection or a live general-purpose look-at solver.

For other motion controls, retain the Sweep38 editing guide and tested ranges.
Native build scripts require the Mozu repository and preserved ancestor inputs.
The archived native itself does not require those source inputs to open or edit.
Sweep39 is a separate review candidate; no adopted release is overwritten.
