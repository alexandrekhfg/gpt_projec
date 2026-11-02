# Legendas de teste — v2

A transcrição foi executada com Whisper no GitHub Actions, sem depender da publicação do ambiente GPT. Foram feitas três passagens: small, turbo e turbo em janelas de 12 segundos.

A primeira saída foi rejeitada por erros e repetição. A última saída foi comparada por texto e confiança. Nomes, siglas, endereços e frases inconsistentes foram omitidos ou sinalizados no teste; não foram inventados.

- `encerramento-pt.srt`: legendas de teste separadas.
- `encerramento-pt.ass`: legendas com destaque progressivo por palavra.
- `ajustes-de-revisao.json`: intervalos que exigem conferência.
- `legendas-revisaveis.json`: grupos usados no vídeo.
- `transcricao-original.json` e `.txt`: saída automática bruta, com erros, preservada para rastreabilidade.

**Não houve conferência por escuta humana nesta sessão. Esta é uma versão de teste, com legendas parciais e trechos sinalizados, não uma transcrição integral certificada.**

Para corrigir, edite os textos e tempos com base no áudio. Depois ajuste os intervalos de `ajustes-de-revisao.json` e gere novamente os arquivos. As legendas também estão presentes como camada editável em `projeto/compositions/captions.html`.
