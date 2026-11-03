# Business Model — Social Music
2026-11-03 · analista: Claude (venture suite) · script: `unit_economics.py` (rode `python3 unit_economics.py` para refazer)

> **Nenhum custo deste modelo foi medido.** Não há orçamento de fornecedor, protótipo nem venda. Cada entrada está marcada: `sourced` (com fonte) ou `assumption` (suposição minha). Use como mapa do que precisa ser verdade, não como previsão.

## 1. Tipo e unidade
Hardware de consumo vendido direto ao consumidor. A unidade é **o pedido**. Não há assinatura nem evidência de recompra; por isso **LTV = margem do primeiro pedido**. Contar com uma segunda compra ou com acessórios seria esperança, não dado (regra do guia do plugin).

## 2. Entradas
| Entrada | Pess / Base / Otim | Rótulo |
|---|---|---|
| Preço | US$59 / 69 / 79 | assumption. Âncoras: Emodo US$49,99, genéricos US$10–48, Tuneshine US$199,99 (sourced, competitors) |
| BOM (peças: tela, chip, bateria, placa, caixa, clipe, embalagem) por unidade em ~1.000 un. | US$30 / 22 / 16 | assumption (low) — sem orçamento. Painel e-ink colorido de 1,54" a US$7,49–12,49 no varejo (sourced, Waveshare) é a única peça com preço |
| Montagem e teste | US$4 / 3 / 2,50 | assumption |
| Tarifa de importação nos EUA (China) | 25% / 20% / 15% | sourced em parte: +12,5% Section 301 desde 24/07/2026 + taxa básica e listas antigas conforme o código do produto, indefinido (market-research Q5) |
| Frete China→EUA por unidade | US$2 / 1,50 / 1 | assumption |
| Envio ao cliente nos EUA | US$8 / 7 / 6 | assumption |
| Cartão | 2,9% + US$0,30 | sourced (tarifa padrão de pagamento online nos EUA; não reconferida) |
| Devoluções e garantia | 8% / 5% / 3% do preço | assumption |
| CAC (custo para conquistar um cliente) via anúncio direto | US$40 / 25 / 12 | assumption (low) — nenhum dado de canal ainda |
| Custos fixos únicos | FCC US$5,5 mil, UN38.3 US$1 mil, molde da caixa US$8 mil, protótipos US$2 mil, jurídico US$1,5 mil = **US$18 mil** | FCC e UN38.3 sourced como faixas (Q5, low); resto assumption |
| Custo fixo mensal | US$150 | assumption; **salário do fundador = 0, o que deixa o modelo mais bonito do que é** |

## 3. Unit economics (por unidade)
```
Base (preço US$69):
  custo de fábrica   = BOM 22 + montagem 3                         = US$25,00
  custo desembarcado = 25,00 × (1 + 0,20 tarifa) + 1,50 frete      = US$31,50
  custo variável     = 31,50 + 7,00 envio + 69 × (0,029 + 0,05) + 0,30 = US$44,25
  lucro bruto        = 69 − 44,25                                   = US$24,75 (margem 36%)
  sobra após CAC     = 24,75 − 25                                   = −US$0,25

Pessimista (US$59): lucro bruto −US$0,23 (margem 0%) → sobra após CAC −US$40,23
Otimista   (US$79): lucro bruto  US$45,76 (margem 58%) → sobra após CAC  US$33,76
```
- **LTV:CAC** = lucro bruto do 1º pedido / CAC → base 24,75/25 = **0,99** (problema: o guia considera <1,5 ruim e ≥3 saudável). Otimista 3,8; pessimista negativo.
- **Payback do CAC:** é imediato quando a sobra é positiva (só no otimista). No base, cada cliente pago por anúncio **não se paga**.
- **Ponto de equilíbrio dos custos fixos:** 18.000 / 24,75 = **727 unidades** (base); 393 (otimista); nunca (pessimista).

### Sensibilidade (base, variando ±20%)
| Variável | Efeito na sobra por unidade |
|---|---|
| **Preço** | **±US$12,71** ← a que mais mexe |
| BOM | ±US$5,28 |
| CAC | ±US$5,00 |
| Envio ao cliente | ±US$1,40 |
| Tarifa | ±US$1,00 |

| Preço (custos do base) | Lucro bruto | Sobra após CAC US$25 |
|---|---|---|
| US$49,99 (preço do Emodo) | US$7,24 | −US$17,76 |
| US$59 | US$15,54 | −US$9,46 |
| US$69 | US$24,75 | −US$0,25 |
| US$79 | US$33,96 | US$8,96 |
| US$89 | US$43,17 | US$18,17 |
| US$99 | US$52,38 | US$27,38 |

**O número a validar primeiro é o preço que o curador paga**, porque é ele que decide se o modelo funciona. O BOM real vem em segundo (pedir orçamento).

## 4. Projeção de 18 meses (resumo; tabela completa no script)
Linha do tempo assumida: meses 1–6 construir e certificar; mês 8 fecha crowdfunding (300 / 1.000 / 2.500 apoiadores — o base repete o Pins Collective, 1.042 apoiadores); mês 10 paga a fábrica; mês 12 entrega; meses 13–18 venda direta (40/mês fixo; 100/mês +10%; 300/mês +15%).

| Cenário | Ponto mais baixo do caixa | Caixa acumulado no mês 18 | Fica positivo |
|---|---|---|---|
| Pessimista | −US$49.864 (mês 18, ainda caindo) | −US$49.864 | nunca em 18 meses |
| Base | −US$21.104 (mês 18, ainda caindo) | −US$21.104 | **não empata em 18 meses** |
| Otimista | −US$18.150 (mês 7) | +US$150.294 | mês 8 (crowdfunding), sustentado a partir do 13 |

No base, o crowdfunding deixa o caixa positivo por dois meses, mas pagar a fábrica e entregar consome tudo. Depois disso, a venda por anúncio perde US$0,25 por unidade e o caixa não se recupera.

## 5. Veredito
**O modelo não funciona ainda.** Pela regra do plugin, se só funciona no otimista, o veredito é "ainda não". O que precisa ser verdade para virar:
1. **Preço ≥ ~US$79** sem perder o comprador. É acima do Emodo (US$49,99), então só se sustenta se o automático e o design valerem a diferença. Não testado.
2. **Conquistar cliente barato:** CAC ≤ ~US$12–15 vindo de comunidades, crowdfunding e boca a boca, não de anúncio pago. Não testado.
3. **BOM ≤ ~US$16–22** em ~1.000 unidades. Precisa de orçamento real.

**Números de corte (kill numbers):**
- Se o curador só paga **até ~US$50** (preço do Emodo), o lucro bruto fica em ~US$7 por unidade e o negócio **nunca** se paga com anúncio.
- Com preço de US$69, se o **CAC passar de ~US$25**, a venda direta destrói caixa.

## 6. Próximo passo
- **Preço:** testar disposição a pagar nas entrevistas (`/venture:customers`, perguntas sobre gasto atual) e, depois, numa página de pré-venda com preço visível (`/venture:gtm`, seção de preço).
- **Custo:** pedir orçamento de BOM a 2–3 fornecedores com o datasheet do módulo escolhido.
