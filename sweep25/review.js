'use strict';
const $=id=>document.getElementById(id),native=$('native'),source=$('source');
let view='oblique',axisRows=[];
const labels={front:'正面',oblique:'斜め',side:'側面',top:'真上'};
const roles={oblique:'気に入った原本 · 3回の払いとタイミングの基準',front:'独立して生成した正面 · 体の向きと手の内向き移動',side:'独立して生成した側面 · 前傾と前へのリーチ',top:'独立して生成した真上 · 向きと弧の方向だけを参照'};
const notes={oblique:'斜めの原本を、行為と3回の払いの時間基準にしています。',front:'正面では腹・肩の線が少し向きを変え、手が足の前を内側へ通ります。払いの時間は斜めの原本と異なります。',side:'側面では胴体の小さな前傾と、それより大きい首の注意、肩と肘による前へのリーチを確認できます。',top:'真上は方向と隠れ方の資料です。参考動画は大きな1回の弧で、実リグの3回のリズムには使っていません。頭に隠れた肩・胴体の角度は測定できません。'};
function reportError(e){$('status').textContent='読み込みに失敗しました。再読み込みしてください。';console.error(e);}
let transportRevision=0;
function pause(){transportRevision++;native.pause();source.pause();}
function playbackError(e){if(e.name!=='AbortError')reportError(e);}
function playVideos(videos){
  transportRevision++;
  for(const video of videos){
    if(video.ended||(Number.isFinite(video.duration)&&video.currentTime>=video.duration-.02))video.currentTime=0;
    video.play().catch(playbackError);
  }
}
function update(){const t=native.currentTime,f=Math.max(0,Math.min(359,Math.round(t*60)));$('time').value=f;$('position').textContent=(f/60).toFixed(3)+' s';drawAxes(f);}
function drawAxes(f){const row=axisRows[f];if(!row)return;const p=row.views[view],o=p.origin.map(v=>v*400);let svg='';for(const [key,color,label] of [['x','#bd4e46','X'],['front','#248267','前'],['up','#446ec1','上']]){const q=p[key].map(v=>v*400),dx=q[0]-o[0],dy=q[1]-o[1],n=Math.hypot(dx,dy);if(n<2){svg+=`<circle cx="${q[0]}" cy="${q[1]}" r="4" fill="${color}" stroke="white"/>`;continue;}const ux=dx/n,uy=dy/n;svg+=`<path d="M${o[0]},${o[1]} L${q[0]},${q[1]}" stroke="white" stroke-width="5"/><path d="M${o[0]},${o[1]} L${q[0]},${q[1]}" stroke="${color}" stroke-width="2.5"/><path d="M${q[0]},${q[1]} L${q[0]-ux*9+uy*4},${q[1]-uy*9-ux*4} L${q[0]-ux*9-uy*4},${q[1]-uy*9+ux*4} Z" fill="${color}"/><text x="${q[0]+6}" y="${q[1]-5}" fill="${color}" stroke="white" stroke-width="3" paint-order="stroke" font-size="12" font-weight="700">${label}</text>`;}svg+=`<circle cx="${o[0]}" cy="${o[1]}" r="3" fill="#303438" stroke="white"/>`;$('axes').innerHTML=svg;$('angles').textContent='設計した胴体の回転角：前傾 '+row.bodyDegrees[0].toFixed(1)+'° ／ 横の傾き '+row.bodyDegrees[1].toFixed(1)+'° ／ 向き '+row.bodyDegrees[2].toFixed(1)+'°';}
function seek(f){if($('linked-playback').checked)pause();else native.pause();native.currentTime=Math.max(0,Math.min(359,f))/60;update();}
function redraw(){for(const id of ['source-view','view-name'])$(id).textContent=labels[view];$('source-role').textContent=roles[view];$('source-note').textContent=notes[view];$('pair').textContent=view==='top'?'弧の向きを並べる':'払いの姿勢を並べる';document.querySelectorAll('[data-view]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.view===view)));$('poses').innerHTML=['hold','prepare','work','recover','second-work','settled'].map(p=>`<figure><figcaption>${({hold:'構え',prepare:'準備',work:'前・内側へ払う',recover:'戻し終える','second-work':'もう一度払う',settled:'落ち着く'})[p]}<small>${labels[view]}</small></figcaption><a href="pilot02/${p}-${view}.png" target="_blank"><img src="pilot02/${p}-${view}.png" alt="${p} ${labels[view]}" loading="lazy"></a></figure>`).join('');$('sheets').innerHTML=Array.from({length:6},(_,i)=>`<p><a href="motion01/media/sheet-${view}-${i}.jpg" target="_blank">${labels[view]} · ${i}.000–${(i+1-1/60).toFixed(3)}秒 · frames ${i*60}–${i*60+59}</a></p>`).join('');update();}
function loadVideo(v,path,t){return new Promise((resolve,reject)=>{const done=()=>{v.removeEventListener('error',fail);v.currentTime=t;v.playbackRate=Number($('speed').value);resolve();};const fail=()=>{v.removeEventListener('loadedmetadata',done);reject(new Error(path));};v.addEventListener('loadedmetadata',done,{once:true});v.addEventListener('error',fail,{once:true});v.src=path;});}
let changing=false;
for(const [video,other] of [[source,native],[native,source]]){
  video.addEventListener('play',()=>{
    if(changing||video.paused||!$('linked-playback').checked||!other.paused)return;
    playVideos([other]);
  });
  video.addEventListener('pause',()=>{
    if(changing||!video.paused||!$('linked-playback').checked||other.paused)return;
    other.pause();
  });
}
$('linked-playback').onchange=()=>{
  const linked=$('linked-playback').checked;
  $('play').textContent=linked?'両方を再生':'実リグを再生';
  if(linked&&(!native.paused||!source.paused))playVideos([native,source]);
};
document.querySelectorAll('[data-view]').forEach(b=>b.onclick=async()=>{
  if(changing||view===b.dataset.view)return;
  const resume=[native,source].filter(v=>!v.paused),t=native.currentTime,sourceTime=source.currentTime;
  changing=true;pause();const revision=transportRevision;
  view=b.dataset.view;native.poster=`pilot02/hold-${view}.png`;redraw();
  let loaded=false;
  try{
    await Promise.all([loadVideo(native,`motion01/media/${view}.mp4`,Math.min(t,359/60)),loadVideo(source,`sources/${view}.mp4`,Math.min(sourceTime,5.98))]);
    update();loaded=true;
  }catch(e){reportError(e);}finally{changing=false;}
  if(loaded&&revision===transportRevision&&resume.length)playVideos(resume);
});
$('play').onclick=()=>playVideos($('linked-playback').checked?[native,source]:[native]);$('pause').onclick=pause;$('both').onclick=()=>{pause();native.currentTime=source.currentTime=0;playVideos([native,source]);};$('previous').onclick=()=>seek(Math.round(native.currentTime*60)-1);$('next').onclick=()=>seek(Math.round(native.currentTime*60)+1);$('time').oninput=()=>seek(Number($('time').value));document.querySelectorAll('[data-time]').forEach(b=>b.onclick=()=>seek(Math.round(Number(b.dataset.time)*60)));$('speed').onchange=e=>[native,source].forEach(v=>v.playbackRate=Number(e.target.value));$('show-axes').onchange=e=>{$('axes').toggleAttribute('hidden',!e.target.checked);update();};
const sourceWorkTime={oblique:61/30,front:81/30,side:64/30,top:96/30};
$('pair').onclick=()=>{if(changing)return;pause();seek(122);source.currentTime=sourceWorkTime[view];};
source.addEventListener('timeupdate',()=>{$('source-position').textContent='参考 '+source.currentTime.toFixed(3)+' s';});
native.addEventListener('timeupdate',update);native.addEventListener('seeked',update);
if(native.requestVideoFrameCallback){const tick=()=>{update();native.requestVideoFrameCallback(tick);};native.requestVideoFrameCallback(tick);}else{const tick=()=>{if(!native.paused)update();requestAnimationFrame(tick);};requestAnimationFrame(tick);}
async function start(){const fetchJSON=async p=>{const r=await fetch(p);if(!r.ok)throw new Error(p);return r.json();};const [axes,e]=await Promise.all([fetchJSON('axes.json'),fetchJSON('evidence.json')]);axisRows=axes;const values=[['実リグの評価',e.samples+'時刻＋全360出力フレーム'],['胴体に対する肩と腕','元の付け根と腕の長さを維持'],['実際に表示される足','全検証時刻で位置の変化なし'],['腕の制御と実形状の最大差',e.fk.toExponential(2)],['穂先の接地・浮きとの最大差',e.floor.toExponential(2)],['出力と全身リグの一致',e.capture.toExponential(2)+' · 13時刻の全可視形状比較'],['保存→再読込',e.reopen.toExponential(2)],['振り幅 / 体の連動を編集→復元',e.amplitudeRestore.toExponential(2)+' / '+e.bodyRestore.toExponential(2)]];$('metrics').innerHTML=values.map(r=>'<tr>'+r.map(v=>'<td>'+v+'</td>').join('')+'</tr>').join('');update();}
redraw();start().catch(reportError);
