# Sweep30 editable torso rig

Open `sweep30-torso.blend`. Select `Sweep30 | Torso and sweep` and its custom
properties. Frames1–240 at60fps contain one four-second sweep; frame241 is the
quiet endpoint. Preserve this reviewed native and save edits under new names.

| Control | Meaning | Default |
| --- | --- | --- |
| Chest yaw | Authored chest heading curve, degrees | 0 to-15 |
| Pelvis yaw | Separate lower heading curve, degrees | 0 to-3 |
| Chest turn gain | Scale chest heading; shoulders, arms, neck and tool heading follow | 1 |
| Pelvis turn gain | Scale pelvis heading and the lower-frame tail transport | 1 |
| Torso articulation | 0 gives the common rigid-body comparison;1 enables separate torso/leg response | 1 |
| Turn separation | 0 aligns lower yaw with the chest while retaining ankle anchoring | 1 |
| Leg anchoring | Fade gray leg/ankle rotation toward the unchanged planted paw | 1 |
| Body coupling | Scale forward and sideways inclination | 1 |
| Amplitude | Scale the existing local arm stroke and its posture contribution | 1 |
| Work posture / Stroke | Ordinary curves for preparation and one work/return sequence | animated |
| Attention / Head response | Local rigid-head attention, delayed0.07s | animated |
| Unloaded lift / Bristle drag | Floor clearance on return and small straw-tip response | animated |

The comparison deliberately holds chest, head, shoulders, arms, grip and tool
tasks equal between A and B. A changes the entire body/thigh branch with one
frame. B keeps the lower frame quieter while turning the chest; fixed visible
paws are excluded from both transforms. The native keeps the original arm
length/shape and prior local shoulder/elbow action. It does not reproduce the
entire excursion of the generated front broom path.

## Persistent deformation

The last unapplied Geometry Nodes modifier on `A189 | E final character`
owns the new field. It consumes the existing `s25_posture_body` attribute,
which marks body/thigh vertices before the planted paws are joined. The
underlying shape graph and belly material attributes are retained.

Rest height defines two broad quintic ramps. Lower rotation blends from zero
atZ-0.035 to full lower-frame response atZ0.30. Relative torso yaw blends
fromZ0.36 to the chest shelf atZ0.90. Original shoulder centers are atZ0.981,
so both attachment roots use the exact complete chest frame. Each section
uses rotation angles, not a weighted blend of scaled matrices. Pure yaw
preserves section radius; the combined inclination field is not claimed to
preserve local volume exactly.

Both complete live arms and the unchanged head assembly follow a rigid chest
frame. The tail follows the lower frame as a rigid volume. Existing geometric
overlap is retained at attachments. The shaft keeps its material grip point;
its floor inclination is solved from the actual evaluated holding paw.

No external video, mesh cache, custom frame handler or custom Python driver
namespace is needed for playback. Ordinary animation curves and built-in
driver expressions remain editable in the native. Source scripts reproduce
the extension from the unchanged Sweep25 native in this repository. The full
native contains the existing scaffold; editing it does not require rerunning
the authoring script. Changing scaffold proportions, topology or the original
material attributes requires revalidating these height bands and attachments.

## Tested domain and limits

The native pilot checks57times, all seven A/B keys, seven actual control
changes/restorations and four further edits after reopening with scripts
disabled. Displayed paw drift is zero at those checks. Original rest, final
rest and reopened coordinates return exactly in the recorded comparisons.

The control ranges are editing aids, not a certificate that every combination
is safe. This candidate begins and ends holding the broom. Pickup/release,
individual finger articulation, stepping, contact forces, balance simulation,
general motion qualification and skeletal runtime export are outside this
experiment. Owner adoption is separate from these observations.
