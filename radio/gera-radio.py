# -*- coding: utf-8 -*-
"""Radio e revista, refeito na linguagem dos cartazes: paleta do DEA, Poppins
pesada em caixa-baixa, formas cortadas em diagonal, faixa sangrando e a logo
da Agora no lockup. Mesmo conteudo do documento anterior, arte nova."""
import sys
sys.path.insert(0, '.')
import logo, parceiros

FONTES = open('fontes-poppins.css', encoding='utf-8').read()
QR = open('qr.txt', encoding='utf-8').read()

AMARELO='#F4EA4D'; AZUL='#469DE2'; AZULP='#1B6CA8'; VERMELHO='#D53C2C'

def mistura(frente, fundo, a):
    f = [int(frente[i:i+2],16) for i in (1,3,5)]
    b = [int(fundo[i:i+2],16) for i in (1,3,5)]
    return '#%02X%02X%02X' % tuple(round(f[i]*a + b[i]*(1-a)) for i in range(3))
INK='#14171A'; PAPEL='#FBFAF7'; CINZA='#5A6068'

def lockup(cor, tam='11mm'):
    return f'''<div class="lock">
  <img class="lg" src="{logo.b64(cor)}" alt="Ágora" style="width:{tam};height:{tam}">
  <div class="lock-tx" style="color:{cor}"><b>ágora</b><b>gestão<span>2026</span></b></div>
</div>'''

def cab(secao, num):
    return f'''<div class="cab">
  {lockup(INK)}
  <div class="cab-d"><b>{secao}</b><span>{num}</span></div>
</div>
<div class="regra"><i>D E A</i><span>diretório dos estudantes de arquitetura · ufba</span></div>'''

def chip(tx, fundo=INK, cor=AMARELO):
    return f'<div class="chip" style="background:{fundo};color:{cor}">{tx}</div>'

def faixa(tx, fundo=INK, cor=AMARELO, num=''):
    n = f'<i>{num}</i>' if num else ''
    return f'<div class="faixa" style="background:{fundo};color:{cor}">{tx}{n}</div>'

def numeros(itens, cor=AZULP):
    cel = ''.join(f'<div class="num"><b style="color:{cor}">{v}</b><span>{r}</span></div>'
                  for v, r in itens)
    return f'<div class="nums">{cel}</div>'

def duas(a_tit, a_tx, b_tit, b_tx):
    return f'''<div class="duas">
  <div class="cx"><div class="cx-cab" style="background:{AZULP}">{a_tit}</div><p>{a_tx}</p></div>
  <div class="cx"><div class="cx-cab" style="background:{VERMELHO}">{b_tit}</div><p>{b_tx}</p></div>
</div>'''

def passos(itens, cor=AZULP):
    cel = ''.join(f'<div class="pas"><b style="color:{cor}">{n}</b><strong>{t}</strong><p>{x}</p></div>'
                  for n, t, x in itens)
    return f'<div class="paslinha">{cel}</div>'

def lista(itens, cor=AZULP):
    cel = ''.join(f'<div class="it"><b style="color:{cor}">{n}</b><div><strong>{t}</strong><p>{x}</p></div></div>'
                  for n, t, x in itens)
    return f'<div class="itens">{cel}</div>'

def caixa(tit, tx, fundo=AMARELO):
    return f'<div class="caixa" style="background:{fundo}"><strong>{tit}</strong><p>{tx}</p></div>'

def tempo(itens):
    cel = ''.join(f'<div class="tp"><b>{d}</b><p>{x}</p></div>' for d, x in itens)
    return f'<div class="tempo">{cel}</div>'

def pagina(secao, num, chip_tx, h1, lead, corpo, rodape, rotulo):
    return f'''<section class="pg" data-document-role="page" data-label="{rotulo}">
 <div class="fio"><i></i><i></i><i></i></div>
 {cab(secao, num)}
 {chip(chip_tx)}
 <h1>{h1}</h1>
 <p class="lead">{lead}</p>
 {corpo}
 {faixa(rodape, INK, AMARELO, num)}
</section>'''

