# -*- coding: utf-8 -*-
"""Junta as tres familias de cartaz num arquivo so, com uma capa na frente,
para mandar inteiro pra uma pessoa do DEA.

As tres familias usam os mesmos nomes de classe (.pg, h1, .etq, .qr...), entao
cada CSS e escopado por uma classe de familia antes de entrar no mesmo arquivo.
Sem isso, o CSS de uma familia atropela a outra."""
import re, importlib.util

import sys; sys.path.insert(0, '.')
import logo as _logo

QR = open('qr.txt', encoding='utf-8').read()
AMARELO='#F4EA4D'; AZUL='#1B6CA8'; AZULC='#469DE2'; VERMELHO='#D53C2C'
INK='#14171A'; PAPEL='#FBFAF7'

def partes(arq):
    s = open(arq, encoding='utf-8').read()
    blocos = re.findall(r'<style>(.*?)</style>', s, re.S)
    corpo = s[s.rindex('</style>')+len('</style>'):]
    return blocos[0], blocos[1], corpo

def escopa(css, fam):
    """Prefixa cada seletor com a classe da familia. `body` vira a propria
    pagina, para a fonte-base de cada familia nao vazar para as outras."""
    saida = []
    for bloco in css.split('}'):
        if '{' not in bloco:
            continue
        sel, decl = bloco.split('{', 1)
        limpo = re.sub(r'/\*.*?\*/', '', sel, flags=re.S).strip()
        if not limpo or limpo.startswith('@page') or limpo == '*':
            continue
        alvos = []
        for um in limpo.split(','):
            um = um.strip()
            if um == 'body':
                alvos.append(f'.{fam}.pg')
            elif um.startswith('.pg'):
                alvos.append(f'.{fam}{um}')
            else:
                alvos.append(f'.{fam} {um}')
        saida.append(','.join(alvos) + '{' + decl.strip() + '}')
    return '\n'.join(saida)

FAMILIAS = [
    ('cartazes-agora.html',   'fam-q', 'Quadrados'),
    ('cartazes-xerox.html',   'fam-x', 'Xerox'),
    ('cartazes-colagem.html', 'fam-c', 'Colagem'),
]

fontes, css_todos, secoes = [], [], []
for arq, fam, nome in FAMILIAS:
    f, c, corpo = partes(arq)
    for regra in re.findall(r'@font-face\{.*?\}', f, re.S):
        if regra not in fontes:
            fontes.append(regra)
    css_todos.append(f'/* ── {nome} ── */\n' + escopa(c, fam))
    corpo = re.sub(r'<section class="pg', f'<section class="{fam} pg', corpo)
    secoes.append(corpo.strip())

CAPA = f'''<section class="fam-capa pg" data-document-role="page" data-label="Capa">
 <div class="fio"><i></i><i></i><i></i></div>
 <div class="topo">
   <div class="mk">{_logo.tag(INK, 'logo')}</div>
   <div class="tx"><b>Ágora</b><span>Gestão 2026 · DEA FAUFBA</span></div>
 </div>
 <h1>Cartazes do Mural</h1>
 <p class="lead">O Mural é a página onde qualquer aluno da FAUFBA marca, em 40 segundos,
 o que trava o curso dele. O que é marcado vira número público no mesmo dia — e é isso
 que muda a conversa com a Faculdade: em vez de “uns alunos reclamaram”, ela passa a ver
 quantos são.</p>
 <p class="lead">Está no ar, ligado a uma planilha na conta do DEA, e já foi testado
 por colegas. Estes são os cartazes para colocar de pé nos murais.</p>

 <h2>Três direções de arte, mesma mensagem</h2>
 <div class="fam">
  <div class="cx" style="border-color:{AZUL}">
    <b style="color:{AZUL}">1 · Quadrados</b>
    <p>O símbolo da ágora repetido em campo. A mais sóbria — funciona bem no digital
    e em mural de vidro, ao lado de comunicado oficial.</p>
  </div>
  <div class="cx" style="border-color:{INK}">
    <b style="color:{INK}">2 · Xerox</b>
    <p>Na linha gráfica do DCE: duas cores chapadas, sem meio-tom nenhum. Feita para
    fotocópia em massa — sai igual no xerox da esquina, e sai barato.</p>
  </div>
  <div class="cx" style="border-color:{VERMELHO}">
    <b style="color:{VERMELHO}">3 · Colagem</b>
    <p>Papel rasgado, fita crepe, estrelas. A mais quente e a mais “mural de faculdade”.
    Chama mais atenção de longe.</p>
  </div>
 </div>

 <h2>Como imprimir</h2>
 <p class="lead">Tudo em <b>A4</b>, escala <b>100%</b> — nada de “ajustar à página”, que
 encolhe a margem e corta o fio de cor no topo. E marque <b>imprimir gráficos de fundo</b>,
 senão os cartazes saem brancos. Para A3, é o mesmo arquivo ampliado a 141%.</p>

 <div class="pe">
   <div class="qr"><img src="{QR}" alt="QR do Mural"><span>aponte a câmera</span></div>
   <div class="pe-tx">
     <b>mural-faufba.netlify.app</b>
     <p>Os três QR dos cartazes apontam para cá. Vale conferir com a câmera antes de
     mandar imprimir — se o link mudar, os cartazes impressos ficam mortos.</p>
   </div>
 </div>
</section>'''

