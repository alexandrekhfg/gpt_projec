# Legendas pendentes

Esta versão contém textos gráficos editoriais, mas ainda não contém legendas das falas.
O download do modelo Whisper small foi bloqueado por HTTP 403 no ambiente de origem.
Não foi gerada nem inventada uma transcrição.

Para transcrever em uma máquina com acesso ao modelo oficial:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-transcricao.txt
.venv/bin/whisper projeto/assets/original.mp4 --model small --language pt --device cpu --fp16 False --word_timestamps True --output_format all --output_dir legendas
```

Revise os nomes, as falas e os tempos antes de incorporar as legendas ao vídeo.
