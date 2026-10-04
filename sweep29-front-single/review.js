'use strict';
const trials = JSON.parse(document.getElementById('trials').textContent);
const movie = document.getElementById('movie');
const chooser = document.getElementById('trial');
const play = document.getElementById('play');
const rate = document.getElementById('rate');
const scrub = document.getElementById('frame');
let current;
function label(id, value) { document.getElementById(id).textContent = value; }
function link(text, href) {
  const a = document.createElement('a'); a.textContent = text; a.href = href; return a;
}
function update() {
  play.textContent = movie.paused ? 'Play' : 'Pause';
  const seconds = Number.isFinite(movie.currentTime) ? movie.currentTime : 0;
  const frame = Math.min(current.frames - 1, Math.floor(seconds * current.fps + 0.00001));
  scrub.value = frame;
  label('time', `${seconds.toFixed(2)}s / frame ${frame} of ${current.frames - 1}`);
}
function choose() {
  movie.pause(); current = trials.find(t => t.id === chooser.value);
  scrub.max = current.frames - 1;
  label('error', ''); label('title', current.title); label('decision', current.decision);
  label('finding', current.summary); label('limits', current.limits.join(' '));
  label('format', `${current.width} × ${current.height} / ${current.fps}fps / ${current.frames} original frames`);
  document.getElementById('input').src = current.first;
  const caption = document.getElementById('input-caption');
  caption.replaceChildren(document.createTextNode(current.last ? 'Same pose supplied as both endpoints. ' : 'Starting pose only. '), link('First image', current.first));
  if (current.last) caption.append(document.createTextNode(' · '), link('Last image', current.last));
  const sheets = document.getElementById('sheets'); sheets.replaceChildren();
  for (const sheet of current.sheets) {
    const a = link('', sheet.file); const img = document.createElement('img');
    img.src = sheet.file; img.alt = `Frames ${sheet.first}–${sheet.last}`; img.loading = 'lazy';
    a.append(img); sheets.append(a);
  }
  const evidence = document.getElementById('evidence'); evidence.replaceChildren();
  for (const [name, file] of [['Review', 'review.json'], ['Exact prompt', 'PROMPT.txt'], ['Provenance', 'provenance.json']]) {
    if (evidence.childNodes.length) evidence.append(document.createTextNode(' · '));
    evidence.append(link(name, `${current.id}/${file}`));
  }
  for (const item of current.diagnostics) evidence.append(document.createTextNode(' · '), link(item.name, item.file));
  document.getElementById('original').href = current.movie;
  movie.src = current.movie; movie.load(); movie.playbackRate = Number(rate.value); update();
}
play.addEventListener('click', async () => {
  if (!movie.paused) { movie.pause(); return; }
  if (movie.ended) movie.currentTime = 0;
  try { await movie.play(); } catch (error) { label('error', error.message); }
});
document.getElementById('restart').addEventListener('click', () => { movie.pause(); movie.currentTime = 0; });
for (const [id, step] of [['prev', -1], ['next', 1]]) {
  document.getElementById(id).addEventListener('click', () => {
    movie.pause(); const frame = Math.min(current.frames - 1, Math.floor(movie.currentTime * current.fps + 0.00001));
    movie.currentTime = Math.max(0, Math.min(current.frames - 1, frame + step)) / current.fps + 0.00001;
  });
}
rate.addEventListener('change', () => { movie.playbackRate = Number(rate.value); });
scrub.addEventListener('input', () => { movie.pause(); movie.currentTime = Number(scrub.value) / current.fps + 0.00001; });
document.getElementById('loop').addEventListener('change', event => { movie.loop = event.target.checked; });
chooser.addEventListener('change', choose);
for (const event of ['timeupdate', 'play', 'pause', 'ended', 'seeked', 'loadedmetadata']) movie.addEventListener(event, update);
movie.addEventListener('error', () => label('error', `Media load failed (${movie.error?.code ?? 'unknown'}).`));
choose();
