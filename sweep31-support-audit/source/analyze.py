"""Read-only image/control audit. Image features never drive the native rig."""
import hashlib
import importlib.util
import json
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
OUT = ROOT/'output/rig_candidates/chores214_20260925/v2/sweep31_support_audit'
CASE = ROOT/'output/ssot_candidates/sweep29_front_single_20261004/wan3-r01'
NATIVE = OUT.parent/'sweep30_torso/pilot01'
FONT = '/System/Library/Fonts/Supplemental/Arial.ttf'
KEYS = [0, 39, 44, 48, 52, 56, 60, 64, 68, 72, 78, 86, 96, 119]


def sha(path):
    with path.open('rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def read_video(path):
    cap = cv2.VideoCapture(str(path))
    fps = cap.get(cv2.CAP_PROP_FPS)
    images = []
    while True:
        ok, bgr = cap.read()
        if not ok:
            break
        images.append(cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB))
    cap.release()
    return images, fps


def masks(rgb, cutoff=100):
    r, g, b = [rgb[..., i].astype(float) for i in range(3)]
    dark = (r > 30) & (np.maximum.reduce([r, g, b]) < cutoff) & (np.maximum.reduce([r, g, b])-np.minimum.reduce([r, g, b]) < 23)
    gray = (r > 112) & (r < 186) & (g > 115) & (g < 188) & (b > r+5)
    belly = (r > 211) & (r < 245) & (g > 185) & (g < 226) & (b > 140) & (b < 206) & (r > g+12) & (g > b+22)
    nose = (r > 130) & (r < 213) & (g < 115) & (r > 1.45*g) & (b < 140)
    green = (g > r+12) & (g > b+7) & (r > 35) & (g < 220)
    tool = ((r > g+19) & (g > b+15) & (r > 112) & (b < 141) & (g < 199)) | green
    return dict(dark=dark, gray=gray, belly=belly, nose=nose, green=green, tool=tool)


def component(mask, box, minimum=10):
    h, w = mask.shape
    x, y, X, Y = [round(v*s) for v, s in zip(box, (w, h, w, h))]
    crop = np.zeros_like(mask, dtype=np.uint8)
    crop[y:Y, x:X] = mask[y:Y, x:X]
    n, labels, stats, centers = cv2.connectedComponentsWithStats(crop)
    ids = [i for i in range(1, n) if stats[i, cv2.CC_STAT_AREA] >= minimum]
    if not ids:
        return None
    i = max(ids, key=lambda k: stats[k, cv2.CC_STAT_AREA])
    x, y, dx, dy, area = stats[i].tolist()
    return dict(center=centers[i].tolist(), box=[x, y, x+dx-1, y+dy-1], area=area)


def median(values):
    return float(np.median(values)) if len(values) else None


def edge(mask, box, direction, obstruction=None):
    """Median edge in a narrow ROI; obstruction flag prevents false foot tracks."""
    h, w = mask.shape
    x, y, X, Y = [round(v*s) for v, s in zip(box, (w, h, w, h))]
    pts, blocked = [], 0
    if direction in ('left', 'right'):
        for yy in range(y, Y):
            xs = np.flatnonzero(mask[yy, x:X])
            if len(xs):
                xx = int(xs[0] if direction == 'left' else xs[-1])+x
                pts.append((xx, yy))
                if obstruction is not None and obstruction[max(0, yy-2):yy+3, max(0, xx-3):xx+4].any():
                    blocked += 1
    else:
        for xx in range(x, X):
            ys = np.flatnonzero(mask[y:Y, xx])
            if len(ys):
                yy = int(ys[-1])+y
                pts.append((xx, yy))
                if obstruction is not None and obstruction[max(0, yy-3):yy+4, max(0, xx-2):xx+3].any():
                    blocked += 1
    return dict(value=median([p[0] if direction != 'bottom' else p[1] for p in pts]),
                count=len(pts), blocked=blocked, accepted=bool(pts) and blocked == 0,
                points=pts)


