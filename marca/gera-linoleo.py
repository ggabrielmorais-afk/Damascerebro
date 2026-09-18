# -*- coding: utf-8 -*-
"""Marca da Agora em linoleo: o mesmo quadrado de cantos abertos, mas talhado.
Fundo transparente de verdade — os furos sao subcaminhos com fill-rule evenodd,
nao mancha branca por cima. Semente fixa: a marca sai identica toda vez."""
import math, random

L, E, G = 100.0, 18.0, 16.0     # lado, espessura, folga do canto
INK, BRANCO = '#14171A', '#FFFFFF'

def talhado(r, x, y, w, h, tremor=.42, chance=.06, lasca=(.9, 1.9), passo=2.0):
    """Contorno de um retangulo como se tivesse sido cortado a goiva: quase reto,
    com tremido pequeno e, de vez em quando, uma lasca maior."""
    p = []
    def lado(x0, y0, x1, y1):
        d = math.hypot(x1-x0, y1-y0)
        n = max(2, int(d/passo))
        nx, ny = -(y1-y0)/d, (x1-x0)/d
        for i in range(n+1):
            t = i/n
            if i in (0, n):
                j = r.uniform(-.28, .28)
            elif r.random() < chance:
                j = r.uniform(*lasca) * r.choice((-1, 1))
            else:
                j = r.uniform(-tremor, tremor)
            p.append((x0+(x1-x0)*t + nx*j, y0+(y1-y0)*t + ny*j))
    lado(x, y, x+w, y); lado(x+w, y, x+w, y+h)
    lado(x+w, y+h, x, y+h); lado(x, y+h, x, y)
    return 'M' + ' L'.join(f'{a:.2f},{b:.2f}' for a, b in p) + ' Z'

def furo(r, cx, cy, raio):
    """Falha de tinta: poligono irregular que vira buraco pelo evenodd."""
    n = r.randint(5, 7)
    p = []
    for i in range(n):
        a = 2*math.pi*i/n + r.uniform(-.25, .25)
        d = raio * r.uniform(.55, 1.25)
        p.append((cx + d*math.cos(a), cy + d*math.sin(a)))
    return 'M' + ' L'.join(f'{a:.2f},{b:.2f}' for a, b in p) + ' Z'

def barra(r, x, y, w, h, n_furos=3):
    d = [talhado(r, x, y, w, h)]
    for _ in range(n_furos):
        cx = r.uniform(x + w*.16, x + w*.84)
        cy = r.uniform(y + h*.16, y + h*.84)
        d.append(furo(r, cx, cy, r.uniform(.35, 1.0)))
    return ' '.join(d)

def respingo(r, cx, cy, raio):
    return furo(r, cx, cy, raio)

def marca(cor, semente=7):
    r = random.Random(semente)
    barras = [
        barra(r, G/2, 0,       L-G, E),          # topo
        barra(r, L-E, G/2,     E,   L-G),        # direita
        barra(r, G/2, L-E,     L-G, E),          # base
        barra(r, 0,   G/2,     E,   L-G),        # esquerda
    ]
    # respingos de tinta soltos, do lado de fora
    fora = []
    for cx, cy, raio in ((L*.52, -3.0, .75), (L+2.6, L*.36, .6), (-2.8, L*.66, .7),
                         (L*.28, L+2.8, .8), (L*.88, L+2.3, .5)):
        fora.append(respingo(r, cx, cy, raio))
    d = ' '.join(barras + fora)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-6 -6 112 112">\n'
            f'  <path fill-rule="evenodd" d="{d}" fill="{cor}"/>\n</svg>\n')

open('marca-linoleo.svg', 'w', encoding='utf-8').write(marca(INK))
open('marca-linoleo-branca.svg', 'w', encoding='utf-8').write(marca(BRANCO))
print('svg tinta e branca gerados')
