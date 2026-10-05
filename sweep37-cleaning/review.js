'use strict';
const $ = id => document.getElementById(id);
const video = $('candidate'), reference = $('reference');
const labels = {front:'Front',oblique:'Oblique',side:'Side',reverse:'Opposite oblique',back:'Back',top:'Top'};
let playing = false, changing = false, generation = 0, viewRequest = 0, pendingTime = 0;
let orbitFrame = 0, orbitRunning = false, orbitLast = 0;
const orbitCache = new Map();
const frameAt = t => Math.min(359, Math.max(0, Math.floor(t * 60 + .001)));
const showError = e => { $('error').textContent = String(e.message || e); };
function update() {
  const t = Math.min(6, video.currentTime || 0), frame = frameAt(t);
  $('seek').value = frame;
  $('time').textContent = `${t.toFixed(2)} / 6.00 s · frame ${String(frame).padStart(3,'0')}`;
  $('play').textContent = playing ? 'Pause animation' : 'Play animation';
}
function pause() { generation++; playing = false; video.pause(); reference.pause(); update(); }
function setTime(t) {
  const bounded = Math.min(359/60, Math.max(0,t)) + .00001;
  video.currentTime = bounded;
  if(reference.readyState >= 1) reference.currentTime = bounded;
  update();
}
async function play() {
  if(changing) return;
  if(video.ended || video.currentTime >= 5.998) setTime(0);
  const request = ++generation;
  playing = true;
  video.playbackRate = reference.playbackRate = Number($('speed').value);
  update();
  const tasks = [video.play()];
  if($('reference-panel').open) { reference.currentTime = video.currentTime; tasks.push(reference.play()); }
  try { await Promise.all(tasks); }
  catch(error) { if(generation === request) { pause(); showError(error); } }
}
$('play').addEventListener('click',()=>{if(playing)pause();else play();});
$('previous').addEventListener('click',()=>{pause();setTime((frameAt(video.currentTime)-1)/60);});
$('next').addEventListener('click',()=>{pause();setTime((frameAt(video.currentTime)+1)/60);});
$('seek').addEventListener('input',()=>{const frame=Number($('seek').value);pause();setTime(frame/60);});
$('speed').addEventListener('change',()=>{video.playbackRate=reference.playbackRate=Number($('speed').value);});
function loadVideo(url) {
  return new Promise((resolve,reject)=>{
    function cleanup(){video.removeEventListener('loadedmetadata',ready);video.removeEventListener('error',failed);}
    function ready(){cleanup();resolve();}
    function failed(){cleanup();reject(new Error('The selected animation could not load.'));}
    video.addEventListener('loadedmetadata',ready,{once:true});video.addEventListener('error',failed,{once:true});
    video.src=url;video.load();
  });
}
$('view').addEventListener('change',async()=>{
  const t=changing?pendingTime:video.currentTime, wasPlaying=playing, request=++viewRequest;
  pause();changing=true;pendingTime=t;
  $('caption').textContent=`Sweep37 · ${labels[$('view').value]}`;
  try {
    await loadVideo(`media/${$('view').value}.mp4`);
    if(request!==viewRequest)return;
    video.playbackRate=Number($('speed').value);setTime(t);changing=false;
    if(wasPlaying)await play();
  } catch(error){if(request===viewRequest){changing=false;showError(error);}}
});
for(const button of document.querySelectorAll('[data-time]'))button.addEventListener('click',()=>{pause();setTime(Number(button.dataset.time));});
video.addEventListener('ended',()=>{pause();if($('loop').checked){setTime(0);play();}});
for(const event of ['loadedmetadata','timeupdate','seeked','play','pause'])video.addEventListener(event,update);
video.addEventListener('error',()=>showError('The animation could not load. Reload this page to try again.'));
reference.addEventListener('error',()=>showError('The original reference could not load. The native animation is still available.'));
$('reference-panel').addEventListener('toggle',()=>{
  if(!$('reference-panel').open)reference.pause();
  else if(playing){reference.currentTime=video.currentTime;reference.playbackRate=video.playbackRate;reference.play().catch(error=>{if(playing&&$('reference-panel').open)showError(error);});}
});
function warmOrbit(pose) {
  if(orbitCache.has(pose))return;
  const images=[];
  for(let i=0;i<72;i++){const image=new Image();image.src=`orbit/${pose}-${String(i).padStart(3,'0')}.jpg`;images.push(image);}
  orbitCache.set(pose,images);
}
function updateOrbit() {
  const pose=$('orbit-pose').value;
  $('orbit').src=`orbit/${pose}-${String(orbitFrame).padStart(3,'0')}.jpg`;
  $('orbit').alt=`${pose==='hold'?'Holding':'Sweeping'} pose, ${orbitFrame*5} degrees`;
  $('orbit-angle').textContent=`${orbitFrame*5}°${orbitFrame===0?' · front':''}`;
  $('orbit-seek').value=orbitFrame;
}
$('orbit-seek').addEventListener('input',()=>{orbitRunning=false;$('orbit-play').textContent='Rotate pose';orbitFrame=Number($('orbit-seek').value);updateOrbit();});
$('orbit-pose').addEventListener('change',()=>{if(orbitRunning)warmOrbit($('orbit-pose').value);updateOrbit();});
$('orbit-play').addEventListener('click',()=>{orbitRunning=!orbitRunning;orbitLast=performance.now();$('orbit-play').textContent=orbitRunning?'Pause rotation':'Rotate pose';if(orbitRunning)warmOrbit($('orbit-pose').value);});
$('orbit').addEventListener('error',()=>showError('The selected angle could not load.'));
function tick(now){
  if(playing&&!video.paused&&$('reference-panel').open&&!reference.paused&&reference.readyState>=2&&Math.abs(reference.currentTime-video.currentTime)>.075)reference.currentTime=video.currentTime;
  if(orbitRunning&&now-orbitLast>=1000/12){const steps=Math.floor((now-orbitLast)/(1000/12));orbitLast+=steps*(1000/12);orbitFrame=(orbitFrame+steps)%72;updateOrbit();}
  update();requestAnimationFrame(tick);
}
requestAnimationFrame(tick);
