'use strict';
const $=id=>document.getElementById(id), video=$('candidate'), reference=$('reference');
let playing=false, changing=false, generation=0, viewRequest=0, pendingTime=0;
let orbitFrame=0, orbitRunning=false, orbitLast=0;
const labels={front:'Front',oblique:'Oblique',side:'Side'};
const requestedTime=Number(new URLSearchParams(location.search).get('t')||0);
let initialTimeApplied=false;
const frameAt=t=>Math.min(479,Math.max(0,Math.floor(t*60+.001)));
const showError=e=>{$('error').textContent=String(e.message||e);};
function update(){const t=Math.min(8,video.currentTime||0);$('seek').value=frameAt(t);$('time').textContent=`${t.toFixed(2)} / 8.00 s · frame ${String(frameAt(t)).padStart(3,'0')}`;$('play').textContent=playing?'Pause animation':'Play animation';}
function pause(){generation++;playing=false;video.pause();reference.pause();update();}
function setTime(t){const bounded=Math.min(479/60,Math.max(0,t))+.00001;video.currentTime=bounded;if(reference.readyState>=1)reference.currentTime=bounded;update();}
async function play(){if(changing)return;if(video.ended||video.currentTime>=7.998)setTime(0);const request=++generation;playing=true;video.playbackRate=reference.playbackRate=Number($('speed').value);reference.currentTime=video.currentTime;update();try{await Promise.all([video.play(),reference.play()]);}catch(e){if(generation===request){pause();showError(e);}}}
$('play').addEventListener('click',()=>playing?pause():play());
$('previous').addEventListener('click',()=>{pause();setTime((frameAt(video.currentTime)-1)/60);});
$('next').addEventListener('click',()=>{pause();setTime((frameAt(video.currentTime)+1)/60);});
$('seek').addEventListener('input',()=>{const t=Number($('seek').value)/60;pause();setTime(t);});
$('speed').addEventListener('change',()=>{video.playbackRate=reference.playbackRate=Number($('speed').value);});
function load(target,url){return new Promise((resolve,reject)=>{function cleanup(){target.removeEventListener('loadedmetadata',ready);target.removeEventListener('error',failed);}function ready(){cleanup();resolve();}function failed(){cleanup();reject(new Error('The selected animation could not load.'));}target.addEventListener('loadedmetadata',ready,{once:true});target.addEventListener('error',failed,{once:true});target.src=url;target.load();});}
$('view').addEventListener('change',async()=>{const t=changing?pendingTime:video.currentTime,wasPlaying=playing,request=++viewRequest;pause();changing=true;pendingTime=t;const view=$('view').value;$('view-label').textContent='/ '+labels[view];try{await Promise.all([load(video,`media/${view}.mp4`),load(reference,`before/${view}.mp4`)]);if(request!==viewRequest)return;video.playbackRate=reference.playbackRate=Number($('speed').value);setTime(t);changing=false;if(wasPlaying)await play();}catch(e){if(request===viewRequest){changing=false;showError(e);}}});
for(const b of document.querySelectorAll('[data-time]'))b.addEventListener('click',()=>{pause();setTime(Number(b.dataset.time));});
video.addEventListener('ended',()=>{pause();if($('loop').checked){setTime(0);play();}});
for(const event of ['loadedmetadata','timeupdate','seeked','play','pause'])video.addEventListener(event,update);
for(const item of [video,reference])item.addEventListener('error',()=>showError('The comparison could not load. Reload this page to try again.'));
reference.addEventListener('loadedmetadata',()=>{reference.currentTime=video.currentTime;});
function applyInitialTime(){if(!initialTimeApplied&&video.readyState>=1&&reference.readyState>=1){initialTimeApplied=true;setTime(Number.isFinite(requestedTime)?requestedTime:0);}}
video.addEventListener('loadedmetadata',applyInitialTime);
reference.addEventListener('loadedmetadata',applyInitialTime);
applyInitialTime();
function updateOrbit(){$('orbit').src=`orbit/work-${String(orbitFrame).padStart(3,'0')}.jpg`;$('orbit').alt=`Adjusted work pose, ${orbitFrame*5} degrees`;$('orbit-angle').textContent=`${orbitFrame*5}°${orbitFrame===0?' · front':''}`;$('orbit-seek').value=orbitFrame;}
$('orbit-seek').addEventListener('input',()=>{orbitRunning=false;$('orbit-play').textContent='Rotate pose';orbitFrame=Number($('orbit-seek').value);updateOrbit();});
$('orbit-play').addEventListener('click',()=>{orbitRunning=!orbitRunning;orbitLast=performance.now();$('orbit-play').textContent=orbitRunning?'Pause rotation':'Rotate pose';});
$('orbit').addEventListener('error',()=>showError('The selected angle could not load.'));
function tick(now){if(playing&&!video.paused&&reference.readyState>=2&&Math.abs(reference.currentTime-video.currentTime)>.075)reference.currentTime=video.currentTime;if(orbitRunning&&now-orbitLast>=1000/12){const n=Math.floor((now-orbitLast)/(1000/12));orbitLast+=n*(1000/12);orbitFrame=(orbitFrame+n)%72;updateOrbit();}update();requestAnimationFrame(tick);}
requestAnimationFrame(tick);
