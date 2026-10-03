# -*- coding: utf-8 -*-
"""Podcast agora, revista em 2027: o nome do Mural, o encaixe com o aniversario
da FAU, o episodio zero e a linha editorial da revista. Mesma arte da proposta
de setembro: reaproveita os blocos e o CSS do gera-radio.py."""
import io, sys
sys.path.insert(0, '.')

src = io.open('gera-radio.py', encoding='utf-8').read()
ns = {}
exec(src.split('# ── 01 capa')[0], ns)                      # blocos e cores
exec(src[src.index("CSS = f'''"):src.index('html = (')], ns)  # CSS
g = ns
pagina, lista, duas, caixa, tempo, passos = (g['pagina'], g['lista'], g['duas'],
                                             g['caixa'], g['tempo'], g['passos'])
chip, logo, parceiros = g['chip'], g['logo'], g['parceiros']
INK, AMARELO, AZULP, VERMELHO, QR = g['INK'], g['AMARELO'], g['AZULP'], g['VERMELHO'], g['QR']
mistura = g['mistura']

# ── 01 capa ───────────────────────────────────────────────────────────────
capa = f'''<section class="pg capa" data-document-role="page" data-label="Capa">
 <div class="fio"><i></i><i></i><i></i></div>
 <img class="logo-fundo" src="{logo.b64(mistura(INK, AMARELO, .13))}" alt="">
 <img class="logo-capa" src="{logo.b64(INK)}" alt="Ágora">
 {chip('proposta interna · pra decidir junto', INK, AMARELO)}
 <h1 class="tit" style="font-size:46pt">podcast agora,<br>revista em 2027</h1>
 <p class="lead-capa">A reunião de 30/09 deixou a revista pro ano que vem e pediu a linha
 editorial e a identidade ainda neste semestre. O podcast não precisa esperar. Aqui estão o
 nome do Mural, o encaixe com o aniversário da FAU, o primeiro episódio pronto pra gravar e a
 linha editorial da revista.</p>
 <div class="indice">
   <b>o que tem aqui dentro</b>
   <div class="ix"><i>02</i>o nome do mural</div>
   <div class="ix"><i>03</i>aniversário da fau</div>
   <div class="ix"><i>04</i>episódio zero</div>
   <div class="ix"><i>05</i>próximos episódios</div>
   <div class="ix"><i>06</i>linha editorial</div>
   <div class="ix"><i>07</i>como a edição nasce</div>
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

# ── 02 o nome ─────────────────────────────────────────────────────────────
p2 = pagina('o nome', '02', 'decidir antes de imprimir',
  'trocar o nome<br>não muda o programa',
  'Em 28/09 a Maria Luísa e a Ana Camile apontaram dois problemas no nome Mural: confunde com o '
  'que já existe e passa a ideia de expor, quando o que a ferramenta faz é escutar. A troca é '
  'texto em quatro linhas do site e nos três cartazes. Estrutura, endereço e respostas ficam.',
  '<div class="sub">três opções</div>'
  + lista([('01', 'Pulso', 'Tomar o pulso da Faculdade: mede e escuta, sem prometer mais que '
            'isso. Funciona nas frases que a gente vai repetir: "responde o Pulso", "o Pulso '
            'mostrou que 90 pessoas querem TDA II", "relato sigiloso pelo Pulso".'),
           ('02', 'Escuta', 'A palavra que a Ana usou no grupo, e a que mais diz o que a '
            'ferramenta faz. O cuidado: universidade usa "escuta" pra serviço de acolhimento '
            'psicológico, e no mês da campanha contra assédio alguém pode esperar um '
            'acolhimento que o DEA não oferece.'),
           ('03', 'Soma', '"Soma aí": juntar e contar ao mesmo tempo. Vai bem no placar e mal '
            'no canal sigiloso, onde ninguém quer somar, quer ser ouvido.')])
  + duas('o que muda',
         'O título da página, a marca no topo, a descrição que aparece quando alguém '
         'compartilha o link e o nome nos três cartazes do Canva. Meia hora de trabalho, '
         'contando os cartazes.',
         'o que fica',
         'O endereço mural-faufba.netlify.app, então o QR continua valendo. As respostas já '
         'gravadas. A cota de três temas de quem já respondeu: os códigos internos guardam o '
         'nome antigo de propósito, porque trocar zeraria a cota.')
  + caixa('Minha sugestão: Pulso',
          'É a única das três que serve igual pro placar e pro canal sigiloso sem prometer o '
          'que o DEA não entrega. Se o grupo preferir Escuta, o cartaz amarelo ganha uma linha '
          'dizendo o que acontece com o relato e onde fica a denúncia oficial.'),
  'decidiu o nome, imprime na mesma semana.', 'O nome')

# ── 03 aniversario ────────────────────────────────────────────────────────
p3 = pagina('aniversário da fau', '03', '30 de outubro',
  'três coisas<br>que se encaixam',
  'A reunião de 30/09 marcou duas ações pro aniversário: a campanha contra assédio, com a '
  'palestra da professora de Direito do Observatório, e a exposição permanente de arte '
  'estudantil. As duas se ligam ao que o DEA já tem no ar, e o podcast entra junto.',
  lista([('01', 'Campanha e canal sigiloso', 'O cartaz amarelo já convida a relatar em sigilo, '
          'e a campanha vai mandar gente pra lá. Antes: escolher as duas pessoas que leem os '
          'relatos, pedir à professora que revise o texto do canal e anunciar o canal no fim da '
          'palestra. O canal acolhe e encaminha; a denúncia formal segue pela via oficial. '
          'Relato nunca entra no placar.'),
         ('02', 'Exposição e revista, um edital só', 'Quem inscreve trabalho na exposição '
          'autoriza, no mesmo formulário, a publicação na primeira edição da revista, com '
          'crédito. Pra inaugurar em 30/10, o edital sai até 09/10: inscrição até 18/10, '
          'curadoria de 19 a 23/10, montagem na semana do aniversário.'),
         ('03', 'Episódio gravado na semana', 'Meia hora com a professora depois da palestra, '
          'ou com quem fez a curadoria. Vira o primeiro episódio com convidado, que a proposta '
          'de setembro já previa pro fim de outubro.'),
         ('04', 'Divulgação pelo Boletim', 'A Comunicação da FAU tem formulário pra pedir '
          'divulgação de evento e de edital, e o que entra lá sai no Boletim FAUFBA, que chega '
          'às listas de estudantes, docentes e técnicos. Evento: forms.gle/ptBEbYehuaQKEi8L9. '
          'Edital: forms.gle/Ri5yTT4t9bDR8XTu9.')], AZULP)
  + caixa('Mandar agora pra programação oficial',
          'A programação da semana sai da Direção, com o Fábio. Se a palestra e a inauguração '
          'forem mandadas agora, entram no cartaz oficial e na divulgação da própria Faculdade. '
          'É também a hora de pedir a parede da exposição permanente.', VERMELHO),
  'um edital, duas entregas.', 'Aniversário da FAU')

# ── 04 episodio zero ──────────────────────────────────────────────────────
p4 = pagina('podcast', '04', 'pronto pra gravar',
  'episódio zero:<br>15 minutos',
  'A proposta de setembro previa um episódio zero entre três pessoas do DEA sobre os primeiros '
  'números do Mural. Os cartazes ainda não foram colados e o número ainda é pequeno, então o '
  'assunto muda pro que o DEA decidiu em 30/09, que todo estudante deveria saber e quase '
  'ninguém sabe.',
  '<div class="sub">roteiro</div>'
  + tempo([('00:00 · 1 min', 'Abertura. Quem fala, semestre e turno de cada um, e o que é o '
            'podcast.'),
           ('01:00 · 5 min', 'O que o DEA decidiu: aniversário da FAU, campanha contra assédio, '
            'exposição, festa com a Atlética.'),
           ('06:00 · 4 min', 'O Mural: o que é, por que número pesa (os 90 interessados em '
            'TDA II, que a Direção não teve como rebater) e como responder em 40 segundos.'),
           ('10:00 · 3 min', 'Como entrar: edital da exposição, processo seletivo do DEA no '
            'próximo semestre, onde mandar pauta.'),
           ('13:00 · 2 min', 'Fechamento: data do próximo episódio e onde ouvir.')])
  + '<div class="sub">como fazer</div>'
  + passos([('01', 'Três pessoas', 'Uma produz: marca a sala, escreve a descrição, publica. '
             'Uma conduz. Uma conta o que foi decidido, de preferência quem esteve em 30/09.'),
            ('02', 'Gravação', 'Sala de porta fechada e sem ventilador. Um celular no meio da '
             'mesa, em modo avião, em cima de um pano dobrado. Grava 30 segundos de teste.'),
            ('03', 'Corte', 'Audacity no computador ou CapCut no celular, os dois de graça. '
             'Tira o começo e o fim, iguala o volume.'),
            ('04', 'Publicação', 'Capa fixa no Canva, na identidade do DEA. Sobe no YouTube do '
             'DEA e no Spotify for Creators, que é gratuito e aceita o e-mail do DEA.')]),
  '15 minutos. nenhum convidado de fora.', 'Episódio zero')

# ── 05 proximos episodios ─────────────────────────────────────────────────
p5 = pagina('podcast', '05', 'a pauta já existe',
  'depois do zero,<br>assunto não falta',
  'Os cinco episódios da proposta de setembro continuam valendo. Os e-mails da Faculdade desde '
  'agosto deram data e assunto a vários deles, e trouxeram pauta nova.',
  lista([('01', 'Estudar trabalhando', 'Em julho a lista de interessados nas disciplinas sem '
          'turma no noturno circulou por e-mail, com o nome de todo mundo. Em agosto alguém '
          'perguntou na lista se tinha retorno: eram obrigatórias e pré-requisito de TFG.'),
         ('02', 'Atravessar o TFG', 'O Colegiado marcou a Semana de TFG de 7 a 18 de dezembro. '
          'Gravar nela, com quem acabou de defender, e convidar as mesmas pessoas pra revista.'),
         ('03', 'Quem ganhou lá fora', 'A equipe BIM Officers, notícia do Boletim FAUFBA nº 06, '
          'ficou em 3º lugar na Buildathon 2026 e em 1º no Brasil. Assunto pronto e gente '
          'querendo contar.'),
         ('04', 'A Faculdade fora dos muros', 'O escritório modelo CURIAR, a extensão com '
          'comunidade (Mulheres da Laje, Travesía) e as notas públicas que a FAU assinou no '
          'semestre.'),
         ('05', 'O que o Mural mostrou', 'Fica pra dezembro, com o número do semestre fechado. '
          'Vira também a seção de números da revista.'),
         ('06', 'Quem saiu daqui', 'Egresso recente. Os premiados de TFG do CAU-BA deste ano '
          'são o convite natural, quando o resultado sair.')])
  + caixa('Nome do podcast: a decidir junto',
          'Uma ideia pra começar a conversa: Corredor. É onde a conversa sobre a Faculdade já '
          'acontece todo dia, sem ninguém gravando.'),
  'seis episódios com assunto.', 'Próximos episódios')

# ── 06 linha editorial ────────────────────────────────────────────────────
p6 = pagina('revista', '06', 'linha editorial',
  'uma frase<br>decide o que entra',
  'A revista mostra o que a FAUFBA produz e como é estudar aqui, contado por quem estuda. Pauta '
  'que não cabe nessa frase fica de fora, por melhor que seja.',
  duas('é',
       'Registro do semestre. Trabalho de estudante com a palavra de quem fez. Crítica com '
       'número, que vem do Mural, e com o nome de quem assina. Texto direto, do jeito que a '
       'gente fala, sem academiquês.',
       'não é',
       'Jornal de denúncia. Vitrine só dos melhores trabalhos. Canal oficial da Direção. Lugar '
       'de crítica a professor com nome: vale a regra do tema Didática do Mural, que mede a '
       'aula sem nomear ninguém.')
  + '<div class="sub">seções fixas · cerca de 32 páginas</div>'
  + lista([('01', 'Prancha · 12 a 14 p.', 'Ateliê, TFG, maquete. Cada trabalho com um parágrafo '
            'do autor. Semestres e turnos misturados, o noturno incluído.'),
           ('02', 'Em números · 4 p.', 'O semestre pelo Mural: o que mais travou, por turno, e o '
            'que a Faculdade respondeu.'),
           ('03', 'Conversa · 4 p.', 'Uma entrevista longa. Pode sair transcrita de um episódio '
            'do podcast.'),
           ('04', 'Ensaio · 4 p.', 'Fotografia do prédio e de quem usa ele.'),
           ('05', 'Fora dos muros · 2 a 4 p.', 'Extensão, escritório modelo, a cidade.'),
           ('06', 'Quem saiu daqui · 2 p.', 'Um egresso recente conta o que a Faculdade '
            'preparou e o que não preparou.')]),
  'se não cabe na frase, não entra.', 'Linha editorial')

# ── 07 como a edicao nasce ────────────────────────────────────────────────
p7 = pagina('revista', '07', 'o trabalho é curadoria',
  'como uma edição<br>nasce',
  'Ninguém precisa apurar notícia. O material já existe no HD de quem fez, nas bancas e no '
  'podcast. O trabalho é escolher, pedir o parágrafo e montar.',
  lista([('01', 'Chamada', 'O edital da exposição em outubro e a Semana de TFG em dezembro. A '
          'mesma inscrição já pede a autorização de publicação.'),
         ('02', 'Seleção', 'Três pessoas na curadoria. Semestres e turnos variados, processo '
          'conta tanto quanto resultado, imagem que se lê no celular.'),
         ('03', 'Parágrafo do autor', 'Até 600 caracteres sobre o que tentou fazer. É ele que '
          'transforma imagem bonita em conteúdo.'),
         ('04', 'Montagem', 'Um modelo fixo na identidade do DEA. Cada edição só troca o '
          'conteúdo, então a segunda sai mais rápido que a primeira.'),
         ('05', 'Revisão', 'Outra pessoa lê tudo antes de sair. Nome errado e crédito faltando '
          'são os erros que mais custam.'),
         ('06', 'PDF', 'Drive do DEA, WhatsApp e Instagram. Sem gráfica e sem custo.')])
  + caixa('Regras desde a primeira edição',
          'Autorização por escrito no formulário de inscrição, com crédito. Foto e entrevista de '
          'pessoa só com consentimento. Nenhuma matrícula, telefone ou e-mail publicado. '
          'Trabalho de membro do DEA passa pela mesma curadoria. Erro publicado se corrige na '
          'edição seguinte.')
  + duas('equipe',
         'Uma pessoa na edição, três na curadoria, uma no design e uma na revisão. O novo cargo '
         'de Marketing pode dividir o design com a identidade visual da gestão.',
         'nome',
         'A decidir junto. Duas ideias pra começar: Prancha, a unidade de tudo que a gente '
         'entrega, e Escala.'),
  'o material já existe. falta juntar.', 'Como a edição nasce')

# ── 08 calendario ─────────────────────────────────────────────────────────
p8 = pagina('calendário', '08', 'de outubro ao começo de 2027',
  'as datas<br>que já existem',
  'Quase todas vêm de e-mail do Colegiado, da Direção ou da Reitoria. O que o DEA faz é chegar '
  'nelas com coisa pronta.',
  tempo([('seg 05/10', 'Conversa com o Neto, no Colegiado. Levar o Mural como alternativa aos '
          'formulários que ninguém responde.'),
         ('05 a 16/10', 'Pesquisa da Coordenação Acadêmica sobre a Matriz T, com formandos e '
          'pré-formandos.'),
         ('até 09/10', 'Edital da exposição publicado, com pedido de divulgação no Boletim.'),
         ('semana de 13/10', 'Episódio zero gravado.'),
         ('30/10', 'Aniversário da FAU: palestra, inauguração da exposição, episódio com '
          'convidado.'),
         ('13 ou 14/11', 'Festa com a Atlética. As aulas já param de 23 a 25/11 pelo Seminário '
          'Estudantil de Pesquisa, e o sábado evita mais uma discussão sobre aula perdida.'),
         ('07 a 18/12', 'Semana de TFG: episódio "Atravessar o TFG" e convite pra revista.'),
         ('19/12', 'Fim do semestre, com linha editorial e identidade da revista fechadas.'),
         ('início de 2027.1', 'Edição 01 da revista, em PDF.')])
  + caixa('Correção da proposta de setembro',
          'O concurso do CAU-BA fecha em 06/10 e premia prática de ensino adotada em 2025, '
          'inscrita por docente. O Mural não se encaixa, ao contrário do que a proposta dizia. A '
          'edição de 2027 pode servir, se o podcast tiver um professor como proponente ainda em '
          '2026.', VERMELHO),
  'mural-faufba.netlify.app', 'Calendário')

p8 = p8.replace('<div class="faixa"', '''<div class="fecho">
   <div class="regra" style="flex:1"><i>D E A</i><span>diretório dos estudantes de
   arquitetura · ufba</span></div>
   <img class="lgf" src="''' + logo.b64(INK) + '''" alt="Ágora">
   <img class="deaf" src="''' + parceiros.dea() + '''" alt="DEA FAUFBA">
 </div>
 <div class="faixa"''')

QA = ''
if '--qa' in sys.argv:
    QA = ('<script>document.fonts.ready.then(function(){var r=[].map.call('
          'document.querySelectorAll(".pg"),function(p,i){var f=p.querySelector(".faixa,.faixa-capa");'
          'var b=f?Math.round(p.getBoundingClientRect().bottom-f.getBoundingClientRect().bottom):-1;'
          'return (i+1)+":"+(p.scrollHeight-p.clientHeight)+"/"+b});'
          'document.body.insertAdjacentHTML("beforeend","<pre id=qa>"+r.join(" ")+"</pre>")})</script>')

html = ('<title>Podcast agora, revista em 2027 · Gestão Ágora · DEA FAUFBA</title>\n'
        '<style>' + g['FONTES'] + '</style>\n<style>' + g['CSS'] + '</style>\n'
        + '\n'.join([capa, p2, p3, p4, p5, p6, p7, p8]) + '\n' + QA)
saida = 'dea-outubro-qa.html' if QA else 'dea-outubro.html'
io.open(saida, 'w', encoding='utf-8').write(html)
print(saida, 'escrito')
