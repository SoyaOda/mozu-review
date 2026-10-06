# Sweep39 attention correction

The owner identified Sweep38 looking to image-left of the broom work region.
Sweep39 rotates the complete existing head toward that region, preserving the
face itself, existing pitch/roll and all body/arm/paw/broom motion.

## Authored target

Horizontal target =75% fixed work centroid +25% current broom-tip center,
gated by the original Look task score. World yaw spans0..26.27060degrees.
The native stores this as a C1 Bezier action with one reversible Alignment control.
At the reported3.75seconds, horizontal error to the actual tip changes40.83 to3.76degrees.
Across227loaded-work samples, mean absolute tip-bearing error changes36.40 to14.32degrees.
The target intentionally stays calm: it does not track the tip exactly at full
reach/gather, and52of227work samples have a larger tip-bearing error than before.
It is a work-area attention choice, not certified eye-ray/floor contact.

## Native and visual evidence

- Source38 SHA256: `1506208bafef6e9a4b97712071d4af8d7190e5c2fc9ae512e301639b80b73370`; bytes preserved.
- New native: 221261836bytes; SHA256 `b55a9deb9540033de7503a641cb788532186123d42ae11c5134678bdf60dac40`.
- Eleven original-source key times restore head and protected geometry exactly.
- At3.75seconds, restored front/side/oblique renders match the original38 decoded
  pixels exactly, confirming the comparison uses identical camera/render conditions.
  The selected pilot and continuous capture also match exactly in all three views.
- 17pose/control rows and4reopened edit rows pass. Alignment0/0.5/1 edits reset exactly.
- All480output times plus132interstitial times retain eleven
  non-head geometry fields exactly between original and corrected attention.
- Maximum rigid-head residual: 4.01904879e-07.
- Native C1 curve maximum parity error: 2.86120919e-06degrees.
- Closed endpoint equals neutral exactly. No external playback images or libraries.
- All1440front/side/oblique viewframes,72work-pose angles and42pilot images reviewed.
- Three complete8-second movies decode at60fps with the recorded safe image margins.

The inherited render-only snapshot method copies actual evaluated native positions,
topology, shader attributes and material-driver values. No temporal mesh or image
interpolation substitutes for native evaluation. Prior38body/contact checks are
provenance; this candidate independently verifies unchanged geometry and rigid head motion.

## Delivery and limits

The public page synchronizes old/new motion in three views and provides speed,
seek, frame-step, loop and a72-angle work-pose inspection. Browser and public-transfer
receipts are supplied separately with the candidate. The editable ZIP contains the
self-contained native, source scripts, guide and bound evidence.

The first capture attempt failed at a Python module-name collision before native
opening. It was repaired and rerun through the host queue; it was not a motion RED.
The pilot builder is retained as native-pilot.py.snapshot. The capture helper avoids
redundant frame updates at the same time; it does not change the saved native.

Main-agent review only. The inherited15architecture issues and11full-release gates
remain open, as does owner adoption. Arbitrary control combinations, runtime transport,
stepping and tool pickup are outside this correction. Earlier originals are preserved.
