# Encerramento da gira — edição em camadas

Projeto editável criado com HyperFrames 0.9.2 a partir do vídeo fornecido pelo proprietário deste repositório.

## Baixar os vídeos

- [Prévia leve, aproximadamente 17 MB](videos/encerramento-editado-previa.mp4)
- [Render de maior qualidade, aproximadamente 91 MB](videos/encerramento-camadas-sem-legendas.mp4)
- [Vídeo original, aproximadamente 22 MB](projeto/assets/original.mp4)

No GitHub, abra o arquivo e clique em **Download raw file** (ícone de download).

Duração: aproximadamente 1min38,6s. Saída: MP4 H.264, 1280×720, 30 fps, áudio AAC.
A resolução de origem é 848×478; a saída ampliada não adiciona detalhes à filmagem original.

## O que foi editado

Zooms suaves de entrada e saída, título animado de abertura, moldura e cantos dourados,
barra de progresso, card editorial intermediário e cartela de encerramento.
O conteúdo do áudio original foi preservado; o renderizador reduziu o nível geral
em 2,5 dB para conter picos acima do teto de entrega.

**As legendas das falas ainda estão pendentes.** Os textos visuais não são transcrições.
Veja [o estado e os comandos de transcrição](legendas/STATUS.md).

## Estrutura

- `projeto/index.html`: composição e timeline GSAP editáveis.
- `projeto/assets/original.mp4`: fonte original.
- `projeto/assets/gsap.min.js`: runtime GSAP 3.15.0 usado na composição.
- `projeto/package.json`: comandos com HyperFrames fixado em 0.9.2.
- `videos/`: os dois MP4s renderizados.
- `revisao/`: quadros usados na revisão visual, incluindo um extraído do MP4 final.

Caches, ambientes Python, dependências npm e arquivos temporários de renderização não são necessários ao projeto e não estão incluídos.

## Executar e renderizar

Requisitos: Node.js 22 ou superior, FFmpeg/FFprobe e Chrome/Chromium.

```bash
cd projeto
npx --yes hyperframes@0.9.2 doctor
npm run check
npm run dev
```

Para gerar outro MP4:

```bash
cd projeto
npx --yes hyperframes@0.9.2 render --quality delivery -o ../videos/novo-render.mp4
```

No Linux com Chromium instalado, caso a detecção do navegador falhe:

```bash
export HYPERFRAMES_BROWSER_PATH=/usr/bin/chromium
```

A validação executada na versão entregue passou em runtime, layout, movimento,
contraste e áudio. Permaneceram quatro avisos de organização em subcomposições;
eles não impediram o render. O arquivo leve foi decodificado por completo sem erros.

A publicação deste repositório não publica nem altera o ambiente de nuvem do GPT.
