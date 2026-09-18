# Cartazes do Mural — gestão Ágora

São **três famílias** de cartazes, com a mesma mensagem e três direções de arte.
Imprima a que o pessoal do DEA escolher — ou as três, em murais diferentes.

## Para mandar inteiro: `Mural-Cartazes-Agora-DEA.pdf`

Um PDF só, 10 páginas: **uma capa** que explica o Mural e as três direções, mais os
nove cartazes. É este que vai para quem ainda não viu nada — não precisa de contexto
por fora. Fonte: `cartazes-todos.html`, montado por `junta.py`.

> `junta.py` escopa o CSS de cada família por uma classe (`.fam-q`, `.fam-x`, `.fam-c`)
> antes de juntar tudo. As três usam os mesmos nomes de classe (`.pg`, `h1`, `.etq`,
> `.qr`), então sem isso uma atropela a outra.

## A marca

Os nove cartazes usam a **marca em linóleo** (`marca/marca-linoleo.svg`) — o quadrado
de cantos abertos, talhado. Nos cartazes de colagem ela aparece carimbada e torta, no
canto de cima da folha.

---

## Família 1 — quadrados (`Agora-Cartazes-A4.pdf`)

Três cartazes **A4** (210 × 297 mm), para imprimir em papel comum e colar nos
murais da FAUFBA. Todos levam o QR do Mural: `mural-faufba.netlify.app`.

| # | Fundo | Chamada | Serve para |
|---|-------|---------|-----------|
| 1 | Azul `#1B6CA8` | Fale. Todo mundo vai ler. | O placar público — o que você marca vira número no mesmo dia |
| 2 | Amarelo `#F4EA4D` | Fale. Só quem precisa vai ler. | O canal sigiloso — nunca aparece no placar |
| 3 | Vermelho `#D53C2C` | 40 segundos. Três temas. Um semestre. | A regra de uso e os oito temas |

---

## Família 2 — xerox (`Agora-Cartazes-A4-Xerox.pdf`)

Na gramática das artes do **DCE/UFBA**: duas cores chapadas, formas cortadas em
diagonal, caixa-baixa pesada e empilhada, linha institucional espaçada. Feita para
sobreviver à fotocópia — não tem meio-tom nenhum, então sai igual no xerox da esquina.

| # | Fundo | Chamada |
|---|-------|---------|
| 1 | Amarelo `#F4EA4D` | fale. todo mundo vai ler. |
| 2 | Tinta `#14171A` | fale. só quem precisa vai ler. |
| 3 | Vermelho `#D53C2C` | 40 segundos. três temas. um semestre. |

Tipografia: **Poppins** 900 e 700, tudo em caixa-baixa no display.
Fonte editável: `cartazes-xerox.html`.

**A regra do corte:** o corte vive nas **formas** — o símbolo, a etiqueta, a faixa,
a caixa do QR. O texto corrido fica limpo. É assim na referência: as letras de "DCE"
são recortadas, mas "diretório central dos estudantes" não é. Cortar o texto do
cartaz destrói a leitura e não é o estilo.

---

## Família 3 — colagem (`Agora-Cartazes-A4-Colagem.pdf`)

A direção dos modelos escolhidos no Canva: fundo chapado lilás ou rosa, uma folha
de papel **rasgada e torta** por cima, estrelas do movimento estudantil espalhadas,
fitas crepe segurando o papel, etiquetas chapadas e um recorte em silhueta no topo.

| # | Fundo | Folha | Recorte | Chamada |
|---|-------|-------|---------|---------|
| 1 | Lilás `#A294DA` | Kraft | Megafone | Fale na Ágora. Todo mundo vai ler. |
| 2 | Rosa `#E33C82` | Kraft | Cadeado | Fale. Só quem precisa vai ler. |
| 3 | Creme `#F1EADC` | Lilás | Fachada | 40 segundos. Três temas. Um semestre. |

Tipografia: **Anton** no título, **Inter** no corpo. Fonte editável: `cartazes-colagem.html`.

### As bordas rasgadas são geradas, não desenhadas

Cada folha tem a borda irregular gerada por código, com semente fixa — o mesmo
cartaz sai idêntico toda vez. Para variar o rasgo, troque o número da semente em
`gera-colagem.py` (`semente=3`, `11`, `23`).

### Se quiser trocar os recortes por foto de verdade

Os três recortes são silhuetas em SVG, não foto. Funcionam impressos, mas a
referência usa **foto recortada em preto e branco de alto contraste**. Se você
gerar as imagens no Flow, é só soltar no lugar do desenho, no Canva. Prompts:

1. **Megafone** — `black and white high contrast halftone photograph of a hand
   holding a vintage megaphone, cut out on pure white background, 1970s protest
   poster collage element, heavy grain, no text`
2. **Cadeado / sigilo** — `black and white high contrast halftone photograph of a
   closed brass padlock on a folded paper envelope, cut out on pure white
   background, xerox texture, protest zine collage element, no text`
3. **Fachada da FAUFBA** — `black and white high contrast halftone photograph of a
   neoclassical university building facade with columns and a pediment, small
   crowd of student silhouettes on the steps, cut out on pure white background,
   1970s Brazilian student movement poster collage, heavy grain, no text`

Peça em formato quadrado ou 4:3, fundo branco liso, e recorte no Canva com
*Editar imagem → Remover fundo* se vier com fundo.

---

## Como imprimir

1. Abra o PDF da família escolhida.
2. Imprima em A4, **escala 100%** (nada de "ajustar à página" — isso encolhe a
   margem e corta o fio de cor no topo).
3. Marque **imprimir cor de fundo / gráficos de fundo**, senão os cartazes saem
   brancos.

Se precisar de A3, imprima o mesmo PDF em A3 com ampliação de 141%.

## Como editar

`cartazes-agora.html` é a fonte. As fontes (Anton e Inter) estão embutidas em
base64, então o arquivo abre igual em qualquer máquina, sem internet. Para gerar
o PDF de novo, abra no navegador e imprima em PDF com A4 e margens zeradas.

## Regras da marca

- O quadrado aberto (com os quatro cantos vazados) é a ágora: praça aberta.
- No cartaz 2 o quadrado aparece **fechado**. É proposital: ali o canal é selado.
- Em fundo escuro a marca é sempre branca inteira, nunca colorida.
- O fio de três cores no topo nunca repete a cor do fundo do cartaz.
