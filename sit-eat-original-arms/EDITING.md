# Original-profile eating arms

The selected native is resolved by `output/rig_candidates/siteat212_20260925/arm_preserve_20261005/selection.json`. Work on a new copy. Preserve every predecessor and adopted release.

## Controls and motion ownership

Use the original Mode control at3 for the seated meal, frames1–1329 at60fps. The native contains Actions and unapplied Geometry Nodes; there is no external playback handler.

Each original arm object has its existing sit-performance Geometry Nodes modifier. The separate arm Actions own `Swing`, `dRaise`, and `dForward`. These are three shoulder rotations of the original default arm. Original `Surface follow` and `Original blend` tracks keep the inherited body attachment throughout the entry and exit. Do not replace the original shoulder triangle or its offset.

In this qualified family, `dBend`, `Elbow`, `Wrist`, `Wrist side`, `Paw roll`, and `Elbow plane` stay0; `kStretch`, `kGirth`, and `kPaw` stay1. Changing these creates a different shape family requiring another review. Rounding the outline by relocating the shoulder or substituting a new neutral mesh would violate this candidate's purpose.

`SE212 | Action channels` owns food presentation (`propPitch`, `propForward`, `propUp`, `propSide`), bite cuts, final ingestion and the inherited face/head/body performance. The food attachment reads the actual live arm-tip vertices. Keep this Action and both arm Actions together. The six mouthful contacts are215,401,575,749,911,1061. Original default arms return by1279; the final hold ends1329.

## Reproduction and evidence

The source lane is `scripts/research/siteat212_20260925/arm_preserve_20261005/`. `pilot.py` establishes original shape/root preservation. `cradle.py`, `edge_presentation.py` and `restage.py` author separate food-holding revisions. `presentation_timing.py` holds the final lowered-turn staging. Every builder refuses to overwrite its native or evidence directory.

After selecting and visually reviewing a candidate, `audit.py` checks fractional poses, modes, reopened controls, actual food geometry, and direct/cache pixel parity. `capture.py` renders every native frame and checks original-shape membership and the feet. `media.py` exports and fully decodes the movies and chronological review boards. These run through the shared Windows FIFO; never start a second owned heavy request while one is queued or running. `--resume` is only for a stopped capture with a matching verified prefix, never a replacement for waiting on a live job.

`meal_complete_20261004/food_states.py` caches only the six exact static food CSG states in the disposable render scene. The selected native is never saved with that cache. `snapshot_fast.py` retains the original complete face/mouth field layers. An earlier approximate capture cache is not used.

Batch review uses `pack_capture_batch.py` and `review_capture_batch.py` for immutable36-frame batches. Extract batches after the Windows capture writer stops to avoid overlapping progress-file access. A main-agent receipt is recorded only after inspecting all four sheets. `finalize_visual_review.py --check-prefix` validates those receipts without declaring meal completion. After all37 batches and media finish, run it without that option to bind every reviewed row, image hash and receipt to the final capture and movie manifest. Browser playback is recorded separately.

Windows capture recovery: the first render stopped at966 because replacing the progress JSON raised WinError5. An overlapping reader is a possible cause, not proven lock ownership. `recover_capture_manifest.py` performed a one-use, exact-hash recovery for that stopped job: it verified all966 frames, archived both manifests, and promoted the fully written pending frame. The unchanged capture resumed at967 and completed1329 frames plus media successfully. This was an execution recovery, not a failed motion gate or a new native revision. All37 batches are now reviewed and bound to the final capture; no capture job remains active.

The finished reports delimit the actual verified pose and control domain. This is a stylized complete meal review, not physical fingers/grasp, a mouth-cavity simulation, a runtime export, broad native-release qualification or owner adoption.
