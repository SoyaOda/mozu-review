"use strict";
const $ = id => document.getElementById(id);
const source = $("source"), baseline = $("baseline"), candidate = $("candidate");
const nativeVideos = [baseline, candidate];
const data = JSON.parse($("data").textContent);
let changing = false, playing = false, view = "front", playGeneration = 0;
const fps = 60, frames = 240, duration = 4;
const frameAt = t => Math.min(frames - 1, Math.max(0, Math.floor(t * fps + .001)));
const linked = () => $("source-link").checked ? [...nativeVideos, source] : nativeVideos;

function showError(error) { $("error").textContent = String(error?.message || error); }
function pauseAll() {
  playGeneration++;
  changing = true;
  for (const video of linked()) video.pause();
  changing = false;
  playing = false;
  $("play").textContent = "Play comparison";
}
function seek(seconds, pause = true) {
  if (pause) pauseAll();
  const time = Math.max(0, Math.min(duration - 1 / fps, seconds));
  changing = true;
  for (const video of linked()) video.currentTime = time + .00001;
  changing = false;
  paint();
}
async function playAll() {
  if (candidate.ended || candidate.currentTime >= duration - .002) seek(0);
  const generation = ++playGeneration;
  changing = true;
  playing = true;
  $("play").textContent = "Pause comparison";
  try {
    baseline.currentTime = candidate.currentTime;
    if ($("source-link").checked) source.currentTime = candidate.currentTime;
    await Promise.all(linked().map(video => video.play()));
  } catch (error) {
    if (generation === playGeneration) { showError(error); pauseAll(); }
  } finally {
    if (generation === playGeneration) changing = false;
  }
}
function paint() {
  const i = frameAt(candidate.currentTime);
  $("seek").value = i;
  $("time").textContent = `${candidate.currentTime.toFixed(2)} / 4.00 s · frame ${String(i).padStart(3, "0")} / 239`;
  const context = $("axes").getContext("2d");
  context.clearRect(0, 0, 480, 480);
  if ($("show-axes").checked && data.axes[i]?.[view]) {
    for (const [part, color] of [["upper", "#277979"], ["lower", "#cb7c3c"]]) {
      const axes = data.axes[i][view][part], [x, y] = axes.center.map(v => v * 480);
      context.strokeStyle = color; context.fillStyle = color; context.lineWidth = 2.5;
      for (const key of ["lateral", "front"]) {
        context.beginPath(); context.moveTo(x, y);
        context.lineTo(axes[key][0] * 480, axes[key][1] * 480); context.stroke();
      }
      context.beginPath(); context.arc(x, y, 3, 0, Math.PI * 2); context.fill();
    }
    const contact = data.axes[i][view].contact;
    if (contact) { context.strokeStyle = "#344e40"; context.lineWidth = 2;
      context.beginPath(); context.arc(contact[0]*480, contact[1]*480, 6, 0, Math.PI*2); context.stroke(); }

  }
}
$("play").onclick = () => playing ? pauseAll() : playAll();
$("previous").onclick = () => seek((frameAt(candidate.currentTime) - 1) / fps);
$("next").onclick = () => seek((frameAt(candidate.currentTime) + 1) / fps);
$("seek").oninput = () => seek(Number($("seek").value) / fps);
$("speed").onchange = () => {
  for (const video of [source, ...nativeVideos]) video.playbackRate = Number($("speed").value);
};
$("show-axes").onchange = paint;
$("source-link").onchange = () => {
  source.controls = !$("source-link").checked;
  if ($("source-link").checked) {
    source.currentTime = candidate.currentTime;
    if (playing) source.play().catch(showError);
    else source.pause();
  }
};
let viewRequest = 0;
function loadVideo(video, url) {
  return new Promise((resolve, reject) => {
    const loaded = () => { video.removeEventListener("error", failed); resolve(); };
    const failed = () => { video.removeEventListener("loadedmetadata", loaded); reject(new Error(`Could not load ${url}`)); };
    video.addEventListener("loadedmetadata", loaded, {once:true});
    video.addEventListener("error", failed, {once:true});
    video.src = url; video.load();
  });
}
$("view").onchange = async () => {
  const request = ++viewRequest, time = candidate.currentTime, wasPlaying = playing;
  pauseAll();
  view = $("view").value;
  const label = view[0].toUpperCase() + view.slice(1);
  $("view-caption").textContent = `${label} · low hand path and steady world attention`;
  $("baseline-caption").textContent = `${label} · earlier raised hand and local head counterturn`;
  try {
    await Promise.all([loadVideo(candidate, `media/Sweep33-${view}.mp4`),
                       loadVideo(baseline, `media/previous32-${view}.mp4`)]);
    if (request !== viewRequest) return;
    for (const video of nativeVideos) video.playbackRate = Number($("speed").value);
    seek(time);
    if (wasPlaying) await playAll();
  } catch (error) { if (request === viewRequest) showError(error); }
};
for (const button of document.querySelectorAll("[data-seconds]")) {
  button.onclick = () => seek(Number(button.dataset.seconds));
}
for (const video of [source, ...nativeVideos]) {
  video.addEventListener("error", () => showError(`Could not load ${video.currentSrc}`));
  video.addEventListener("play", () => {
    if (!changing && !video.paused && (video !== source || $("source-link").checked)) {
      if (video !== candidate) candidate.currentTime = video.currentTime;
      playAll();
    }
  });
  video.addEventListener("pause", () => {
    if (!changing && video.paused && !video.ended && (video !== source || $("source-link").checked)) pauseAll();
  });
  video.addEventListener("seeking", () => {
    if (changing || (video === source && !$("source-link").checked)) return;
    changing = true;
    for (const other of linked()) if (other !== video && Math.abs(other.currentTime - video.currentTime) > .035) other.currentTime = video.currentTime;
    changing = false;
  });
}
candidate.addEventListener("ended", () => {
  if ($("loop").checked) { seek(0); playAll(); }
  else {
    pauseAll();
    changing = true;
    for (const video of linked()) if (video !== candidate) video.currentTime = duration;
    changing = false;
    paint();
  }
});
function tick() {
  if (playing && !candidate.paused) {
    if (Math.abs(baseline.currentTime - candidate.currentTime) > .09) baseline.currentTime = candidate.currentTime;
    if ($("source-link").checked && Math.abs(source.currentTime - candidate.currentTime) > .12) source.currentTime = candidate.currentTime;
  }
  paint(); requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
