"use strict";
const $ = id => document.getElementById(id);
const videos = [$("source"), $("baseline"), $("candidate")];
const master = videos[2];
const data = JSON.parse($("data").textContent);
let playing = false, generation = 0;
const frameAt = (t, fps, length) => Math.max(0, Math.min(length - 1, Math.floor(t * fps + .001)));
function error(e) { $("error").textContent = String(e?.message || e); }
function pause() {
  generation++;
  playing = false;
  for (const v of videos) v.pause();
  $("play").textContent = "Play comparison";
}
function seek(t) {
  pause();
  const time = Math.max(0, Math.min(239 / 60, t));
  for (const v of videos) v.currentTime = time + .00001;
  paint();
}
async function play() {
  if (master.ended || master.currentTime >= 3.998) seek(0);
  for (const v of videos) v.currentTime = master.currentTime;
  const token = ++generation;
  playing = true;
  $("play").textContent = "Pause comparison";
  try { await Promise.all(videos.map(v => v.play())); }
  catch (e) { if (token === generation) { error(e); pause(); } }
}
function dot(c, x, y, color, size = 4) {
  c.fillStyle = color; c.beginPath(); c.arc(x, y, size, 0, 2 * Math.PI); c.fill();
}
function paint() {
  const i = frameAt(master.currentTime, 60, 240);
  $("seek").value = i;
  $("time").textContent = `${master.currentTime.toFixed(2)} / 4.00 s · source ${String(frameAt(videos[0].currentTime, 30, 120)).padStart(3, "0")} /119 · native ${String(i).padStart(3, "0")} /239`;
  data.forEach((s, j) => {
    const c = $("overlay-" + j).getContext("2d");
    c.clearRect(0, 0, 480, 480);
    if (!$("features").checked) return;
    const r = s.rows[frameAt(videos[j].currentTime, s.fps, s.rows.length)];
    const scale = 480 / s.pixels;
    c.save(); c.scale(scale, scale); c.lineWidth = 1.5 / scale;
    const [x, y, X, Y] = r.headBounds;
    c.strokeStyle = "#328e9d"; c.strokeRect(x, y, X - x, Y - y);
    dot(c, ...r.nose, "#ef4267", 4 / scale);
    dot(c, ...r.binding, "#30955e", 4 / scale);
    c.setLineDash([5 / scale, 4 / scale]); c.strokeStyle = "#b2b9b0";
    c.beginPath(); c.moveTo(s.restAxis, .58 * s.pixels); c.lineTo(s.restAxis, .90 * s.pixels); c.stroke(); c.setLineDash([]);
    for (const [height, px] of r.belly) if (px !== null) dot(c, px, height * s.pixels, "#ae38bd", 3 / scale);
    for (const [left, right, bottom] of r.soles) if (bottom !== null) {
      c.strokeStyle = "#347ce0"; c.lineWidth = 3 / scale;
      c.beginPath(); c.moveTo(left * s.pixels, bottom); c.lineTo(right * s.pixels, bottom); c.stroke();
    }
    c.restore();
  });
}
$("play").onclick = () => playing ? pause() : play();
$("previous").onclick = () => seek((frameAt(master.currentTime, 60, 240) - 1) / 60);
$("next").onclick = () => seek((frameAt(master.currentTime, 60, 240) + 1) / 60);
$("seek").oninput = () => seek(Number($("seek").value) / 60);
$("speed").onchange = () => videos.forEach(v => { v.playbackRate = Number($("speed").value); });
$("features").onchange = paint;
for (const button of document.querySelectorAll("[data-time]")) button.onclick = () => seek(Number(button.dataset.time));
for (const v of videos) v.addEventListener("error", () => error(`Could not load ${v.currentSrc}`));
master.addEventListener("ended", () => { if ($("loop").checked) { seek(0); play(); } else { pause(); paint(); } });
function tick() {
  if (playing && !master.paused) for (const v of videos.slice(0, 2)) {
    if (Math.abs(v.currentTime - master.currentTime) > .09) v.currentTime = master.currentTime;
  }
  paint(); requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
