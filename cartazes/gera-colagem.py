# -*- coding: utf-8 -*-
"""Cartazes do Mural, familia 'colagem' — retoma a direcao dos modelos que o
Gabriel escolheu: fundo chapado lilas/rosa, folha de papel rasgada e torta por
cima, estrelas de movimento estudantil, fitas crepe, etiquetas chapadas e
recortes em silhueta. Sem foto: os recortes sao desenhados em SVG, e ele pode
trocar por foto de verdade depois (os prompts estao no LEIA-ME)."""
import math, random, importlib.util

import sys; sys.path.insert(0, '.')
import logo as _logo

FONTES = open('fontes-anton-inter.css', encoding='utf-8').read()
QR = open('qr.txt', encoding='utf-8').read()

LILAS   = '#A294DA'
ROSA    = '#E33C82'
CORAL   = '#E8604C'
KRAFT   = '#D9C39B'
CREME   = '#F1EADC'
PAPEL   = '#FBF7EF'
ROXO    = '#4B2F86'
INK     = '#14171A'
AMARELO = '#F4EA4D'

def mistura(frente, fundo, a):
    f = [int(frente[i:i+2],16) for i in (1,3,5)]
    b = [int(fundo[i:i+2],16) for i in (1,3,5)]
    return '#%02X%02X%02X' % tuple(round(f[i]*a + b[i]*(1-a)) for i in range(3))

# ── papel rasgado ──────────────────────────────────────────────────────────
def rasgado(semente, w=100, h=140, dente=1.6, passo=5):
    """Retangulo com as quatro bordas irregulares, como papel rasgado a mao.
    Semente fixa: o mesmo cartaz sai igual toda vez que eu gero."""
    r = random.Random(semente)
    p = []
    def borda(x0, y0, x1, y1):
        d = math.hypot(x1-x0, y1-y0)
        n = max(3, int(d/passo))
        nx, ny = -(y1-y0)/d, (x1-x0)/d      # normal da borda
        for i in range(n+1):
            t = i/n
            j = 0 if i in (0, n) else r.uniform(-dente, dente)
            p.append((x0+(x1-x0)*t + nx*j, y0+(y1-y0)*t + ny*j))
    borda(0, 0, w, 0); borda(w, 0, w, h); borda(w, h, 0, h); borda(0, h, 0, 0)
    return 'M' + ' L'.join(f'{x:.2f},{y:.2f}' for x, y in p) + ' Z'

def folha(semente, cor, w=100, h=140, sombra=None):
    extra = (f'<path d="{rasgado(semente+99, w, h)}" fill="{sombra}" '
             f'transform="translate(1.4,1.8)"/>') if sombra else ''
    return (f'<svg viewBox="-3 -3 {w+6} {h+6}" preserveAspectRatio="none" class="fl">'
            f'{extra}<path d="{rasgado(semente, w, h)}" fill="{cor}"/></svg>')

# ── estrela do movimento estudantil ────────────────────────────────────────
def estrela(cor, giro=0):
    pts = []
    for i in range(10):
        a = math.pi/2 + i*math.pi/5
        raio = 50 if i % 2 == 0 else 20
        pts.append(f'{50+raio*math.cos(a):.1f},{50-raio*math.sin(a):.1f}')
    return (f'<svg viewBox="0 0 100 100" style="transform:rotate({giro}deg)">'
            f'<polygon points="{" ".join(pts)}" fill="{cor}"/></svg>')

# ── recortes em silhueta (lugar das fotos) ─────────────────────────────────
MEGAFONE = '''<svg viewBox="0 0 120 100">
 <path d="M52 28 L104 6 L104 94 L52 72 Z" fill="{c}"/>
 <rect x="30" y="34" width="24" height="32" rx="3" fill="{c}"/>
 <path d="M30 40 L14 44 L14 56 L30 60 Z" fill="{c}"/>
 <rect x="8" y="52" width="16" height="30" rx="7" fill="{c}"
  transform="rotate(-24 16 67)"/>
 <path d="M108 30 a26 26 0 0 1 0 40" stroke="{c}" stroke-width="5" fill="none"/>
 <path d="M114 18 a40 40 0 0 1 0 64" stroke="{c}" stroke-width="5" fill="none"/>
</svg>'''

