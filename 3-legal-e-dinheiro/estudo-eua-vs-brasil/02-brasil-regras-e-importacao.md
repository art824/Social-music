# Vender o badge no Brasil: regras, importação e custo

Pesquisa de 03/11/2026. Parte do estudo "EUA ou Brasil primeiro". Não é conselho jurídico nem tributário. Nada aqui é decisão: são fatos, riscos e, onde marcado, uma inclinação do pesquisador.

**Como ler as marcas.** [fonte: URL, data] = li a fonte (data da página quando existe; senão, data do acesso, 03/11/2026). [estimativa] = conta ou palpite meu. [não verificado] = não achei fonte confiável. Muitas fontes são blogs de contabilidade ou empresas que vendem o serviço (têm interesse em mostrar o processo como necessário); aviso quando é o caso. O site do Planalto (texto da lei do consumidor) bloqueou o acesso; não contornei.

## Resumo em 7 pontos

1. **Anatel é o maior obstáculo.** Sem a homologação (aprovação oficial) de um produto com Wi-Fi/Bluetooth, não se pode importar nem vender. Custo estimado de R$10 mil a R$30 mil e meses de prazo, e o titular precisa estar no Brasil.
2. **Piloto para testar mercado não é permitido.** A Receita diz que a exceção de "amostras" não vale para lote piloto, estoque ou distribuição a influenciadores.
3. **Imposto:** produto de US$25 de fábrica chega a cerca de R$240 já nacionalizado (cerca de 1,8 vez o custo) [estimativa]. Com a Anatel diluída, cerca de R$270.
4. **MEI** (limite R$81 mil por ano) esgota com cerca de 195 unidades a R$415. Dúvida aberta: se o MEI pode importar para revender.
5. **Crowdfunding:** Kickstarter não aceita criador com endereço no Brasil. Catarse aceita CPF, mas cobra 13% [fonte abaixo].
6. **Inmetro:** não achei exigência para bateria de lítio portátil ou carregador USB. Lacuna a confirmar.
7. **Direito do consumidor** (arrependimento de 7 dias, garantia legal de 90 dias) vale desde o primeiro cliente.

## 1. Anatel

