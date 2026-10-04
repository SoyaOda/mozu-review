"""Extend an untouched Sweep25 copy with native chest/pelvis/ankle ownership."""
import hashlib
import importlib.util
import json
import math
import os
import shutil
import sys
from pathlib import Path

import bpy
import numpy as np
from mathutils import Matrix, Vector

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import torso_math as T

spec = importlib.util.spec_from_file_location('sweep25_author', HERE.parent/'sweep25/native.py')
OLD = importlib.util.module_from_spec(spec)
spec.loader.exec_module(OLD)
K, N, S, A = OLD.K, OLD.N, OLD.S, OLD.A
OUT = K.O/'v2/sweep30_torso'/os.environ.get('SWEEP30_TRIAL', 'pilot01')
SOURCE = K.O/'v2/sweep25/motion01/sweep25-semantic.blend'
SOURCE_SHA = '1cfc32aa8a05d2d26d8c3602839e8312e855f29dd4f77405b7fefc1a8044dfc6'
REFERENCE_SHA = 'f47916172a0d827d3e68527cfdd167d2dea7b3a357f5cca19f0ae804b861cd6a'
CTRL = 'Sweep30 | Torso and sweep'
PATH = OUT/'sweep30-torso.blend'
ARM = OLD.ARM
VIEWS = OLD.VIEWS
VARIABLES = dict(w='Work posture', p='Stroke', a='Amplitude', h='Attention',
                 r='Head response', u='Unloaded lift', b='Bristle drag', c='Body coupling',
                 cy='Chest yaw', py='Pelvis yaw', cg='Chest turn gain', pg='Pelvis turn gain',
                 ar='Torso articulation', la='Leg anchoring', ts='Turn separation')
PITCH, ROLL, CHEST = '(3*w+2*p*a)*c', '(-w-.8*p*a)*c', 'cy*cg'
PELVIS = f'({CHEST})+ar*ts*(py*pg-({CHEST}))'
set_time = OLD.set_time


def write_json(path, data):
    path.write_text(json.dumps(data, indent=2)+'\n')


def driver(owner, path, expression, ctrl, index=None):
    if index is None:
        owner.driver_remove(path)
        fc = owner.driver_add(path)
    else:
        owner.driver_remove(path, index)
        fc = owner.driver_add(path, index)
    d = fc.driver
    d.type, d.expression = 'SCRIPTED', expression
    while d.variables:
        d.variables.remove(d.variables[0])
    for name, key in VARIABLES.items():
        v = d.variables.new()
        v.name, v.type = name, 'SINGLE_PROP'
        v.targets[0].id = ctrl
        v.targets[0].data_path = '["'+key+'"]'
    return d


def value(f, label, expression, ctrl):
    node = f.node('ShaderNodeValue')
    node.name = node.label = label
    driver(f.g, f'nodes["{node.name}"].outputs[0].default_value', '10000*('+expression+')', ctrl)
    return f.op('MULTIPLY', node.outputs[0], .0001)


def field(f, position, ctrl, mode):
    """Rotate rest sections; upper attachments use one rigid chest frame."""
    pitch = value(f, 'Forward work inclination', PITCH+'*pi/180', ctrl)
    roll = value(f, 'Side work inclination', ROLL+'*pi/180', ctrl)
    chest = value(f, 'Chest world heading', CHEST+'*pi/180', ctrl)
    yaw = chest
    if mode == 'body':
        z = f.parts(position)[2]
        lower = f.smooth(f.op('DIVIDE', f.op('SUBTRACT', z, T.ANKLE_START), T.HIP_END-T.ANKLE_START), quintic=True)
        upper = f.smooth(f.op('DIVIDE', f.op('SUBTRACT', z, T.TWIST_START), T.CHEST_END-T.TWIST_START), quintic=True)
        support = f.op('SUBTRACT', 1., f.op('MULTIPLY', value(f, 'Supported lower blend', 'ar*la', ctrl), f.op('SUBTRACT', 1., lower)))
        difference = value(f, 'Distributed relative chest turn', 'ar*ts*(py*pg-cy*cg)*pi/180', ctrl)
        yaw = f.op('ADD', chest, f.op('MULTIPLY', difference, f.op('SUBTRACT', 1., upper)))
        pitch, roll, yaw = (f.op('MULTIPLY', x, support) for x in (pitch, roll, yaw))
    elif mode == 'pelvis':
        yaw = value(f, 'Lower frame heading', '('+PELVIS+')*pi/180', ctrl)
    point = f.vec('SUBTRACT', position, T.PIVOT)
    for axis, angle in zip(((1, 0, 0), (0, 1, 0), (0, 0, 1)), (pitch, roll, yaw)):
        point = f.rotate(point, axis, angle)
    return f.vec('ADD', point, T.PIVOT)


