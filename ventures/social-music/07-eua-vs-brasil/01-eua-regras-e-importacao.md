# Vender nos EUA: regras, hardware e importação (para um fundador no Brasil)

Pesquisa de 03/11/2026. Legenda: [fonte: URL, data] = lido ou resumido nesta pesquisa; [estimativa] = conta ou suposição minha; [não verificado] = sem fonte confiável. A maioria das fontes é de laboratórios, escritórios e blogs de logística, que têm interesse comercial; as oficiais que consegui ler estão indicadas. Nada aqui é decisão: são fatos, custos e riscos.

## Resumo
1. Mesmo com módulo ESP32 já aprovado, o produto final precisa de testes. Estimativa de laboratório: US$ 6,5 mil a 12 mil, mais um possível teste de exposição do corpo à radiação (SAR). É mais de 10 vezes o orçamento de €500.
2. A FCC (agência americana de rádio e eletrônicos) exige uma "parte responsável" nos EUA na rota de declaração própria, e um agente americano na rota de certificação. Uma regra proposta em 2026 quer ampliar isso.
3. Tarifa sobre produto chinês hoje: 12,5% (nova, desde 24/07/2026), somada talvez a 7,5% ou 25% (listas antigas): de 12,5% a 37,5% do valor declarado, conforme o código do produto, ainda não confirmado.
4. A isenção para remessas pequenas ("de minimis") acabou para todos os países. Mandar um pacote da China a cada cliente ficou burocrático.
5. Não precisa morar nos EUA, mas quase tudo é mais fácil com uma empresa americana (LLC), que custa US$ 1 mil a 4 mil por ano.
6. Bateria: o teste de transporte UN 38.3 é obrigatório por lei; UL é exigência de varejistas, não da lei federal.

## 1. FCC (Federal Communications Commission)

Seu badge tem dois tipos de circuito para a FCC:

