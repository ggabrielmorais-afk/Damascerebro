# -*- coding: utf-8 -*-
"""As logos do DEA e do DCE, tiradas do PDF final que o Gabriel montou.

O DCE veio em branco sobre preto, sem canal alfa: o proprio brilho vira a
transparencia, e dai sai em qualquer cor. O DEA e colorido, entao so o fundo
branco e recortado — a cor dele nao se mexe."""
from PIL import Image
import base64, io, os

def _dce_mask():
    im = Image.open('pdfimg_e43c108d.png').convert('L')
    return im.crop(im.point(lambda v: 255 if v > 40 else 0).getbbox())

def _dea_rgba():
    im = Image.open('pdfimg_78f8ed88.jpeg').convert('RGB')
    # recorta o branco de fundo, mantendo as cores da marca
    alfa = im.convert('L').point(lambda v: 0 if v > 235 else 255)
    out = im.convert('RGBA'); out.putalpha(alfa)
    return out.crop(out.getbbox())

_cache = {}

def _uri(img):
    buf = io.BytesIO(); img.save(buf, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()

def dce(cor='#14171A', alt=180):
    if ('dce', cor, alt) in _cache: return _cache[('dce', cor, alt)]
    m = _dce_mask()
    esc = alt / m.height
    m = m.resize((max(1, int(m.width*esc)), alt), Image.LANCZOS)
    rgb = tuple(int(cor.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
    img = Image.new('RGBA', m.size, rgb + (0,)); img.putalpha(m)
    _cache[('dce', cor, alt)] = _uri(img)
    return _cache[('dce', cor, alt)]

def dea(alt=180):
    if ('dea', alt) in _cache: return _cache[('dea', alt)]
    im = _dea_rgba()
    esc = alt / im.height
    im = im.resize((max(1, int(im.width*esc)), alt), Image.LANCZOS)
    _cache[('dea', alt)] = _uri(im)
    return _cache[('dea', alt)]