def replace_posture(ob, ctrl, mode):
    mod = next(m for m in ob.modifiers if m.name.startswith('Sweep25 | Rigid posture'))
    group = bpy.data.node_groups.new('Sweep30 | '+mode+' transport', 'GeometryNodeTree')
    for io in ('INPUT', 'OUTPUT'):
        group.interface.new_socket(name='Geometry', in_out=io, socket_type='NodeSocketGeometry')
    f = N.Fields(group)
    f.stage('Rest coordinates > coherent '+mode+' frame')
    gi, go = f.node('NodeGroupInput'), f.node('NodeGroupOutput')
    position = f.node('GeometryNodeInputPosition').outputs[0]
    base = np.array(ob.matrix_world)
    inv = np.linalg.inv(base)
    world = f.vec('ADD', f.transform(tuple(tuple(base[:3, i]) for i in range(3)), position), tuple(base[:3, 3]))
    final = field(f, world, ctrl, mode)
    local = f.vec('ADD', f.transform(tuple(tuple(inv[:3, i]) for i in range(3)), final), tuple(inv[:3, 3]))
    moved = f.node('GeometryNodeSetPosition')
    f.put(moved.inputs['Geometry'], gi.outputs[0])
    f.put(moved.inputs['Position'], local)
    if mode == 'body':
        f.put(moved.inputs['Selection'], f.op('GREATER_THAN', f.attr('s25_posture_body', 'FLOAT'), .5))
    f.put(go.inputs[0], moved.outputs[0])
    mod.name, mod.node_group = 'Sweep30 | '+mode+' frame', group
    N.layout(group)


def animate(ctrl, scene):
    ctrl.animation_data_clear()
    for name, (default, lo, hi, description) in {
        'Torso articulation': (1., 0., 1., '0 common rigid frame; 1 independent pelvis/chest sections'),
        'Leg anchoring': (1., 0., 1., 'Fade lower gray attachment rotation to the unchanged planted paws'),
        'Turn separation': (1., 0., 1., '1 uses independent pelvis yaw; 0 aligns lower yaw with the chest while retaining leg anchoring'),
        'Chest turn gain': (1., 0., 1.5, 'Scale the authored chest yaw; shoulders, arms and rigid head follow'),
        'Pelvis turn gain': (1., 0., 1.5, 'Scale the separate lower yaw; tail root follows the lower frame'),
        'Chest yaw': (0., -25., 25., 'Authored chest heading in degrees; not a source-measured angle'),
        'Pelvis yaw': (0., -8., 8., 'Authored supported lower heading in degrees'),
    }.items():
        ctrl[name] = default
        ctrl.id_properties_ui(name).update(min=lo, max=hi, description=description)
    for key in ('Amplitude', 'Body coupling'):
        ctrl[key] = 1.
    curves = dict(T.SCORES)
    for key, source in [('Attention', 'Work posture'), ('Head response', 'Stroke')]:
        curves[key] = [(min(4., t+.07), value) for t, value in T.SCORES[source]]
    for key, knots in curves.items():
        for t, val in knots:
            ctrl[key] = float(val)
            ctrl.keyframe_insert(data_path='["'+key+'"]', frame=1+60*t)
    for layer in ctrl.animation_data.action.layers:
        for strip in layer.strips:
            for bag in strip.channelbags:
                for fc in bag.fcurves:
                    points = fc.keyframe_points
                    for i, p in enumerate(points):
                        p.interpolation = 'BEZIER'
                        p.handle_left_type = p.handle_right_type = 'FREE'
                        dl = (p.co.x-points[i-1].co.x)/3 if i else 1.
                        dr = (points[i+1].co.x-p.co.x)/3 if i+1 < len(points) else 1.
                        p.handle_left, p.handle_right = (p.co.x-dl, p.co.y), (p.co.x+dr, p.co.y)
                    fc.update()
    scene.render.fps, scene.frame_start, scene.frame_end = 60, 1, 240
    set_time(scene, 0)


