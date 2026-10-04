# Sweep34 broom shape and grip

Status: reviewed comparison candidate; no motion adoption.
Owner request: natural broom length, shape and holding direction across viewing angles.

The selected F2 design is a compact hand broom. The grip-to-bristle-bottom reach drops from1.09 to0.74scene units, about32percent. Fan width changes from0.58 to0.51, while thickness grows from0.11 to0.19. The upper handle is0.12. The fixed holding region moves to distal material q>0.84, and the heading adds-30degrees at full Stroke. Every original character vertex and the arm performance remain unchanged.

The native shaft tilt stays about33.86–41.18degrees from vertical over129checked times. The rounded fan is visible from side and oblique views, and the shorter handle no longer has to lie far forward to reach the floor. These are scene-coordinate design measurements, not physical dimensions recovered from the source video.

## Why this design

Three pilot rounds were evaluated on the unchanged Sweep33 character. The first96images showed that shortening alone did not fix the grip: some long upper shafts produced small exposed brown patches through the forearm. The second48images and actual contained-vertex checks rejected transverse orientations that put the fan into the paws and still crossed the upper arm.

A joint864-case search then varied the fixed distal grip region, lower/upper reach and continuous heading response.188coarse-feasible cases survived seven sampled poses. Three diverse finalists were checked against native geometry and reviewed in72images over four poses and six views. F2 keeps a visible fan from both front and side, passes farther across the non-holding foot and seats the short upper handle in the actual hand. The earlier trials remain available on the comparison page.

The attachment changes by approximately0.05units because it uses a narrower distal material region. This does not modify the character's hand, arm length, shoulder, pose curves or body response. Overlap inside the distal holding hand is intentional; modeled fingers are not part of this character.

## Native evidence

- Complete saved native:221089528bytes, SHA256`595b8d9a66f21cfd45e9726162a0a96a97d0be419b2dfa8dece04d27135d8c49`. Mac and render-host copies match.
- Fourteen native times preserve all twelve character geometry fields exactly. `Design on=0` exactly restores the original Sweep33 broom at each of those times.
-129native-versus-independent-math poses: maximum coordinate error9.90e-7scene units; maximum floor/lift residual1.07e-7.
- Thirteen native poses: zero tool triangle intersections or contained vertices in the body/paws, tail and free arm; zero proximal holding-arm triangle intersections (mean material q<0.80). The head remains vertically separated. Crossing/disjoint triangle fixtures validate the overlap method.
- Twelve individual controls visibly change the broom and reset exactly, both before and after reopening with scripts disabled. Character signatures stay exact during the edit probes. Endpoint and reopen coordinate errors are0.
- No linked libraries, unpacked images, external geometry cache or custom Python playback requirement. Geometry Nodes and ordinary drivers remain editable.

The saved native has never been overwritten. The first full-capture admission failed before rendering because its parity harness tried to reduce the free arm's empty prop array. The harness now excludes empty arrays; this did not require a native or motion change.

## Full-action geometry and capture correspondence

All 240 displayed times and 116 intervening work/recovery times pass the selected floor/lift and actual-surface checks. Tool triangle/contained-vertex counts remain zero for the protected body, paws, tail, free arm and proximal holding arm. Minimum vertical head/tool separation is 0.406412 scene units. Maximum independent native coordinate error is 9.89e-07; maximum floor/lift residual is 1.06e-07.

All 240 captured times preserve the planted paws and gray ankle boundary within 0 scene units. Eighteen full-scene correspondence cases (nine times in each broom mode) bound the lightweight live-field capture to the complete native scene, with maximum vertex error 5.07e-07. The complete native remains editable; the comparison movies contain sampled native geometry, not interpolated video frames.

## Visual review and media

All 1,440 candidate frames and 480 new baseline frames were covered by complete time sheets and verified identical rest frames. The earlier four baseline movies are reused exactly from Sweep33. All eight newly encoded movies decode to 240 frames at 60fps, with a minimum 36pixel frame margin. All 288 orbit images and 12 shaded close views were inspected, alongside the 216 pilot images from the three design rounds.

The new short handle remains seated in the hand through the sweep and return; the isolated brown shaft patches seen in earlier trials are absent. The fan remains volumetric in side/oblique and shaded views. Rear/top angles naturally hide the broom behind the body or head during parts of the action. This is expected occlusion, not a geometry intersection. No blank image, frame crop or abrupt prop-shape change was observed.

The two fixed-time 72angle orbits sample the holding and sweeping poses. They complement six complete animated views; they do not mathematically certify every possible camera/time. The comparison and downloadable native retain the unchanged original prop as a reference.

## Scope

This is a comparison candidate for the authored four-second held-broom sweep. It does not adopt a new motion, qualify every control combination or reconstruct support forces. Fingers, pickup/release, stepping, arbitrary combined control collisions and skeletal runtime transport are outside the reviewed domain. All15inherited architecture issues and11full-release gates remain open. Main-agent implementation and review only; no independent sign-off.

Input Sweep33 SHA256`ad2edb651a5465fbc7cb94f9c27df193243423cdf5eb3474b975190ecbd5be10` and all adopted releases remain preserved.
