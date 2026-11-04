# Handoff da sessão na nuvem para a máquina local (04/11/2026)

Versão passo a passo para leigos, em texto simples: 00-comece-aqui/COMO-RETOMAR.txt

A conversa da nuvem não pode ser levada. O que continua é o repositório. Tudo o que importa está nos arquivos abaixo.

## Como retomar localmente
1. Clone: `git clone https://github.com/art824/Social-music.git` e entre na pasta.
2. Troque para a branch do trabalho: `git checkout main-wddo4z`. (A branch main ainda não tem o trabalho; ver abaixo.)
3. Abra o Claude Code dentro da pasta: `claude`. O arquivo CLAUDE.md é lido sozinho e manda ler 00-comece-aqui/estado-do-projeto.md primeiro.
4. Cole esta primeira mensagem:

> Estamos retomando o projeto Social Music vindo de uma sessão na nuvem. Leia CLAUDE.md, depois 00-comece-aqui/estado-do-projeto.md, depois 00-comece-aqui/handoff.md e 2-produto-e-prototipo/prototipo-plano.md. Resuma em 10 linhas onde estamos, o que está decidido, o que está em aberto e qual é o próximo passo. Não construa nada que eu não pedir.

## Onde está cada coisa
- Mapa de uma página: 00-comece-aqui/estado-do-projeto.md
- Plano do protótipo (proposta): 2-produto-e-prototipo/prototipo-plano.md
- Pesquisas por tema: um arquivo pesquisa-*.md dentro de cada pasta de tema; decisões e log: 00-comece-aqui/concept.md; Sebrae e Living Hub: 5-brasil-e-apoio/sebrae.md
- Processo venture (mercado, concorrentes, modelo, veredito): 1-ideia-e-mercado/ventures/social-music/
- Estudo EUA contra Brasil: 3-legal-e-dinheiro/estudo-eua-vs-brasil/ (comece pelo 00-comparacao.md)
- Mapa visual das trilhas: 00-comece-aqui/mapa-visual.html (abre no navegador)
- Relatório visual: 1-ideia-e-mercado/ventures/social-music/relatorio-visual.html
- Teste de capas de álbum: 2-produto-e-prototipo/tools/art_coverage.py
- Modelo 3D provisório que ninguém pediu: 2-produto-e-prototipo/cad/ (pode apagar)

## O que NÃO está no repositório
- O PDF do registro do conceito de 14/10/2026 (foi enviado no chat; guarde sua cópia e mande para o seu e-mail).
- Dois artefatos privados no claude.ai (relatório visual e mapa). Os arquivos HTML estão no repositório; os links são só uma cópia.
- O Notion que o Claude criou: sem uso. Pode apagar quando quiser.
- Ferramentas instaladas na nuvem (build123d, OpenSCAD, Playwright): não vêm junto. Só reinstale quando for modelar a caixa (etapa 3 do protótipo).
- O plugin "venture" real: localmente você pode instalar o original (heyparsadev/claude-venture-plugin). Na nuvem seguimos o método dele à mão.

## Estado
Branch main-wddo4z está enviada ao GitHub. Nenhuma pull request foi aberta e a branch main não foi atualizada. Se quiser a main atualizada, é um merge que pode ser pedido ao Claude local.

## Organização das pastas (04/11/2026)
O repositório foi reorganizado por tema: 00-comece-aqui, 1-ideia-e-mercado, 2-produto-e-prototipo, 3-legal-e-dinheiro, 4-marketing-e-redes, 5-brasil-e-apoio. Cada pasta tem um README com o que está decidido, em aberto e onde estão os detalhes. Para falar de um assunto, abra só a pasta dele.

## Plugin venture: AJUSTE NECESSÁRIO se for instalar
A pasta `ventures/` foi movida para `1-ideia-e-mercado/ventures/` por escolha do fundador. O plugin "venture" original (github.com/heyparsadev/claude-venture-plugin) espera `ventures/social-music/` na RAIZ do projeto. Se instalar o plugin, ele não vai achar este trabalho. Duas saídas: (1) mover `1-ideia-e-mercado/ventures/` de volta para a raiz (com `git mv`); (2) deixar como está e dizer ao plugin onde o trabalho está. Os caminhos dentro dos arquivos já foram atualizados para o local novo e precisariam ser revertidos na saída 1.

## Em palavras simples: as duas cópias do projeto no GitHub
O GitHub guarda o projeto em "cópias" chamadas branches. Todo o nosso trabalho está na cópia `main-wddo4z`. A cópia oficial `main` é a que o GitHub entrega por padrão quando você baixa o projeto. Se ela estiver vazia, você baixa o projeto sem nada. Por isso a `main` foi atualizada com tudo (merge = copiar o trabalho de uma cópia para outra, sem apagar nada).
