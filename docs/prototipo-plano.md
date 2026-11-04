# Plano do primeiro protótipo (PROPOSTA do Claude de 04/11/2026, nada decidido, nada comprado)

Objetivo: uso pessoal e conteúdo para as redes. Não é venda. A certificação de rádio (FCC/Anatel) só importa para vender e está estacionada (ver ventures/social-music/07-eua-vs-brasil/).

## Ordem proposta
Etapa 1 (semanas 1 a 3): placa de desenvolvimento com tela, ligada ao computador por USB, sem caixa. Meta única: tocar música no iPhone e a capa aparecer na tela. O Claude escreve o firmware (o programa que roda dentro da placa); o fundador grava na placa por um comando.
Etapa 2 (semana 3 ou 4): ligar bateria pequena de lítio (~400 mAh) e medir a duração real. Medir a placa com paquímetro. O Claude modela a caixa em 3D (build123d) com as medidas reais.
Etapa 3: imprimir uma caixa simples com costas que aceitem alfinete de broche, ímã ou cordão, para testar clipe e colar com a mesma peça.

## Peças e custo (total estimado €60 a 150; orçamento €500)
| Item | Preço | Origem do número |
|---|---|---|
| Waveshare ESP32-S3 1,69" 240x280 (conector de bateria confirmado) | US$16 | pesquisa anterior, não conferido hoje |
| Alternativa: M5StickS3 240x135 (já com caixa e bateria) | €24,50 (Botland) | pesquisa anterior |
| Bateria de lítio ~400 mAh | ~€5 a 10 | estimativa |
| Paquímetro, alfinetes de broche, ímãs, cabo USB-C | ~€15 a 30 | estimativa |
| Frete e imposto | ~€10 a 25 | estimativa |
| Impressão 3D | ~€0 a 60 | estimativa |

## Riscos técnicos (nenhum testado)
1. Ler o nome da música do iPhone por Bluetooth (recurso AMS da Apple): pesquisa anterior diz que é possível; nunca testado em placa.
2. O iPhone não manda a capa, só o texto. A capa vem de uma busca (iTunes ou Deezer) por Wi-Fi: no protótipo, Wi-Fi de casa ou hotspot do celular. Um app no celular resolveria, mas é muito mais trabalho.
3. Bateria: 2 a 4 h estimadas com LCD, não medidas.
4. Tamanho: tela dessa classe tem ~28 mm; a placa com bateria será maior que um badge de 3 cm.

## Decisões que são do fundador (inclinação do Claude marcada)
- Placa: inclinação para a Waveshare 1,69". Não decidido.
- LCD ou e-ink: inclinação para LCD no v0 e e-ink numa versão 2. Não decidido.
- Fixação: o v0 pode ter alfinete e cordão, sem decidir entre clipe e colar.
- Onde imprimir: perguntado, sem resposta ainda. Impressora própria não recomendada agora.

## Paris contra BH (pesquisa rasa de 04/11/2026; buscas trouxeram pouco)
- Paris: entrega rápida; anúncios de placas com tela €9 a €47 mais €4 a €10 de frete (Fruugo.fr, marketplace de terceiros); Botland não confirmado; fablabs de biblioteca com inscrição; preço de impressão não achado.
- BH: sem preço de placa em reais; fablabs no Newton Paiva e em Betim; SENAI CIT sem tabela pública; impressão ~R$50 por peça em média (fonte fraca).
- Importação para o Brasil: até US$50, imposto federal 0% mais ICMS de 17%; acima, sobe muito (relatório 02).
- Inclinação do Claude, não decisão: comprar placa e bateria em Paris agora e fazer o software e a medição lá; imprimir a caixa depois de medir.

## Viagem de avião Paris a Brasil
- Bateria de lítio na mala de mão, não despachada (fontes: blogs; sem página oficial da ANAC achada). Uma bateria de ~400 mAh tem ~1,5 Wh [cálculo], muito abaixo do limite comum de 100 Wh. Proteger os contatos com fita.
- Cota de isenção da Receita para viagem aérea: US$1.000 por pessoa [fonte: sites sobre bagagem, não a Receita]. Peças de ~€100 ficam abaixo. Guardar recibo.
- Protótipo de uso pessoal e Anatel: não estudado.
