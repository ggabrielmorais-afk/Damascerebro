# -*- coding: utf-8 -*-
"""Duas paginas para mandar a uma pessoa do DEA: uma capa que explica o Mural e
uma pagina de escolha com as nove artes lado a lado. Quem recebe decide olhando
uma pagina so, em vez de rolar dez."""
import base64, sys
sys.path.insert(0, '.')
import logo

FONTES = open('fontes-anton-inter.css', encoding='utf-8').read()
QR = open('qr.txt', encoding='utf-8').read()
AMARELO='#F4EA4D'; AZUL='#1B6CA8'; AZULC='#469DE2'; VERMELHO='#D53C2C'
INK='#14171A'; PAPEL='#FBFAF7'

def png(arq):
    return 'data:image/png;base64,' + base64.b64encode(open(arq, 'rb').read()).decode()

FAM = [
    ('Quadrados', AZUL,     'q', 'Sóbria. Funciona no digital e em mural de vidro, '
                                 'ao lado de comunicado oficial.'),
    ('Xerox',     INK,      'x', 'Duas cores chapadas, sem meio-tom. Feita para fotocópia '
                                 'em massa — sai igual no xerox da esquina, e sai barato.'),
    ('Colagem',   VERMELHO, 'c', 'Papel rasgado, fita crepe, estrelas. A mais quente, '
                                 'a que chama atenção de longe.'),
]

capa = f'''<section class="pg capa" data-document-role="page" data-label="Capa">
 <div class="fio"><i></i><i></i><i></i></div>
 <div class="topo">
   {logo.tag(INK)}
   <div class="tx"><b>Ágora</b><span>Gestão 2026 · DEA FAUFBA</span></div>
 </div>
 <h1>Cartazes do Mural</h1>
 <p class="lead">O Mural é a página onde qualquer aluno da FAUFBA marca, em 40 segundos,
 o que trava o curso dele. O que é marcado vira número público no mesmo dia — e é isso
 que muda a conversa com a Faculdade: em vez de “uns alunos reclamaram”, ela passa a ver
 quantos são.</p>
 <p class="lead">Está no ar, ligado a uma planilha na conta do DEA, e já foi testado por
 colegas. Faltam os cartazes. Na página seguinte estão três direções de arte com a mesma
 mensagem — a ideia é escolher uma.</p>
 <h2>Como imprimir, depois de escolher</h2>
 <p class="lead">Tudo em <b>A4</b>, escala <b>100%</b> — nada de “ajustar à página”, que
 encolhe a margem e corta o fio de cor no topo. E marque <b>imprimir gráficos de fundo</b>,
 senão os cartazes saem brancos. Para A3, é o mesmo arquivo ampliado a 141%.</p>
 <div class="pe">
   <div class="qr"><img src="{QR}" alt="QR do Mural"><span>aponte a câmera</span></div>
   <div class="pe-tx">
     <b>mural-faufba.netlify.app</b>
     <p>Os nove cartazes apontam para cá. Vale conferir com a câmera antes de mandar
     imprimir — se o link mudar, o que já está na parede morre junto.</p>
   </div>
 </div>
</section>'''

colunas = ''
for nome, cor, tag, desc in FAM:
    tiras = ''.join(f'<img src="{png(f"tira_{tag}{i}.png")}" alt="{nome} {i}">' for i in (1, 2, 3))
    colunas += f'''<div class="col">
   <div class="cab" style="background:{cor}">{nome}</div>
   <div class="tiras">{tiras}</div>
   <p class="desc">{desc}</p>
 </div>'''

escolha = f'''<section class="pg esc" data-document-role="page" data-label="Escolha">
 <div class="fio"><i></i><i></i><i></i></div>
 <h1>Três direções, mesma mensagem</h1>
 <p class="lead">Cada coluna traz o mesmo trio — placar público, canal sigiloso e a regra dos
 três temas. Muda só a arte.</p>
 <div class="grade">{colunas}</div>
 <p class="rod">Gestão Ágora · DEA FAUFBA · mural-faufba.netlify.app</p>
</section>'''

