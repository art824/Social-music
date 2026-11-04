# Venture Review — Social Music
2026-11-03 · board-style review · advogado do diabo: rodado (fresh context) · relatório em português

## 1. State of the venture
Uma ideia sem nenhuma evidência de cliente.
- **A favor:**
  - um espaço vazio real: ninguém faz um vestível que mostre sozinho a capa do que toca;
  - tendências a favor: o físico virou objeto de exibição e os jovens preferem acessórios discretos.
- **Contra:**
  - um concorrente grande no mesmo formato e preço (Emodo, US$49,99) que pode copiar o diferencial por software;
  - um modelo financeiro que só fecha no cenário otimista, com custos que são todos suposições;
  - um mercado de escala de marca independente.
- **O que não sabemos:**
  - se alguém usa uma tela no peito todo dia;
  - se o modo ao vivo vale mais que um favorito fixo;
  - se alguém paga ~US$79.
- **Recursos:**
  - fundador com <€500 e 5–10 h por semana até março, mudando da França para o Brasil em janeiro;
  - ambição (marca ou startup) ainda indefinida.

## 2. Scorecard + coherence
| Dimension | Source | Grade (A–F) | Evidence | Freshness |
|---|---|---|---|---|
| Problem & demand validation | 01-discovery | **?** | 0 entrevistas; dor só do fundador | — |
| Market attractiveness | 02-market | **C−** (rebaixado de C) | TAM ~US$0,4–1,2 bi multiplica todo comprador de merch pelo preço; o filtro real ("usaria uma tela no corpo") não tem dado | hoje |
| Competitive position | 03-competitors | **C** (rebaixado de C+) | quadrante vazio, mas o diferencial é software (copiável) e o quadrante tem histórico de fracassos (Pins Collective, Playbutton, Tidbyt) | hoje |
| Product-market fit | 04-pmf | **?** | não mensurável | — |
| GTM execution & traction | 05-gtm | **?** | só plano | — |
| Economics viability | 06-model | **D** | base LTV:CAC 0,99, não empata em 18 meses; ~US$18 mil de custos fixos sem fonte de dinheiro; só o otimista fecha | hoje |

"Não sabemos" aparece em 3 de 6 dimensões. Esse é o maior risco.

**Coerência:**
- **Preço:** o GTM escolhe US$79 e o modelo base usa US$69. O modelo fica **stale** até o preço ser testado.
- **Metas:** a meta do portão (100 inscritos) está abaixo da meta do próprio GTM (300).
- **Datas:** a lista estava marcada para dez/2026, mas os vídeos do protótipo só saem em fev/2027. O GTM fica **stale**.
- **Segmento:** o GTM mira os mesmos "curadores" que o market-research recomendou. Consistente, mas ninguém confirmou que eles amam o produto.
- **Suposições esquecidas sem teste:** recarga diária; uso de uma tela no corpo; constrangimento do modo ao vivo.

## 3. Advogado do diabo — o que mudou
Veredito dele: **SURVIVES WITH DOWNGRADES**.

| Objeção | Gravidade | Como tratei |
|---|---|---|
| O portão de 31/03 não consegue reprovar: o recrutamento já garante "gasto passado", a pergunta 4 induz o "sim", o A/B com ~50 por braço é cara ou coroa (Fisher p≈0,26) e US$5 de depósito não é compromisso | crítica | **Aceita.** Portão reescrito (seção 5) |
| Ordem invertida: o protótipo automático (caro, risco baixo) vem antes do teste barato que pode matar a ideia (usar uma tela no corpo) | crítica | **Aceita.** Teste de uso com um badge manual primeiro; protótipo automático sai do período até março |
| O tempo não fecha: ~120–220 h de trabalho contra 105–210 h disponíveis | major | **Aceita.** Corte de escopo e regra "sem dados em 31/03 = parar" |
| O modo ao vivo se contradiz: se ninguém lê o badge, o ao vivo vale pouco; se precisam ler, a tela de ~28 mm é pequena a 1–2 m | major | **Aceita como hipótese a medir.** O teste de uso registra o tempo em "tocando agora" vs "favorito" |
| Mesmo passando, não há como financiar: ~US$18 mil sem fonte; Kickstarter não aceita criadores no Brasil; a FCC exige uma parte responsável nos EUA | major | **Aceita.** Memo de "caminho de saída" antes de qualquer gasto com hardware. Dados citados por ele (Kickstarter help, 47 CFR §2.909), confiança média |
| Quadrante com histórico de fracassos; nem a Divoom provou demanda pelo Emodo | minor | **Aceita.** Acompanhar as avaliações do Emodo até março, de graça |

