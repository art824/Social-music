# Handoff da sessão na nuvem para a máquina local (04/11/2026)

A conversa da nuvem não pode ser levada. O que continua é o repositório. Tudo o que importa está nos arquivos abaixo.

## Como retomar localmente
1. Clone: `git clone https://github.com/art824/Social-music.git` e entre na pasta.
2. Troque para a branch do trabalho: `git checkout main-wddo4z`. (A branch main ainda não tem o trabalho; ver abaixo.)
3. Abra o Claude Code dentro da pasta: `claude`. O arquivo CLAUDE.md é lido sozinho e manda ler docs/estado-do-projeto.md primeiro.
4. Cole esta primeira mensagem:

> Estamos retomando o projeto Social Music vindo de uma sessão na nuvem. Leia CLAUDE.md, depois docs/estado-do-projeto.md, depois docs/handoff.md e docs/prototipo-plano.md. Resuma em 10 linhas onde estamos, o que está decidido, o que está em aberto e qual é o próximo passo. Não construa nada que eu não pedir.

## Onde está cada coisa
- Mapa de uma página: docs/estado-do-projeto.md
- Plano do protótipo (proposta): docs/prototipo-plano.md
- Pesquisas por tema: docs/pesquisa-acumulada.md; decisões e log: docs/concept.md; Sebrae e Living Hub: docs/sebrae.md
- Processo venture (mercado, concorrentes, modelo, veredito): ventures/social-music/
- Estudo EUA contra Brasil: ventures/social-music/07-eua-vs-brasil/ (comece pelo 00-comparacao.md)
- Mapa visual das trilhas: docs/mapa-visual.html (abre no navegador)
- Relatório visual: ventures/social-music/relatorio-visual.html
- Teste de capas de álbum: tools/art_coverage.py
- Modelo 3D provisório que ninguém pediu: cad/ (pode apagar)

## O que NÃO está no repositório
- O PDF do registro do conceito de 14/10/2026 (foi enviado no chat; guarde sua cópia e mande para o seu e-mail).
- Dois artefatos privados no claude.ai (relatório visual e mapa). Os arquivos HTML estão no repositório; os links são só uma cópia.
- O Notion que o Claude criou: sem uso. Pode apagar quando quiser.
- Ferramentas instaladas na nuvem (build123d, OpenSCAD, Playwright): não vêm junto. Só reinstale quando for modelar a caixa (etapa 3 do protótipo).
- O plugin "venture" real: localmente você pode instalar o original (heyparsadev/claude-venture-plugin). Na nuvem seguimos o método dele à mão.

## Estado
Branch main-wddo4z está enviada ao GitHub. Nenhuma pull request foi aberta e a branch main não foi atualizada. Se quiser a main atualizada, é um merge que pode ser pedido ao Claude local.