| | Radiador intencional | Radiador não intencional |
|---|---|---|
| O que é | O rádio Bluetooth/Wi-Fi (emite de propósito) | O resto do circuito digital (emite ruído sem querer) |
| Via normal | Certificação: laboratório testa e uma TCB (Telecommunication Certification Body, entidade credenciada) emite o "FCC ID" | SDoC (Supplier's Declaration of Conformity): você testa e declara, sem FCC ID |
| Responsável | O requerente ("grantee") | A "parte responsável" |

[fonte: compliancegate.com/fcc-certification e compliancetesting.com/fcc-self-certification, consultorias, 2025-2026]. Quem usa SDoC pode optar por certificar [fonte: 47 CFR 2.906(c), customsmobile.com/regulations/expand/title47_chapterI_part2_subpartJ_subjgrp214_section2.906, verificado 03/11/2026].

**Módulo ESP32-S3 já certificado.** A Espressif tem concessão "modular única" do módulo ESP32-S3-WROOM-1U: FCC ID 2AC7Z-ESPS3WROOM1U, de 31/03/2022 [fonte: documentation.espressif.com/ESP32-S3-WROOM-1U FCC Certification.pdf, lido]. O ID da versão WROOM-1 não achei [não verificado]. A concessão avisa que o produto final deve cumprir as regras (guia KDB 996369) e que "aprovação separada é exigida para configurações portáteis (seção 2.1093) e antenas diferentes". Um badge no corpo é portátil, o que aciona a avaliação de exposição à radiação (SAR).

**O que ainda falta com módulo aprovado:**
1. Testes de emissão do circuito digital (Parte 15B). Preços conflitantes: US$ 1,5 mil a 2,5 mil, cerca de um dia [fonte: digi.com/Support/knowledge-base/fcc-modular-approval, sem data] contra US$ 6,5 mil a 10 mil [fonte: compliancetesting.com/fcc-certification-faqs/fcc-certification-cost, 24/04/2025, laboratório que vende o serviço].
2. SAR ou isenção. Pela fórmula da FCC (KDB 447498), a 5 mm de distância e 2,4 GHz a isenção vale só até cerca de 10 mW [cálculo meu; slides da FCC em transition.fcc.gov/oet/ea/presentations/files/apr22/43-RF-Exposure-Policies.pdf; confirmar com laboratório]. A concessão lista 19,8 mW no Bluetooth e 324 mW no Wi-Fi. Baixar a potência por software pode ajudar; se a FCC aceita sem novo pedido, não sei. Preço do teste SAR: não achei [não verificado].
3. Etiqueta "Contains FCC ID" ou e-label (informação na tela, até 3 passos de menu, opcional) [fonte: compliancegate.com/fcc-labeling-marking-guide, sem data].
4. Chip solto na sua placa, sem módulo: certificação completa, US$ 9 mil a 12 mil [fonte: compliancetesting.com, 24/04/2025].
5. Bluetooth SIG (dona da marca Bluetooth): qualificação para usar a marca. Não é lei. A tabela mostra US$ 12 mil para membro Adopter [fonte: bluetooth.com/develop-with-bluetooth/qualification-listing/qualification-listing-fees, 2026; leitura incerta, não verificado].

**Prazo.** Sem fonte forte: 6 a 8 semanas num blog de vendedores [fonte: seller.alibaba.com, 2026]; 9 dias num laboratório chinês [fonte: jjrlab.com, 2024]. [estimativa: 1 a 3 meses com fila e reteste].

**Laboratórios na China.** Em set/2025 a FCC abriu processo contra sete laboratórios controlados pela China e não renovou quatro [fonte: broadbandbreakfast.com/fcc-withdraws-recognition-from-chinese-labs, 09/09/2025]. Quem usa SDoC não pode se apoiar em laboratório sob controle de "entidade proibida" e deve guardar prova disso [fonte: mondaq.com, 2025]. Os laboratórios mais baratos ficam na China; quais ainda servem, não verifiquei.

**Parte responsável e representante nos EUA:**

| Via | Exigência | Fonte |
|---|---|---|
| SDoC | A parte responsável (fabricante, montador ou importador) "deve estar localizada nos Estados Unidos" | 47 CFR 2.909(b), customsmobile.com (seção 2.909), verificado 03/11/2026 |
| Certificação | Não exige parte responsável nos EUA, mas todo requerente, nacional ou estrangeiro, designa um agente nos EUA para receber citações (2.911(d)(7)); não pode ser a TCB | Mesma fonte; siq.si/?p=28772 (consultoria, sem data) |
| Proposta | Todo requerente teria uma parte responsável nos EUA (importador, varejista ou outro). Publicada em 07/08/2026, comentários até 08/09/2026; ainda não é regra final | arnoldporter.com, 09/2026 |

Quem pode ser: sua LLC americana, um importador, um 3PL (centro de logística) ou um serviço de agente (preço não achado) [não verificado]. Sem ninguém nos EUA, a via SDoC fecha.

**Vender antes da aprovação.** A regra 2.803 proíbe "comercializar" aparelho sem autorização. A exceção que li vale para clientes empresariais, em fase de desenvolvimento, com aviso escrito de que a entrega espera a conformidade [fonte: law.cornell.edu/cfr/text/47/2.803, versões mistas]. Se uma pré-venda a consumidores conta como oferta de venda, não consegui confirmar. É a primeira pergunta para um advogado.

## 2. Bateria de lítio

| Tema | Obrigatório por lei? | Prática de mercado |
|---|---|---|
| UN 38.3 (testes de segurança para transporte) | Sim. Toda célula/bateria de lítio precisa ser de tipo testado e o fabricante tem de ter um resumo do teste; só pilha-botão instalada em aparelho é isenta do resumo [fonte: 49 CFR 173.185, law.cornell.edu/cfr/text/49/173.185, lido] | Peça o relatório ao fabricante da bateria; custo de testar por conta própria: não achei |
| Tamanho | ~400 mAh a 3,7 V = 1,5 Wh [cálculo meu], bem abaixo de 20 Wh (célula) e 100 Wh (bateria) das regras simplificadas | |
| Envio aéreo | Desde 01/01/2026, bateria embalada junto com aparelho (PI 966) deve estar a 30% de carga; instalada no aparelho (PI 967) pode ir até 100% [fonte: jauch.com/blog/en/un-38-3-new-regulations-for-the-air-transport-of-lithium-batteries-from-2026, 2026] | Transportadoras podem cobrar taxa ou recusar [não verificado] |
| UL 2054, UL/IEC 62133 | Não achei lei federal que exija; UL só obriga quando uma regra o incorpora (exemplo: UL 4200A para pilha-botão) [fonte: compliancegate.com/lithium-battery-safety-standards-united-states, 06/2024] | A Amazon exige resumo UN 38.3, ficha SDS e UL 62133/2054 [fonte: compliancegate.com/?p=4744, 26/08/2025]. Kickstarter e Shopify: não verificado |
| Lei de Reese | Só vale para pilha-botão; bateria plana recarregável fica de fora [conclusão minha] | |

Risco extra: a Califórnia incluiu produtos com bateria embutida no programa de lixo eletrônico (SB 1215): taxa no ponto de venda desde 01/01/2026, relatórios de fabricantes desde 01/07/2027 [fonte: bdlaw.com, 2025]. Se um badge pequeno é "produto coberto" e qual a taxa: não confirmei.

## 3. Outras regras

| Regra | Obrigatória? |
|---|---|
| CPSC (agência de segurança de produtos) | Produto de uso geral só precisa de certificado (GCC) se existir norma da CPSC aplicável, emitido pelo importador ou fabricante; desde 08/07/2026 o certificado é enviado eletronicamente à alfândega [fonte: cpsc.gov/GCC, lido]. Não é produto infantil se for para adultos: a definição (menores de 12 anos) é de memória, não consegui abrir a página [não verificado] |
| Prop 65 (Califórnia, avisos de químicos) | Sim, mas empresa com menos de 10 funcionários fica isenta do aviso; contratos com varejistas podem exigir assim mesmo. Multa até US$ 2.500 por violação por dia [fonte: oehha.ca.gov/proposition-65/businesses-and-proposition-65, 2026; sgs.com, 07/2026] |
| RoHS e etiqueta "Made in China" | Não achei lei federal equivalente à RoHS europeia; a marcação de origem é exigida pela alfândega (19 USC 1304) [ambos de memória, não verificado]. Declaração RoHS da fábrica é prática de mercado |
| Garantia (Magnuson-Moss) | Ninguém é obrigado a dar garantia; se der por escrito em produto acima de US$ 15, o texto deve estar disponível antes da compra [fonte: FTC, via busca, sem data] |
| Regra de envio da FTC | Quem anuncia prazo precisa esperar cumpri-lo; se atrasar, pede consentimento ou reembolsa [fonte: ftc.gov/business-guidance/resources/business-guide-ftcs-mail-internet-or-telephone-order-merchandise-rule]. Se vale para crowdfunding: não confirmei |
| Devolução e seguro | Sem prazo federal; 30 dias é a expectativa [estimativa]. Seguro de responsabilidade do produto não é lei; US$ 1 milhão é o padrão pedido por varejistas e custa de US$ 500 a 1.200/ano em e-commerce comum, mais para eletrônicos [fonte: howtostartanllc.com, 02/2026] |

## 4. Tarifas e importação em 2026

**O que mudou:**
- 20/02/2026: a Suprema Corte decidiu (6 a 3) que a lei IEEPA não autoriza tarifas; as tarifas "fentanil" e "recíprocas" pararam em 24/02/2026 [fonte: plantemoran.com, 02/2026; airliftusa.com/tariff-updates/china, 25/09/2026].
- 24/02 a 24/07/2026: sobretaxa de 10% (Seção 122); uma fonte diz 15%.
- Desde 24/07/2026: sobretaxa de 12,5% sobre a China (Seção 301, trabalho forçado), somada às antigas [fonte: zonos.com/docs/guides/country-guides/united-states/section-301-forced-labor e portless.com/blogs/section-301-tariffs-china, 2026]. Uma tabela do escritório Holland & Knight mostra 13%, o texto 12,5% [hklaw.com, 07/2026]; usei 12,5%.
- Tarifas antigas da Seção 301 continuam: 25% (Listas 1 a 3) ou 7,5% (Lista 4A) [fonte: airliftusa.com, 25/09/2026]. Exclusões por produto valem até 09-10/11/2026; improvável cobrirem o badge [não verificado].

| Cenário (valor declarado ~US$ 20 = preço de fábrica, não os US$ 79) | Tarifa | Imposto por unidade |
|---|---|---|
| Fora das listas antigas | 12,5% | US$ 2,50 |
| Lista 4A | 7,5% + 12,5% = 20% | US$ 4,00 |
| Listas 1 a 3 | 25% + 12,5% = 37,5% | US$ 7,50 |
| Isento da sobretaxa de 12,5% (lista de eletrônicos) | só as antigas | US$ 0 a 5 |

[estimativa minha; não confirmei em qual lista ou isenção o produto cai; a tarifa-base pode ser 0%.]

**Código HTS** (Harmonized Tariff Schedule, a tabela que define a alíquota). Provável: 8517.62.00 (aparelhos de transmissão de dados). A alfândega classificou smartwatches assim porque o rádio dá "caráter essencial" ao produto, decisão H257947 de 2015, portanto antiga [fonte: willsonintl.com/news/cbp-rules-on-smartwatch-classification, 08/2015]. Alternativa: 8543.70.99. Não achei decisão para um badge com tela. Dá para pedir à alfândega uma decisão vinculante ou consultar um despachante.

**De minimis** era a regra que liberava pacotes até US$ 800 sem imposto. Acabou para China em 02/05/2025 e para todos os países em 29/08/2025. Em 24/06/2026 a alfândega (CBP) tornou a suspensão indefinida fora do correio; cada pacote precisa de entrada formal ou informal (até US$ 2.500) com código de 10 dígitos [fonte: Federal Register, govinfo.gov/content/pkg/FR-2026-06-24/html/2026-12670.htm, lido]. No correio, desde 24/07/2026, quem declara precisa ser dono, comprador ou despachante e ter fiança aduaneira [fonte: thomsonreuters.com (regulatory-insights, 01/07/2026)]. Um adiamento para 20/01/2027 de certas entradas postais aparece só em busca [não verificado].

**DDP e DAP.** DDP (Delivered Duty Paid): o vendedor paga imposto e desembaraço; o cliente nada. DAP (Delivered At Place): o cliente paga ao receber, com mais pacotes recusados [fonte: shippypro.com/blog/en/ddp-vs.-dap-ddu-who-pays-customs-duties-2026-e-commerce-guide, 2026]. Quem faz DDP é o "importador de registro" (IOR). Um não residente pode ter fiança contínua de US$ 250 a 600/ano [fonte: borderbuddy.com, 2026], mas não achei regra clara para pessoa física estrangeira; há serviços de IOR, sem preço [não verificado].

## 5. Imposto de venda (sales tax)

- Desde o caso Wayfair (2018), vendedor remoto cobra imposto no estado onde passa de um limite, em geral US$ 100 mil (vários estados já eliminaram o critério de 200 transações) [fonte: beancount.io/blog/2026/07/22/sales-tax-nexus-2026-economic-nexus-thresholds-100k-200-transaction-trap-wayfair-guide, 22/07/2026].
- Marketplaces (Amazon, Etsy) recolhem por você; na loja própria o dever é seu [mesma fonte].
- Com ~US$ 18 mil em 50 estados, provavelmente nenhum limite é atingido [estimativa]. Estoque em 3PL cria presença física no estado e pode gerar obrigação [de memória, não verificado].
- LLC com dono estrangeiro entrega o formulário 5472 todo ano, mesmo sem lucro; multa citada de US$ 25 mil [fonte: taxesforexpats.com/articles/foreign-business/foreign-owned-single-member-llc, 2026; conferir no IRS].

## 6. Logística

| Rota | Custo por unidade (item pequeno) | Observações |
|---|---|---|
| China direto ao cliente (DDP) | Frete ~US$ 2-5 [fonte fraca: sino-shipping.com, 03/2026, sem imposto] + imposto US$ 2,5-7,5 + taxa de desembaraço por pacote (não achei) | 6 a 15 dias. Cada pacote é uma entrada na alfândega. Devolver à China é impraticável: reembolso sem devolução [estimativa] |
| Lote a um 3PL nos EUA | Pick and pack US$ 1,50-3,50 pelo 1º item; mínimo mensal US$ 250-275; setup ShipBob ~US$ 975; caixa de armazenagem US$ 1-5/mês; conta real 20-50% acima da cotada [fonte: eightx.co e fulfill.com, 2026, preços não públicos] + postagem nos EUA ~US$ 7,6 por 1 lb [fonte: idshipthat.app, sem data] | O lote tem um só desembaraço (IOR e fiança). Devolução é doméstica |
| Brasil aos EUA | Não achei tarifa | O Exporta Fácil dos Correios não aceita carga perigosa pela IATA, e lítio é assim classificado [fonte: Sebrae, infográfico Exporta Fácil, sem data; confirmar]. O produto entraria antes no Brasil com impostos de importação (outro relatório) |

## 7. Brasileiro, não residente

- **Marca (USPTO):** desde 03/08/2019 quem mora fora dos EUA precisa de advogado americano [fonte: uspto.gov/subscription-center/2019/new-rule-requires-foreign-domiciled-trademark-applicants-and-registrants; confirmar se mudou]. Preço do advogado: não achei. Registrar não é obrigatório para vender.
- **Empresa:** Delaware custa US$ 110 de abertura, US$ 300/ano de imposto e US$ 50-150/ano de agente; total para não residente US$ 1 mil a 4 mil/ano [fonte: binderr.com/marketplace/us/cost-of-forming-a-delaware-llc, 08/07/2026]. O EIN (número fiscal) sai por fax, correio ou telefone, sem SSN [fonte: alazlaw.com, 2026]. Banco: Mercury aceita não residentes caso a caso; Relay passou a exigir SSN/ITIN [fonte: jupid.com, 07/2026].
- **Pagamentos:** Shopify Payments não existe para lojistas no Brasil (fórum), Stripe incerto [fonte: community.shopify.com, 2023-2025]; uma LLC americana contorna isso.
- **Crowdfunding:** o Kickstarter lista 25 países de criadores, sem o Brasil [fonte: help.kickstarter.com, sem data; confirmar].

## O que pode inviabilizar ou encarecer

1. Entrada de US$ 8 mil a 25 mil [estimativa: FCC, SAR, SIG, LLC, seguro]; só o teste FCC pode ser um terço a dois terços da meta de US$ 18 mil.
2. Falta de parte responsável nos EUA fecha a via mais barata e pode virar regra geral.
3. SAR do uso no corpo, deixado em aberto pela concessão do módulo.
4. Margem: o modelo anterior dava US$ 7 a 25 de lucro bruto por unidade; imposto de US$ 2,5-7,5, frete e devoluções comem boa parte.
5. Regras instáveis: tarifas mudaram várias vezes em 2026 e a FCC restringe produtos da China a cada trimestre (roteadores em 03/2026, inversores em 07/2026) [fonte: arnoldporter.com, 09/2026].
6. Pré-venda a consumidor antes da aprovação FCC: risco legal em aberto.

## Inclinação do pesquisador (não é decisão)

Protótipo e lista de interessados não exigem nada disso; o custo começa ao vender unidades. O passo mais barato é pedir cotação de Parte 15B e SAR a 2 ou 3 laboratórios para um produto com módulo ESP32-S3 e potência reduzida. Nada que li indica que enviar do Brasil ajude nos EUA; o Brasil só ganha se o estudo brasileiro mostrar custo menor.

## O que eu não consegui confirmar

- Lista da Seção 301 (4A ou 1-3), isenção da sobretaxa de 12,5% e HTS correto do badge.
- Se pré-venda a consumidor conta como "oferta de venda" (2.803).
- Preços de teste SAR, de agente americano, de serviço de IOR para pessoa física estrangeira e de decisão de classificação.
- Quais laboratórios chineses ainda são aceitos; FCC ID do WROOM-1 (não 1U).
- Prazo real de laboratório.
- Se o badge é produto coberto pelo SB 1215 e a taxa; se a regra de envio da FTC vale para crowdfunding.
- Frete direto China-EUA em 2026 e taxas de desembaraço por pacote (só estimativas de empresas de logística).
- Kickstarter, Stripe e Shopify para residente no Brasil (fontes de fórum).
- Sites que bloquearam e que não contornei: congress.gov, fcc.gov, ecfr.gov e federalregister.gov (tela de bloqueio) e parte do tarifflens.ai. Usei espelhos (customsmobile.com, govinfo.gov, law.cornell.edu) para o texto das regras.
