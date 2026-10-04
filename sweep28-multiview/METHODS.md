# Sweep28 methods and interpretation limits

## One source interval

Every submitted case receives the same90-frame temporal crop of the primary oblique original:
sourceframes24–113, original0.8–3.8s,30fps,960x960. The crop is losslessly encoded and every
decoded pixel was compared to its corresponding original frame, with zero differences.
The full six-second original remains available beside the crop. No generated movie is retimed,
interpolated, reversed, stabilized or combined with another output.

The crop contains two working reaches and two recoveries. It excludes the third stroke and final
settle, so a good pilot would certify only this interval. Output timestamps use each provider
movie's native frame rate.49frames at16fps last3.0625s;73frames at24fps last3.0417s.
The final displayed sample is at3.0s in both formats. These facts do not imply that the source
has been resampled into a synchronized multi-camera recording.

## Review order

1. Verify the exact submitted video/image hashes, prompt and untouched downloaded movie.
2. Decode every native frame, retaining timestamps and image hashes.
3. Inspect all chronological sheets for actual viewpoint, identity, grip, tool continuity,
   apparent support, body proportions, tail continuity and work/recovery behavior.
4. Inspect enlarged key images where a relationship is ambiguous. Keep a decisive camera or
   identity failure as a rejection, even if some temporal behavior survives.
5. Compare actual seconds in linked playback. Event buttons refer to source poses. Candidate
   disagreement is visible and is not removed with phase shifts or time stretching.

All review decisions belong to the main agent. No independent model or subagent review was used.

## Color-feature diagnostics

`measure.py` reads native decoded frames and resizes only the analysis images to960x960.
The provider original remains unchanged. It measures the largest green component belowy400,
HSV hue34–85, saturation>=65, value>80, area>=50pixels. On the source, three Kling outputs and Bernini rear-oblique-r02,
seven explicit key masks identify the green broom binding. The full traces retain all native
samples. A missing detection is kept missing and is not interpolated.

Bernini front-r01 changes the binding and yields39missing detections out of49frames. Its remaining
green candidates are not accepted as the original binding. No quantitative timing claim uses
that trace. A visually plausible graph cannot rescue a changed identity or a failed feature mask.

Four fixed crop-time windows locate binding-x extrema: work1[0.90,1.35], return1[1.45,1.90],
work2[2.00,2.40], return2[2.55,2.85]. The report also retains every sample within3pixels of each
extremum as a plateau band. An extremum is an image-feature event, not a unique whole-body pose,
an anatomical joint angle or a precise physical delay. Extrema can move within a flat plateau.
No temporal alignment, trajectory fitting or cross-view3D reconstruction is performed.

The dark lower silhouette uses maxRGB<80 belowy690, connected area>=100pixels, and components
whose bottom lies within6pixels of the lowest qualifying component. This excludes a separated
tail stub but can still include a connected arm/body region. The exposed sole-bottom and rear
edge are image observations only. Broom occlusion changes the apparent leftmost dark pixel by
many pixels in the original itself; that bounding box cannot measure a step. The source's full
foot/contact audit remains Sweep27.

## Image guides

Kling front-r02 and side-r02 additionally receive byte-identical existing neutral front/side
images from Sweep25. The exact files and hashes are displayed in the comparison page. They guide
camera orientation and character appearance; they are not source motion, anatomical measurements
or adopted joint-angle constraints. Their input status is honestly recorded as UNREGISTERED.
The current platform policy permits these inputs under the owner's standing generation authority.

## What generated views can establish

A successful output may supply a coherent visual hypothesis for the hidden side of a pose.
It does not add an independent physical measurement. The same model can repeat the same invented
joint arrangement in multiple views. Fixed-looking feet do not measure weight, ground reaction,
friction, balance or3D penetration. Apparent hip/chest separation remains ambiguous until a common
editable rig is tested from several cameras with explicit contact and shape constraints.

## Provider documentation

- [Kling O3 Pro video-edit input schema](https://fal.ai/models/fal-ai/kling-video/o3/pro/video-to-video/edit/api)
- [Bernini-R video-edit input schema](https://fal.ai/models/fal-ai/bernini-r/edit-video/api)
- [Kling pricing](https://fal.ai/models/fal-ai/kling-video/o3/pro/video-to-video/edit)
- [Bernini pricing](https://fal.ai/models/fal-ai/bernini-r/edit-video)

Checked2026-10-04. Generic mediagen estimates are caller-supplied from these advertised rates;
the broker marks them unverified. Actual billed cost is not returned by these jobs.
