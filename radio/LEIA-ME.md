# Rádio e revista — proposta interna

`DEA-Radio-e-Revista-Agora.pdf` — 8 páginas, A4. Refeito na mesma linguagem dos
cartazes: paleta do DEA, **Poppins** pesada em caixa-baixa, formas cortadas em
diagonal, faixa sangrando no rodapé de cada página e a logo da Ágora no lockup.

| Página | O que tem |
|---|---|
| 01 | Capa, com índice e o QR do Mural |
| 02 | Ponto de partida — o Mural já está no ar, e o que ele não resolve |
| 03 | Histórico — já morreu antes, e o que mudou |
| 04 | A rádio — formato, episódio zero, o caminho em 4 passos |
| 05 | Pauta — cinco episódios já com assunto, e o perfil dos convidados |
| 06 | A revista — o que entra, e por que PDF em vez de gráfica |
| 07 | Custo — R$ 0, e onde pode aparecer dinheiro depois (SIATEX) |
| 08 | Calendário — datas que já existem, de outubro a novembro |

## O conteúdo é o mesmo

O texto veio do documento anterior, que já tinha passado por duas revisões suas.
Só uma correção de tempo verbal: a Congregação de 4 de setembro **já aconteceu**,
então "vai pedir à PROGRAD" virou "decidiu pedir".

## As logos

- **Ágora** — servida por `logo.py` em qualquer cor, a partir de `logo-mask.png`.
- **DEA** — recortada do fundo branco do PDF final dos cartazes, por `parceiros.py`.
  O original está em `dea-logo-origem.jpeg`.
- **DCE** — não entrou. No seu PDF ela está em vetor e não sai limpa na extração.
  **Posicione no Canva**, como você fez nos cartazes: o lugar natural é ao lado da
  logo do DEA, no fecho da página 8 e na assinatura da capa.

## Editar

`gera-radio.py` monta o HTML. Cada página é uma chamada de `pagina()`, e os blocos
de conteúdo são funções (`numeros`, `duas`, `passos`, `lista`, `caixa`, `tempo`).
Para mexer em texto, é só editar a chamada — o layout se refaz sozinho.

Depois de gerar, confira o transbordo: `node verify-rd.js` acusa qualquer página
cujo conteúdo passe de A4.
