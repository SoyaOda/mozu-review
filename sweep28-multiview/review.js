'use strict';
const source = document.getElementById('source');
const candidate = document.getElementById('candidate');
const videos = [source, candidate];
const cases = JSON.parse(document.getElementById('cases').textContent);
const picker = document.getElementById('case');
const scrub = document.getElementById('scrub');
const linked = document.getElementById('linked');
let selected = cases[0];
let targetTime = 1.7;
let syncing = false;
let loading = false;
let requestedPlay = false;

function report(e) { document.getElementById('error').textContent = String(e.message || e); }
function pauseBoth() { requestedPlay=false; videos.forEach(v=>v.pause()); }
function seek(t) {
  targetTime = Math.max(0, Math.min(2.9666667, t));
  syncing = true;
  for (const v of videos) if (v.readyState >= 1) v.currentTime = Math.min(targetTime, v.duration-.001);
  syncing = false;
}
async function playBoth() {
  requestedPlay=true;
  const result=await Promise.allSettled(videos.map(v=>v.play()));
  for (const r of result) if (r.status === 'rejected') report(r.reason);
}
function choose(id) {
  if(candidate.getAttribute('src') && source.readyState>=1)
    targetTime=Math.min(source.currentTime,2.9666667);
  pauseBoth();
  selected=cases.find(c=>c.id===id);
  loading=true;
  candidate.src=selected.movie;
  document.getElementById('name').textContent=selected.label;
  document.getElementById('decision').textContent=selected.decision;
  document.getElementById('finding').textContent=selected.finding;
  document.getElementById('limits').textContent=selected.limits;
  document.getElementById('format').textContent=`${selected.width} × ${selected.height} / ${selected.fps}fps / ${selected.duration.toFixed(3)}s`;
  document.getElementById('download').href=selected.movie;
  document.getElementById('evidence').replaceChildren(...selected.evidence.flatMap((item,i)=>{
    const a=document.createElement('a'); a.href=item.href; a.textContent=item.label;
    return i?[document.createTextNode(' · '),a]:[a];
  }));
  document.getElementById('sheets').replaceChildren(...selected.sheets.map(s=>{
    const a=document.createElement('a'); a.href=s;
    const img=document.createElement('img'); img.src=s; img.loading='lazy'; img.alt=`${selected.label}: original chronological frames`;
    a.append(img); return a;
  }));
}
for (const v of videos) {
  v.playbackRate=.5;
  v.addEventListener('loadedmetadata',()=>{
    v.playbackRate=Number(document.getElementById('speed').value);
    v.currentTime=Math.min(targetTime,v.duration-.001);
    if (v===candidate) loading=false;
    if(requestedPlay) v.play().catch(report);
  });
  v.addEventListener('play',()=>{
    if(linked.checked && !loading) {
      requestedPlay=true;
      for(const other of videos) if(other!==v && other.paused) other.play().catch(report);
    }
  });
  v.addEventListener('pause',()=>{if(linked.checked && !loading) pauseBoth();});
  v.addEventListener('seeking',()=>{
    if(syncing || loading || !linked.checked) return;
    targetTime=Math.min(v.currentTime,2.999);
    syncing=true;
    for(const other of videos) if(other!==v && other.readyState>=1 && Math.abs(other.currentTime-targetTime)>.04)
      other.currentTime=Math.min(targetTime,other.duration-.001);
    syncing=false;
  });
  v.addEventListener('ended',()=>{if(linked.checked) pauseBoth();});
  v.addEventListener('error',()=>report('The original movie could not be loaded: '+v.getAttribute('src')));
}
picker.addEventListener('change',()=>choose(picker.value));
document.getElementById('play').addEventListener('click',()=>{
  if(videos.some(v=>!v.paused)) pauseBoth();
  else {if(source.currentTime>=2.96) seek(0); playBoth();}
});
document.getElementById('restart').addEventListener('click',()=>{pauseBoth();seek(0);});
for(const [id,delta] of [['prev',-1],['next',1]]) document.getElementById(id).addEventListener('click',()=>{
  pauseBoth();seek((Math.round(source.currentTime*30)+delta)/30+.0001);
});
scrub.addEventListener('input',()=>{pauseBoth();seek(Number(scrub.value)/30+.0001);});
document.getElementById('speed').addEventListener('change',e=>videos.forEach(v=>{v.playbackRate=Number(e.target.value);}));
linked.addEventListener('change',()=>{if(linked.checked) {pauseBoth();seek(source.currentTime);}});
document.querySelectorAll('[data-time]').forEach(b=>b.addEventListener('click',()=>{pauseBoth();seek(Number(b.dataset.time));}));
function tick() {
  document.getElementById('play').textContent=videos.some(v=>!v.paused)?'Pause both':'Play both';
  document.getElementById('status').textContent=`Crop ${source.currentTime.toFixed(2)}s (original ${(source.currentTime+.8).toFixed(2)}s) · candidate ${candidate.currentTime.toFixed(2)}s`;
  scrub.value=Math.round(source.currentTime*30);
  requestAnimationFrame(tick);
}
choose(selected.id);
requestAnimationFrame(tick);
