"""Build reviewable SRT/ASS captions and an editable HyperFrames captions layer."""
import json, re, html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
D=98.566667
source=json.loads((ROOT/'legendas/transcricao-original.json').read_text())
adjustments=json.loads((ROOT/'legendas/ajustes-de-revisao.json').read_text()) if (ROOT/'legendas/ajustes-de-revisao.json').exists() else {'ranges':[]}
blocked=adjustments['ranges']
groups=[]; rejected=[]
for seg in source['segments']:
 text=seg['text'].strip()
 tokens=re.findall(r'\w+',text.lower())
 repetitive=(len(tokens)>12 and len(set(tokens))/len(tokens)<.18) or len(re.findall(r'\b[\w.-]+\.(?:com|org|net)(?:\.\w+)?',text,re.I))>2
 if repetitive or seg.get('compression_ratio',0)>2.8 or seg.get('avg_logprob',0)<-1.0:
  rejected.append({'start':seg['start'],'end':seg['end'],'text':text,'reason':'baixa confiabilidade ou repetição'})
  continue
 words=seg.get('words') or []
 if not words and text:words=[{'word':text,'start':seg['start'],'end':seg['end']}]
 current=[]
 for w in words:
  w={'text':w['word'].strip(),'start':max(.1,float(w['start'])),'end':min(D,max(float(w['end']),float(w['start'])+.04))}
  if any(w['start']<r['end'] and w['end']>r['start'] for r in blocked):continue
  if 23.65<=w['start']<24 and w['text'].lower().strip('.,')=='primeira':continue
  if not w['text'] or w['end']<=w['start']:continue
  if current and (len(current)>=6 or len(' '.join(x['text'] for x in current))+len(w['text'])>34 or w['start']-current[-1]['end']>.45 or w['end']-current[0]['start']>3.2):
   groups.append(current);current=[]
  current.append(w)
 if current:groups.append(current)
merged=[]
for g in groups:
 if merged and g[0]['start']-merged[-1][-1]['end']<.45 and len(g)+len(merged[-1])<=7 and len(' '.join(w['text'] for w in merged[-1]+g))<=34 and g[-1]['end']-merged[-1][0]['start']<=3.3:
  merged[-1]+=g
 else:merged.append(g)
groups=merged
items=[]
for i,g in enumerate(groups):
 start=g[0]['start'];end=min(D,max(g[-1]['end']+.12,start+.6))
 if i+1<len(groups):end=min(end,groups[i+1][0]['start'])
 text=' '.join(w['text'] for w in g)
 text=re.sub(r'\bgíria aberta\b','gira aberta',text,flags=re.I)
 items.append({'start':start,'end':end,'text':text,'words':g})
for r in blocked:
 if r.get('label'):
  start=max(.2,r['start']);end=min(r['end'],start+3.0)
  items.append({'start':start,'end':end,'text':r['label'],'words':[{'text':r['label'],'start':start,'end':end}],'marker':True})
items.sort(key=lambda g:g['start'])
for i in range(len(items)-1):items[i]['end']=min(items[i]['end'],items[i+1]['start'])
(ROOT/'legendas/legendas-revisaveis.json').write_text(json.dumps({'groups':items,'excluded':rejected,'note':'Transcrição automática; nomes e trechos de baixa clareza exigem revisão humana.'},ensure_ascii=False,indent=2))
def srt_time(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
def ass_time(t):
 cs=round(t*100);return f'{cs//360000}:{cs//6000%60:02}:{cs//100%60:02}.{cs%100:02}'
srt='\n\n'.join(f"{i+1}\n{srt_time(g['start'])} --> {srt_time(g['end'])}\n{g['text']}" for i,g in enumerate(items))+'\n'
(ROOT/'legendas/encerramento-pt.srt').write_text(srt)
ass='''[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
WrapStyle: 0
ScaledBorderAndShadow: yes
[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Caption,DejaVu Sans,34,&H0087DDF3,&H00FFFFFF,&H30000000,&H30000000,-1,0,0,0,100,100,0,0,3,9,0,2,110,110,40,1
[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
'''
for g in items:
 chunks=[];pos=g['start']
 for w in g['words']:
  gap=max(0,round((w['start']-pos)*100))
  if gap:chunks.append('{\\k'+str(gap)+'}')
  chunks.append('{\\kf'+str(max(1,round((w['end']-w['start'])*100)))+'}'+w['text'].replace('{','').replace('}','')+' ');pos=w['end']
 ass+=f"Dialogue: 0,{ass_time(g['start'])},{ass_time(g['end'])},Caption,,0,0,0,,{''.join(chunks).strip()}\n"
(ROOT/'legendas/encerramento-pt.ass').write_text(ass)
# Editable equivalent in HyperFrames; the delivery MP4 burns ASS onto the rendered visual master.
css='''#root{position:absolute;inset:0;font-family:Oswald;color:white} .caption-line{position:absolute;left:0;right:0;bottom:42px;text-align:center} .caption-text{display:inline-block;max-width:1080px;padding:10px 18px;background:rgba(0,0,0,.78);font-size:36px;line-height:1.22;color:#fff;border-radius:4px}'''
body=[];js=[]
for i,g in enumerate(items):
 spans=' '.join(f'<span id="cw-{i}-{j}">{html.escape(w["text"])}</span>' for j,w in enumerate(g['words']))
 body.append(f'<div id="caption-{i}" class="clip" data-start="{g["start"]:.3f}" data-duration="{g["end"]-g["start"]:.3f}" data-track-index="1"><div class="caption-line"><div class="caption-text">{spans}</div></div></div>')
 for j,w in enumerate(g['words']):js.append(f"tl.set('#cw-{i}-{j}',{{color:'#f3dd87'}},{w['start']:.3f});")
scene=f'<template><style>{css}</style><div id="root" data-composition-id="captions" data-width="1280" data-height="720">'+''.join(body)+'</div><script>const tl=gsap.timeline({paused:true});'+''.join(js)+'window.__timelines.captions=tl;</script></template>'
(ROOT/'projeto/compositions/captions.html').write_text(scene)
p=ROOT/'projeto/index.html';s=p.read_text();host=f'<div id="captions" class="clip" data-composition-id="captions" data-composition-src="compositions/captions.html" data-start="0" data-duration="{D}" data-track-index="5" data-track-kind="captions" data-width="1280" data-height="720" style="position:absolute;inset:0;z-index:20"></div>'
s=s.replace('<!-- CAPTION_HOST -->',host);p.write_text(s)
print('Grupos:',len(items),'Trechos excluídos:',len(rejected))
