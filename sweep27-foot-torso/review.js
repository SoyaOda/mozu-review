'use strict';
const video = document.getElementById('source');
const play = document.getElementById('play');
const scrub = document.getElementById('scrub');
const overlay = document.getElementById('overlay');
const error = document.getElementById('error');
const crops = [
  {canvas: document.getElementById('feet'), box: [315, 775, 280, 85]},
  {canvas: document.getElementById('torso'), box: [285, 630, 340, 200]}
];
let evidence = null;
let diagnostics = null;
let desiredFrame = 61;

function report(e) { error.textContent = String(e.message || e); }
function seek(frame) {
  desiredFrame = Math.max(0, Math.min(179, Math.round(frame)));
  video.pause();
  if (video.readyState >= 1) video.currentTime = desiredFrame / 30 + 0.0001;
}
function marker(ctx, p, color) {
  ctx.beginPath(); ctx.arc(p[0], p[1], 2.7, 0, Math.PI*2);
  ctx.fillStyle = color; ctx.fill(); ctx.strokeStyle = 'white'; ctx.lineWidth = .8; ctx.stroke();
}
function render() {
  const frame = Math.min(179, Math.max(0, Math.floor(video.currentTime*30 + .001)));
  scrub.value = frame;
  document.getElementById('time').textContent = `f${frame} / ${video.currentTime.toFixed(2)}s`;
  play.textContent = video.paused ? 'Play source' : 'Pause source';
  if (video.readyState < 2) return;
  for (const {canvas, box} of crops) {
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(video, ...box, 0, 0, canvas.width, canvas.height);
    if (!overlay.checked || !evidence || !diagnostics) continue;
    ctx.save(); ctx.scale(canvas.width/box[2], canvas.height/box[3]); ctx.translate(-box[0], -box[1]);
    const row = evidence.rows[frame];
    if (canvas.id === 'feet') {
      ctx.beginPath(); ctx.moveTo(332,846); ctx.lineTo(563,846);
      ctx.setLineDash([3,3]); ctx.lineWidth = .8; ctx.strokeStyle = '#159b82'; ctx.stroke(); ctx.setLineDash([]);
      for (const [name, track] of Object.entries(diagnostics.selectedTracks)) {
        marker(ctx, track.points[frame].slice(1), name === 'upper_junction' ? '#bd4549' : '#159b82');
      }
    } else {
      for (const [y,x] of Object.entries(row.back_edge_x_by_y)) marker(ctx, [x,Number(y)], '#7864b5');
    }
    ctx.restore();
  }
  if (evidence && diagnostics) {
    const r = evidence.rows[frame];
    const junction = diagnostics.selectedTracks.upper_junction.points[frame];
    const base = diagnostics.selectedTracks.upper_junction.points[0];
    document.getElementById('live').textContent =
      `Upper junction ΔY ${(junction[2]-base[2]).toFixed(1)}px · `+
      `back contour X ${r.back_edge_x_by_y['675']} / ${r.back_edge_x_by_y['790']}px · `+
      `front foot patch ${r.front_patch_occluded ? 'partly occluded' : 'exposed'}`;
  }
}
play.addEventListener('click', async () => {
  if (!video.paused) video.pause();
  else {
    if (video.ended || video.currentTime >= 5.97) seek(0);
    try { await video.play(); } catch (e) { report(e); }
  }
});
document.getElementById('restart').addEventListener('click', () => seek(0));
document.getElementById('prev').addEventListener('click', () => seek(Math.round(video.currentTime*30)-1));
document.getElementById('next').addEventListener('click', () => seek(Math.round(video.currentTime*30)+1));
document.getElementById('speed').addEventListener('change', e => { video.playbackRate = Number(e.target.value); });
scrub.addEventListener('input', () => seek(Number(scrub.value)));
overlay.addEventListener('change', render);
document.querySelectorAll('[data-frame]').forEach(button => button.addEventListener('click', () => seek(Number(button.dataset.frame))));
video.playbackRate = .5;
video.addEventListener('loadedmetadata', () => { video.currentTime = desiredFrame/30 + .0001; });
for (const event of ['loadeddata','seeked','timeupdate','play','pause','ended']) video.addEventListener(event, render);
video.addEventListener('error', () => report(new Error('The original source video could not be loaded.')));
Promise.all(['evidence.json','diagnostics.json'].map(async url => {
  const response = await fetch(url); if (!response.ok) throw new Error(`Could not load ${url}`); return response.json();
})).then(([a,b]) => { evidence=a; diagnostics=b; render(); }).catch(report);
function animate() { render(); requestAnimationFrame(animate); }
requestAnimationFrame(animate);
