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
| Customer discovery (`/venture:customers`) | not started | — | — |
| Market research (`/venture:market-research`) | not started | — | — |
| Competitor analysis (`/venture:competitors`) | not started | — | — |
| PMF assessment (`/venture:pmf`) | not started | — | — |
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
- [pre-venture, 2026-10-14] Mais próximo existente em formato: Divoom Emodo, badge de 1,8" com clipe, ~US$40, sem música sincronizada; Tuneshine, display de capa de mesa, US$199. (sites/reviews, med)
- [pre-venture, 2026-10-14] API Web do Spotify em modo de desenvolvimento limitada a 5 usuários; cota ampliada exige empresa registrada e 250k MAU. A abordagem escolhida evita a API do Spotify (lê o "now playing" do sistema). (TechCrunch fev/2026, high)
- [pre-venture, 2026-10-21] Bateria: estimativa própria (não medida) de ~2–4 h com LCD numa placa de desenvolvimento e bateria de 400 mAh; e-ink colorido gasta energia só ao redesenhar, mas leva ~19 s e pisca. (cálculo próprio + Waveshare, low/med)

## Open questions & riskiest assumptions

<!-- Format: - [ ] assumption — how to test it. Modules add here; customers & pmf help test. -->

- [ ] Pessoas pagam por um objeto físico que exibe o gosto musical, em vez de só compartilhar de graça (Wrapped, stories) — testar em entrevistas Mom Test sobre compras passadas de merch/pins/vinil e com uma página de pré-venda.
- [ ] O usuário aceita carregar e recarregar o badge com frequência (LCD = diário; e-ink = mais raro, mas lento) — testar vestindo um protótipo por 2 semanas.
- [ ] O modo "ao vivo" não constrange o usuário a ponto de desligar (músicas que ele não quer mostrar) — testar com os modos Favorito/Off no protótipo e contar quantas vezes ele esconde.

## Decision log

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-10-19 | Produto só de exibição: um clipe, um botão, uma luz; sem touchscreen | Minimalismo; touch adiciona custo e problemas sem função relevante |
| 2026-10-20 | Três modos no botão (Tocando agora / Favorito / a definir); luz acesa só em "tocando agora" | Quem vê sabe se é o que toca ou o favorito |
| 2026-10-24 | Claude faz a modelagem 3D (build123d) | Fundador não precisa mexer na modelagem |
| 2026-11-03 | Mercado: EUA primeiro, Brasil depois; relatórios em português; pesquisa de mercado profunda | Respostas do fundador no intake |
