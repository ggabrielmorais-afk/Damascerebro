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

Pra responder um tema do placar, o estudante informa a matrícula da UFBA.
São nove dígitos, começando em 2, e o app confere o formato antes de deixar
enviar. Isso rejeita erro de digitação, não confirma que a pessoa existe.

A matrícula viaja até o Apps Script e **nunca é gravada**. O script a
transforma numa marca embaralhada, usando o `SEGREDO` que está no topo do
`Codigo.gs`, e guarda só essa marca. A mesma matrícula gera sempre a mesma
marca, e a marca não volta a ser matrícula.

Com isso:

- a mesma matrícula responde no máximo `limite` temas por semestre, três por
  padrão, e trocar de aparelho não zera a cota;
- o painel mostra quantos estudantes distintos responderam, contando marcas
  diferentes, sem saber nenhuma delas;
- dá pra conferir uma matrícula específica rodando a função `conferir()` no
  editor do Apps Script.

Antes de publicar, **troque o `SEGREDO`** por uma frase comprida qualquer, e
nunca mais mude. Se mudar depois, as marcas antigas param de bater com as
novas e a cota reinicia pra todo mundo.

Trocar de semestre é mudar o campo `semestre` no `index.html`. A cota zera e
a contagem recomeça, sem apagar nada do que já foi respondido.

A denúncia e o "quero ajudar" são enviados **sem matrícula e sem código**. O
primeiro porque precisa ser anônimo de verdade. O segundo porque pode levar
contato, e contato mais identificador ligaria as respostas do placar a uma
pessoa com nome.

## O que nunca aparece no placar

Os relatos sensíveis vão para a segunda planilha e a função que alimenta o
painel não abre esse arquivo. O placar não tem como mostrá-los.