**O que é.** Agência Nacional de Telecomunicações. Todo produto que emite rádio (Wi-Fi, Bluetooth) precisa ser **homologado** antes de entrar no país e de ser vendido [fonte: https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/manuais/despacho-de-importacao/topicos-1/procedimentos-preliminares/outros-controles-1/anatel, 12/08/2026]. O badge entra na categoria "radiação restrita" (Resolução 680/2017 e Ato 14448/2017) [fonte: https://documentation.espressif.com/ESP32-S3-WROOM-1%20Anatel%20Certification.pdf, emitido 02/07/2025].

**Como funciona.** Um laboratório testa o produto; um **OCD** (Organismo de Certificação Designado: empresa privada autorizada pela Anatel) emite o certificado; o OCD registra no sistema da Anatel e sai o número de homologação, que vai impresso no produto [fonte: https://ib-lenhardt.com/kb/anatel-requirements, atualizado 27/10/2026; https://yescert.com.br/blog/anatel/modulos-iot-dispositivos-wireless-regras-anatel-importadores/, 23/07/2026].

**Certificação e Declaração de Conformidade são coisas diferentes.** A Declaração de Conformidade é só para **uso próprio**: vale para uma unidade (por número de série), não para o modelo, e "não vale para comercialização". Só equipamentos de Categoria II e que não ficam ligados à tomada [fonte: https://www.gov.br/anatel/pt-br/regulado/certificacao-de-produtos/declaracao-de-conformidade, acesso 03/11/2026]. Para vender, é a certificação via OCD.

| Item | O que achei | Qualidade da fonte |
|---|---|---|
| Taxa da Anatel | Zero desde out/2019 (antes R$200 uso próprio, R$500 comercial) [fonte: https://yescert.com.br/blog/anatel/quanto-custa-a-homologacao-anatel-guia-completo-de-custos/, atualizado 24/10/2026] | Consultoria |
| Custo (OCD + laboratório + tradução + amostras) | Módulo Wi-Fi+Bluetooth: R$6–10 mil. Smartwatch/pulseira: R$10–30 mil [fonte: mesmas páginas da YesCert, 2026] | Quem vende o serviço. [estimativa] para o badge: R$10–30 mil, porque é vestível (pode exigir teste de exposição ao corpo, o "SAR") |
| Prazo | Anatel: 16 a 30 dias corridos, só a etapa dela [fonte: https://www.gov.br/pt-br/servicos/homologar-produtos-de-telecomunicacoes-anatel, acesso 03/11/2026]. Ciclo todo (testes e retestes): 45–70 dias úteis para módulo [fonte: YesCert, 23/07/2026] | Oficial + consultoria. Plano realista: 3 a 5 meses [estimativa] |
| Manutenção | Revisão a cada 2 anos para Wi-Fi/Bluetooth [fonte: ib-lenhardt, 27/10/2026] | Consultoria |

**Quem pode pedir? Fontes divergem.** O portal gov.br diz "pessoas físicas e jurídicas", mas lista CNPJ e contrato social entre os documentos, e exige conta gov.br prata ou ouro. A Receita diz que o importador legitimado é "o detentor da homologação ou seu representante legal" e que o código é "pessoal e intransferível". Fabricante estrangeiro precisa de representante no Brasil [fonte: ib-lenhardt, 27/10/2026]. No certificado do módulo da Espressif, o solicitante é uma empresa brasileira com CNPJ. Se um CPF pode ser titular de uma certificação comercial: [não verificado]. O custo e a necessidade de ser titular no Brasil já pesam na decisão de empresa.

**Módulo já homologado ajuda?** Só um pouco. O ESP32-S3-WROOM-1 tem certificado ICC 06.083/2023.1, válido até 11/07/2027. O próprio certificado diz que é "produto não acabado" e que integrá-lo em outro equipamento "requer nova avaliação". Quem integra deve citar o certificado no manual. A YesCert diz que o módulo "pode simplificar", mas mudar antena ou layout de rádio pode exigir nova avaliação. Quanto desconto exato: perguntar a um OCD [não verificado]. O certificado vence em 07/2027; renovação: [não verificado].

**Pré-venda e crowdfunding.** A importação de produto para comercialização só é permitida com homologação prévia. A exceção de amostras cobre unidades "exclusivamente para ensaios"; não vale para testar aceitação comercial, formar estoque nem distribuir a influenciadores [fonte: Receita, 12/08/2026]. Se anunciar e aceitar pagamento antes da homologação já conta como "comercialização" sancionável: [não verificado]; é pergunta para advogado. Hoje o texto da Resolução 715 (art. 83) lista "comercialização de produto não homologado" como infração [fonte: busca sobre Resolução 715/780, 2025].

**Se vender sem homologar.** Retenção na alfândega e devolução à origem; apreensão; multas; suspensão da homologação; responsabilização de importador, vendedor e até do marketplace [fonte: Receita, 12/08/2026]. Exemplos de valor: R$500 à Tectoy por vender powerbank sem homologação (2022; a planilha da Anatel previa até R$27.500) [fonte: https://tecnoblog.net/noticias/tectoy-e-multada-em-r-500-pela-anatel-por-vender-powerbank-sem-homologacao/, 16/05/2022]; multa de R$47,3 mil à Amazon e R$353 mil ao Magalu em casos maiores (2022 a 2024, fonte jornalística resumida, antiga). Para um vendedor pequeno, o risco maior é ser removido de marketplace e ter o estoque apreendido, não a multa.

## 2. Inmetro

**O que é.** Instituto que torna obrigatória a certificação de segurança de certos produtos.

**O que achei.** Nada confirma certificação compulsória para bateria de lítio portátil, powerbank ou carregador USB:
- A lista de produtos com certificação compulsória na Receita não cita bateria de lítio, powerbank, carregador USB nem fonte de alimentação (só baterias automotivas e plugues/tomadas) [fonte: https://www.gov.br/receitafederal/pt-br/assuntos/aduana-e-comercio-exterior/manuais/despacho-de-importacao/topicos-1/procedimentos-preliminares/outros-controles-1/inmetro-produtos-sujeitos-a-certificacao-compulsoria, 12/08/2026].
- O Inmetro estuda regra só para baterias de reposição de bicicletas e patinetes elétricos; conclusão prevista para dez/2026 [fonte: https://www.gov.br/inmetro/pt-br/centrais-de-conteudo/noticias/inmetro-estuda-novas-regras-para-baterias-e-recarga-de-veiculos-eletricos-no-pais, atualizado 29/10/2026].
- Portaria 148/2022 cobre eletrodomésticos e carregadores de pilha AA/AAA/C/D/9V e inclui aparelhos "classe III" alimentados por bateria recarregável. Um badge não é eletrodoméstico, mas ninguém confirmou isso [não verificado] [fonte: gov.br/inmetro, perguntas frequentes sobre a Portaria 148, 2026].
- Carregadores de celular: nota local de 2019 diz que eram isentos de certificação Inmetro [fonte: https://www.parana.pr.gov.br/Audio/Ipem-Parana-apreende-carregadores-de-celular-por-risco-seguranca, 2019, antiga].
- O produto vai com cabo USB-C e sem carregador de tomada (hipótese). Isso reduz o risco.

**Atenção:** a Anatel já multou venda de powerbank sem homologação, então bateria e carregador também podem cair na Anatel, não no Inmetro [fonte: Tecnoblog, 16/05/2022]. Confirmar com um OCD no mesmo orçamento.

## 3. Importação

**O que é cada sigla.** *Remessa Conforme*: programa da Receita em que sites estrangeiros cadastrados recolhem imposto na hora da compra. *II*: Imposto de Importação (federal). *ICMS*: imposto estadual, calculado "por dentro" (o imposto entra na própria base, o que o encarece). *RADAR*: cadastro na Receita para quem importa como empresa.

**Regras vigentes para encomendas pessoa física, em 2026.** Fontes não são unânimes; use como ordem de grandeza.

| Faixa | II (federal) | ICMS | Fonte e status |
|---|---|---|---|
| Até US$50, em site do Remessa Conforme | 0% desde mai/2026 (antes 20%) | 17% (estados divergem; 17 a 20%) | MP 1.357/2026 de 12/05/2026; lei (PLV 13/2026) sancionada 10/09/2026 [fonte: https://fenacon.org.br/noticias/isencao-da-taxa-das-blusinhas-em-compras-ate-us-50-e-sancionada/, 11/09/2026]. ICMS 17% em MG: [fonte: https://www.fazenda.mg.gov.br/noticias/2023/2023.10.10_importacao/, 10/10/2023, antiga]; aumento para 20% decidido pelo Confaz em dez/2024, aplicação em MG [não verificado] |
| US$50,01 a US$3.000 | 60% com dedução de US$20 (tabela da MP). A lei permite à Fazenda cortar para 30%; se já foi cortado, [não verificado]; uma fonte diz "30%" com teto de R$3 mil, outra usa US$3.000 | 17% | [fonte: https://www2.camara.leg.br/legin/fed/medpro/2026/medidaprovisoria-1357-12-maio-2026-799111-exposicaodemotivos-179369-pe.html, 12/05/2026] |
| Site fora do Remessa Conforme | 60% sem isenção até US$50 | 17% | [fonte: https://meutudo.com.br/blog/noticias/2026/09/10/taxa-das-blusinhas-ja-acabou-presidente-sanciona-nova-lei-hoje-mas-imposto-nao-sera-zerado/, 10/09/2026] |

**Pessoa física ou CNPJ.**
- Pessoa física: pode importar para **uso próprio**. Importar para revender com CPF não é permitido; a Receita pode apreender [fonte: https://toexceed.com.br/blog/2026/09/09/importacao-simplificada-regras-tributacao-e-limites/, 09/09/2026, blog de importação]. Uma compra de 10 unidades idênticas de placa pode parecer comércio [estimativa].
- CNPJ: pode importar para revenda. O fluxo normal é a importação formal, com RADAR, inscrição estadual e CNAE compatível; análise de 10 a 30 dias úteis; taxa Siscomex de R$214,50 por adição [fonte: https://www.contabilidadezen.com.br/blog/importacao-revenda-tributacao-como-formalizar-2026/, 30/06/2026]. Empresa do Simples Nacional paga II, IPI, PIS e Cofins na entrada, sem crédito, e ICMS também (mesma fonte).
- **MEI importa? Fontes se contradizem.** Uma diz que o MEI não pode importar pelo regime formal; outras dizem que pode tirar o RADAR, mas não importar para vender como atacadista [fonte: https://jornalcontabil.com.br/noticia/nota-fiscal-impostos-e-importacao-entenda-como-funciona-para-o-mei/ e CNA Brasil, sem data]. Resolver com um despachante ou contador. Custo de despachante: [não verificado].
- O regime simplificado (até US$3.000) para empresas: duas fontes dizem que PJ pode, uma diz que "não se aplica a PJ" [fonte: contabilidadezen, 30/06/2026]. Conflito não resolvido.

**1 a 10 unidades de protótipo e componentes (placa, tela, bateria).**

| Rota | Imposto efetivo | Prazo | Risco |
|---|---|---|---|
| AliExpress/site do Remessa Conforme até US$50 como pessoa física, para uso próprio | cerca de 20,5% (só ICMS 17% "por dentro") | [não verificado]; estimativa 2 a 6 semanas | Placa com Wi-Fi/Bluetooth sem selo Anatel pode ser retida pela Anatel nos Correios [fonte: https://olhardigital.com.br/noticia/anatel-confirma-reter-eletronicos-para-homologacao-veja-o-que-pode-ser-taxado/79476, 2018, antiga] |
| Pedido de US$100 em loja fora do programa (courier) | 60% com dedução de US$20: US$40 de II; mais ICMS 17% por dentro dá cerca de US$69 de imposto (+69%) [estimativa a partir da tabela] | 1 a 2 semanas [estimativa] | Courier cobra taxa de despacho (valor não verificado) |
| Trazer na mala | Cota de bagagem (valor não verificado) | Imediato | Anatel permite trazer produto de viagem, segundo reportagem antiga |

Para uso próprio, o selo da Anatel não é exigido se o produto já foi homologado; se não for, a Declaração de Conformidade por unidade é exigida antes do uso [fonte: https://www.gov.br/anatel/pt-br/regulado/certificacao-de-produtos/importacao-para-uso-proprio, atualizado 04/09/2026]. A página não trata de protótipo nem de remessa postal. Receita (12/08/2026): remessa postal não regularizada pode ser devolvida à origem.

**Baterias de lítio.** A página dos Correios diz que as normas da ANAC não autorizam bateria avulsa ou instalada em equipamento por via aérea em mala postal; no terrestre, até 2 pacotes com no máximo 4 células ou 2 baterias instaladas. Na seção internacional, íon-lítio é "postagem proibida" (regra para enviar do Brasil, a regra de importar eu não achei) [fonte: https://www.correios.com.br/enviar/proibicoes-e-restricoes, sem data, rodapé 2026]. Couriers como a DHL aceitam bateria instalada em equipamento (ONU 3481), até 20 Wh por célula e 100 Wh por bateria, mas só para contas aprovadas [fonte: https://mydhl.express.dhl/pw/en/help-and-support/shipping-advice/what-can-i-ship/lithium-batteries.html, 2026]. Uma bateria de 400 mAh a 3,7 V tem cerca de 1,5 Wh [cálculo próprio], bem abaixo dos limites; o problema é o processo, não a potência. Bateria avulsa por correio comum: evite.

## 4. Estrutura para vender

| Item | MEI | ME / Simples Nacional |
|---|---|---|
| Faturamento máximo | R$81 mil por ano. Até 20% acima paga DAS complementar e vira ME; acima disso, retroage [fonte: https://www.gov.br/memp/pt-br/teto-do-mei, 16/09/2026] | ME: R$360 mil; EPP: R$4,8 milhões [fonte: blogs contábeis, 2026] |
| Mudança em andamento | PLP 186/2026 aprovado pelo Senado em 15/10/2026: R$110 mil (2027), R$140 mil (2028); aguardava sanção em 19/10, vale só quando a lei entrar em vigor [fonte: https://crcma.org.br/noticias/senado-aprova-aumento-do-limite-de-faturamento-do-mei-e-perdao-de-dividas, 19/10/2026] | |
| Custo mensal | DAS R$82,05 (comércio), R$86,05 (serviços), R$87,05 (ambos) [fonte: https://www8.receita.fazenda.gov.br/simplesnacional/noticias/NoticiaCompleta.aspx?id=c3b2044c-ff97-432a-b33c-ecf2a3df6dc3, 02/01/2026] | Imposto sobre vendas a partir de 4% (Anexo I, comércio), 7,3% de R$180 a 360 mil; contador: [não verificado]; estimativa R$150–400 por mês |
| Atividade (CNAE) | Lista fechada. Comércio de informática (4751-2/01) aparece como permitido em site de terceiros; vender "pela internet" ou montar/fabricar eletrônico [não verificado] | Qualquer CNAE compatível |
| Importa e revende? | Contraditório (seção 3) | Sim, via RADAR |
| Nota fiscal | Dispensado em venda a consumidor final PF, salvo se pedir; obrigatório para venda a empresa; usa NFA-e (nota avulsa). Uma fonte diz que enviar mercadoria exige nota; como online sempre envia, assuma que sim [fonte: https://sebraepr.com.br/comunidade/artigo/tudo-o-que-voce-precisa-saber-sobre-notas-fiscais-para-mei, sem data, resumo por busca] | NF-e com certificado digital e sistema emissor (custo [não verificado]) |
| Sócio / funcionário | Sem sócio; 1 funcionário (2 se a lei passar) | Sócios e mais funcionários |

Verdade incômoda: o MEI foi pensado para vender coisa pequena. Hardware importado com Anatel de R$10–30 mil e estoque de US$12 mil não cabe bem nele. Pergunta para o contador: abrir direto como ME, ou MEI só para o Sebraetec e depois migrar.

## 5. Direito do consumidor (CDC, Lei 8.078/1990)

- **Fornecedor** inclui quem importa e quem monta (art. 3º) [fonte: https://www.procon.sp.gov.br/wp-content/uploads/2020/02/CDCdeBolso.pdf, 2020]. Você responde mesmo que a fábrica seja chinesa.
- **Arrependimento (art. 49):** compra fora da loja (site, rede social) pode ser cancelada em **7 dias** do recebimento, com devolução de tudo que foi pago (mesma fonte). Quem paga o frete de volta: [não verificado]; costuma ser o vendedor.
- **Garantia legal (arts. 24, 26):** 90 dias para durável (30 para não durável). **Garantia contratual** é adicional e por escrito (art. 50) (mesma fonte). Defeito: 30 dias para o fornecedor consertar antes de o cliente exigir troca ou dinheiro (art. 18) [fonte: https://www.guarulhos.sp.gov.br/sites/default/files/2025-03/Cartilha%20-%20Consumidor%20Consciente.pdf, 2025, guia municipal].
- **Assistência técnica e peças (art. 32):** [não verificado nas fontes]; pela minha leitura geral, exige oferecer peças e assistência enquanto o produto é fabricado. Num badge, na prática é trocar a unidade.
- **Loja online (Decreto 7.962/2013):** mostrar CNPJ/CPF, endereço, canal de atendimento, preço total com frete [fonte: https://www.pjf.mg.gov.br/administracao_indireta/procon/material_grafico/cartilhas/arquivos/guia-comercio-eletronico.pdf, sem data].

## 6. Pagamentos e frete

| Meio | Taxa típica | Observação |
|---|---|---|
| Mercado Pago | Pix grátis; cartão à vista "a partir de" 3,08% [fonte: https://www.cartoesdecredito.me/contas/taxas-cobradas-nos-apps-de-pagamentos-em-2026/, jul/2026] | Blog de terceiros |
| Pagar.me | Pix 0,99%, cartão à vista 4,19%; exige CNPJ ou MEI ativo [fonte: https://pagar.me/precos, 03/11/2026] | Preço de promoção de Black Friday |
| Stripe Brasil | Cartão 3,99% + R$0,39; Pix 1,19% só por convite [fonte: https://stripe.com/br/pricing, 03/11/2026] | Exigência de CNPJ não informada |
| Mercado Livre | Eletrônicos 10 a 14% (clássico) e 15 a 19% (premium), mais tarifa fixa e frete [fonte: https://ecomcalctools.com/pt-br/blog/taxas-mercado-livre-2026/, 10/2026] | Fontes de terceiros divergem |
| Shopee | 14% + 6% do frete grátis = 20%, mais R$4 por item (CNPJ); CPF paga mais [fonte: https://www.ruacep.com.br/guias/ecommerce/comissao-marketplace-ml-amazon-shopee-magalu-2026/, 2026] | Fontes divergem (CPF R$3 ou R$7) |

Marketplaces: o Mercado Livre remove anúncios de produto irregular e pode banir o vendedor (relato de 2021 a 2024). Para eletrônico sem Anatel, é bloqueio provável [não verificado para o badge].

Frete nacional: PAC até 1 kg a partir de R$15,70 e Sedex a partir de R$25,90, valores regionais "estimados" de site não oficial; reajuste de 4,26% em abril/2026 [fonte: https://cidesp.com.br/conteudo/tabela-de-precos-do-correio-guia-atualizado-2026, 2026; https://superfrete.com/blog/reajuste-precos-correios, 2026]. Para um item de 300 g: cerca de R$20 [estimativa]. Valor exato: simulador dos Correios.

## 7. Crowdfunding e pré-venda

| Plataforma | Fato | Fonte |
|---|---|---|
| Kickstarter | Brazil **não** está na lista de países de lançamento (há França, México, EUA, etc.). Exige residência no país, documento do país e conta bancária local | https://help.kickstarter.com/hc/en-us/articles/115005128594-What-countries-can-projects-launch-from, 03/11/2026 |
| Catarse | Sem custo para publicar; 13% do arrecadado se bater a meta (trecho da página, via busca); cerca de 4% disso é pagamento e antifraude. Pessoa física ou empresa; precisa de verificação de identidade e conta bancária brasileira; criador no exterior sem documento brasileiro não consegue sacar | https://crowdfunding.catarse.com.br/nossa-taxa (a página aberta não mostra o total, só o trecho de 4%); https://ajuda.catarse.com.br/pt-BR/articles/16803897-quem-pode-arrecadar-dinheiro-pelo-catarse, 03/11/2026 |
| Impostos na Catarse | O criador emite a nota de recompensa física; a plataforma não decide o tratamento tributário | https://ajuda.catarse.com.br/pt-BR/articles/16803898-impostos-e-documentos-fiscais-referentes-ao-valor-arrecadado, 03/11/2026 |
| Kickante, Benfeitoria, Indiegogo | Páginas de taxas não abriram (404) ou a busca não achou | [não verificado] |

A ajuda da Catarse não menciona regra específica para eletrônico ou protótipo. O dinheiro de uma campanha conta como faturamento: 25 depósitos de US$20 não estouram o MEI, mas uma campanha de US$30 mil sim (cerca de R$157 mil, quase o dobro do limite) [cálculo com R$5,25 por US$]. Mesmo no Brasil, entregar o produto exige a Anatel.

O fundador mora na França até janeiro/2027. Kickstarter aceita lançamento da França; se ele cumpre residência, documento e conta francesa: [não verificado]. É tema do relatório de estrutura.

## 8. Preço realista (custo ilustrativo de US$25)

**Ilustrativo, não é cotação.** Hipóteses [estimativa]: custo na fábrica US$25 por unidade acabada, com bateria; frete aéreo US$1,50; dólar R$5,25 (fechamento de 28/09/2026: R$5,2260 [fonte: https://renovainvest.com.br/dolar-hoje/]); lote de 500 unidades; ME no Simples; II 16% e IPI 10% (as faixas reais vão de 0 a 35% e de 0 a 30%, dependem da classificação do produto na NCM, que não fiz); PIS 2,1% e Cofins 9,65% [fonte: contabilidadezen, 30/06/2026]; ICMS 18% (alíquota geral de MG, não verificada) por dentro; Anatel R$15 mil / 500 unidades.

| Linha | R$ por unidade |
|---|---|
| Custo na fábrica + frete (US$26,50) | 139 |
| Imposto de Importação (16%) | 22 |
| IPI (10% sobre valor + II) | 16 |
| PIS + Cofins | 16 |
| ICMS (18% por dentro) | 43 |
| Siscomex e despachante diluídos | 4 |
| **Custo nacionalizado** | **cerca de 240** |
| Anatel diluída (R$15 mil / 500) | 30 |
| Frete Correios + embalagem | 25 |
| **Custo antes de impostos sobre a venda, cartão e devoluções** | **cerca de 295** |

Sobre o preço de venda: Simples 6% (4 a 7,3%) + cartão/gateway 3,5% + reserva de devolução e garantia 5% [estimativa] = 14,5%.

| Preço ao consumidor | Em US$ | Sobra por unidade (antes de marketing e do seu tempo) |
|---|---|---|
| R$345 | 66 | zero (ponto de equilíbrio) |
| R$415 (US$79 convertido) | 79 | cerca de R$60 (14%) |
| R$530 | 101 | cerca de R$158 (30% de margem bruta) |

Leitura: no preço-alvo dos EUA (US$79), o Brasil deixa cerca de R$60 por unidade e quase nada para anúncio. Para ter 30% de margem bruta, o preço teria de ser cerca de US$100, o dobro do Emodo (US$49,99, concorrente direto citado no VENTURE.md). Declarar valor menor na importação para pagar menos imposto é subfaturamento, que a Receita pune; não é caminho. [Não verificado: a pena exata.]

## Inclinação do pesquisador, não decisão

Vender no Brasil primeiro exige, antes do primeiro cliente: Anatel (R$10–30 mil e meses), empresa, importação formal e nota fiscal. Não consegui encontrar uma forma legal de testar demanda no Brasil com um lote pequeno de produto com rádio. O que se pode fazer sem a Anatel: lista de espera e depósito reembolsável (juridicamente é questão para advogado). Aponto isso como risco, não conclusão. As alternativas e comparação com os EUA ficam no relatório de síntese.

## O que eu não consegui confirmar

1. Se pessoa física (CPF) pode ser titular de uma certificação Anatel comercial.
2. Quanto um módulo já homologado reduz o custo; custo real do badge (peça orçamento a 2 OCDs).
3. Se aceitar pré-venda ou depósito antes da homologação é "comercialização" ilegal.
4. Se existe exigência do Inmetro para o badge, a bateria ou o carregador (baterias portáteis e fontes USB não aparecem nas listas).
5. Se o MEI pode importar para revender; se pode montar ou fabricar eletrônico; quais CNAE servem.
6. Se a redução do II de 60% para 30% (acima de US$50) já está em vigor; alíquota exata de ICMS em MG hoje.
7. Despachante, courier e honorários de contador (valores).
8. Prazos reais de entrega de AliExpress e courier em 2026; regra atual dos Correios para importar bateria de lítio instalada.
9. Taxas atuais de Kickante, Benfeitoria e Indiegogo; se o Indiegogo aceita criador residente no Brasil.
10. Exigência de arrependimento com frete de devolução; art. 32 do CDC (texto bloqueado).
