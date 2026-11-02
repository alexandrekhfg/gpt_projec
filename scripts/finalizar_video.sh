#!/usr/bin/env bash
set -euo pipefail
# Run from the repository root after reviewing legendas/transcricao-original.json.
python3 scripts/build_captions.py
export HYPERFRAMES_BROWSER_PATH="${HYPERFRAMES_BROWSER_PATH:-/usr/bin/chromium}"
cd projeto
npx --yes hyperframes@0.9.2 check
npx --yes hyperframes@0.9.2 render --quality delivery -o ../videos/encerramento-v2-visual.mp4
cd ..
ffmpeg -v error -i videos/encerramento-v2-visual.mp4 -c:v libx264 -preset fast -crf 24 -pix_fmt yuv420p -c:a aac -b:a 128k -movflags +faststart -y videos/encerramento-v2-legendado.mp4
