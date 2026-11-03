# Pesquisa acumulada (tudo que foi achado nas conversas, por tema)

Atualizado em 03/11/2026. Itens com "(estimativa)" ou "(não verificado)" não têm fonte confirmada. Detalhes e links de cada estudo estão nos arquivos indicados.

## 1. O panorama: quem já tentou algo parecido
**Aplicativos digitais que mostram o que estranhos ouvem (quase todos morreram):** Soundwave (2013–2016, 1,5 mi de downloads, comprado pelo Spotify e desligado), Highlight, Glancee, Banjo, Sonar, Color (US$41 mi levantados, cerca de um ano de vida), Google Latitude, Zenly (35 mi de usuários ativos por mês, desligado pela Snap em fev/2023), Tastebuds.fm (desligado em abr/2023). Causas citadas: precisa de muita gente no mesmo lugar ao mesmo tempo, bateria, privacidade (mulheres evitam divulgar localização). Os apps atuais desse tipo (Around Music, Music Around, Sound Radar) quase não têm avaliações. O pedido "ver o que quem está perto ouve" está no Spotify com status "Not Right Now".
**Digitais vivos, só para amigos:** Airbuds (15 mi de downloads, 5 mi MAU, 1,5 mi DAU, US$10 mi levantados), MUBR, Spotivity; o Spotify lançou "atividade de escuta" para amigos em jan/2026.
**Físicos:** Divoom Emodo (badge de tela colorida, US$49,99, jul/2026, imagem manual), Divoom Pixoo, Tuneshine (tela de capa de mesa, US$199,99), Spotify Car Thing (descontinuado e desativado em dez/2024), Humane Ai Pin (encerrado em 2025). tshirtOS (2012) nunca foi vendida; o fundador apontou que não é comparável, e o análogo real é o Emodo.
**Plataformas:** Spotify restringiu a API (nov/2024; 250 mil usuários e empresa registrada para cota ampliada desde 2025; modo de desenvolvimento com 5 usuários e conta Premium desde fev/2026). iOS limita muito o Bluetooth em segundo plano.

## 2. Como o produto pegaria os dados (resposta técnica, ainda não validada)
- **Texto (música, artista, álbum):** iPhone via Apple Media Service (Bluetooth LE, serviço público com exemplos em ESP32: Adafruit, Moddable, MusicStation, ctrl01); Android via notificação e sessão de mídia. Funciona com qualquer app de música, inclusive Bandcamp e SoundCloud.
- **Capa:** o serviço acima não traz imagem. Busca por artista e álbum em iTunes Search API (termos: só para "promover conteúdo da loja"; risco de uso comercial), Deezer, MusicBrainz/Cover Art Archive. Teste próprio: pelo menos uma fonte achou 17 de 18 álbuns, do mainstream ao underground (ferramenta: tools/art_coverage.py).
- AVRCP 1.6 (capa por Bluetooth clássico) existe mas funciona de forma inconsistente. MFi (Apple): US$99/ano mais chip e custos de conformidade (estimativa de dezenas de milhares de dólares segundo um fornecedor; não verificado).
- Reconexão com iPhone tem problemas relatados em fóruns (par antigo guardado).

## 3. Os três reenquadramentos que discutimos
1. **Badge:** sem rede de usuários, mas quase nenhum sucesso comercial vestível; o objeto que vende (Tuneshine) é de mesa.
2. **Lugar como unidade** (mapas de música: Radio Garden, Radiooooo, Cities and Memory, Serendipity do Spotify): funciona quando o conteúdo é curado ou transmitido, nunca com escuta agregada de usuários.
3. **Local de encontro** (disco silenciosa com luzes por canal: mercado de US$812,6 mi em 2024; TouchTunes em 65 mil locais): funciona porque o local fornece a densidade; apps de "parceiro de show" viraram cidades-fantasma.

## 4. A tese do fundador (19/10/2026)
O propósito é **orgulho e autoexpressão** (como uma camiseta de banda), não provocar encontros. O valor é unilateral: não precisa de densidade nem de ninguém reconhecer a capa. Pontos fracos levantados: o feed ao vivo é sem filtro (por isso os modos Ao vivo/Favorito/Desligado); "pessoas mainstream não ligam" provavelmente é falso (fandoms gastam muito); tela pode destoar de quem prefere objetos analógicos.

## 5. Propriedade intelectual (14/10/2026)
- Ideia não é patenteável; só mecanismo técnico concreto. Brasil é **first-to-file** (Lei 9.279/96, art. 7).
- Direito autoral (Lei 9.610/98) protege o texto, não a ideia (art. 8). Registro com data certa em cartório (RTD) ou carimbo de tempo é prova de data, não de titularidade. Mandar o PDF por e-mail é o carimbo de tempo mais barato.
- NDA: investidores e aceleradoras quase nunca assinam no primeiro contato; usar com fabricantes e parceiros técnicos depois.
- Depois de ter um desenho: **desenho industrial** (renovação R$840), **modelo de utilidade** (exame R$560, R$280 com desconto), patente de invenção (combinação de peças conhecidas costuma ser considerada óbvia). Desconto de ~50% para pessoa física, MEI e microempresa (tabela INPI 2025; conferir).
- O PDF datado "concept_record_2026-10-14.pdf" foi enviado no chat, **não está no repositório**; o fundador deve manter a própria cópia e mandá-la por e-mail a si mesmo.