CSS = f'''
@page{{size:A4;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;
 background:{PAPEL};display:flex;flex-direction:column}}
.pg:last-child{{break-after:auto}}
.fio{{position:absolute;top:0;left:0;right:0;height:5mm;display:flex}}
.fio i{{flex:1}}
.fio i:nth-child(1){{background:{AMARELO}}}
.fio i:nth-child(2){{background:{AZULC}}}
.fio i:nth-child(3){{background:{VERMELHO}}}

.capa{{padding:20mm 18mm 16mm}}
.capa .topo{{display:flex;align-items:center;gap:5mm}}
.capa .topo .mk{{width:17mm;height:17mm;flex:none;display:block;object-fit:contain}}
.capa .tx b{{font-family:'Anton',sans-serif;font-weight:400;font-size:16pt;display:block;
 line-height:1;letter-spacing:.05em;text-transform:uppercase;color:{INK}}}
.capa .tx span{{font-weight:800;font-size:8pt;letter-spacing:.16em;text-transform:uppercase;
 display:block;margin-top:2mm;color:#5A6068}}
.capa h1{{font-family:'Anton',sans-serif;font-weight:400;font-size:44pt;line-height:1;
 color:{AZUL};margin-top:11mm}}
.capa h2{{font-family:'Anton',sans-serif;font-weight:400;font-size:17pt;color:{INK};
 margin-top:11mm}}
.capa .lead{{font-size:11pt;line-height:1.5;color:{INK};margin-top:4mm;max-width:168mm}}
.capa .pe{{margin-top:auto;display:flex;align-items:center;gap:7mm;
 border-top:.6mm solid #D8D3C8;padding-top:7mm}}
.capa .qr{{width:34mm;flex:none}}
.capa .qr img{{width:100%;display:block;image-rendering:pixelated}}
.capa .qr span{{display:block;text-align:center;margin-top:2mm;font-weight:800;font-size:7pt;
 letter-spacing:.1em;text-transform:uppercase;color:#5A6068}}
.capa .pe-tx b{{font-family:'Anton',sans-serif;font-weight:400;font-size:19pt;color:{AZUL};
 display:block}}
.capa .pe-tx p{{font-size:9.5pt;line-height:1.45;color:#3C424A;margin-top:3mm;max-width:130mm}}

.esc{{padding:16mm 14mm 12mm}}
.esc h1{{font-family:'Anton',sans-serif;font-weight:400;font-size:26pt;line-height:1;
 color:{AZUL};margin-top:4mm}}
.esc .lead{{font-size:10pt;line-height:1.45;color:#3C424A;margin-top:3mm;max-width:172mm}}
.esc .grade{{display:flex;gap:10mm;justify-content:center;margin-top:6mm}}
.esc .col{{width:46mm;flex:none;display:flex;flex-direction:column}}
.esc .cab{{color:{PAPEL};font-weight:800;font-size:9.5pt;letter-spacing:.14em;
 text-transform:uppercase;padding:2.2mm 3mm;text-align:center}}
.esc .tiras{{display:flex;flex-direction:column;gap:3mm;margin-top:3mm}}
.esc .tiras img{{width:100%;display:block;border:.35mm solid #DDD8CD}}
.esc .desc{{font-size:8.5pt;line-height:1.4;color:#3C424A;margin-top:3.5mm}}
.esc .rod{{margin-top:auto;font-weight:800;font-size:8pt;letter-spacing:.12em;
 text-transform:uppercase;color:#5A6068;text-align:center}}
'''

html = ('<title>Cartazes do Mural — escolha — Gestão Ágora</title>\n'
        '<style>' + FONTES + '</style>\n<style>' + CSS + '</style>\n'
        + capa + '\n' + escolha + '\n')
open('cartazes-escolha.html', 'w', encoding='utf-8').write(html)
print('cartazes-escolha.html escrito')