CADEADO = '''<svg viewBox="0 0 120 100">
 <path d="M38 46 L38 32 a22 22 0 0 1 44 0 L82 46" stroke="{c}" stroke-width="11"
  fill="none" stroke-linecap="square"/>
 <rect x="24" y="44" width="72" height="52" rx="5" fill="{c}"/>
 <circle cx="60" cy="64" r="7" fill="{f}"/>
 <rect x="56.5" y="66" width="7" height="16" fill="{f}"/>
</svg>'''

FACHADA = '''<svg viewBox="0 0 120 100">
 <path d="M60 6 L112 30 L8 30 Z" fill="{c}"/>
 <rect x="8" y="33" width="104" height="5" fill="{c}"/>
 <g fill="{c}">
  <rect x="16" y="40" width="10" height="38"/><rect x="36" y="40" width="10" height="38"/>
  <rect x="55" y="40" width="10" height="38"/><rect x="74" y="40" width="10" height="38"/>
  <rect x="94" y="40" width="10" height="38"/>
 </g>
 <rect x="4" y="80" width="112" height="6" fill="{c}"/>
 <rect x="0" y="88" width="120" height="6" fill="{c}"/>
 <g fill="{c}">
  <circle cx="22" cy="92" r="4"/><circle cx="40" cy="93" r="4.5"/>
  <circle cx="58" cy="92" r="4"/><circle cx="76" cy="93" r="4.5"/><circle cx="96" cy="92" r="4"/>
 </g>
</svg>'''

def recorte(desenho, cor, fundo=PAPEL):
    return desenho.format(c=cor, f=fundo)

# ── cartaz ─────────────────────────────────────────────────────────────────
def cartaz(rotulo, fundo, cor_folha, cor_tit, etq_cor, etq_tx, desenho,
           titulo, corpo, mini, estrelas, rodape_cor=PAPEL, semente=1, cor_estrela=None,
           cor_carimbo=INK):
    cor_estrela = cor_estrela or CORAL
    sombra = mistura('#000000', fundo, .16)
    est = ''.join(
        f'<div class="est" style="left:{x}mm;top:{y}mm;width:{s}mm;height:{s}mm">'
        f'{estrela(cor_estrela, g)}</div>' for x, y, s, g in estrelas)
    return f'''<section class="pg" data-document-role="page" data-label="{rotulo}"
 style="background:{fundo}">
 {est}
 <div class="folha">{folha(semente, cor_folha, sombra=sombra)}</div>
 <div class="fita" style="left:22mm;top:36mm;transform:rotate(-38deg)"></div>
 <div class="fita" style="left:150mm;top:38mm;transform:rotate(36deg)"></div>
 <div class="fita" style="left:24mm;top:244mm;transform:rotate(34deg)"></div>
 <div class="carimbo">{_logo.tag(cor_carimbo, 'carimbo-img')}</div>
 <div class="miolo">
   <div class="rec">
     <div class="rec-fl">{folha(semente+7, PAPEL, 100, 74)}</div>
     <div class="rec-dw">{recorte(desenho, INK, PAPEL)}</div>
   </div>
   <div class="etq" style="background:{etq_cor}">{etq_tx}</div>
   <h1 style="color:{cor_tit}">{titulo}</h1>
   <p class="corpo">{corpo}</p>
   <div class="qr-box">
     <div class="qr"><img src="{QR}" alt="QR do Mural"></div>
     <p class="mini">{mini}</p>
   </div>
 </div>
 <div class="ass" style="background:{CORAL}">gestão ágora<br><b>DEA FAUFBA</b></div>
 <div class="url" style="color:{rodape_cor}">mural-faufba.netlify.app</div>
</section>'''

c1 = cartaz(
    'Colagem 1 — placar público', LILAS, KRAFT, ROXO, CORAL, 'o que trava você na faufba',
    MEGAFONE,
    'Fale na Ágora.<br>Todo mundo<br>vai ler.',
    'O que você marcar vira número público no mesmo dia. É assim que a Faculdade '
    'para de ouvir “uns alunos reclamaram” e passa a ver quantos são.',
    'Sem login. Sem nome.<br>Só a matrícula, que<br>não fica guardada.',
    [(12, 60, 13, -8), (176, 22, 16, 12), (188, 150, 11, -14), (8, 196, 15, 6),
     (166, 262, 13, 18), (30, 268, 10, -10)], PAPEL, 3)

