# -*- coding: utf-8 -*-
"""A logo da Agora que o Gabriel gerou no Flow, recortada do fundo branco e
servida em qualquer cor, como data URI. O recorte e feito uma vez e guardado
em logo-mask.png: dali em diante e so pintar o canal alfa."""
from PIL import Image
import base64, io, os

MASK = 'logo-mask.png'

def _mask():
    if not os.path.exists(MASK):
        src = Image.open('../images/1.jpg').convert('L')
        m = src.point(lambda v: 255 if v < 150 else 0).convert('L').crop(
            src.point(lambda v: 255 if v < 150 else 0).convert('L').getbbox())
        w, h = m.size
        lado = max(w, h); folga = int(lado * .04)
        tela = Image.new('L', (lado + 2*folga, lado + 2*folga), 0)
        tela.paste(m, (folga + (lado - w)//2, folga + (lado - h)//2))
        tela.save(MASK)
    return Image.open(MASK)

_cache = {}

def b64(cor, tam=900):
    """data URI da logo pintada nessa cor, com fundo transparente."""
    chave = (cor, tam)
    if chave in _cache:
        return _cache[chave]
    rgb = tuple(int(cor.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    a = _mask().resize((tam, tam), Image.LANCZOS)
    img = Image.new('RGBA', (tam, tam), rgb + (0,))
    img.putalpha(a)
    buf = io.BytesIO(); img.save(buf, 'PNG', optimize=True)
    _cache[chave] = 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()
    return _cache[chave]

def tag(cor, classe='mk', tam=900):
    return f'<img class="{classe}" alt="Ágora" src="{b64(cor, tam)}">'
