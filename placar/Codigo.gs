/* =====================================================================
   MURAL FAUFBA — código da planilha
   Cole este arquivo em script.google.com, logado como faufba.dea@gmail.com.
   Preencha os dois IDs abaixo e publique como aplicativo da web.

   Regra de uso: cada matrícula responde no máximo LIMITE temas por semestre.
   A matrícula chega ao script, vira uma marca embaralhada e é descartada.
   Ela nunca é gravada em lugar nenhum, e a marca não volta a ser matrícula.
   Relatos sensíveis e "quero ajudar" não carregam matrícula nem código.
   ===================================================================== */

// ID da planilha PÚBLICA (placar, sugestões, quero ajudar, vagas).
// O ID é o trecho entre /d/ e /edit no endereço da planilha.
var ID_PLACAR  = 'COLE_AQUI_O_ID_DA_PLANILHA_DO_PLACAR';

// ID de uma SEGUNDA planilha, separada, só pros relatos sensíveis.
// Compartilhe essa com uma ou duas pessoas, nominalmente. Mais ninguém.
var ID_RELATOS = 'COLE_AQUI_O_ID_DA_PLANILHA_DE_RELATOS';

// Teto de temas por pessoa por semestre. Precisa bater com o `limite` do app.
var LIMITE = 3;

// SEGREDO DA CASA. Troque por uma frase comprida e sem sentido, qualquer uma,
// e nunca mude depois, senão as marcas antigas param de bater com as novas.
// É ele que impede alguém com a planilha na mão de descobrir as matrículas.
var SEGREDO = 'TROQUE_ESTA_FRASE_POR_OUTRA_QUALQUER_E_NUNCA_MAIS_MUDE';

/* Transforma a matrícula numa marca que não volta atrás.
   A mesma matrícula sempre vira a mesma marca, então dá pra contar pessoas
   e barrar repetição. A marca não é matrícula e não chega a nome nenhum. */
function marca(matricula) {
  var m = String(matricula || '').replace(/\D/g, '');
  if (!m) return '';
  var bytes = Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, SEGREDO + '|' + m, Utilities.Charset.UTF_8);
  var hex = '';
  for (var i = 0; i < bytes.length; i++) {
    var b = (bytes[i] < 0 ? bytes[i] + 256 : bytes[i]).toString(16);
    hex += (b.length === 1 ? '0' : '') + b;
  }
  return hex.substring(0, 20);
}

/* Confere uma matrícula sem abrir a planilha de nomes de ninguém.
   Rode daqui mesmo: escreva a matrícula entre as aspas, salve, e execute
   esta função. O resultado aparece em Execuções, no menu da esquerda. */
function conferir() {
  var MATRICULA = '000000000';
  var SEMESTRE  = '2026.2';
  var n = jaUsou(marca(MATRICULA), SEMESTRE);
  Logger.log('A matrícula ' + MATRICULA + ' respondeu ' + n + ' tema(s) em ' + SEMESTRE + '.');
  return n;
}

/* ------------------------- recebe respostas ------------------------- */
function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);
    var agora = new Date();

    if (d.tipo === 'relato') {
      aba(ID_RELATOS, 'relatos', ['quando', 'o que', 'onde', 'como seguir', 'contato', 'texto'])
        .appendRow([agora, lista(d.oque), lista(d.onde), d.seguir || '', d.contato || '', d.texto || '']);
      return resposta({ ok: true });
    }

    if (d.tipo === 'placar') {
      var id = String(d.id || ''), sem = String(d.semestre || '');
      var mk = marca(d.matricula);
      if (!mk) return resposta({ ok: false, motivo: 'sem matricula' });
      if (jaUsou(mk, sem) >= LIMITE) {
        aba(ID_PLACAR, 'recusados', ['quando', 'marca', 'codigo', 'semestre', 'tema', 'motivo'])
          .appendRow([agora, mk, id, sem, d.temaNome || '', 'acima do teto de ' + LIMITE + ' temas']);
        return resposta({ ok: false, motivo: 'limite' });
      }
      aba(ID_PLACAR, 'envios', ['quando', 'marca', 'codigo', 'semestre', 'tema', 'itens'])
        .appendRow([agora, mk, id, sem, d.temaNome || '', lista(d.itens)]);

      var s = aba(ID_PLACAR, 'respostas', ['quando', 'tema', 'tema nome', 'item', 'turno', 'linha', 'marca']);
      var itens = d.itens || [];
      for (var i = 0; i < itens.length; i++) {
        s.appendRow([agora, d.tema || '', d.temaNome || '', itens[i], d.turno || '',
                     i === 0 ? (d.extra || '') : '', mk]);
      }
    } else if (d.tipo === 'sugestao') {
      aba(ID_PLACAR, 'sugestoes', ['quando', 'sugestao', 'pode ajudar', 'codigo'])
        .appendRow([agora, d.texto || '', d.ajudo ? 'sim' : '', String(d.id || '')]);
    } else if (d.tipo === 'ajudar') {
      aba(ID_PLACAR, 'ajudar', ['quando', 'como', 'tempo', 'contato'])
        .appendRow([agora, lista(d.como), d.tempo || '', d.contato || '']);
    } else if (d.tipo === 'vaga') {
      aba(ID_PLACAR, 'vagas', ['quando', 'vaga', 'codigo'])
        .appendRow([agora, d.vaga || '', String(d.id || '')]);
    }
    return resposta({ ok: true });
  } catch (err) {
    return resposta({ ok: false, erro: String(err) });
  }
}

