# Mural FAUFBA

Página única, sem framework e sem servidor próprio. O estudante marca o que
está travando, em 40 segundos, sem login e sem nome.

## Arquivos

- `index.html` — o app inteiro. É o único arquivo que precisa ser hospedado.
- `Codigo.gs` — o código que vai no Apps Script da conta do DEA.

## Ligar na planilha

1. Na conta `faufba.dea@gmail.com`, criar duas planilhas: `Mural — placar` e
   `Mural — relatos`. Precisam ser arquivos separados, porque o
   compartilhamento de cada um é diferente.
2. A planilha de relatos é compartilhada com uma ou duas pessoas, nominalmente.
3. Em `script.google.com`, novo projeto, colar o conteúdo de `Codigo.gs`.
4. Preencher `ID_PLACAR` e `ID_RELATOS` com o trecho do endereço de cada
   planilha entre `/d/` e `/edit`.
5. Implantar como aplicativo da web. Executar como **eu mesmo**, acesso para
   **qualquer pessoa**. É isso que permite responder sem login.
6. Copiar o endereço terminado em `/exec` e colar no topo de `index.html`,
   entre as aspas de `endpoint`. Ali também ficam `semestre` e `limite`.

Sem esse endereço o app roda em modo demonstração: nada sai do navegador e a
etiqueta no topo diz "demonstração". Com o endereço, a etiqueta muda para
"no ar" e os números começam do zero, porque passam a ser reais.

## Hospedar

Arrastar a pasta em `app.netlify.com/drop`. Sai um endereço público na hora.
Só então gerar os cartazes com o QR definitivo.

## Quem pode responder, e quantas vezes

Cada aparelho recebe um código aleatório de doze caracteres, guardado no
próprio navegador. Ele não contém nome, matrícula nem e-mail. Com esse código,
a pessoa responde no máximo `limite` temas por semestre, três por padrão.

A quarta tentativa é barrada na tela e recusada de novo no `Codigo.gs`, que
registra a tentativa na aba `recusados`. O painel mostra quantas pessoas
responderam e quantas tentativas ficaram fora da conta.

Trocar de semestre é mudar o campo `semestre` no `index.html`. A cota de todo
mundo zera e a contagem recomeça.

A denúncia e o "quero ajudar" são enviados **sem código nenhum**. O primeiro
porque precisa ser anônimo de verdade. O segundo porque pode levar contato, e
contato mais código ligaria as respostas do placar a uma pessoa com nome.

## O que nunca aparece no placar

Os relatos sensíveis vão para a segunda planilha e a função que alimenta o
painel não abre esse arquivo. O placar não tem como mostrá-los.
