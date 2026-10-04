# Sweep28 source-conditioned alternate-view study

Owner requested proceeding with the agreed multi-angle generation and analysis strategy on2026-10-04.
The original oblique sweep remains the primary motion authority. New videos are supplemental hypotheses, not physical ground truth.
No mechanical fitting or native rig change is included in this stage.

## Exact input

Original: `output/ssot_candidates/sweep23_fixedshoulder_20261003/r01/original/output.mp4`,
SHA256 `21f8a76609d8bbaa3a100592d7f38ece48f469d622f0130e4532f635bd318fd4`.
The input uses sourceframes24–113 inclusive,0.8–3.8s,90frames at30fps,960x960.
A lossless H264 temporal crop retains exact decoded pixels for all90frames; no retiming/interpolation/spatial editing.
CropSHA256 `43478a044fe90c08f3ac2e904d25fb6397e8d6417a5841b801cbbfbdf17ac6f4`.
Lineage and all90 pixel comparisons are in `output/ssot_candidates/sweep28_multiview_20261004/source/lineage.json`.
The clip contains two reaches and two recoveries; the third stroke and final settle are outside this pilot.

## Prior evidence reused

Sweep25 already tried Wan3 with the liked reference video: front-r01,side-r01 andfront-r02 retained the oblique view.
Front-r02 included a correct front image but still failed camera coverage. Selected Sweep25 views instead used
image endpoints and semantic action prompts; they are not source-video-conditioned synchronized views.
Read `../sweep25/SOURCE_REVIEW.md`. This study tests direct video-editing endpoints and checks actual event timing;
it does not repeat the failed Wan3 video-reference approach or relabel independent motion as synchronized.

## Trial and budget

Round1 compares direct video editing: Bernini-R front and Kling O3 Pro front. Both receive the same entire crop.
Bernini:49frames requested at16fps,848px long edge; anticipated3.0625s x$0.08/s = $0.245.
Kling: source3s x$0.168/s = $0.504. Initial total$0.749.
The advertised rates were checked on2026-10-04 at:
- https://fal.ai/models/fal-ai/bernini-r/edit-video
- https://fal.ai/models/fal-ai/kling-video/o3/pro/video-to-video/edit
Both estimates were submitted to mediagen before paid generation. Generic endpoint estimates are caller-supplied,
not internally price-verified. Current spend_control=platform; no owner approval token is required.
fal authenticated probe: status404,ok=true (nil-UUID status test). No credentials are copied or accessed by the caller.

Select the more faithful method for exact side and rear-oblique views. If neither preserves timing/identity/support,
record failures and adjust the method/prompt using those specific observations. Do not treat an attractive new performance
as another camera of the original. View instructions are targets, never proof of calibrated angle.

## Analysis

Bind every decision to the untouched provider movie hash and provenance. Decode all original timestamps.
Inspect every frame for viewpoint, anatomical identity, fixed support, body proportions, hand/shaft contact and visibility.
Compare work/recovery timing to source1.1/1.7/2.2/2.7s in crop time; preserve actual playback rate for this check.
Screen coordinates across different cameras cannot be compared as equal3D joints. Measure within-view image features,
then compare event timing and semantic relationships. Distinguish camera drift, body rotation and foot displacement.
A passing supplemental result must have no unresolved blocking issue in its stated scope. Keep rejected results for comparison.
Do not infer a pelvis/chest or paw angle from a moving covering boundary, nor treat matching generated views as independent evidence.

## Delivery

Provide a source/candidate comparison player, complete frame sheets, measurements and explicit decisions/limitations.
Continue the existing owner-authorized public review delivery. Preserve Sweep25 native and all adopted releases.

## Final outcome

Six requests completed; all366frames reviewed. All six are rejected for the original same-performance alternate-view scope.
Round2 added exact front/side image guides to Kling; round3 added material/identity constraints to Bernini front/rear requests.
Rear presentation changed, but the source timing/action did not survive. No further generation is pending and no generated view
is registered as motion SSOT. Total caller-estimated cost$2.247, actual billing unavailable. Read REPORT.md and METHODS.md.
