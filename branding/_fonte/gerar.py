"""Gera todas as peças do kit de marca em PNG.

Uso: python3 branding/_fonte/gerar.py [nome-da-peca ...]
Requer o Google Chrome instalado (usa o modo headless para tirar o print de cada peça).
"""
import re, subprocess, sys, pathlib

FONTE = pathlib.Path(__file__).resolve().parent
KIT = FONTE.parent
CHROME = 'google-chrome'

PASTAS = {
    'perfil-': 'perfil',
    'destaque-': 'instagram/destaques',
    'post-': 'instagram/posts',
    'story-': 'instagram/stories',
    'facebook-': 'meta-bm',
    'og-': 'meta-bm',
    'linkedin-': 'outros',
    'whatsapp-': 'whatsapp',
    'logo-': 'logo',
}

logo = (FONTE / 'logo-path.txt').read_text().strip()
html = (FONTE / 'kit.template.html').read_text().replace('%%LOGO%%', logo)
(FONTE / 'kit.html').write_text(html)

pecas = re.findall(r"A\['([^']+)'\] = \{ w: (\d+), h: (\d+)(, transparent: true)?", html)
filtro = set(sys.argv[1:])

for nome, w, h, transp in pecas:
    if filtro and nome not in filtro:
        continue
    pasta = next(p for pre, p in PASTAS.items() if nome.startswith(pre))
    saida = KIT / pasta / f'{nome}.png'
    saida.parent.mkdir(parents=True, exist_ok=True)
    cmd = [CHROME, '--headless', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1',
           '--allow-file-access-from-files', '--virtual-time-budget=6000',
           f'--window-size={w},{h}', f'--screenshot={saida}']
    if transp:
        cmd.append('--default-background-color=00000000')
    cmd.append((FONTE / 'kit.html').as_uri() + '#' + nome)
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f'{pasta}/{nome}.png  {w}x{h}')

# Símbolo em vetor, para gráficas e para a Meta (BM)
svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="120 106 272 285"><path fill="{}" d="' + logo + '"/></svg>\n'
for nome, cor in [('verde', '#22C58B'), ('branco', '#EAF0F7'), ('marinho', '#0A1628')]:
    (KIT / 'logo' / f'logo-simbolo-{nome}.svg').write_text(svg.format(cor))

# Corta as sobras transparentes dos logos (com respiro de 4%)
from PIL import Image
for png in (KIT / 'logo').glob('*.png'):
    im = Image.open(png)
    x0, y0, x1, y1 = im.getbbox()
    m = int(max(x1 - x0, y1 - y0) * .04)
    corte = im.crop((x0, y0, x1, y1))
    final = Image.new('RGBA', (corte.width + 2 * m, corte.height + 2 * m), (0, 0, 0, 0))
    final.paste(corte, (m, m))
    final.save(png)