def extend(scene):
    ctrl = bpy.data.objects[OLD.CTRL]
    ctrl.name = CTRL
    animate(ctrl, scene)
    replace_posture(bpy.data.objects[K.PARTS['joined']], ctrl, 'body')
    replace_posture(bpy.data.objects[K.PARTS['tail']], ctrl, 'pelvis')
    replace_posture(bpy.data.objects['S126 | Body-bound shoulders'], ctrl, 'chest')
    for name in ARM.values():
        group = bpy.data.objects[name].modifiers[0].node_group
        f = N.Fields(group)
        f.stage('Sweep30 | One rigid chest attachment frame')
        node = group.nodes['Evaluated arm before prop attachment']
        position = f.node('GeometryNodeInputPosition').outputs[0]
        f.put(node.inputs['Position'], field(f, position, ctrl, 'chest'))
        heading = group.nodes.get('Tool follows body heading')
        if heading:
            driver(group, f'nodes["{heading.name}"].outputs[0].default_value', '10000*('+CHEST+')*pi/180', ctrl)
            heading.label = 'Tool floor heading follows the chest task'
        N.layout(group)
    carrier = bpy.data.objects['Sweep25 | Rigid posture carrier']
    carrier.name = 'Sweep30 | Rigid chest carrier'
    for i, expression in enumerate((PITCH, ROLL, CHEST)):
        driver(carrier, 'rotation_euler', '('+expression+')*pi/180', ctrl, i)
    for ob in (ctrl, carrier):
        ob.update_tag()
    set_time(scene, 0)
    return ctrl


def snapshot():
    return dict(body=K.vertices(K.PARTS['joined']), tail=K.vertices(K.PARTS['tail']),
                shoulders=K.vertices('S126 | Body-bound shoulders'),
                **{side: OLD.geometry(bpy.data.objects[name]) for side, name in ARM.items()},
                head=OLD.head_vertices())


def difference(a, b):
    def values(x, y):
        if isinstance(x, dict):
            return max(values(x[k], y[k]) for k in x)
        if isinstance(x, tuple):
            return max([values(u, v) for u, v in zip(x, y) if len(u)] or [0.])
        return float(np.max(np.abs(x-y)))
    return values(a, b)


def rigid_array(v, angles):
    return (v-np.array(T.PIVOT))@np.array(T.rotation(*angles)).T+T.PIVOT


def deformed_array(v, angles, articulation=1., leg=1.):
    # Vectorized independent calculation, outside Geometry Nodes.
    q = v[:, 2]
    low = np.clip((q-T.ANKLE_START)/(T.HIP_END-T.ANKLE_START), 0, 1)
    high = np.clip((q-T.TWIST_START)/(T.CHEST_END-T.TWIST_START), 0, 1)
    low = low**3*(10+low*(-15+6*low))
    high = high**3*(10+high*(-15+6*high))
    support = 1-articulation*leg*(1-low)
    pitch, roll, chest, pelvis = (angles[k] for k in ('pitch', 'roll', 'chest', 'pelvis'))
    a = np.deg2rad(pitch*support)
    b = np.deg2rad(roll*support)
    c = np.deg2rad((chest+articulation*(pelvis-chest)*(1-high))*support)
    x, y, z = (v-np.array(T.PIVOT)).T
    y, z = y*np.cos(a)-z*np.sin(a), y*np.sin(a)+z*np.cos(a)
    x, z = x*np.cos(b)+z*np.sin(b), -x*np.sin(b)+z*np.cos(b)
    x, y = x*np.cos(c)-y*np.sin(c), x*np.sin(c)+y*np.cos(c)
    return np.column_stack((x, y, z))+T.PIVOT


