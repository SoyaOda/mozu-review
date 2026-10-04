"""Export reproducible plots of observable image features, not joint trajectories."""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT/'output/rig_candidates/chores214_20260925/v2/sweep31_support_audit'
data = json.loads((OUT/'image-evidence.json').read_text())['series']
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10, 'svg.fonttype': 'none'})
fig, axes = plt.subplots(2, 2, figsize=(12, 7), layout='constrained')
fig.patch.set_facecolor('#f5f2eb')
features = [('headEnvelopeMidX', 'Head-envelope midpoint X', False),
            ('noseOffsetInsideHead', 'Nose offset inside head', False),
            ('bindingX', 'Broom binding X vs initial head midpoint', True),
            ('belly_0.765_left', 'Lower cream-belly left edge X', False)]
for axis, (key, label, absolute) in zip(axes.flat, features):
    axis.set_facecolor('#fffefa')
    for name, color, style in [('source', '#196c63', '-'), ('A-common', '#917854', '--'), ('B-articulated', '#c94a50', '-')]:
        s = data[name]
        origin = s['rows'][0]['values']['headEnvelopeMidX' if absolute else key]
        values = [None if r['values'][key] is None else (r['values'][key]-origin)/s['restHeadWidth']*100 for r in s['rows']]
        axis.plot([r['seconds'] for r in s['rows']], values, color=color, linestyle=style, linewidth=2,
                  label={'source': 'Source29', 'A-common': 'Sweep30 A', 'B-articulated': 'Sweep30 B'}[name])
    axis.set_title(label, loc='left', fontweight='bold')
    axis.set_xlabel('Time (s)')
    axis.set_ylabel('% of initial head width' + ('' if absolute else ' / change from rest'))
    axis.axhline(0, color='#7f8983', linewidth=.8)
    axis.grid(axis='y', color='#dfe3dd', linewidth=.6)
    axis.set_xlim(0, 4)
    axis.spines[['top', 'right']].set_visible(False)
axes[0, 0].legend(loc='lower left', frameon=False, ncol=3, fontsize=9)
fig.suptitle('Observed presentation and reach — no hidden joint reconstruction', fontsize=15, fontweight='bold', x=.02, ha='left')
fig.savefig(OUT/'feature-curves.svg')
svg = OUT/'feature-curves.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
fig.savefig(OUT/'feature-curves.png', dpi=150)
(OUT/'chart-runtime.json').write_text(json.dumps({'matplotlib': matplotlib.__version__, 'input': 'image-evidence.json'}, indent=2)+'\n')
print('Four diagnostic plots exported')
