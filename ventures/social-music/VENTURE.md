# Venture: Social Music

- **One-liner:** Um badge vestível e minimalista que mostra a capa do álbum que você está ouvindo agora (ou o seu favorito), para quem tem orgulho do próprio gosto musical: uma camiseta de banda que muda com o que toca.
- **Type:** own
- **Stage:** idea
- **Target market & geography:** Jovens adultos (~18–30) para quem o gosto musical é parte da identidade e que já o vestem (camisetas de banda, pins, patches, vinil); segmento de teste: fandoms. EUA primeiro, Brasil depois.
- **Business type:** other (hardware vestível de consumo + app companheiro, venda direta ao consumidor)
- **Report language:** pt
- **Created:** 2026-11-03
- **Last updated:** 2026-11-03

## Status

| Module | Status | Latest output | Updated |
|--------|--------|---------------|---------|
| Customer discovery (`/venture:customers`) | in progress (guia pronto; 0 entrevistas) | 01-discovery/interview-guide-2026-11-03.md | 2026-11-03 |
| Market research (`/venture:market-research`) | done 2026-11-03 | 02-market/market-research-2026-11-03.md | 2026-11-03 |
| Competitor analysis (`/venture:competitors`) | not started | — | — |
| PMF assessment (`/venture:pmf`) | done 2026-11-03 (Mode A: plano; PMF não mensurável) | 04-pmf/pmf-measurement-plan-2026-11-03.md | 2026-11-03 |
| GTM strategy (`/venture:gtm`) | not started | — | — |
| Business model (`/venture:model`) | not started | — | — |
| Venture review (`/venture:review`) | not started | — | — |

<!-- Status values: not started | in progress | done YYYY-MM-DD | stale (needs refresh) -->

## Key facts & numbers

<!-- Each module appends its most important findings here (max ~10 bullets per module).
     Format: - [module, YYYY-MM-DD] finding (source, confidence) -->

- [pre-venture, 2026-11-03] Materiais existentes: `docs/concept.md` (decisões e pesquisa até agora), `tools/art_coverage.py` (teste de capas), `cad/` (modelo 3D com medidas provisórias). (repositório, high)
- [pre-venture, 2026-10-22] Busca de capa por artista + álbum encontrou 17/18 álbuns de mainstream a underground em pelo menos uma fonte gratuita (iTunes, Deezer, Cover Art Archive); "encontrado" = a busca retornou resultado, edição não conferida. (teste próprio, med)
- [pre-venture, 2026-10-19] Airbuds (app de "o que meus amigos ouvem") tem 15M downloads, 5M MAU, 1,5M DAU e US$10M captados — demanda por exibir gosto musical existe, mas para amigos, não estranhos. (TechCrunch / Music Ally, set/2025, med)
- [pre-venture, 2026-10-19] Spotify Wrapped 2025: 200M usuários engajados e 500M compartilhamentos nas primeiras 24h. (números da própria Spotify via TechCrunch, dez/2025, med)
- [pre-venture, 2026-10-14] Mais próximo existente em formato: Divoom Emodo, badge de 1,8" com clipe, ~US$40 (corrigido pelo market-research: US$49,99), sem música sincronizada; Tuneshine, display de capa de mesa, US$199. (sites/reviews, med)
- [pre-venture, 2026-10-14] API Web do Spotify em modo de desenvolvimento limitada a 5 usuários; cota ampliada exige empresa registrada e 250k MAU. A abordagem escolhida evita a API do Spotify (lê o "now playing" do sistema). (TechCrunch fev/2026, high)
- [pre-venture, 2026-10-21] Bateria: estimativa própria (não medida) de ~2–4 h com LCD numa placa de desenvolvimento e bateria de 400 mAh; e-ink colorido gasta energia só ao redesenhar, mas leva ~19 s e pisca. (cálculo próprio + Waveshare, low/med)
- [market-research, 2026-11-03] Sem número público de merch musical só dos EUA ou do Brasil; global ~US$16,3 bi em 2030 com crescimento de 1,6%/ano (MIDiA 2024, med); Universal merch €811 mi em 2025, estável (UMG, high).
- [market-research, 2026-11-03] EUA 18–29: 55,3 mi pessoas (Census 2025, med-high); Brasil 18–29: 36,7 mi (Censo 2022, high).
- [market-research, 2026-11-03] TAM EUA 18–29 (compra única) ~US$0,39–1,15 bi; SOM 3 anos ~7,7 mil–44 mil unidades (US$0,4–2,7 mi); otimista implausível vs comparáveis. Extrapolação própria (low).
- [market-research, 2026-11-03] Divoom Emodo, badge com tela, US$49,99 desde jul/2026 — concorrente direto e âncora de preço (divoom.com, high).
- [market-research, 2026-11-03] Físico como exibição: vinil EUA ~US$1,04 bi em 2025, 19º ano de alta (RIAA, high); 50% dos compradores sem toca-discos (Luminate 2023, med).
- [market-research, 2026-11-03] Jovens 16–24 preferem acessórios e marca discreta "que só fã reconhece" (MIDiA 3T2025, med).
- [market-research, 2026-11-03] Crowdfunding análogo (Pins Collective): 1.042 apoiadores, US$102 mil; hardware entrega no prazo em ≤32% dos casos (Kicktraq; Jensen & Özkil 2018, med).
- [market-research, 2026-11-03] Entrada: FCC US$3–8 mil com módulo pré-certificado; Anatel R$6–50 mil e exige empresa brasileira; +12,5% tarifa sobre China nos EUA desde 24/07/2026 (várias, low–high).
- [market-research, 2026-11-03] Segmento de entrada recomendado (decisão do fundador): "curadores" de gosto variado nos EUA, 18–29; fandoms como segundo teste.

