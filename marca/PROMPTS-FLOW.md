# Prompts de Flow para a marca da Ágora

## Três regras antes de gerar

**1. Nunca peça o nome escrito.** Todo gerador erra letra com acento — "ÁGORA" vai
sair "AGÔRA", "ÁGRORA" ou pior. Gere **só o símbolo** e coloque o nome no Canva
depois, em Anton ou Poppins 900. Todo prompt aqui termina com `no text, no letters`.

**2. Gere em preto no branco.** Pedir cor específica faz o gerador inventar
gradiente e sombra. Preto chapado em fundo branco sai limpo, e você recolore no
Canva para a paleta do DEA: amarelo `#F4EA4D`, azul `#469DE2`, vermelho `#D53C2C`,
azul profundo `#1B6CA8`, tinta `#14171A`.

**3. O teste é imprimir a 1 cm.** Marca de gestão vive pequena: no rodapé do
cartaz, no canto do story, no carimbo. Se some a 1 cm, não serve — por mais
bonita que esteja na tela.

---

## Direção A — a praça

A ágora é a praça de assembleia. Símbolo: um quadrado que não fecha.

**A1**
```
flat vector logo icon, a bold geometric square outline made of four thick
separate bars that do not touch at the corners, open gaps at each corner,
solid black on pure white background, uniform stroke weight, perfectly
symmetrical, centered, minimal brutalist mark, sharp edges, print ready,
no text, no letters, no gradient, no shadow, no 3d
```

**A2**
```
flat vector logo icon, top view floor plan of an open public square, a thick
black square border with four wide openings, small solid squares scattered
inside representing people gathered, solid black on pure white background,
architectural plan drawing reduced to a minimal symbol, high contrast,
no text, no letters, no gradient, no shadow
```

---

## Direção B — a arquitetura

Somos arquitetura. A marca pode carregar isso sem virar desenho de prédio.

**B1**
```
flat vector logo icon, five thick vertical bars of different heights standing
on a horizontal base line, a colonnade reduced to pure geometry, solid black
on pure white background, uniform stroke weight, minimal swiss design mark,
sharp edges, centered, no text, no letters, no gradient, no shadow, no 3d
```

**B2**
```
flat vector logo icon, a wide triangle pediment resting on four thick columns,
neoclassical facade reduced to the simplest possible geometric symbol, solid
black on pure white background, bold stencil style, high contrast, centered,
no text, no letters, no perspective, no gradient, no shadow
```

---

## Direção C — as vozes

O Mural é gente falando junto. Símbolo: falas que formam uma praça.

**C1**
```
flat vector logo icon, four thick speech bubble tails arranged in a square
formation pointing toward the empty center, solid black on pure white
background, bold geometric shapes, uniform weight, minimal mark, centered,
symmetrical, no text, no letters, no gradient, no shadow, no 3d
```

**C2**
```
flat vector logo icon, a dense grid of small solid black squares of slightly
different sizes forming one large square shape, some squares missing, like a
public notice board filled with posts, solid black on pure white background,
minimal modular mark, centered, no text, no letters, no gradient, no shadow
```

---

## Direção D — o carimbo militante

Para casar com os cartazes de colagem e xerox.

**D1**
```
black linocut woodcut print of a bold geometric open square symbol with gaps
at the corners, rough hand carved texture, visible ink bleed and imperfect
edges, stamped on white paper, 1970s Brazilian student movement print, high
contrast, no text, no letters, no gradient, no color
```

**D2**
```
rough black rubber stamp impression of a simple geometric square symbol with
open corners, uneven ink coverage, worn edges, slightly rotated, stamped on
plain white paper, protest zine aesthetic, high contrast, no text, no letters,
no gradient, no color
```

---

## Na hora de escolher, descarte se

- **Fecha o quadrado.** Ágora é praça aberta. Quadrado fechado é o contrário:
  é o cartaz do canal sigiloso, não da gestão.
- **Tem mais de um peso de traço.** Traço grosso num lado e fino no outro não
  sobrevive à redução.
- **Precisa de mais de duas cores** para ser entendida.
- **Tem letra escondida**, mesmo que borrada — o gerador insiste nisso.
- **Some ao imprimir a 1 cm.** Teste antes de decidir.

## Depois de escolher

O Flow devolve PNG com borda macia, que não serve como marca final. Duas saídas:

1. Me mande a imagem escolhida e eu redesenho como **SVG limpo**, com geometria
   exata, nas três versões (tinta, cores e branca) e nos PNGs de 512 e 128 — foi
   assim que a marca atual foi feita.
2. Ou vetorize você: Illustrator (*Image Trace → Black and White Logo*), Inkscape
   (*Traçar bitmap*) ou vectorizer.ai. Depois limpe os nós tortos à mão.

## O que já existe

A marca atual está nesta pasta: `marca-ink.svg`, `marca-cores.svg`, `marca-branca.svg`
e os PNGs. É a Direção A1 — quatro barras, cantos abertos, `L=100 E=18 G=16`.
Ela já está nos três cartazes e no Mural, então serve de base de comparação:
se o que sair do Flow não for claramente melhor que ela a 1 cm, fique com ela.

**Regra da versão negativa:** em fundo escuro a marca é sempre **branca inteira**,
nunca colorida — uma barra colorida some no escuro. Isso já quebrou uma vez.
