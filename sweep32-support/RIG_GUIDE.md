# Sweep32 editable supported sweep

Open `sweep32-support.blend` in Blender5.2. Select `Sweep32 | Supported whole-body sweep` and its custom properties. Frames1–240 at60fps contain the four-second gesture; frame241 is its quiet endpoint. Save later edits as a new version.

| Control | Responsibility | Reviewed value |
| --- | --- | --- |
| Support reference | Interpolate the declared central and non-holding-sole authoring references; local arm/head action stays identical | 1 chosen; 0 comparison |
| Common yaw | Common upper body, shoulder and tail heading curve | approximately0 to-26degrees |
| Turn gain | Scale that common heading | 1 |
| Inclination | Common forward and sideways body inclination | 1 |
| Arm reach | Shoulder-led inward/front sweep at the original arm material length | 1 |
| Head leveling | Gentle local counter-inclination of the rigid head | 1 |
| Work posture / Stroke | Ordinary C1 animation curves for preparation, sweep and return | animated |
| Attention / Head response | Delayed rigid-head attention; independent of body transport | animated |
| Unloaded lift / Bristle drag | Small return clearance and straw response | animated |

Inherited Sweep30 properties remain for the archived graph's provenance. They are disconnected from the final Sweep32 transport. Edit the controls listed above; changing an inherited chest/pelvis property is not a Sweep32 performance adjustment.

## Foot-to-body relationship

The authoring reference is the non-holding sole centroid, approximately(-0.37652278,-0.06862354,-0.286308885). It is a fixed declared point. The generated front video does not uniquely determine a physical pivot or which foot bears the load. Both displayed soles remain planted.

The last Sweep32 Geometry Nodes modifier on `A189 | E final character` consumes the original `s25_posture_body` selection. The9988displayed paw vertices remain outside that moving selection. A separate lower gray band is fixed as well. The original shape graph and material attributes stay in place.

Below the upper trunk, every rest-height section receives one rigid rotation about the declared reference. A quintic weight grows from zero atZ-0.045 to one atZ0.50. Points at the same original height retain their pairwise distances. The field is exactly the common trunk transform aboveZ0.50 and identity belowZ-0.045; the joins are C2. This prevents the first pilot's per-side mixture from pinching or bulging individual sections. It is not a volume-preserving or force-balance solver: longitudinal strain still exists and has been inspected in the authored action.

The trunk, shoulder sockets and tail share one frame. There is no separate chest-versus-pelvis twist control in this action. Gray lower sections accommodate that transform over both paw contacts.

## Arms, head and tool

The original club-arm material length, girth and paw dimensions are unchanged. Shoulder inward/front articulation and a soft elbow create the visible reach. The complete evaluated arm is carried by the trunk after local articulation. Its actual holding-paw centroid defines the broom grip; there is no independently animated world-space hand target or arm-length stretch.

The original broom dimensions remain fixed. A continuous floor-contact branch determines its inclination from the actual grip height, heading and small authored return lift. The shaft stays rigid; only straw below the binding receives the small drag response.

The head remains a rigid assembly. A parent frame carries the original neck attachment through the common body transform; local pitch, counterturn and modest leveling control attention. Facial geometry, eye shapes and material ownership are preserved. The late work interval begins a small gradual return instead of freezing every part on one pose.

## Editing and verification

The native uses ordinary animation curves, built-in driver expressions and persistent Geometry Nodes. It does not need an external geometry cache, custom frame handler or a custom Python driver namespace. Reopening with scripts disabled was tested. The source extension scripts require the Mozu repository; they are not a separate stand-alone model generator.

The native pilot covers55times, seven H0/H1 pose pairs in four views, five control edits/restorations and five more after reopening. Rest and endpoint coordinates match the original within floating-point precision; the reopened native matches exactly. The contact-reference and central-reference cases use identical local arm/head curves but intentionally different world transport.

The displayed slider ranges are editing aids, not a certificate for all combinations. Shape-graph, proportion, topology or material-attribute changes require new attachment and surface checks. Pickup/release, stepping, contact forces, general motion qualification and skeletal runtime export are outside this four-second sweep candidate.
