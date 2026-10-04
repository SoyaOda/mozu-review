"""Build a portable audit with unchanged source/native movies and traceable evidence."""
import hashlib
import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
BASE = ROOT/'output/rig_candidates/chores214_20260925/v2/sweep31_support_audit'
OUT = BASE/'review'
DOCS = ROOT/'docs/research/chores214_20260925/sweep31_support_audit'
PRIOR = BASE.parent/'sweep30_torso'
CASE = ROOT/'output/ssot_candidates/sweep29_front_single_20261004/wan3-r01'


def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def read(path):
    return json.loads(path.read_text())


def copy(source, destination):
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)
    assert sha(source) == sha(destination)


def linked(name, label):
    label = html.escape(label)
    return f'<a href="figures/{name}" target="_blank"><img loading="lazy" src="figures/{name}" alt="{label}">{label}</a>'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    evidence = read(BASE/'image-evidence.json')
    pilot = read(PRIOR/'pilot01/pilot.json')
    assert evidence['scriptSHA256'] == sha(HERE/'analyze.py')
    assert evidence['nativeSHA256'] == pilot['nativeSHA256'] == sha(PRIOR/'pilot01/sweep30-torso.blend')
    state = read(CASE/'state.json')
    source = CASE/state['video']['file']
    assert sha(source) == evidence['series']['source']['videoSHA256']
    copy(source, OUT/'media/source29.mp4')
    for name in ('A-common', 'B-articulated'):
        path = PRIOR/'pilot01/media'/f'{name}-front.mp4'
        assert sha(path) == evidence['series'][name]['videoSHA256']
        copy(path, OUT/'media'/path.name)
    for path in sorted(set([*BASE.glob('source-*.jpg'), *BASE.glob('*-feature-keys.jpg'),
                            BASE/'comparison-2s.jpg', *BASE.glob('feature-*.png'), BASE/'feature-curves.svg'])):
        copy(path, OUT/'figures'/path.name)
    for name in ('image-evidence.json', 'rig-audit.json', 'visual-review.json', 'chart-runtime.json'):
        copy(BASE/name, OUT/'evidence'/name)
    for name in ('pilot.json', 'visual-review.json'):
        copy(PRIOR/'pilot01'/name, OUT/'evidence'/('sweep30-'+name))
    copy(PRIOR/'sequence-review.json', OUT/'evidence/sweep30-sequence-review.json')
    for name in ('torso_math.py', 'native.py'):
        path = HERE.parent/'sweep30_torso'/name
        assert sha(path) == pilot['scripts'][name]
        copy(path, OUT/'source'/name)
    for name in ('analyze.py', 'charts.py', 'page.py', 'review.js', 'template.html'):
        copy(HERE/name, OUT/'source'/name)
    for name in ('PLAN', 'REPORT', 'RIG_RETHINK'):
        path = DOCS/(name+'.md')
        copy(path, OUT/path.name)
        (OUT/(name+'.html')).write_text('<!doctype html><html lang="en"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Sweep31 / '+name+'</title><style>body{max-width:1040px;margin:30px auto;padding:0 20px;'
            'background:#f5f2eb;color:#233c32;font:16px/1.7 system-ui}pre{font:inherit;white-space:pre-wrap;'
            'overflow-wrap:anywhere}a{color:#196c63}</style><a href="./">Back to comparison</a><pre>'
            +html.escape(path.read_text())+'</pre></html>')
    compact = []
    for name in ('source', 'A-common', 'B-articulated'):
        s = evidence['series'][name]
        compact.append(dict(fps=s['fps'], pixels=s['rows'][0]['pixels'][0], restAxis=s['rows'][0]['values']['headEnvelopeMidX'],
                            rows=[dict(headBounds=r['headBounds'], nose=r['nose']['center'], binding=r['binding']['center'],
                                       belly=[[float(h), r['values'][f'belly_{h}_left']] for h in ('0.675', '0.715', '0.765')],
                                       soles=[[.330, .350, r['values']['nonholding_sole']], [.53, .55, r['values']['holding_sole']]]) for r in s['rows']]))
    metrics = []
    for key, label in [('headEnvelopeMidX', 'Gray head-envelope midpoint X'), ('noseOffsetInsideHead', 'Nose offset within head X'),
                       ('bindingX', 'Green broom binding X'), ('belly_0.715_left', 'Middle cream edge X'), ('belly_0.765_left', 'Lower cream edge X')]:
        vals = [evidence['series'][n]['summary'][key]['headWidthNormalizedRange']*100 for n in ('source', 'A-common', 'B-articulated')]
        metrics.append('<tr><td>'+label+'</td>'+''.join(f'<td>{v:.2f}%</td>' for v in vals)+f'<td>{vals[2]/vals[0]*100:.0f}%</td></tr>')
    video_html = []
    for j, (id_, title, description, filename) in enumerate([
        ('source', 'Source29 / front reference', 'Original generated source · 30fps', 'source29.mp4'),
        ('baseline', 'Sweep30 A / common frame', 'Central pivot · no relative torso yaw or leg fade', 'A-common-front.mp4'),
        ('candidate', 'Sweep30 B / articulated', 'Central pivot · relative yaw and leg fade enabled', 'B-articulated-front.mp4')]):
        video_html.append(f'<article class="video-card"><h3>{title}</h3><p class="note">{description}</p>'
                          f'<div class="stage"><video id="{id_}" aria-label="{title}" src="media/{filename}" preload="auto" muted playsinline></video>'
                          f'<canvas id="overlay-{j}" width="480" height="480" aria-hidden="true"></canvas></div></article>')
    values = {'{{VIDEOS}}': ''.join(video_html), '{{METRICS}}': ''.join(metrics),
              '{{DATA}}': json.dumps(compact, separators=(',', ':')).replace('<', '\\u003c'),
              '{{EVENTS}}': ''.join(f'<button data-time="{i/30:.8f}">{name} / f{i:03}</button>' for name, i in [
                  ('Hold', 0), ('Prepare', 44), ('Cross', 52), ('Inward sweep', 60), ('Return', 68), ('Late return', 78), ('Settle', 96)]),
              '{{FULL}}': ''.join(linked(f'source-full-{i}.jpg', f'Source frames {i*30}–{i*30+29}') for i in range(4)),
              '{{SUPPORT}}': ''.join(linked(f'source-support-{i}.jpg', f'Feet/trunk frames {i*30}–{i*30+29}') for i in range(4)),
              '{{KEYS}}': ''.join(linked(n+'-feature-keys.jpg', n+' · 14 annotated keys') for n in ('source', 'A-common', 'B-articulated')),
              '{{OVERLAYS}}': ''.join(linked(f'feature-{i:03}.png', f'Feature ownership · source f{i:03}') for i in (0, 44, 52, 60, 68, 78, 96))}
    page = (HERE/'template.html').read_text()
    for key, value in values.items():
        page = page.replace(key, value)
    assert '{{' not in page
    (OUT/'index.html').write_text(page)
    copy(HERE/'review.js', OUT/'review.js')
    files = [dict(path=str(p.relative_to(OUT)), bytes=p.stat().st_size, sha256=sha(p))
             for p in sorted(OUT.rglob('*')) if p.is_file() and p.name != 'manifest.json']
    (OUT/'manifest.json').write_text(json.dumps(dict(scope='Read-only support-axis and body-transport audit',
        nativeSHA256=evidence['nativeSHA256'], referenceSHA256=sha(source), files=files), indent=2)+'\n')
    print('SWEEP31_REVIEW_READY', len(files), sum(f['bytes'] for f in files))


if __name__ == '__main__':
    main()