CSS_CAPA = f'''
.fam-capa.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;
 background:{PAPEL};padding:20mm 18mm 16mm;font-family:'Inter',system-ui,sans-serif;
 display:flex;flex-direction:column}}
.fam-capa .fio{{position:absolute;top:0;left:0;right:0;height:5mm;display:flex}}
.fam-capa .fio i{{flex:1}}
.fam-capa .fio i:nth-child(1){{background:{AMARELO}}}
.fam-capa .fio i:nth-child(2){{background:{AZULC}}}
.fam-capa .fio i:nth-child(3){{background:{VERMELHO}}}
.fam-capa .topo{{display:flex;align-items:center;gap:5mm}}
.fam-capa .mk{{width:17mm;height:17mm;flex:none}}
.fam-capa .mk .logo{{width:100%;height:100%;display:block;object-fit:contain}}
.fam-capa .tx b{{font-family:'Anton',sans-serif;font-weight:400;font-size:16pt;
 display:block;line-height:1;letter-spacing:.05em;text-transform:uppercase;color:{INK}}}
.fam-capa .tx span{{font-weight:800;font-size:8pt;letter-spacing:.16em;
 text-transform:uppercase;display:block;margin-top:2mm;color:#5A6068}}
.fam-capa h1{{font-family:'Anton',sans-serif;font-weight:400;font-size:44pt;
 line-height:1;letter-spacing:-.005em;color:{AZUL};margin-top:11mm}}
.fam-capa h2{{font-family:'Anton',sans-serif;font-weight:400;font-size:17pt;
 color:{INK};margin-top:10mm;letter-spacing:.01em}}
.fam-capa .lead{{font-size:11pt;line-height:1.5;color:{INK};margin-top:4mm;max-width:168mm}}
.fam-capa .fam{{display:flex;gap:5mm;margin-top:5mm}}
.fam-capa .cx{{flex:1;border-left:1.6mm solid;padding:1mm 0 1mm 4mm}}
.fam-capa .cx b{{font-size:10.5pt;display:block;letter-spacing:.02em}}
.fam-capa .cx p{{font-size:9.5pt;line-height:1.45;color:#3C424A;margin-top:2mm}}
.fam-capa .pe{{margin-top:auto;display:flex;align-items:center;gap:7mm;
 border-top:.6mm solid #D8D3C8;padding-top:7mm}}
.fam-capa .qr{{width:34mm;flex:none}}
.fam-capa .qr img{{width:100%;display:block;image-rendering:pixelated}}
.fam-capa .qr span{{display:block;text-align:center;margin-top:2mm;font-weight:800;
 font-size:7pt;letter-spacing:.1em;text-transform:uppercase;color:#5A6068}}
.fam-capa .pe-tx b{{font-family:'Anton',sans-serif;font-weight:400;font-size:19pt;
 color:{AZUL};display:block;letter-spacing:.01em}}
.fam-capa .pe-tx p{{font-size:9.5pt;line-height:1.45;color:#3C424A;margin-top:3mm;max-width:130mm}}
'''

html = ('<title>Cartazes do Mural — Gestão Ágora — DEA FAUFBA</title>\n'
        '<style>' + '\n'.join(fontes) + '</style>\n'
        '<style>\n@page{size:A4;margin:0}\n*{box-sizing:border-box;margin:0;padding:0}\n'
        + CSS_CAPA + '\n' + '\n'.join(css_todos) + '\n</style>\n'
        + CAPA + '\n' + '\n'.join(secoes) + '\n')
open('cartazes-todos.html', 'w', encoding='utf-8').write(html)
print('cartazes-todos.html escrito · fontes unicas:', len(fontes))