# ── 01 capa ───────────────────────────────────────────────────────────────
capa = f'''<section class="pg capa" data-document-role="page" data-label="Capa">
 <div class="fio"><i></i><i></i><i></i></div>
 <img class="logo-fundo" src="{logo.b64(mistura(INK, AMARELO, .13))}" alt="">
 <img class="logo-capa" src="{logo.b64(INK)}" alt="Ágora">
 {chip('proposta interna · semestre 2026.2', INK, AMARELO)}
 <h1 class="tit">rádio<br>e revista</h1>
 <p class="lead-capa">As duas já existiram na FAUFBA, e as duas pararam. Este documento
 é sobre o que mudou, quanto custa, e o que a gente faz na primeira semana.</p>
 <div class="indice">
   <b>o que tem aqui dentro</b>
   <div class="ix"><i>02</i>ponto de partida</div>
   <div class="ix"><i>03</i>histórico</div>
   <div class="ix"><i>04</i>a rádio</div>
   <div class="ix"><i>05</i>pauta</div>
   <div class="ix"><i>06</i>a revista</div>
   <div class="ix"><i>07</i>custo</div>
   <div class="ix"><i>08</i>calendário</div>
 </div>
 <div class="ass-capa">
   <div class="regra" style="border-color:{INK}"><i>D E A</i><span>diretório dos estudantes
   de arquitetura · ufba</span></div>
   <img class="dea" src="{parceiros.dea()}" alt="DEA FAUFBA">
 </div>
 <div class="faixa-capa">
   <div><b>o Mural já está no ar</b><span>mural-faufba.netlify.app</span></div>
   <div class="qr"><img src="{QR}" alt="QR do Mural"><span>aponte a câmera</span></div>
 </div>
</section>'''

p2 = pagina('ponto de partida', '02', 'antes de pedir qualquer coisa nova',
  'o primeiro passo<br>já foi dado',
  'O Mural está publicado e gravando respostas de verdade. Rádio e revista deixam de ser '
  'ideia solta e passam a ser o segundo passo de uma coisa que já anda.',
  numeros([('8', 'temas abertos pra resposta, de oferta de disciplina a didática'),
           ('40s', 'é o tempo de responder, sem login e sem nome'),
           ('R$ 0', 'de verba, do protótipo até o que está no ar hoje')])
  + duas('resolve',
         'O Mural mede o que trava o estudante, por tema e por turno, e devolve o número '
         'na hora. Cada matrícula responde três temas por semestre, então o número aguenta '
         'ser questionado numa reunião.',
         'não resolve',
         'Número não conta história. Ninguém se emociona com uma tabela e ninguém guarda '
         'uma planilha. É aí que entram a rádio e a revista.')
  + caixa('A divisão de trabalho entre as três coisas',
          'O Mural diz <b>quantos</b>. A rádio e a revista dizem <b>quem</b> e <b>como é</b>. '
          'Sem as duas, a Faculdade ouve estatística e esquece na semana seguinte.'),
  'o mural mede. a rádio e a revista contam.', 'Ponto de partida')