## 4. Top 3 risks (ranked) e o teste mais barato de cada
1. **Ninguém usa uma tela no corpo por semanas,** nem o fundador. Teste: 2 semanas com um badge manual barato (genérico de US$15–48 ou Emodo, US$49,99) e capas carregadas à mão. Fundador + 3 pessoas.
2. **Ninguém paga ~US$79.** Teste: página com preço único de US$79 e depósito de ≥US$20 (ou pré-venda reembolsável do valor cheio), com vídeo editado da capa mudando ("porta falsa", página que mede interesse antes do produto existir).
3. **Não há como chegar ao mercado mesmo com demanda.** Teste: meia página escrita com plataforma de pré-venda aberta a quem mora no Brasil, entidade, responsável FCC nos EUA e fonte dos ~US$18 mil.

## 5. Recommendation — PERSEVERE (reestruturado), com portão que pode reprovar
**Seguir só com validação barata, nesta ordem, e parar por padrão se não houver dados.**

**Persevere SE, até 31/03/2027:**
- (a) no teste de uso, o fundador e ≥2 de 3 pessoas usam o badge ≥4 dias na 2ª semana, sem largar por causa da recarga; **e**
- (b) ≥25 depósitos de ≥US$20 (ou pré-vendas reembolsáveis) a US$79, de pessoas fora da rede do fundador; **e**
- (c) o memo de caminho de saída mostra uma rota plausível (plataforma, responsável FCC, fonte do dinheiro).

**Pivot** se (a) passar mas o tempo em "favorito" dominar o "tocando agora". Nesse caso o produto vira um badge fixo e simples, que compete com o Emodo e com clones a US$15–48. Repensar preço e formato com `/venture:model` e `/venture:gtm`, ou mirar o caminho só de software (a parte técnica é a que já está resolvida).

**Kill** se (a) falhar, ou se em 31/03 não houver dados. O aprendizado e o código ficam. Parar limpo é uma vitória, não um fracasso.

Os limiares (≥4 dias, ≥25 depósitos, ≥US$20) vêm do advogado do diabo. São escolhas de corte, não benchmarks com fonte. Você pode ajustar, mas sem afrouxar a ponto de o portão não reprovar.

## 6. Next 30 days (até ~03/12/2026)
1. **Comprar um badge manual barato** (genérico ou Emodo, ≤€50) e começar o teste de uso de 2 semanas com você e 3 pessoas, registrando dias usados e o tempo em cada "modo" (capa atual vs favorita). → teste real
2. **Fazer as 5 primeiras entrevistas Mom Test** com o roteiro revisado. Na pergunta 4, perguntar pela "última camiseta de banda que você parou de usar, quando e por quê"; recrutar metade fora de r/vinyl e subs de merch. → `/venture:customers`
3. **Escrever o memo de caminho de saída** (meia página): plataforma de pré-venda, entidade, responsável FCC nos EUA, fonte dos ~US$18 mil. → tarefa real
4. **Atualizar o modelo com preço de US$79** e refazer o portão do GTM com as novas metas. → `/venture:model`, `/venture:gtm`
5. **Anotar uma vez por mês** as avaliações do Emodo (Amazon/Walmart) e as notas de versão do app Divoom. → tarefa real

## Próxima revisão
Depois do teste de uso de 2 semanas, ou em 31/03/2027, o que vier primeiro.
