'use strict';
const source = document.getElementById('source');
const native = document.getElementById('native');
const videos = [source, native];
const scrub = document.getElementById('scrub');
const linked = document.getElementById('linked');
const canvas = document.getElementById('pose');
const ctx = canvas.getContext('2d');
const error = document.getElementById('error');
let evidence = null;
let requestedFrame = 61;
let requestedPlay = false;
let seeking = false;

function report(err) { error.textContent = String(err.message || err); }
function seekFrame(frame) {
  requestedFrame = Math.max(0, Math.min(179, Math.round(frame)));
  const t = requestedFrame / 30 + 0.0001;
  seeking = true;
  for (const video of videos) if (video.readyState >= 1) video.currentTime = t;
  scrub.value = requestedFrame;
  seeking = false;
  draw();
}
async function playBoth() {
  requestedPlay = true;
  const outcomes = await Promise.allSettled(videos.map(video => video.play()));
  const failed = outcomes.find(x => x.status === 'rejected');
  if (failed) { requestedPlay = false; report(failed.reason); }
}
function pauseBoth() { requestedPlay = false; videos.forEach(video => video.pause()); }
for (const video of videos) {
  video.playbackRate = 0.5;
  video.addEventListener('loadedmetadata', () => {
    video.currentTime = requestedFrame / 30 + 0.0001;
    if (requestedPlay) video.play().catch(report);
  });
  video.addEventListener('play', () => {
    if (linked.checked) {
      requestedPlay = true;
      for (const other of videos) if (other !== video && other.paused) other.play().catch(report);
    }
  });
  video.addEventListener('pause', () => {
    if (linked.checked) pauseBoth();
  });
  video.addEventListener('seeking', () => {
    if (!linked.checked || seeking) return;
    seeking = true;
    for (const other of videos) {
      if (other !== video && other.readyState >= 1 && Math.abs(other.currentTime-video.currentTime) > 0.025) {
        other.currentTime = video.currentTime;
      }
    }
    seeking = false;
  });
  video.addEventListener('ended', pauseBoth);
  video.addEventListener('error', () => report(new Error('Could not load '+video.getAttribute('src'))));
}
document.getElementById('play').addEventListener('click', () => {
  if (videos.some(video => !video.paused)) pauseBoth();
  else { if (source.ended || source.currentTime >= 5.96) seekFrame(0); playBoth(); }
});
document.getElementById('restart').addEventListener('click', () => { pauseBoth(); seekFrame(0); });
for (const [id, delta] of [['prev', -1], ['next', 1]]) {
  document.getElementById(id).addEventListener('click', () => {
    pauseBoth(); seekFrame(Math.round(source.currentTime*30)+delta);
  });
}
scrub.addEventListener('input', () => { pauseBoth(); seekFrame(Number(scrub.value)); });
document.getElementById('speed').addEventListener('change', event => {
  videos.forEach(video => { video.playbackRate = Number(event.target.value); });
});
document.querySelectorAll('[data-frame]').forEach(button => button.addEventListener('click', () => {
  pauseBoth(); seekFrame(Number(button.dataset.frame));
}));
linked.addEventListener('change', () => {
  if (linked.checked) {
    native.currentTime = source.currentTime;
    if (!source.paused) native.play().catch(report);
    else native.pause();
  }
});
function dot(p, color, radius=7) {
  ctx.beginPath(); ctx.arc(p[0], p[1], radius, 0, Math.PI*2);
  ctx.fillStyle=color; ctx.fill(); ctx.strokeStyle='white'; ctx.lineWidth=2; ctx.stroke();
}
function line(a, b, color, width=4) {
  ctx.beginPath(); ctx.moveTo(...a); ctx.lineTo(...b); ctx.strokeStyle=color; ctx.lineWidth=width; ctx.stroke();
}
function draw() {
  const frame=Math.max(0,Math.min(179,Math.floor(source.currentTime*30+0.001)));
  ctx.clearRect(0,0,960,960);
  if (evidence && document.getElementById('overlay').checked) {
    const r=evidence.rows[frame];
    line(r.shoulder_visible,r.hand_visible,'#2974bf');
    line(r.hand_visible,r.collar.center,'#b54f9c');
    dot(r.shoulder_visible,'#2974bf'); dot(r.hand_visible,'#2974bf');
    dot(r.collar.center,'#b54f9c'); dot(r.nose.center,'#c53c46');
    for (const eye of r.eyes_visible) dot(eye.center,'#c53c46',4);
    dot([r.lower_body.bbox[2],787],'#6b6dcc');
    dot([r.rear_contact.bbox[2],840],'#22a08c');
    line([325,848],[580,848],'#22a08c',2);
  }
  scrub.value=frame;
  document.getElementById('status').textContent=`Source f${frame} / ${source.currentTime.toFixed(2)}s · native ${native.currentTime.toFixed(2)}s`;
  document.getElementById('play').textContent=videos.some(video=>!video.paused)?'Pause both':'Play both';
}
function tick() { draw(); requestAnimationFrame(tick); }
fetch('pose-evidence.json').then(response => {
  if (!response.ok) throw new Error('Evidence HTTP '+response.status);
  return response.json();
}).then(data => { evidence=data; draw(); }).catch(report);
seekFrame(61);
requestAnimationFrame(tick);