p3 = pagina('histórico', '03', 'encarando de frente',
  'já morreu antes.<br>vale dizer por quê.',
  'A FAUFBA já teve revista e já teve programa em áudio. As duas pararam faz anos. Começar '
  'fingindo que a ideia é inédita é o jeito mais rápido de repetir o mesmo fim.',
  '<div class="sub">o que matou</div>'
  + lista([('01', 'Pauta do zero', 'Toda edição começava com alguém tendo que inventar sobre '
            'o que falar. Isso cansa antes da terceira.'),
           ('02', 'Uma pessoa só', 'Quando essa pessoa se formava ou cansava, acabava junto. '
            'Não havia segunda pessoa sabendo fazer.'),
           ('03', 'Sem data obrigando', 'Sem prazo de fora, a próxima edição podia sempre ser '
            'no mês que vem.')], VERMELHO)
  + '<div class="sub">o que mudou</div>'
  + lista([('01', 'A pauta chega pronta', 'O Mural recolhe toda semana o que está travando os '
            'estudantes. Ninguém precisa inventar assunto: ele vem do que as pessoas marcaram.'),
           ('02', 'A Faculdade decidiu duas vezes que precisa ouvir estudante',
            'A Congregação de 4 de setembro decidiu pedir à PROGRAD uma janela de ajuste por '
            'causa do noturno. A Coordenação Acadêmica marcou pesquisa com formandos pra outubro.'),
           ('03', 'Gravar e publicar hoje custa zero', 'Celular grava, aplicativo gratuito corta, '
            'canal hospeda. O que antes exigia estúdio e gráfica agora exige uma tarde.')], AZULP),
  'o que matou antes não existe mais.', 'Histórico')

p4 = pagina('a rádio', '04', 'uma tarde por episódio',
  'conversa de 30 minutos,<br>gravada em sala',
  'Um professor convidado e dois estudantes, numa sala qualquer da Faculdade, com o celular '
  'no meio da mesa. Áudio, sem câmera. Sobe com uma imagem fixa, então não existe edição de '
  'vídeo pra fazer.',
  duas('tema do primeiro',
       'A Faculdade que temos e a que a gente queria. Conversa aberta, sem pauta fechada e sem '
       'cobrança de ninguém. É o convite mais fácil de aceitar e o mais difícil de gerar atrito.',
       'quem faz o quê',
       'Uma pessoa produz: convida, marca a sala, publica. Outra conduz a conversa. As duas '
       'funções são separadas de propósito, pra ninguém precisar ser bom nas duas.')
  + caixa('Episódio zero, antes de convidar qualquer professor',
          'Grave primeiro uma conversa de quinze minutos entre três pessoas do DEA sobre os '
          'primeiros números do Mural. Ninguém de fora, nenhuma agenda pra combinar, nenhum '
          'risco. Serve pra testar o gravador, o corte e a publicação, e pra chegar no primeiro '
          'convidado mostrando um episódio pronto em vez de uma ideia.')
  + '<div class="sub">o caminho</div>'
  + passos([('01', 'Convite', 'Uma mensagem dizendo que é conversa de 30 minutos, em áudio, '
             'sobre a Faculdade. Nada de questionário mandado antes.'),
            ('02', 'Gravação', 'Sala reservada, celular no gravador, uma hora bloqueada. Grava '
             'corrido, sem parar pra corrigir.'),
            ('03', 'Corte', 'Tira o começo bagunçado e o fim, equaliza o volume. Uma hora em '
             'aplicativo gratuito.'),
            ('04', 'Publicação', 'Capa fixa com a identidade da Ágora, sobe no canal, link no '
             'grupo e no cartaz da semana.')]),
  'grava numa tarde. publica no mesmo dia.', 'A rádio')

