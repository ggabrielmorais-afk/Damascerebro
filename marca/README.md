# Marca da gestão Ágora

## A logo

`oficial/` — é esta. Quatro cantos cheios, o vão no meio de cada lado, textura de
linóleo. Gerada no Flow pelo Gabriel, recortada do fundo branco e servida em cinco
cores, três tamanhos cada, sempre **PNG com transparência**.

| Cor | Onde usar |
|---|---|
| `agora-tinta` `#14171A` | fundo claro, amarelo, papel |
| `agora-branca` `#FFFFFF` | **todo fundo escuro** |
| `agora-amarela` `#F4EA4D` | fundo tinta |
| `agora-azul` `#1B6CA8` | fundo papel, quando o azul é a cor da peça |
| `agora-vermelha` `#D53C2C` | fundo papel ou amarelo |

Tamanhos: `1024` (sem sufixo), `-512`, `-128`. Para impressão use o de 1024.

`agora-mascara.png` é o recorte em preto e branco. É dele que sai qualquer cor
nova: `cartazes/logo.py` carrega essa máscara e pinta o canal alfa na hora, então
não é preciso guardar um arquivo por cor.

```python
import logo
logo.b64('#1B6CA8')          # data URI, pronto pra <img src>
logo.tag('#F4EA4D', 'mk')    # <img class="mk" src="...">
```

## As três regras

1. **Em fundo escuro, a logo é branca inteira.** Nunca colorida — uma parte
   colorida some no escuro. Isso já quebrou uma peça antes.
2. **O vão fica no meio dos lados, não nos cantos.** É o que faz ela ler como
   praça. Não preencher, não fechar, não arredondar.
3. **Mínimo de 1 cm.** Abaixo disso a textura de linóleo empasta e vira borrão.

## A paleta

Amarelo `#F4EA4D` · Azul `#469DE2` · Vermelho `#D53C2C` · Azul profundo `#1B6CA8`
· Tinta `#14171A` · Papel `#FBFAF7`

Tipografia: **Poppins** 900/700/500 e **Anton** no display, **Inter** no texto
corrido das peças mais sóbrias.

## rascunhos/

Versões que eu desenhei antes de existir a logo do Flow: o quadrado de cantos
abertos em vetor, a versão em linóleo e os prompts que geraram a definitiva.
**Não são a marca.** Ficam só como registro do caminho.
