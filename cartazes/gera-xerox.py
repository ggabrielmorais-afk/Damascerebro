# -*- coding: utf-8 -*-
"""Cartazes do Mural, familia 'xerox' — a gramatica das artes do DCE/UFBA:
duas cores chapadas, formas cortadas em diagonal, caixa-baixa pesada e
empilhada, linha institucional espacada. Feito para sobreviver a fotocopia.

Regra de estilo tirada da referencia: o corte vive nas FORMAS (o simbolo, a
etiqueta, a faixa, a caixa do QR). O texto corrido fica limpo — no logo do DCE
as letras de 'DCE' sao recortadas, mas 'diretorio central dos estudantes' nao."""

import importlib.util

import sys; sys.path.insert(0, '.')
import logo as _logo

FONTES = open('fontes-poppins.css', encoding='utf-8').read()
QR = open('qr.txt', encoding='utf-8').read()

AMARELO='#F4EA4D'; INK='#14171A'; VERMELHO='#D53C2C'; PAPEL='#FBFAF7'

def mistura(frente, fundo, a):
    """Transparencia embutida na cor. O importador do Canva descarta opacity,
    entao a cor ja nasce misturada com o fundo do cartaz."""
    f = [int(frente[i:i+2],16) for i in (1,3,5)]
    b = [int(fundo[i:i+2],16) for i in (1,3,5)]
    return '#%02X%02X%02X' % tuple(round(f[i]*a + b[i]*(1-a)) for i in range(3))

def marca(cor, fundo):
    """A logo da Agora, pintada na cor do cartaz. O fundo nao e usado: o PNG
    ja vem com transparencia."""
    return _logo.tag(cor)

def lockup(cor, fundo):
    return f'''<div class="lock">
  <div class="lock-top">
    {marca(cor, fundo)}
    <div class="lock-tx" style="color:{cor}">
      <b>ágora</b><b>gestão<span>2026</span></b><b>mural</b>
    </div>
  </div>
  <div class="lock-pe" style="color:{cor};border-top:1.1mm solid {cor}">
    <i>D E A</i><span>diretório dos estudantes de arquitetura · ufba</span>
  </div>
</div>'''

def cartaz(fundo, cor, caixa_qr, etq, titulo, sub, mini, faixa, rotulo, extra=''):
    fraca = mistura(cor, fundo, .82)
    separador = mistura(cor, fundo, .45)
    return f'''<section class="pg" data-document-role="page" data-label="{rotulo}"
 style="background:{fundo};color:{cor}">
 <div class="grande">{marca(cor, fundo)}</div>
 {lockup(cor, fundo)}
 <div class="etq" style="background:{cor};color:{fundo}">{etq}</div>
 <div class="ar" style="flex:1"></div>
 <h1 style="color:{cor}">{titulo}</h1>
 <p class="sub" style="color:{cor}">{sub}</p>
 <p class="mini" style="color:{fraca}">{mini}</p>
 {extra}
 <div class="ar" style="flex:1.45"></div>
 <div class="faixa" style="background:{cor};color:{fundo}">{faixa}</div>
 <div class="rod">
   <div class="url" style="color:{cor}">mural<i style="color:{separador}">-</i>faufba<i style="color:{separador}">.</i>netlify<i style="color:{separador}">.</i>app</div>
   <div class="qr" style="background:{caixa_qr}">
     <img src="{QR}" alt="QR do Mural"><span style="color:{INK}">aponte a câmera</span>
   </div>
 </div>
</section>'''

c1 = cartaz(
    AMARELO, INK, PAPEL,
    'o que trava você na faufba',
    'fale.<br>todo mundo<br>vai ler.',
    'O que você marcar vira número público no mesmo dia. É assim que a Faculdade '
    'para de ouvir “uns alunos reclamaram” e passa a ver quantos são.',
    'Sem login. Sem nome. Só a matrícula, que não fica guardada.',
    'você é parte da FAU, você é parte dessa história',
    'Xerox 1 — placar público')

c2 = cartaz(
    INK, AMARELO, AMARELO,
    'assédio · discriminação · abuso de poder',
    'fale.<br>só quem precisa<br>vai ler.',
    'Canal sigiloso dentro do Mural. Não aparece no placar em hipótese nenhuma.',
    'Você escolhe se quer ser contatado. Sem nome, sem matrícula.<br>'
    'Canais oficiais: Ouvidoria da UFBA · 180 · 100 · 188 CVV',
    'seu sigilo é garantido, e sua denúncia também',
    'Xerox 2 — canal sigiloso')