def attribute_signature():
    ob = bpy.data.objects[K.PARTS['joined']].evaluated_get(bpy.context.evaluated_depsgraph_get())
    mesh = ob.to_mesh()
    try:
        attrs = {}
        for attr in mesh.attributes:
            if attr.name in ('position', '.select_vert', '.select_edge', '.select_poly'):
                continue
            prop, width = {'FLOAT': ('value', 1), 'FLOAT_VECTOR': ('vector', 3),
                           'FLOAT_COLOR': ('color', 4), 'INT': ('value', 1),
                           'BOOLEAN': ('value', 1)}.get(attr.data_type, (None, 0))
            if prop is None:
                continue
            values = np.empty(len(attr.data)*width)
            attr.data.foreach_get(prop, values)
            attrs[attr.name] = dict(domain=attr.domain, type=attr.data_type,
                                    sha256=hashlib.sha256(values.tobytes()).hexdigest())
        faces = [tuple(poly.vertices) for poly in mesh.polygons]
        return dict(vertices=len(mesh.vertices), polygons=len(mesh.polygons),
                    topologySHA256=hashlib.sha256(repr(faces).encode()).hexdigest(),
                    materials=[m.name if m else None for m in mesh.materials], attributes=attrs)
    finally:
        ob.to_mesh_clear()


def check_pose(scene, ctrl, t, baseline, mask, neck0, articulation=1., leg=1.):
    ctrl['Torso articulation'], ctrl['Leg anchoring'] = articulation, leg
    ctrl.update_tag()
    set_time(scene, t)
    p = T.pose(t)
    actual = snapshot()
    expected = deformed_array(baseline['body'], p, articulation, leg)
    expected[~mask] = baseline['body'][~mask]
    row = dict(seconds=t, articulation=articulation, legAnchoring=leg, controls=T.controls(t),
               bodyDegrees=p, bodyFieldError=float(abs(expected-actual['body']).max()),
               displayedPawDrift=float(abs(actual['body'][~mask]-baseline['body'][~mask]).max()))
    row['curveError'] = max(abs(float(ctrl[k])-v) for k, v in row['controls'].items())
    row['shoulderFrameError'] = float(abs(actual['shoulders']-rigid_array(baseline['shoulders'], (p['pitch'], p['roll'], p['chest']))).max())
    tail_yaw = p['chest']+articulation*(p['pelvis']-p['chest'])
    row['tailFrameError'] = float(abs(actual['tail']-rigid_array(baseline['tail'], (p['pitch'], p['roll'], tail_yaw))).max())
    neck = np.array(bpy.data.objects['M132 | Neck articulation'].matrix_world)
    delta = neck@np.linalg.inv(neck0)
    row['headRigidError'] = max(float(abs(vertices-(baseline['head'][name]@delta[:3, :3].T+delta[:3, 3])).max()) for name, vertices in actual['head'].items())
    w, stroke = row['controls']['Work posture'], row['controls']['Stroke']
    row['arms'] = {}
    for side in 'RL':
        channels = dict(Swing=-15+7*w-7*stroke, Elbow=18*w-6*stroke, dForward=8*w+40*stroke,
                        dRaise=10+5*w, **{'Elbow softness': .55, 'kStretch': 1.}) if side == 'R' else dict(Swing=0., Elbow=0., dRaise=0., kStretch=1.)
        arm, info = S.evaluate(side, channels)
        predicted = rigid_array(arm, (p['pitch'], p['roll'], p['chest']))
        row['arms'][side] = dict(error=float(abs(actual[side][0]-predicted).max()), jacobian=info['jacobianMin'])
        assert row['arms'][side]['error'] < 3e-6, row
        assert info['jacobianMin'] > 0, row
    prop = actual['R'][1]
    hand = actual['R'][0][S.paw_indices('R')].mean(0)
    raw = np.array([v.co[:] for v in bpy.data.objects['Sweep25 | Fixed broom scaffold'].data.vertices])
    beta = OLD.M.broom_tilt(hand[2], row['controls']['Unloaded lift'])
    matrix = np.array(Matrix.Rotation(beta, 4, 'X')@Matrix.Rotation(math.radians(OLD.M.BROOM_YAW), 4, 'Z'))[:3, :3]
    tool = (raw-[0, 0, OLD.M.GRIP])@matrix.T
    tool[:, 1] += .025*row['controls']['Bristle drag']*np.clip((-.335-raw[:, 2])/.275, 0, 1)**2
    heading = np.array(T.rotation(0, 0, p['chest']))
    tool = tool@heading.T+hand
    row['propError'] = float(abs(prop-tool).max())
    row['floorLiftError'] = float(prop[:, 2].min()-OLD.M.FLOOR-row['controls']['Unloaded lift'])
    row['hand'] = hand.tolist()
    for key in ('curveError', 'bodyFieldError', 'shoulderFrameError', 'tailFrameError', 'headRigidError', 'propError', 'floorLiftError'):
        assert abs(row[key]) < 3e-6, (key, row)
    assert row['displayedPawDrift'] < 1e-7, row
    return row, actual