## 6. Instituições no Brasil (resumo; detalhes do Sebrae em docs/sebrae.md)
Sebraetec (subsídio ~70% em Minas, exige CNPJ); SENAI Laboratório Aberto (Fab Lab, BH); UFMG InovaLab e PUCTEC (precisam de vínculo com a universidade; janelas fechadas); InovAtiva (gratuito, sem participação societária; ciclo 2026 não confirmado); Anjos do Brasil núcleo BH (só com protótipo); FINEP/FAPEMIG/BDMG (sem chamada de hardware achada); San Pedro Valley (comunidade). BH é forte em software; Campinas, em hardware.
**Escada de preparo (0–6):** 0 teste barato de uso; 1 resumo de uma página; 2 MEI; 3 resolver dúvidas técnicas no papel; 4 protótipo feio funcionando; 5 evidência com estranhos; 6 investidor (empresa, custos reais, protótipo, ações). Sebraetec e SENAI servem antes do protótipo; investidores só depois.

## 7. Hardware e preços (levantado em out/2026; preços em lojas dos EUA, frete e imposto para a França/Brasil não verificados)
- Placas ESP32-S3 com tela: Waveshare 1.54" 240×240 (US$15–19), 1.69" 240×280 (US$16; US$22 com toque; conector de bateria confirmado), 1.28" redonda 240×240 (~US$16), M5StickS3 240×135 (€24,50 na Botland). M5StickC Plus2 saiu de linha. Telas dessa classe têm ~28 mm de largura (calculado pela diagonal; conferir ficha técnica).
- Para ~5 cm: painel retrato de 2,8" 480×640 (~43×57 mm). A de 2,8" 480×480 é redonda e grande (~71 mm).
- **LCD** (vivo, rápido, barato, gasta bateria) contra **e-ink colorido** (paper-like, quase sem energia, lento e com cores apagadas). Painel e-ink Spectra 6 de 1,54" 240×240: ~US$7,49–12,49; o de 4": US$38–47, 19 s para redesenhar, com piscada e sem atualização parcial; Kaleido 3 só achado a partir de 7,8". E-ink monocromático: US$4–26 por módulo de 2,6–2,9" (não serve para capas).
- Bateria: estimativa própria de 2–4 h com LCD em placa de desenvolvimento e bateria de 400 mAh (não medida); Emodo anuncia ~8 h.
- Carregamento: USB-C (mais barato), contatos magnéticos (precisa de cabo e ferramental próprios), sem fio (mais caro e mais grosso). Preços de componentes são alegações de fornecedores.
- Decisões do fundador: sem touch; botão físico com modos; luz acesa só em "tocando agora"; grampo multiuso; iPhone e Android; ideia nova (não decidida): colar.

## 8. Ferramentas de modelagem 3D
build123d (Python) e OpenSCAD instalados e funcionando na nuvem; só o build123d exporta STEP (editável em FreeCAD, Onshape, Fusion). Decisão do fundador: o Claude modela; ele não precisa mexer. Arquivos em cad/ (medidas provisórias, não ajustadas a nenhuma placa real; criados sem pedido do fundador e podem ser apagados).

## 9. O processo "venture" (03/11/2026)
Pasta ventures/social-music/ (VENTURE.md, mercado, concorrentes, clientes, modelo, entrada no mercado, revisão) e o relatório visual relatorio-visual.html. Veredito: seguir reestruturado e barato, com data para parar (31/03/2027), com três condições: (a) teste de uso, (b) ≥25 depósitos de estranhos, (c) rota de mercado escrita. Modelo base: preço US$69, sobra −US$0,25 por unidade após CAC; só fecha em ~US$79 ou mais. Todos os números de mercado e custo são estimativas não verificadas.

## 10. Crowdfunding, marketing e o debate do Tuneshine (03/11/2026)
- **Kickstarter:** pessoa física só lança de 25 países (França e EUA sim; Brasil não), com residência, documento oficial e conta bancária nesse país. Hardware precisa de protótipo funcional e não pode usar imagem renderizada que pareça produto pronto. Entrega no prazo: 15–32% dos projetos de hardware (estimativas conflitantes). Não confirmado se a situação do fundador (brasileiro com residência na França) vale.
- **Indiegogo:** elegibilidade do Brasil não confirmada (~5% + ~3% e US$0,20 por terceiros). **Crowd Supply:** curadoria forte (recusa mais de 75%), ~12% + processamento (fonte de 2026), foco em hardware aberto. **Catarse, Kickante, Benfeitoria:** brasileiras; taxas divergem (Kickante 6% ou 12–17,5%; Catarse 7,5% ou 13%).
- **Empresa:** MEI tem teto de R$81 mil/ano; campanha de US$30 mil passa disso.
- **Construir em público** (Instagram/TikTok, amigos de marketing): vale como canal; o número que importa é a lista de e-mail com depósito (regra de fornecedores: 1–5% da lista vira apoiador); atenção a custo de tempo e a música em vídeos de conta comercial (não verificado).
- **Debate do Tuneshine:** prova que as pessoas pagam por acabamento quando a alternativa é montar sozinho; não prova volume nem demanda contra um produto pronto de US$49,99; os compradores parecem mais velhos e comprar como presente (inferência). Escolha em aberto: premium de presente (US$99–129+) contra gadget acessível 18–29 (~US$79).
