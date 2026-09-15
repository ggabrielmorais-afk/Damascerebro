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
6. Copiar o endereço terminado em `/exec` e colar na primeira linha de
   `index.html`, entre as aspas de `endpoint`.

Sem esse endereço o app roda em modo demonstração: nada sai do navegador e a
etiqueta no topo diz "demonstração". Com o endereço, a etiqueta muda para
"no ar" e os números começam do zero, porque passam a ser reais.

## Hospedar

Arrastar a pasta em `app.netlify.com/drop`. Sai um endereço público na hora.
Só então gerar os cartazes com o QR definitivo.

## O que nunca aparece no placar

Os relatos sensíveis vão para a segunda planilha e a função que alimenta o
painel não abre esse arquivo. O placar não tem como mostrá-los.