p5 = pagina('pauta', '05', 'cinco episódios já com assunto',
  'ninguém vai precisar<br>inventar pauta',
  'A pauta sai do que o Mural recolheu. Estes cinco já têm assunto, e os dois primeiros já '
  'têm data possível no calendário da Faculdade.',
  lista([('01', 'A Faculdade que temos e a que a gente queria',
          'O piloto. Conversa aberta com um professor convidado.'),
         ('02', 'Estudar trabalhando', 'O curso visto do noturno. Aula que acaba depois do '
          'último ônibus, ateliê sem vaga, trabalho de dia.'),
         ('03', 'Atravessar o TFG', 'Fala direto com formandos e pré-formandos, o mesmo público '
          'da pesquisa da Coordenação em outubro.'),
         ('04', 'O que o Mural mostrou no semestre', 'Os números na mesa, comentados por quem '
          'respondeu e por quem decide.'),
         ('05', 'Quem saiu daqui', 'Um egresso recente conta o que a Faculdade preparou e o '
          'que não preparou.')])
  + '<div class="sub">convidados</div>'
  + '<p class="nota">Os nomes a gente escolhe junto. O que importa é o perfil, porque é ele que '
    'decide se tem assunto e se as pessoas escutam até o fim.</p>'
  + passos([('—', 'Quem voltou de pesquisa fora', 'Chega com assunto pronto e vontade de contar.'),
            ('—', 'Quem dá a disciplina que mais trava', 'Rende a conversa mais útil do semestre.'),
            ('—', 'Professor recém-chegado', 'Ainda enxerga a Faculdade de fora e compara com '
             'onde esteve antes.'),
            ('—', 'Quem os estudantes já procuram', 'A confiança já construída aparece no áudio.')],
           VERMELHO),
  'cinco episódios, zero pauta pra inventar.', 'Pauta')

p6 = pagina('a revista', '06', 'uma edição por semestre',
  'o que a Faculdade produz<br>e ninguém vê',
  'Todo semestre a FAUFBA gera centenas de pranchas, maquetes e ensaios vistos por uma banca '
  'de três pessoas e depois esquecidos no HD de quem fez. A revista é onde isso volta a existir.',
  duas('metade: trabalho de estudante',
       'Prancha ou foto de maquete, com um parágrafo do próprio autor contando o que tentou '
       'fazer. O parágrafo é o que transforma imagem bonita em conteúdo, e custa cinco minutos '
       'de quem já fez o trabalho.',
       'metade: olhar sobre a Faculdade',
       'Entrevistas curtas e um ensaio fotográfico sobre o prédio. É a parte que dá personalidade '
       'à edição e a que exige texto original.')
  + caixa('Uma seção que só existe porque o Mural existe',
          'Quatro páginas com os números do semestre: o que mais travou, por turno, e o que a '
          'Faculdade respondeu. Vira a memória da gestão, e é exatamente o que faltou nas vezes '
          'anteriores, quando a chapa seguinte entrou sem saber o que tinha sido feito.')
  + '<div class="sub">formato</div>'
  + passos([('01', 'O semestre já é o prazo', 'O calendário da Faculdade define a data e ninguém '
             'precisa inventar um.'),
            ('02', 'PDF circula e não custa', 'Abre no celular, vai por WhatsApp, fica guardado. '
             'A Congregação acabou de relatar contingenciamento, então pedir gráfica agora seria '
             'começar por onde a conversa trava.'),
            ('03', 'A curadoria é o trabalho', 'Escolher, pedir o parágrafo, diagramar. Não tem '
             'apuração nem produção do zero, que é onde revista estudantil costuma morrer.')]),
  'uma edição por semestre. o prazo já existe.', 'A revista')

p7 = pagina('custo', '07', 'o que sai do bolso de alguém',
  'nada.<br>o custo é tempo.',
  'Não há uma linha de verba neste documento. Tudo que a rádio e a revista precisam já existe '
  'na Faculdade ou no bolso de quem vai fazer.',
  passos([('—', 'Gravador', 'Celular de quem estiver na sala, no aplicativo que já vem instalado.'),
          ('—', 'Edição de áudio', 'Aplicativo gratuito, no computador ou no próprio celular.'),
          ('—', 'Sala pra gravar', 'Sala da Faculdade, reservada como qualquer atividade estudantil.'),
          ('—', 'Capa e diagramação', 'A identidade da Ágora, que já existe pronta.'),
          ('—', 'Hospedagem', 'Canal do DEA no YouTube, e a revista em PDF, sem gráfica.')], VERMELHO)
  + numeros([('1', 'tarde por episódio, do convite à publicação'),
             ('2h', 'por semana pra manter a revista viva entre edições'),
             ('R$ 0', 'de verba pedida à Faculdade, agora ou depois')])
  + caixa('Onde pode aparecer dinheiro depois',
          'Registrada como ação de extensão no SIATEX, a rádio passa a emitir certificado e pode '
          'contar hora complementar pra quem participa. O registro exige um docente ou técnico '
          'efetivo como proponente. Não é condição pra começar: é o passo que vale dar depois '
          'que existir episódio publicado pra mostrar.'),
  'r$ 0 de verba. o custo é uma tarde.', 'Custo')