temas = (f'<p class="temas" style="color:{mistura(PAPEL, VERMELHO, .82)}">Oferta de disciplina · Matrícula e SIGAA · '
         'Currículo e pré-requisitos · Laboratório e equipamento · Horário e transporte · '
         'Sala e prédio · Didática e aula · Matriz T e concluintes</p>')

c3 = cartaz(
    VERMELHO, PAPEL, PAPEL,
    'semestre 2026.2',
    '40 segundos.<br>três temas.<br>um semestre.',
    'Cada matrícula responde três temas no semestre. Escolha os que mais te travam.',
    'Depois dos três, o Mural agradece e fecha. Vale por todo o semestre.',
    '40 segundos seus mudam toda a FAUFBA',
    'Xerox 3 — 40 segundos', temas)

CSS = f'''
@page{{size:A4;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Poppins',system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;
 padding:13mm 13mm 11mm;display:flex;flex-direction:column}}
.pg:last-child{{break-after:auto}}

.lock{{flex:none;position:relative;z-index:1}}
.etq,.ar{{flex:none}}
/* o simbolo em tamanho de cartaz, sangrando pela direita */
.grande{{position:absolute;right:-18mm;bottom:72mm;width:62mm;height:62mm;z-index:0}}
.grande .mk{{width:100%;height:100%;display:block;object-fit:contain}}
.lock-top{{display:flex;align-items:flex-start;gap:5mm}}
.lock .mk{{width:25mm;height:25mm;flex:none;display:block;object-fit:contain}}
.lock-tx b{{display:block;font-weight:900;font-size:18.5pt;line-height:.87;
 letter-spacing:-.025em;text-transform:lowercase}}
.lock-tx b span{{font-weight:700;margin-left:.07em}}
.lock-pe{{display:flex;align-items:baseline;gap:4mm;margin-top:2.4mm;padding-top:1.7mm}}
.lock-pe i{{font-style:normal;font-weight:900;font-size:9.5pt;letter-spacing:.4em}}
.lock-pe span{{font-weight:700;font-size:7.4pt}}

/* etiqueta com canto cortado — o corte vive nas formas */
.etq{{align-self:flex-start;position:relative;z-index:1;margin-top:8mm;font-weight:900;font-size:9.5pt;
 letter-spacing:.02em;padding:2.4mm 6mm 2.4mm 4mm;text-transform:lowercase;
 clip-path:polygon(0 0,100% 0,100% 58%,90% 100%,0 100%)}}

h1{{position:relative;z-index:1;font-weight:900;font-size:64pt;line-height:.85;
 letter-spacing:-.04em;text-transform:lowercase}}

.sub{{position:relative;z-index:1;font-weight:700;font-size:12pt;line-height:1.34;
 margin-top:7mm;max-width:158mm}}
.mini{{position:relative;z-index:1;font-weight:500;font-size:9.5pt;line-height:1.45;
 margin-top:4mm;max-width:150mm}}
.temas{{position:relative;z-index:1;font-weight:500;font-size:9pt;line-height:1.5;
 margin-top:4mm;max-width:150mm}}

/* faixa chapada com a ponta cortada, sangrando nas laterais */
.faixa{{position:relative;z-index:2;margin:0 -13mm;padding:6mm 13mm 6.5mm;font-weight:900;font-size:22pt;
 line-height:1;letter-spacing:-.03em;text-transform:lowercase;
 clip-path:polygon(0 0,86% 0,100% 34%,100% 100%,0 100%)}}

.rod{{display:flex;align-items:flex-end;justify-content:space-between;gap:8mm;margin-top:7mm}}
.url{{font-weight:900;font-size:15pt;letter-spacing:-.015em;line-height:1.1;max-width:105mm}}
.url i{{font-style:normal}}
.qr{{flex:none;width:38mm;padding:3.2mm;clip-path:polygon(0 0,100% 0,100% 80%,86% 100%,0 100%)}}
.qr img{{width:100%;display:block;image-rendering:pixelated}}
.qr span{{display:block;text-align:center;margin-top:2mm;font-weight:900;
 font-size:6.8pt;letter-spacing:.08em}}
'''

html = ('<title>Cartazes Mural — estilo xerox — Gestão Ágora</title>\n'
        '<style>' + FONTES + '</style>\n'
        '<style>' + CSS + '</style>\n' + c1 + '\n' + c2 + '\n' + c3 + '\n')
open('cartazes-xerox.html', 'w', encoding='utf-8').write(html)
print('escrito')
