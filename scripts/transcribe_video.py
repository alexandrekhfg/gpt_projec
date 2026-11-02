"""Transcribe short Portuguese audio windows on a GitHub runner."""
import json,subprocess
from pathlib import Path
import torch,whisper

torch.set_num_threads(2)
out=Path('legendas');out.mkdir(exist_ok=True)
subprocess.run(['ffmpeg','-v','error','-i','projeto/assets/original.mp4','-vn','-ac','1','-ar','16000','-af','highpass=f=90,lowpass=f=6500,loudnorm=I=-18:TP=-2:LRA=11','-y','/tmp/fala.wav'],check=True)
model=whisper.load_model('turbo')
audio=whisper.load_audio('/tmp/fala.wav')
result={'language':'pt','segments':[],'text':''}
for start in range(0,99,12):
 clip=audio[start*16000:min(len(audio),(start+12)*16000)]
 if len(clip)<1600:continue
 part=model.transcribe(clip,language='pt',task='transcribe',fp16=False,word_timestamps=True,verbose=False,condition_on_previous_text=False,temperature=0,beam_size=3)
 for seg in part['segments']:
  seg['start']+=start;seg['end']+=start
  for word in seg.get('words',[]):word['start']+=start;word['end']+=start
  result['segments'].append(seg)
 print('Janela concluída:',start,flush=True)
result['text']=' '.join(s['text'].strip() for s in result['segments'])
(out/'transcricao-original.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(out/'transcricao-original.txt').write_text('\n'.join(f"[{s['start']:.2f}–{s['end']:.2f}] {s['text'].strip()}" for s in result['segments'])+'\n',encoding='utf-8')