- [customers, 2026-11-03] Modo A concluído: hipótese de ICP e roteiro Mom Test (em inglês, para clientes nos EUA). Nenhuma entrevista feita ainda — nenhuma suposição validada. (próprio, high)

- [pmf, 2026-11-03] PMF não mensurável: 0 usuários. Plano: Sean Ellis com ≥30–40 testadores, dias usados por semana como retenção, % do tempo em cada modo; decisão 8 semanas após o 1º lote de protótipos. (próprio, high)

## Open questions & riskiest assumptions

<!-- Format: - [ ] assumption — how to test it. Modules add here; customers & pmf help test. -->

- [ ] Pessoas pagam por um objeto físico que exibe o gosto musical, em vez de só compartilhar de graça (Wrapped, stories) — testar em entrevistas Mom Test sobre compras passadas de merch/pins/vinil e com uma página de pré-venda.
- [ ] O usuário aceita carregar e recarregar o badge com frequência (LCD = diário; e-ink = mais raro, mas lento) — testar vestindo um protótipo por 2 semanas.
- [ ] O modo "ao vivo" não constrange o usuário a ponto de desligar (músicas que ele não quer mostrar) — testar com os modos Favorito/Off no protótipo e contar quantas vezes ele esconde.

- [ ] O modo ao vivo é o diferencial que faz alguém escolher este badge em vez do Divoom Emodo (US$49,99, pin fixo) — testar em entrevistas: como o entrevistado exibe hoje o que ouve e se o gosto dele muda muito (adicionado por market-research).
- [ ] É possível vender a ~US$50–80 com margem saudável após tarifas, certificação e bateria — testar no módulo model com orçamento real de componentes (adicionado por market-research).

## Decision log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-10-19 | Produto só de exibição: um clipe, um botão, uma luz; sem touchscreen | Minimalismo; touch adiciona custo e problemas sem função relevante |
| 2026-10-20 | Três modos no botão (Tocando agora / Favorito / a definir); luz acesa só em "tocando agora" | Quem vê sabe se é o que toca ou o favorito |
| 2026-10-24 | Claude faz a modelagem 3D (build123d) | Fundador não precisa mexer na modelagem |
| 2026-11-03 | Mercado: EUA primeiro, Brasil depois; relatórios em português; pesquisa de mercado profunda | Respostas do fundador no intake |
