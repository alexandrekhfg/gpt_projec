"""Generate a Portuguese transcript and timing evidence on a GitHub runner."""
import json
import subprocess
from pathlib import Path
import torch
import whisper

torch.set_num_threads(2)
out = Path('legendas')
out.mkdir(exist_ok=True)
model = whisper.load_model('turbo')
subprocess.run(['ffmpeg','-v','error','-i','projeto/assets/original.mp4','-vn','-ac','1','-ar','16000','-af','highpass=f=90,lowpass=f=6500,loudnorm=I=-18:TP=-2:LRA=11','-y','/tmp/fala.wav'],check=True)
result = model.transcribe('/tmp/fala.wav', language='pt', task='transcribe', fp16=False, word_timestamps=True, verbose=False, condition_on_previous_text=False, temperature=0, beam_size=5, initial_prompt='Encerramento da gira. Primeira gira aberta. Agradecimento pela presença de todos.')
(out / 'transcricao-original.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
(out / 'transcricao-original.txt').write_text('\n'.join(f"[{s['start']:.2f}–{s['end']:.2f}] {s['text'].strip()}" for s in result['segments'])+'\n',encoding='utf-8')
print('Transcrição automática concluída; revisão editorial necessária.')