/* quantos temas esta marca já respondeu neste semestre */
function jaUsou(mk, sem) {
  if (!mk) return 0;
  var ss = SpreadsheetApp.openById(ID_PLACAR);
  var s = ss.getSheetByName('envios');
  if (!s || s.getLastRow() < 2) return 0;
  var v = s.getRange(2, 2, s.getLastRow() - 1, 3).getValues();
  var n = 0;
  for (var i = 0; i < v.length; i++) {
    if (String(v[i][0]) === mk && String(v[i][2]) === sem) n++;
  }
  return n;
}

/* ------------------------- devolve o placar ------------------------- */
/* Os relatos NUNCA saem por aqui. Esta função não abre a planilha deles.
   Os códigos dos estudantes também não saem: só os totais. */
function doGet(e) {
  /* Consulta de cota: o app pergunta quantos temas uma matrícula já respondeu,
     antes de deixar enviar. Devolve só o número, mais nada. */
  if (e && e.parameter && e.parameter.m) {
    var quantos = jaUsou(marca(e.parameter.m), String(e.parameter.s || ''));
    return devolve({ usos: quantos }, e.parameter.cb);
  }

  var out = { placar: {}, vagas: {}, sugestoes: [], relatos: [], excluidas: 0, pessoas: 0 };
  try {
    var ss = SpreadsheetApp.openById(ID_PLACAR);

    var r = ss.getSheetByName('respostas');
    if (r && r.getLastRow() > 1) {
      var v = r.getRange(2, 1, r.getLastRow() - 1, 6).getValues();
      for (var i = 0; i < v.length; i++) {
        var tema = String(v[i][1]), item = String(v[i][3]), turno = String(v[i][4]), linha = String(v[i][5]);
        if (!tema || !item) continue;
        if (!out.placar[tema]) out.placar[tema] = {};
        if (!out.placar[tema][item]) out.placar[tema][item] = { manha: 0, tarde: 0, noite: 0, total: 0 };
        var alvo = out.placar[tema][item];
        alvo.total++;
        if (turno === 'manha' || turno === 'tarde' || turno === 'noite') alvo[turno]++;
        if (linha) out.relatos.push({ th: String(v[i][2]), t: linha });
      }
    }

    /* Quantos estudantes distintos responderam. Conta marcas diferentes,
       que é contar matrículas diferentes sem saber nenhuma delas. */
    var en = ss.getSheetByName('envios');
    if (en && en.getLastRow() > 1) {
      var ev = en.getRange(2, 2, en.getLastRow() - 1, 1).getValues();
      var vistos = {};
      for (var p = 0; p < ev.length; p++) { var c = String(ev[p][0]); if (c) vistos[c] = 1; }
      out.pessoas = Object.keys(vistos).length;
    }

    var rec = ss.getSheetByName('recusados');
    if (rec && rec.getLastRow() > 1) out.excluidas = rec.getLastRow() - 1;

    var g = ss.getSheetByName('vagas');
    if (g && g.getLastRow() > 1) {
      var gv = g.getRange(2, 2, g.getLastRow() - 1, 1).getValues();
      for (var j = 0; j < gv.length; j++) {
        var nome = String(gv[j][0]); if (!nome) continue;
        out.vagas[nome] = (out.vagas[nome] || 0) + 1;
      }
    }

    var u = ss.getSheetByName('sugestoes');
    if (u && u.getLastRow() > 1) {
      var uv = u.getRange(2, 2, u.getLastRow() - 1, 2).getValues();
      for (var k = uv.length - 1; k >= 0 && out.sugestoes.length < 40; k--) {
        if (uv[k][0]) out.sugestoes.push({ t: String(uv[k][0]), h: String(uv[k][1]) === 'sim' });
      }
    }
    out.relatos = out.relatos.reverse().slice(0, 40);
  } catch (err) {
    out.erro = String(err);
  }

  return devolve(out, e && e.parameter && e.parameter.cb);
}

function devolve(obj, cb) {
  var texto = JSON.stringify(obj);
  if (cb) {
    return ContentService.createTextOutput(cb + '(' + texto + ')')
      .setMimeType(ContentService.MimeType.JAVASCRIPT);
  }
  return ContentService.createTextOutput(texto).setMimeType(ContentService.MimeType.JSON);
}

/* ------------------------------ apoio ------------------------------ */
function aba(id, nome, cabecalho) {
  var ss = SpreadsheetApp.openById(id);
  var s = ss.getSheetByName(nome);
  if (!s) { s = ss.insertSheet(nome); s.appendRow(cabecalho); s.setFrozenRows(1); }
  return s;
}
function lista(x) { return (x && x.join) ? x.join(' | ') : (x || ''); }
function resposta(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}