def clay_render(scene, rs, path):
    """Isolate the actual evaluated torso/paws to inspect the entire shaded surface."""
    bpy.context.window.scene = scene
    dg = bpy.context.evaluated_depsgraph_get()
    original = bpy.data.objects[K.PARTS['joined']]
    mesh = bpy.data.meshes.new_from_object(original.evaluated_get(dg), preserve_all_data_layers=True, depsgraph=dg)
    ob = bpy.data.objects.new('Sweep30 | Shaded body diagnostic', mesh)
    rs.collection.objects.link(ob)
    ob.matrix_world = original.matrix_world.copy()
    mat = bpy.data.materials.new('Sweep30 | Neutral clay diagnostic')
    mat.use_nodes = True
    bsdf = next(n for n in mat.node_tree.nodes if n.type == 'BSDF_PRINCIPLED')
    bsdf.inputs['Base Color'].default_value = (.45, .45, .45, 1.)
    bsdf.inputs['Roughness'].default_value = .55
    mesh.materials.clear()
    mesh.materials.append(mat)
    for p in mesh.polygons:
        p.material_index = 0
    lamps = []
    for location, power, size in [((3, -4, 5), 700, 4), ((-3, 1, 3), 300, 3)]:
        light = bpy.data.lights.new('Sweep30 | Clay light', 'AREA')
        light.energy, light.shape, light.size = power, 'DISK', size
        lamp = bpy.data.objects.new(light.name, light)
        rs.collection.objects.link(lamp)
        lamp.location = location
        lamp.rotation_euler = (Vector((0, 0, .5))-lamp.location).to_track_quat('-Z', 'Y').to_euler()
        lamps.append(lamp)
    previous_samples = rs.cycles.samples
    rs.cycles.samples = 24
    bpy.context.window.scene = rs
    paths = {}
    for view in ('front', 'oblique', 'side', 'back'):
        if view == 'back':
            K.set_view(rs, 'front')
            rs.camera.location = (0, 7, .60)
            rs.camera.rotation_euler = Vector((0, -7, 0)).to_track_quat('-Z', 'Y').to_euler()
        else:
            K.set_view(rs, view)
            rs.camera.location.z = .60
        rs.camera.data.ortho_scale = 2.05
        dest = path.parent/(path.name+'-'+view+'.png')
        rs.render.filepath = str(dest)
        bpy.ops.render.render(write_still=True)
        paths[view] = dict(file=dest.name, sha256=K.sha(dest))
    rs.cycles.samples = previous_samples
    for lamp in lamps:
        light = lamp.data
        bpy.data.objects.remove(lamp, do_unlink=True)
        bpy.data.lights.remove(light)
    bpy.data.objects.remove(ob, do_unlink=True)
    bpy.data.meshes.remove(mesh)
    bpy.data.materials.remove(mat)
    bpy.context.window.scene = scene
    return paths


