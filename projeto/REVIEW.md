# Revisão da edição v2

Direção: composição editorial em papel quente, verde e cobre; tipografia serifada com revelação por máscara; filmagem que entra e sai de layouts em painéis; duas fotografias recortadas em camada lateral. A proposta evita moldura permanente, cantos piscantes e barra de progresso da primeira versão.

Verificações visuais realizadas: quadros de 1s, 3s, 26s, 65s e 94s, além de seis quadros entre 3,8s e 5,2s para revisar a expansão da imagem.

Validação do visual: lint, runtime, layout, contraste e craft sem erros nem avisos. Um aviso informativo de overflow no recorte de detalhe corresponde à ampliação intencional da imagem dentro da máscara.

Render visual: H.264, 1280×720, 30fps; áudio AAC; duração de 98,566667s. A resolução original de 848×478 limita os detalhes das aproximações.

O som foi preservado e verificado por ferramentas; não houve escuta humana nesta sessão. A primeira transcrição Whisper small apresentou erros e repetição e foi rejeitada. A segunda execução usa Whisper turbo, áudio normalizado e revisão por texto/confiança. As legendas de teste precisam de conferência humana dos nomes e termos específicos.

Ponto mais fraco: o plano de abertura original é distante durante os primeiros segundos. A composição tipográfica dá função a esse trecho, preservando a continuidade do áudio.

## Entrega legendada de teste

A transcrição em janelas curtas terminou pelo GitHub Actions. Foram gerados 27 grupos de legenda, incluindo oito marcadores de trechos pouco claros ou dados a confirmar. Não há sobreposição temporal. As falas não foram conferidas por escuta humana; portanto, o resultado é parcial e revisável.

A versão editável legendada passou em runtime, layout, contraste e craft. Foi mantido um aviso de densidade na trilha de legendas: os 27 grupos ficam em uma única subcomposição para formar uma trilha de captions.

O MP4 de entrega usa legendas ASS com fonte DejaVu Sans Bold 34px e destaque progressivo amarelo por palavra; a camada HTML editável usa Oswald 36px. São duas representações editáveis do mesmo texto e dos mesmos tempos, com diferença tipográfica declarada. O vídeo foi decodificado por completo sem erros e quadros extraídos em 19,4s, 25,1s e 69,5s foram revisados visualmente.
