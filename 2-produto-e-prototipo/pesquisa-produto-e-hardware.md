# Pesquisa: produto e hardware

Antes ficava num arquivo único que foi dividido por tema em 04/11/2026; nenhuma linha foi perdida. Itens com "(estimativa)" ou "(não verificado)" não têm fonte confirmada.

## 2. Como o produto pegaria os dados (resposta técnica, ainda não validada)
- **Texto (música, artista, álbum):** iPhone via Apple Media Service (Bluetooth LE, serviço público com exemplos em ESP32: Adafruit, Moddable, MusicStation, ctrl01); Android via notificação e sessão de mídia. Funciona com qualquer app de música, inclusive Bandcamp e SoundCloud.
- **Capa:** o serviço acima não traz imagem. Busca por artista e álbum em iTunes Search API (termos: só para "promover conteúdo da loja"; risco de uso comercial), Deezer, MusicBrainz/Cover Art Archive. Teste próprio: pelo menos uma fonte achou 17 de 18 álbuns, do mainstream ao underground (ferramenta: 2-produto-e-prototipo/tools/art_coverage.py).
- AVRCP 1.6 (capa por Bluetooth clássico) existe mas funciona de forma inconsistente. MFi (Apple): US$99/ano mais chip e custos de conformidade (estimativa de dezenas de milhares de dólares segundo um fornecedor; não verificado).
- Reconexão com iPhone tem problemas relatados em fóruns (par antigo guardado).

## 7. Hardware e preços (levantado em out/2026; preços em lojas dos EUA, frete e imposto para a França/Brasil não verificados)
- Placas ESP32-S3 com tela: Waveshare 1.54" 240×240 (US$15–19), 1.69" 240×280 (US$16; US$22 com toque; conector de bateria confirmado), 1.28" redonda 240×240 (~US$16), M5StickS3 240×135 (€24,50 na Botland). M5StickC Plus2 saiu de linha. Telas dessa classe têm ~28 mm de largura (calculado pela diagonal; conferir ficha técnica).
- Para ~5 cm: painel retrato de 2,8" 480×640 (~43×57 mm). A de 2,8" 480×480 é redonda e grande (~71 mm).
- **LCD** (vivo, rápido, barato, gasta bateria) contra **e-ink colorido** (paper-like, quase sem energia, lento e com cores apagadas). Painel e-ink Spectra 6 de 1,54" 240×240: ~US$7,49–12,49; o de 4": US$38–47, 19 s para redesenhar, com piscada e sem atualização parcial; Kaleido 3 só achado a partir de 7,8". E-ink monocromático: US$4–26 por módulo de 2,6–2,9" (não serve para capas).
- Bateria: estimativa própria de 2–4 h com LCD em placa de desenvolvimento e bateria de 400 mAh (não medida); Emodo anuncia ~8 h.
- Carregamento: USB-C (mais barato), contatos magnéticos (precisa de cabo e ferramental próprios), sem fio (mais caro e mais grosso). Preços de componentes são alegações de fornecedores.
- Decisões do fundador: sem touch; botão físico com modos; luz acesa só em "tocando agora"; grampo multiuso; iPhone e Android; ideia nova (não decidida): colar.

## 8. Ferramentas de modelagem 3D
build123d (Python) e OpenSCAD instalados e funcionando na nuvem; só o build123d exporta STEP (editável em FreeCAD, Onshape, Fusion). Decisão do fundador: o Claude modela; ele não precisa mexer. Arquivos em 2-produto-e-prototipo/cad/ (medidas provisórias, não ajustadas a nenhuma placa real; criados sem pedido do fundador e podem ser apagados).