p8 = pagina('calendário', '08', 'datas que já existem no calendário da faculdade',
  'de outubro<br>a novembro',
  'Nenhuma destas datas foi inventada aqui. Todas já estão no calendário da Faculdade ou da '
  'Universidade — o que a gente faz é chegar nelas com coisa pronta.',
  tempo([('02 e 09/10', 'Congregação. Dá pra levar o primeiro número consolidado do Mural.'),
         ('05 a 16/10', 'Janela da pesquisa da Coordenação Acadêmica sobre a Matriz T, com '
          'formandos e pré-formandos.'),
         ('semana de 13/10', 'Episódio zero gravado entre nós, sem convidado de fora.'),
         ('fim de outubro', 'Primeiro episódio com professor convidado, publicado.'),
         ('novembro', 'Chamada aberta de trabalhos pra revista, junto com o fim do semestre.'),
         ('23 a 25/11', 'Seminário Estudantil UFBA, campus de Ondina. Espaço pra mostrar o Mural '
          'e a rádio fora da Faculdade.')])
  + caixa('Uma oportunidade que tem prazo',
          'O concurso do CAU-BA, edição 2026, tem categoria de Prática Inovadora no Ensino de '
          'Arquitetura e Urbanismo. O Mural se encaixa, e com um episódio e uma edição publicados '
          'a inscrição fica muito mais forte. Vale conferir o prazo no e-mail que o Colegiado '
          'mandou em setembro.', VERMELHO),
  'mural-faufba.netlify.app', 'Calendário')

p8 = p8.replace('<div class="faixa"', '''<div class="fecho">
   <div class="regra" style="flex:1"><i>D E A</i><span>diretório dos estudantes de
   arquitetura · ufba</span></div>
   <img class="lgf" src="''' + logo.b64(INK) + '''" alt="Ágora">
   <img class="deaf" src="''' + parceiros.dea() + '''" alt="DEA FAUFBA">
 </div>
 <div class="faixa"''')