def measure(rgb, cutoff=100):
    h, w = rgb.shape[:2]
    m = masks(rgb, cutoff)
    nose = component(m['nose'], (.2, .38, .75, .64))
    binding = component(m['green'], (.2, .65, .75, .89))
    assert nose and binding
    head = m['gray'].copy()
    head[round(.59*h):] = False
    yy, xx = np.where(head)
    hb = [int(xx.min()), int(yy.min()), int(xx.max()), int(yy.max())]
    center = (hb[0]+hb[2])/2
    support = {
        'nonholding_outer': edge(m['dark'], (.312, .856, .354, .875), 'left', m['tool']),
        'nonholding_sole': edge(m['dark'], (.330, .875, .350, .894), 'bottom', m['tool']),
        'holding_inner': edge(m['dark'], (.481, .856, .525, .875), 'left', m['tool']),
        'holding_sole': edge(m['dark'], (.53, .875, .55, .894), 'bottom', m['tool']),
    }
    belly = {}
    for y in (.675, .715, .765):
        box = (.29, y-.002, .58, y+.003)
        left = edge(m['belly'], box, 'left', m['tool'] | m['dark'])
        right = edge(m['belly'], box, 'right', m['tool'] | m['dark'])
        belly[str(y)] = dict(left=left, right=right)
    low = {}
    for y in (.79, .81, .825):
        low[str(y)] = dict(left=edge(m['gray'], (.28, y-.002, .65, y+.003), 'left', m['tool'] | m['dark']),
                          right=edge(m['gray'], (.28, y-.002, .65, y+.003), 'right', m['tool'] | m['dark']))
    scalars = {'noseX': nose['center'][0], 'noseY': nose['center'][1],
               'headEnvelopeMidX': center, 'headEnvelopeWidth': hb[2]-hb[0],
               'noseOffsetInsideHead': nose['center'][0]-center,
               'bindingX': binding['center'][0], 'bindingY': binding['center'][1]}
    for key, value in support.items():
        scalars[key] = value['value'] if value['accepted'] else None
    for label, values in [('belly', belly), ('lowerGray', low)]:
        for y, sides in values.items():
            for side, e in sides.items():
                scalars[f'{label}_{y}_{side}'] = e['value'] if e['accepted'] else None
    return dict(pixels=[w, h], nose=nose, binding=binding, headBounds=hb,
                support=support, belly=belly, lowerGray=low, values=scalars)


def stats(rows, key, scale):
    values = [r['values'][key] for r in rows if r['values'][key] is not None]
    if not values:
        return dict(valid=0)
    return dict(valid=len(values), minimum=min(values), maximum=max(values), range=max(values)-min(values),
                headWidthNormalizedRange=(max(values)-min(values))/scale)


def annotated(rgb, row):
    image = Image.fromarray(rgb)
    draw = ImageDraw.Draw(image)
    w, h = image.size
    width = max(1, round(w/400))
    draw.rectangle(row['headBounds'], outline='#328e9d', width=width)
    for key, color in [('nose', '#ef4267'), ('binding', '#30955e')]:
        x, y = row[key]['center']
        draw.ellipse((x-5, y-5, x+5, y+5), fill=color)
    for feature in row['support'].values():
        color = '#347ce0' if feature['accepted'] else '#ef5a2e'
        if feature['points']:
            draw.line(feature['points'], fill=color, width=width+1)
    for section in row['belly'].values():
        for feature in section.values():
            color = '#ae38bd' if feature['accepted'] else '#ef5a2e'
            if feature['points']:
                draw.line(feature['points'], fill=color, width=width+1)
    for section in row['lowerGray'].values():
        for feature in section.values():
            if feature['points']:
                draw.line(feature['points'], fill='#20a89b' if feature['accepted'] else '#ef5a2e', width=width+1)
    return image


