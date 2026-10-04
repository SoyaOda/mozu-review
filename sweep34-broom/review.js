"use strict";
const $ = id => document.getElementById(id);
const before = $("baseline"), after = $("candidate"), videos = [before, after];
const frames = 240, fps = 60, duration = 4;
let playing = false, generation = 0, viewRequest = 0;
const frameAt = t => Math.min(frames - 1, Math.max(0, Math.floor(t * fps + .001)));
const showError = error => { $("error").textContent = String(error?.message || error); };
function pause() {
  generation++;
  videos.forEach(video => video.pause());
  playing = false;
  $("play").textContent = "Play comparison";
}
function seek(time) {
  pause();
  time = Math.max(0, Math.min(duration - 1 / fps, time));
  videos.forEach(video => { video.currentTime = time + .00001; });
  paint();
}
async function play() {
  if (after.ended || after.currentTime >= duration - .002) seek(0);
  const request = ++generation;
  before.currentTime = after.currentTime;
  playing = true;
  $("play").textContent = "Pause comparison";
  try { await Promise.all(videos.map(video => video.play())); }
  catch (error) { if (generation === request) { pause(); showError(error); } }
}
function paint() {
  const frame = frameAt(after.currentTime);
  $("seek").value = frame;
  $("time").textContent = `${after.currentTime.toFixed(2)} / 4.00 s · frame ${String(frame).padStart(3, "0")}`;
}
$("play").onclick = () => playing ? pause() : play();
$("previous").onclick = () => seek((frameAt(after.currentTime) - 1) / fps);
$("next").onclick = () => seek((frameAt(after.currentTime) + 1) / fps);
$("seek").oninput = () => seek(Number($("seek").value) / fps);
$("speed").onchange = () => videos.forEach(video => { video.playbackRate = Number($("speed").value); });
for (const button of document.querySelectorAll("[data-seconds]")) button.onclick = () => seek(Number(button.dataset.seconds));
function loadVideo(video, url) {
  return new Promise((resolve, reject) => {
    function cleanup() { video.removeEventListener("loadedmetadata", ready); video.removeEventListener("error", failed); }
    function ready() { cleanup(); resolve(); }
    function failed() { cleanup(); reject(new Error(`Could not load ${url}`)); }
    video.addEventListener("loadedmetadata", ready, {once:true});
    video.addEventListener("error", failed, {once:true});
    video.src = url;
    video.load();
  });
}
$("view").onchange = async () => {
  const request = ++viewRequest, time = after.currentTime, resume = playing, view = $("view").value;
  const label = $("view").selectedOptions[0].textContent;
  pause();
  $("before-caption").textContent = `${label} · original broom`;
  $("after-caption").textContent = `${label} · revised shape and grip`;
  try {
    await Promise.all([loadVideo(before, `media/before-${view}.mp4`), loadVideo(after, `media/after-${view}.mp4`)]);
    if (request !== viewRequest) return;
    videos.forEach(video => { video.playbackRate = Number($("speed").value); });
    seek(time);
    if (resume) await play();
  } catch (error) { if (request === viewRequest) showError(error); }
};
for (const video of videos) video.addEventListener("error", () => showError(`Could not load ${video.currentSrc}`));
after.addEventListener("ended", () => {
  if ($("loop").checked) { seek(0); play(); }
  else { pause(); before.currentTime = duration; paint(); }
});
let orbitPlaying = false, orbitFrame = 0, orbitTick = 0;
const orbitCache = new Map();
function warmOrbit(pose) {
  if (orbitCache.has(pose)) return;
  const images = [];
  for (let frame = 0; frame < 72; frame++) for (const side of ["before", "after"]) {
    const image = new Image();
    image.src = `orbit/${pose}-${side}-${String(frame).padStart(3, "0")}.jpg`;
    images.push(image);
  }
  orbitCache.set(pose, images);
}
function paintOrbit() {
  const pose = $("orbit-pose").value, angle = orbitFrame * 5;
  for (const side of ["before", "after"]) {
    const image = $("orbit-" + side);
    image.src = `orbit/${pose}-${side}-${String(orbitFrame).padStart(3, "0")}.jpg`;
    image.alt = `${side === "before" ? "Original" : "Revised"} broom, ${pose} pose, ${angle} degrees`;
  }
  $("orbit-seek").value = orbitFrame;
  $("orbit-angle").textContent = `${angle}°${({0:" · front",90:" · side",180:" · back",270:" · opposite side"})[angle] || ""}`;
}
$("orbit-pose").onchange = () => { warmOrbit($("orbit-pose").value); paintOrbit(); };
$("orbit-seek").oninput = () => {
  orbitPlaying = false;
  $("orbit-play").textContent = "Rotate comparison";
  orbitFrame = Number($("orbit-seek").value);
  warmOrbit($("orbit-pose").value);
  paintOrbit();
};
$("orbit-play").onclick = () => {
  orbitPlaying = !orbitPlaying;
  orbitTick = performance.now();
  $("orbit-play").textContent = orbitPlaying ? "Pause rotation" : "Rotate comparison";
  warmOrbit($("orbit-pose").value);
};
for (const id of ["orbit-before", "orbit-after"]) $(id).onerror = () => showError("Could not load orbit image");
function tick(now) {
  if (playing && !after.paused && Math.abs(before.currentTime - after.currentTime) > .07) before.currentTime = after.currentTime;
  if (orbitPlaying && now - orbitTick >= 1000 / 12) {
    const steps = Math.floor((now - orbitTick) / (1000 / 12));
    orbitTick += steps * 1000 / 12;
    orbitFrame = (orbitFrame + steps) % 72;
    paintOrbit();
  }
  paint();
  requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
