"""Generate a Portuguese transcript and timing evidence on a GitHub runner."""
import json
from pathlib import Path
import torch
import whisper

torch.set_num_threads(2)
out = Path('legendas')
out.mkdir(exist_ok=True)
model = whisper.load_model('small')
result = model.transcribe('projeto/assets/original.mp4', language='pt', task='transcribe', fp16=False, word_timestamps=True, verbose=False, condition_on_previous_text=False, temperature=0)
(out / 'transcricao-original.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
(out / 'transcricao-original.txt').write_text('\n'.join(f"[{s['start']:.2f}–{s['end']:.2f}] {s['text'].strip()}" for s in result['segments'])+'\n',encoding='utf-8')
print('Transcrição automática concluída; revisão editorial necessária.')