def sheet(images, rows, indices, path, crop=None, columns=4, cell=(360, 395), overlay=False):
    cw, ch = cell
    board = Image.new('RGB', (columns*cw, ((len(indices)+columns-1)//columns)*ch), '#f5f2eb')
    font = ImageFont.truetype(FONT, 16)
    for j, i in enumerate(indices):
        tile = annotated(images[i], rows[i]) if overlay else Image.fromarray(images[i])
        if crop:
            tile = tile.crop(tuple(round(v*s) for v, s in zip(crop, (tile.width, tile.height)*2)))
        tile.thumbnail((cw-8, ch-34), Image.Resampling.LANCZOS)
        x, y = (j % columns)*cw, (j//columns)*ch
        board.paste(tile, (x+(cw-tile.width)//2, y+30))
        ImageDraw.Draw(board).text((x+8, y+7), f'f{i:03} / {rows[i]["seconds"]:.3f}s', fill='#263931', font=font)
    board.save(path, quality=95)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    index = json.loads((CASE/'decoded/index.json').read_text())
    assert index['videoSHA256'] == 'f47916172a0d827d3e68527cfdd167d2dea7b3a357f5cca19f0ae804b861cd6a'
    source = []
    for item in index['frames']:
        path = CASE/item['file']
        assert sha(path) == item['sha256']
        source.append(np.array(Image.open(path).convert('RGB')))
    assert len(source) == 120
    data = {}
    series = [('source', source, 30.0, index['videoSHA256'])]
    for name in ('A-common', 'B-articulated'):
        path = NATIVE/'media'/f'{name}-front.mp4'
        images, fps = read_video(path)
        assert len(images) == 240 and fps == 60
        series.append((name, images, fps, sha(path)))
    for name, images, fps, digest in series:
        rows = [dict(frame=i, seconds=i/fps, **measure(image)) for i, image in enumerate(images)]
        scale = rows[0]['values']['headEnvelopeWidth']
        result = dict(fps=fps, frames=len(images), videoSHA256=digest, restHeadWidth=scale,
                      summary={k: stats(rows, k, scale) for k in rows[0]['values']}, rows=rows)
        rest_axis = rows[0]['values']['headEnvelopeMidX']
        result['bindingAgainstRestHeadAxis'] = dict(
            restAxisPixels=rest_axis,
            minimumNormalized=(result['summary']['bindingX']['minimum']-rest_axis)/scale,
            maximumNormalized=(result['summary']['bindingX']['maximum']-rest_axis)/scale,
            interpretation='A fixed image reference through the initial head envelope midpoint; not an anatomical midplane.')
        data[name] = result
        if name == 'source':
            for k in range(4):
                indices = list(range(k*30, (k+1)*30))
                sheet(images, rows, indices, OUT/f'source-full-{k}.jpg', columns=5, cell=(288, 312))
                sheet(images, rows, indices, OUT/f'source-support-{k}.jpg', crop=(.22, .585, .735, .9), columns=5, cell=(360, 250))
            sheet(images, rows, KEYS, OUT/'source-feature-keys.jpg', columns=4, cell=(420, 450), overlay=True)
            for i in (0, 44, 52, 60, 68, 78, 96):
                annotated(images[i], rows[i]).save(OUT/f'feature-{i:03}.png')
            sensitivity = {}
            for cutoff in (90, 110):
                alt = [dict(values=measure(a, cutoff)['values']) for a in images]
                sensitivity[str(cutoff)] = {k: stats(alt, k, scale) for k in rows[0]['support']}
            result['darkThresholdSensitivity'] = sensitivity
            result['contactCaveats'] = [
                'Nonholding outer edge and sampled soles are stable across dark cutoffs90,100,110.',
                'Holding inner edge has2px range at90/100 but11px at110: threshold-sensitive; do not use as an exact foot-motion bound.',
                'Holding sole has108/120 unoccluded samples. No step/lift is visually observed; full hidden contact and load remain unknown.']
        else:
            sheet(images, rows, [i*2 for i in KEYS], OUT/f'{name}-feature-keys.jpg', columns=4, cell=(420, 450), overlay=True)
    comparisons = {}
    for name in ('A-common', 'B-articulated'):
        comparisons[name] = {key: data[name]['summary'][key]['headWidthNormalizedRange'] /
                             data['source']['summary'][key]['headWidthNormalizedRange']
                             for key in ('headEnvelopeMidX', 'noseOffsetInsideHead', 'noseX', 'noseY',
                                         'bindingX', 'belly_0.675_left', 'belly_0.715_left', 'belly_0.765_left')}
    board = Image.new('RGB', (1440, 560), '#f5f2eb')
    draw = ImageDraw.Draw(board)
    font = ImageFont.truetype(FONT, 22)
    for column, (name, images, fps, _) in enumerate(series):
        frame = round(2.0*fps)
        tile = Image.fromarray(images[frame]).resize((480, 480), Image.Resampling.LANCZOS)
        board.paste(tile, (480*column, 70))
        draw.text((480*column+16, 15), {'source': 'Source29', 'A-common': 'Sweep30 A: common',
                                     'B-articulated': 'Sweep30 B: articulated'}[name], fill='#263931', font=font)
        draw.text((480*column+16, 43), '2.00 s / original frames, matched display size', fill='#546b61', font=ImageFont.truetype(FONT, 16))
    board.save(OUT/'comparison-2s.jpg', quality=96)
    evidence = dict(schema='Sweep31ObservableImageFeatures1', status='ANALYSIS_ONLY',
                    nativeSHA256=sha(NATIVE/'sweep30-torso.blend'), methods={
                        'units': 'Raw pixel units at each native resolution; range normalized by initial gray-head-envelope width for cross-series comparison.',
                        'labels': 'Source image-left is the non-holding-side foot; image-right is the holding-side foot.',
                        'occlusion': 'Edge points touching tool/arm-class pixels are rejected, not imputed. Gray/cream boundaries are image boundaries, not anatomical joints.',
                        'comparison': 'Independent source/native performances; range diagnostics and named events, not pixel/pose fitting or calibrated 3D reconstruction.'},
                    scriptSHA256=sha(Path(__file__)), normalizedRangeRatiosToSource=comparisons, series=data)
    (OUT/'image-evidence.json').write_text(json.dumps(evidence, indent=2)+'\n')
    spec = importlib.util.spec_from_file_location('s30math', HERE.parent/'sweep30_torso/torso_math.py')
    math = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(math)
    samples = [dict(seconds=i/60, **math.pose(i/60)) for i in range(241)]
    for row in samples:
        row['relativeYaw'] = row['chest']-row['pelvis']
    audit = dict(nativeSHA256=evidence['nativeSHA256'], commonPivot=math.PIVOT,
                 pivotIsNotFootSelected=True, supportSideControl=False, contactRelativeRootTranslationControl=False,
                 supportFieldDependsOnRestZOnly=True, nativeBuildAndReopenEvidence='sweep30_torso/pilot01/pilot.json',
                 peakRelativeYaw=max(samples, key=lambda r: abs(r['relativeYaw'])),
                 controls=samples, sharedABTasks=['chest transform', 'head transform', 'shoulder frames', 'arms', 'grip', 'broom'],
                 implications=['A/B cannot test alternative support pivots because both use the same central PIVOT and equal upper tasks.',
                               'A/B toggles both relative yaw and the leg anchoring fade; C is the closer yaw-only ablation.',
                               'Zero paw drift is enforced by excluding paw vertices; it does not identify the loaded/support side.',
                               'The 12-degree-class differential yaw is authored, not observed from the source.',
                               'The old capability RED checks missing new controls, not a demonstrated source-performance failure.'])
    (OUT/'rig-audit.json').write_text(json.dumps(audit, indent=2)+'\n')
    for name, row in data.items():
        print(name, row['restHeadWidth'], {k: v for k, v in row['summary'].items() if k in ('noseX', 'noseY', 'headEnvelopeMidX', 'noseOffsetInsideHead', 'bindingX', 'nonholding_outer', 'holding_inner', 'nonholding_sole', 'holding_sole')})


if __name__ == '__main__':
    main()