def edit_probe(scene, ctrl, key, val):
    set_time(scene, 2.08)
    a = snapshot()
    previous = ctrl[key]
    ctrl[key] = val
    ctrl.update_tag()
    set_time(scene, 2.08)
    b = snapshot()
    change = difference(a, b)
    ctrl[key] = previous
    ctrl.update_tag()
    set_time(scene, 2.08)
    reset = difference(a, snapshot())
    assert change > 1e-4 and reset < 3e-6, (key, change, reset)
    return dict(control=key, value=val, actualGeometryChange=change, restoreError=reset,
                pawDrift=float(abs(a['body'][~OLD.body_mask()]-b['body'][~OLD.body_mask()]).max()),
                bladeFloorError=float(b['R'][1][:, 2].min()-OLD.M.FLOOR))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    assert not PATH.exists(), 'Never overwrite a saved candidate'
    assert shutil.disk_usage(OUT).free > 5_400_000_000, 'Reserve native and review space above 5GB'
    assert K.sha(SOURCE) == SOURCE_SHA
    scene, rs, _ = K.open_native(SOURCE, res=640)
    rs.render.engine = 'CYCLES'
    rs.cycles.device, rs.cycles.samples, rs.cycles.use_denoising = 'CPU', 8, False
    rs.render.use_persistent_data = False
    set_time(scene, 0)
    baseline = snapshot()
    signature = attribute_signature()
    mask = OLD.body_mask()
    neck0 = np.array(bpy.data.objects['M132 | Neck articulation'].matrix_world)
    # RED is an observed absent capability on the actual pre-extension native.
    old_controller = bpy.data.objects[OLD.CTRL]
    absent = [k for k in ('Chest yaw', 'Pelvis yaw', 'Torso articulation', 'Leg anchoring') if k not in old_controller]
    assert len(absent) == 4
    report = dict(scope='Authored relative torso capability and controlled task-equivalent A/B pilot',
                  sourceSHA256=SOURCE_SHA, referenceSHA256=REFERENCE_SHA,
                  blender=bpy.app.version_string,
                  scripts={p.name: K.sha(p) for p in (Path(__file__), Path(T.__file__))},
                  red=dict(status='EXPECTED_CAPABILITY_FAILURE', absentControls=absent,
                           sourceSHA256=SOURCE_SHA, reason='Only one common body frame exists in the unchanged native'),
                  baselineSurface=signature, rows=[], images=[], clay=[])
    ctrl = extend(scene)
    report['restError'] = difference(baseline, snapshot())
    assert report['restError'] < 3e-6
    assert attribute_signature() == signature, 'Rest topology/material attributes changed'
    write_json(OUT/'pilot.json', report)
    print('SWEEP30_BUILT', report['restError'], flush=True)
    # Interior and key-boundary samples verify the actual deforming native.
    times = sorted(set([i/10 for i in range(41)]+[t for _, t in T.KEYS]+[t for v in T.SCORES.values() for t, _ in v]))
    for i, t in enumerate(times):
        row, actual = check_pose(scene, ctrl, t, baseline, mask, neck0)
        report['rows'].append(row)
        if i % 10 == 0:
            write_json(OUT/'pilot.json', report)
            print('SWEEP30_NATIVE_SAMPLE', i, t, row['bodyFieldError'], flush=True)
    for label, t in T.KEYS:
        equal = {}
        for case, articulation, leg in [('A-common', 0., 1.), ('B-articulated', 1., 1.)]:
            row, actual = check_pose(scene, ctrl, t, baseline, mask, neck0, articulation, leg)
            equal[case] = actual
            paths = K.render(scene, rs, OUT/(case+'-'+label), views=VIEWS)
            report['images'].append(dict(case=case, pose=label, seconds=t, checks=row,
                                         views={v: dict(file=Path(p).name, sha256=K.sha(p)) for v, p in zip(VIEWS, paths)}))
        task_error = max(difference({k: equal['A-common'][k] for k in ('R', 'L', 'head', 'shoulders')},
                                    {k: equal['B-articulated'][k] for k in ('R', 'L', 'head', 'shoulders')}), 0.)
        assert task_error < 3e-6, (label, task_error)
        report['images'][-1]['equalUpperTaskError'] = task_error
        write_json(OUT/'pilot.json', report)
        print('SWEEP30_PILOT_POSE', label, task_error, flush=True)
    for case, articulation, leg, separation in [('A-common', 0., 1., 1.), ('B-articulated', 1., 1., 1.),
                                               ('C-no-relative-turn', 1., 1., 0.), ('D-no-leg-anchor', 1., 0., 1.)]:
        ctrl['Torso articulation'], ctrl['Leg anchoring'], ctrl['Turn separation'] = articulation, leg, separation
        ctrl.update_tag()
        set_time(scene, 2.08)
        if case.startswith(('C-', 'D-')):
            paths = K.render(scene, rs, OUT/(case+'-work-end'), views=VIEWS)
            report['images'].append(dict(case=case, pose='work-end', seconds=2.08,
                                         views={v: dict(file=Path(p).name, sha256=K.sha(p)) for v, p in zip(VIEWS, paths)}))
        report['clay'].append(dict(case=case, pose='work-end', views=clay_render(scene, rs, OUT/(case+'-clay'))))
        write_json(OUT/'pilot.json', report)
    ctrl['Torso articulation'] = ctrl['Leg anchoring'] = ctrl['Turn separation'] = 1.
    ctrl.update_tag()
    set_time(scene, 2.08)
    assert attribute_signature() == signature, 'Deformed topology/material attributes changed'
    report['controlProbes'] = [edit_probe(scene, ctrl, key, val) for key, val in
                               [('Torso articulation', 0.), ('Leg anchoring', 0.), ('Turn separation', 0.), ('Chest turn gain', .5),
                                ('Pelvis turn gain', .5), ('Body coupling', .5), ('Amplitude', .65)]]
    set_time(scene, 0)
    report['endRestError'] = difference(baseline, snapshot())
    readme = bpy.data.texts.new('SWEEP30_README')
    readme.write('Sweep30 supported chest/pelvis articulation candidate.\nSelect Sweep30 | Torso and sweep. Frames1-240 at60fps; quiet endpoint241.\nTorso articulation0 gives common body rotation;1 enables the broad relative yaw field. Leg anchoring fades the gray lower attachment to planted paws.\nChest yaw and Pelvis yaw are degree-valued ordinary curves. Chest turn gain and Pelvis turn gain independently scale them. Body coupling scales pitch/roll; Amplitude scales the local working-arm stroke.\nShoulders, arms and the rigid head follow the chest. Tail follows the lower frame. Belly material coordinates deform with the body.\nThe existing native shape graph is preserved. No external cache, frame handler or custom driver namespace is needed. Rest/scaffold/topology edits require revalidating attachment bands and existing material attributes.\nAuthored from independent front/oblique references, not measured joint angles or source-coordinate fitting. No adoption or all-control-domain certificate.\n')
    bpy.context.window.scene = scene
    bpy.context.preferences.filepaths.save_version = 0
    bpy.ops.wm.save_as_mainfile(filepath=str(PATH), compress=True)
    saved = snapshot()
    bpy.ops.wm.open_mainfile(filepath=str(PATH), use_scripts=False)
    scene, ctrl = bpy.context.scene, bpy.data.objects[CTRL]
    set_time(scene, 0)
    report['reopenError'] = difference(saved, snapshot())
    assert report['reopenError'] < 3e-6
    report['reopenControlProbes'] = [edit_probe(scene, ctrl, key, val) for key, val in
                                     [('Torso articulation', 0.), ('Leg anchoring', .5),
                                      ('Chest turn gain', .65), ('Pelvis turn gain', .5)]]
    set_time(scene, 4)
    report['endpointError'] = difference(baseline, snapshot())
    assert report['endpointError'] < 3e-6
    assert K.sha(SOURCE) == SOURCE_SHA
    report.update(nativeSHA256=K.sha(PATH), nativeBytes=PATH.stat().st_size,
                  sourceUnchanged=True, freeBytes=shutil.disk_usage(OUT).free,
                  status='NATIVE_VERIFIED_VISUAL_REVIEW_PENDING')
    write_json(OUT/'pilot.json', report)
    print('SWEEP30_NATIVE_DONE', report['nativeSHA256'], len(report['rows']), flush=True)


if __name__ == '__main__':
    main()