CSS = f'''
@page{{size:A4;margin:0}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Poppins',system-ui,sans-serif;-webkit-font-smoothing:antialiased}}
.pg{{width:210mm;height:297mm;position:relative;overflow:hidden;break-after:page;
 background:{PAPEL};color:{INK};padding:15mm 15mm 0;display:flex;flex-direction:column}}
.pg:last-child{{break-after:auto}}
.fio{{position:absolute;top:0;left:0;right:0;height:4.5mm;display:flex}}
.fio i{{flex:1}}
.fio i:nth-child(1){{background:{AMARELO}}}.fio i:nth-child(2){{background:{AZUL}}}
.fio i:nth-child(3){{background:{VERMELHO}}}

.cab{{display:flex;align-items:flex-start;justify-content:space-between;margin-top:3mm}}
.lock{{display:flex;align-items:flex-start;gap:3.5mm}}
.lock .lg{{flex:none;display:block;object-fit:contain}}
.lock-tx b{{display:block;font-weight:900;font-size:11pt;line-height:.9;letter-spacing:-.02em}}
.lock-tx b span{{font-weight:700;margin-left:.07em}}
.cab-d{{text-align:right}}
.cab-d b{{display:block;font-weight:900;font-size:10.5pt;letter-spacing:-.01em}}
.cab-d span{{font-weight:900;font-size:19pt;color:{AZULP};line-height:1;display:block;margin-top:1mm}}
.regra{{display:flex;align-items:baseline;gap:3mm;margin-top:3mm;padding-top:2mm;
 border-top:.9mm solid {INK}}}
.regra i{{font-style:normal;font-weight:900;font-size:8pt;letter-spacing:.38em}}
.regra span{{font-weight:700;font-size:6.6pt;color:{CINZA}}}

.chip{{align-self:flex-start;margin-top:7mm;font-weight:900;font-size:8.5pt;letter-spacing:.02em;
 padding:2mm 5.5mm 2mm 3.5mm;clip-path:polygon(0 0,100% 0,100% 56%,91% 100%,0 100%)}}
h1{{font-weight:900;font-size:33pt;line-height:.9;letter-spacing:-.035em;margin-top:5mm}}
.lead{{font-weight:700;font-size:10.5pt;line-height:1.4;margin-top:5mm;max-width:158mm}}
.sub{{font-weight:900;font-size:9pt;letter-spacing:.16em;text-transform:uppercase;
 color:{CINZA};margin-top:7mm;padding-bottom:1.5mm;border-bottom:.4mm solid #D9D4C9}}

.nums{{display:flex;gap:6mm;margin-top:6mm}}
.num{{flex:1}}
.num b{{display:block;font-weight:900;font-size:26pt;line-height:1;letter-spacing:-.03em}}
.num span{{display:block;font-weight:500;font-size:8.5pt;line-height:1.35;margin-top:2mm;color:#3C424A}}

.duas{{display:flex;gap:6mm;margin-top:6mm}}
.cx{{flex:1}}
.cx-cab{{color:{PAPEL};font-weight:900;font-size:8.5pt;letter-spacing:.1em;text-transform:uppercase;
 padding:1.8mm 4mm;clip-path:polygon(0 0,100% 0,100% 55%,93% 100%,0 100%)}}
.cx p{{font-weight:500;font-size:9pt;line-height:1.45;margin-top:3mm;color:#3C424A}}

.paslinha{{display:flex;gap:5mm;margin-top:5mm}}
.pas{{flex:1}}
.pas b{{font-weight:900;font-size:13pt;display:block;line-height:1}}
.pas strong{{display:block;font-weight:900;font-size:9pt;margin-top:2mm;line-height:1.2}}
.pas p{{font-weight:500;font-size:8pt;line-height:1.4;margin-top:1.5mm;color:#3C424A}}

.itens{{display:flex;flex-wrap:wrap;gap:5mm 6mm;margin-top:5mm}}
.it{{flex:1 1 44%;display:flex;gap:3.5mm;align-items:flex-start}}
.it b{{font-weight:900;font-size:13pt;line-height:1;flex:none}}
.it strong{{display:block;font-weight:900;font-size:9pt;line-height:1.2}}
.it p{{font-weight:500;font-size:8.2pt;line-height:1.4;margin-top:1.5mm;color:#3C424A}}

.caixa{{margin-top:6mm;padding:5mm 6mm;color:{INK};
 clip-path:polygon(0 0,100% 0,100% 100%,4% 100%,0 86%)}}
.caixa strong{{display:block;font-weight:900;font-size:10pt;line-height:1.15}}
.caixa p{{font-weight:500;font-size:9pt;line-height:1.45;margin-top:2.5mm}}
.caixa[style*="{VERMELHO}"]{{color:{PAPEL}}}

.fecho{{margin-top:auto;display:flex;align-items:flex-end;gap:7mm;padding-bottom:7mm}}
.fecho .lgf{{width:15mm;height:15mm;object-fit:contain;flex:none}}
.fecho .deaf{{height:15mm;flex:none}}
.fecho .regra{{margin-top:0}}
.nota{{font-weight:500;font-size:9pt;line-height:1.45;margin-top:4mm;color:#3C424A;max-width:160mm}}

.tempo{{margin-top:5mm}}
.tp{{display:flex;gap:5mm;align-items:baseline;padding:2.6mm 0;border-bottom:.35mm solid #E2DDD2}}
.tp b{{font-weight:900;font-size:9pt;letter-spacing:.02em;color:{AZULP};flex:none;width:36mm}}
.tp p{{font-weight:500;font-size:9pt;line-height:1.4;color:#3C424A}}

.faixa{{margin:auto -15mm 0;padding:5mm 15mm;font-weight:900;font-size:13pt;line-height:1;
 letter-spacing:-.02em;display:flex;justify-content:space-between;align-items:baseline;
 clip-path:polygon(0 0,88% 0,100% 40%,100% 100%,0 100%)}}
.faixa i{{font-style:normal;font-size:16pt;opacity:1}}

/* capa */
.capa{{background:{AMARELO};padding:14mm 16mm 0}}
/* no amarelo a primeira faixa do fio sumia: vira tinta */
.capa .fio i:nth-child(1){{background:{INK}}}
.capa .logo-fundo{{position:absolute;right:-30mm;top:108mm;width:104mm;height:104mm;z-index:0;
 object-fit:contain}}
.capa>*:not(.fio):not(.logo-fundo){{position:relative;z-index:1}}
.indice{{margin-top:8mm;max-width:88mm}}
.indice b{{display:block;font-weight:900;font-size:8.5pt;letter-spacing:.16em;
 text-transform:uppercase;color:#6B6428;padding-bottom:2mm;border-bottom:.5mm solid {INK}}}
.ix{{display:flex;gap:4mm;align-items:baseline;padding:1.2mm 0;font-weight:900;font-size:9.5pt;
 border-bottom:.3mm solid #D9CF62}}
.ix i{{font-style:normal;color:#6B6428;font-size:9pt;width:8mm;flex:none}}
.logo-capa{{width:24mm;height:24mm;display:block;object-fit:contain;margin-top:3mm}}
.capa .chip{{margin-top:7mm}}
.tit{{font-size:56pt;line-height:.86;letter-spacing:-.045em;margin-top:5mm}}
.lead-capa{{font-weight:700;font-size:11.5pt;line-height:1.4;margin-top:6mm;max-width:146mm}}
.ass-capa{{margin-top:auto;display:flex;align-items:flex-end;justify-content:space-between;
 gap:8mm;padding-bottom:7mm}}
.ass-capa .regra{{flex:1;margin-top:0}}
.ass-capa .dea{{height:17mm;display:block;flex:none}}
.faixa-capa{{margin:0 -16mm;padding:6mm 16mm;background:{INK};color:{AMARELO};display:flex;
 align-items:center;justify-content:space-between;gap:8mm;
 clip-path:polygon(0 0,86% 0,100% 38%,100% 100%,0 100%)}}
.faixa-capa b{{display:block;font-weight:900;font-size:17pt;line-height:1;letter-spacing:-.02em}}
.faixa-capa span{{display:block;font-weight:700;font-size:10pt;margin-top:2.5mm;letter-spacing:.04em}}
.faixa-capa .qr{{background:{PAPEL};padding:2.6mm;width:28mm;flex:none;
 clip-path:polygon(0 0,100% 0,100% 80%,86% 100%,0 100%)}}
.faixa-capa .qr img{{width:100%;display:block;image-rendering:pixelated}}
.faixa-capa .qr span{{margin-top:1.5mm;font-size:5.6pt;font-weight:900;text-align:center;
 color:{INK};letter-spacing:.06em}}
'''

html = ('<title>Rádio e revista — Gestão Ágora — DEA FAUFBA</title>\n'
        '<style>' + FONTES + '</style>\n<style>' + CSS + '</style>\n'
        + '\n'.join([capa, p2, p3, p4, p5, p6, p7, p8]) + '\n')
open('radio-agora.html', 'w', encoding='utf-8').write(html)
print('radio-agora.html escrito')