c2 = cartaz(
    'Colagem 2 — canal sigiloso', ROSA, KRAFT, ROXO, ROXO, 'sigiloso',
    CADEADO,
    'Fale.<br>Só quem precisa<br>vai ler.',
    'Canal sigiloso dentro do Mural. Seu relato não aparece no placar em hipótese '
    'nenhuma, e você escolhe se quer ser contatado.',
    'Sem nome, sem matrícula.<br>Ouvidoria da UFBA<br>180 · 100 · 188 CVV',
    [(14, 30, 15, -12), (180, 64, 12, 16), (6, 142, 11, 8), (184, 214, 15, -6),
     (26, 262, 12, 14), (150, 268, 10, -16)], AMARELO, 11, CREME)

c3 = cartaz(
    'Colagem 3 — 40 segundos', CREME, LILAS, INK, CORAL, 'semestre 2026.2',
    FACHADA,
    '40 segundos.<br>Três temas.<br>Um semestre.',
    'Cada matrícula responde três temas no semestre. Escolha os que mais te travam: '
    'oferta, SIGAA, currículo, laboratório, horário, prédio, didática, Matriz T.',
    'Depois dos três, o Mural<br>agradece e fecha. Vale<br>por todo o semestre.',
    [(10, 40, 14, 10), (182, 36, 12, -14), (188, 178, 14, 8), (8, 210, 11, -8),
     (32, 270, 13, 16), (160, 266, 11, -12)], ROXO, 23, ROSA, PAPEL)

CSS = f'''
@page{{size:A4;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page}}
.pg:last-child{{break-after:auto}}

.est{{position:absolute;z-index:1}}
.est svg{{width:100%;height:100%;display:block}}

.folha{{position:absolute;left:19mm;top:29mm;width:172mm;height:224mm;z-index:2;
 transform:rotate(-1.1deg)}}
.fl{{width:100%;height:100%;display:block}}

/* fita crepe segurando a folha */
.fita{{position:absolute;width:32mm;height:9.5mm;background:#C9B48C;z-index:4}}

.miolo{{position:absolute;left:28mm;top:38mm;width:154mm;height:207mm;z-index:5;
 transform:rotate(-1.1deg);display:flex;flex-direction:column;align-items:center;
 text-align:center;padding:4mm 6mm}}

.rec{{position:relative;width:86mm;height:64mm;flex:none;margin-bottom:6mm}}
.rec-fl{{position:absolute;inset:0}}
.rec-dw{{position:absolute;left:9mm;top:7mm;right:9mm;bottom:7mm}}
.rec-dw svg{{width:100%;height:100%;display:block}}

.etq{{color:{PAPEL};font-weight:800;font-size:10pt;letter-spacing:.14em;
 text-transform:uppercase;padding:2.4mm 6mm;transform:rotate(.8deg);flex:none}}

h1{{font-family:'Anton',sans-serif;font-weight:400;font-size:46pt;line-height:.95;
 letter-spacing:.005em;margin-top:6mm;flex:none}}

.corpo{{font-size:11.5pt;line-height:1.45;color:{INK};margin-top:6mm;max-width:124mm;
 font-weight:500}}

.qr-box{{margin-top:auto;display:flex;align-items:center;gap:6mm;text-align:left}}
.qr{{background:{PAPEL};padding:3mm;width:40mm;flex:none;transform:rotate(1.4deg)}}
.qr img{{width:100%;display:block;image-rendering:pixelated}}
.mini{{font-size:9.5pt;line-height:1.42;color:{INK};font-weight:600}}

.carimbo{{position:absolute;right:26mm;top:44mm;width:20mm;height:20mm;z-index:6;
 transform:rotate(7deg)}}
.carimbo img{{width:100%;height:100%;display:block;object-fit:contain}}
.ass{{position:absolute;left:14mm;bottom:20mm;z-index:6;color:{PAPEL};
 font-weight:800;font-size:11pt;line-height:1.25;letter-spacing:.1em;
 text-transform:uppercase;padding:3.5mm 6mm;transform:rotate(-3.5deg)}}
.ass b{{font-weight:800;letter-spacing:.16em}}

.url{{position:absolute;right:14mm;bottom:11mm;z-index:6;font-weight:800;
 font-size:10.5pt;letter-spacing:.08em}}
'''

html = ('<title>Cartazes Mural — colagem — Gestão Ágora</title>\n'
        '<style>' + FONTES + '</style>\n'
        '<style>' + CSS + '</style>\n' + c1 + '\n' + c2 + '\n' + c3 + '\n')
open('cartazes-colagem.html', 'w', encoding='utf-8').write(html)
print('cartazes-colagem.html escrito')
