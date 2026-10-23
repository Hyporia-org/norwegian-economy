#!/usr/bin/env python3
"""Publiseringskontroll for Norsk Økonomi.

Kjør fra repo-roten:  python3 tools/kontroll.py
Med JavaScript-paritet (krever Node 18+):  python3 tools/kontroll.py --js

Kontrollerer:
  1. Unike id-er i alle HTML-sider.
  2. At alle interne ankre (#...) og lenker mellom sidene finnes.
  3. At alle [Kxx]-lenker peker til en kilde i kilderegisteret.
  4. At nøkkeltallene på forsiden er lik tallene i det innebygde datasettet.
  5. At versjonsnummeret er likt i README, forside og JSON-LD.
  6. (--js) At 06C-kalkulatoren og 06B-modellene gir rapportens kontrolltall.
Avslutter med kode 1 ved feil.
"""
import json, re, subprocess, sys, tempfile
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROT = Path(__file__).resolve().parent.parent
SIDER = ['index.html', 'delrapport_06B/index.html', 'delrapport_06C/index.html']
feil = []

class Samler(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids = []; self.hrefs = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.append(a['id'])
        if tag == 'a' and a.get('href'): self.hrefs.append(a['href'])

def les(rel):
    return (ROT / rel).read_text(encoding='utf-8')

parsed = {}
for side in SIDER:
    p = Samler(); p.feed(les(side)); parsed[side] = p
    dup = [k for k, v in Counter(p.ids).items() if v > 1]
    if dup: feil.append(f'{side}: duplikate id-er: {", ".join(dup[:15])}')

# 2. Ankre og lenker mellom sider
for side, p in parsed.items():
    mappe = (ROT / side).parent
    for h in p.hrefs:
        if h.startswith(('http://', 'https://', 'mailto:')): continue
        url, _, anker = h.partition('#')
        if url:
            mal = (mappe / url).resolve()
            if not mal.exists():
                feil.append(f'{side}: lenke til fil som mangler: {h}'); continue
            mal_rel = mal.relative_to(ROT).as_posix()
            if anker and mal_rel in parsed and anker not in parsed[mal_rel].ids:
                feil.append(f'{side}: anker mangler i {mal_rel}: #{anker}')
        elif anker and anker not in p.ids:
            feil.append(f'{side}: anker mangler: #{anker}')

# 3. Kildehenvisninger
hoved = les('index.html')
kilder = set(re.findall(r'<span id="(k\d+)"></span>', hoved))
for k in set(re.findall(r'href="#(k\d+)"', hoved)):
    if k not in kilder: feil.append(f'index.html: kildehenvisning uten kilde: {k}')
ulenket = re.findall(r'\[K\d+\](?!</a>)', re.sub(r'<script.*?</script>', '', hoved, flags=re.S))
if ulenket: feil.append(f'index.html: {len(ulenket)} kildehenvisninger uten lenke, f.eks. {ulenket[0]}')

# 4. Nøkkeltall mot datasett
obs = json.loads(re.search(r'const OBSERVASJONER\s*=\s*(\[.*?\]);', hoved, re.S).group(1))
def verdi(serie, periode):
    return next(float(o['verdi']) for o in obs if o['serie'] == serie and o['periode'] == periode)
def nb(x, d=1):
    return f'{x:,.{d}f}'.replace(',', ' ').replace('.', ',')
forventet = {
    'Fastlands-BNP · vekst 2025': nb(verdi('fastlandsvekst', '2025')) + ' %',
    'Boligandel av bruttoformue · 2024': nb(verdi('formue_bolig_andel', '2024')) + ' %',
    'Strukturelt oljekorrigert underskudd · 2027': nb(verdi('underskudd_nb2027', '2027')) + ' mrd.',
    'Samlet fruktbarhetstall · 2025': nb(verdi('fruktbarhet', '2025'), 2),
}
for etikett, tall in forventet.items():
    m = re.search(r'<div class="label">' + re.escape(etikett) + r'.*?</div><strong>(.*?)</strong>', hoved, re.S)
    if not m: feil.append(f'Nøkkeltall ikke funnet: {etikett}')
    elif m.group(1).strip() != tall: feil.append(f'Nøkkeltall «{etikett}»: viser {m.group(1)}, datasettet gir {tall}')

# 5. Versjon
readme = les('README.md')
v_readme = re.search(r'forskningsportal v(\d+\.\d+)', readme, re.I)
v_hero = re.search(r'versjon (\d+\.\d+) ·', hoved)
v_ld = re.search(r'"version": "(\d+\.\d+)"', hoved)
vs = {n: (m.group(1) if m else None) for n, m in [('README', v_readme), ('forside', v_hero), ('JSON-LD', v_ld)]}
if len(set(vs.values())) != 1 or None in vs.values(): feil.append(f'Versjonsnummer stemmer ikke: {vs}')

# 6. JavaScript-paritet
if '--js' in sys.argv:
    s06c = les('delrapport_06C/index.html')
    js = re.search(r"<script>\s*'use strict';(.*?)</script>", s06c, re.S).group(1)
    modell = js[:js.find('function chart')]
    test = r'''
const vals={};const document={getElementById:id=>({get value(){return vals[id]}})};
''' + modell + r'''
function kjør(o,f){for(const k of ids)vals[k]=init[k];Object.assign(vals,o);return model(f);}
const r10=kjør({nav:3000000,navgrowth:20});
const r11=kjør({});
console.log(JSON.stringify({wt10:Math.round(r10.wtSum),gap10:Math.round(r10.gapSum),pStay:Math.round(r11.pStay),pMove:Math.round(r11.pMove),parity:r11.parity}));
'''
    with tempfile.NamedTemporaryFile('w', suffix='.js', delete=False, encoding='utf-8') as f:
        f.write(test); navn = f.name
    ut = json.loads(subprocess.run(['node', navn], capture_output=True, text=True, check=True).stdout)
    fasit = json.loads(les('delrapport_06C/modellresultater_06C_v02.json'))
    sjekk = [('wt10', 'wealth_tax_total_10_years'), ('gap10', 'unfunded_private_liquidity_total'),
             ('pStay', 'pv_stay'), ('pMove', 'pv_move_at_20_percent_foreign')]
    for a, b in sjekk:
        if ut[a] != fasit[b]: feil.append(f'06C: HTML gir {a}={ut[a]}, Python-modellen {b}={fasit[b]}')
    if abs(ut['parity'] - fasit['parity_foreign_capital_gain_rate']) > 1e-9:
        feil.append(f'06C: paritet {ut["parity"]} ≠ {fasit["parity_foreign_capital_gain_rate"]}')
    # 06B: rapportens kontrollpunkter (kap. 5 og 6) mot scenario-CSV
    rader = [l.split(';') for l in les('delrapport_06B/scenarioer_10_ar.csv').lstrip('﻿').splitlines()[1:]]
    a_sum = sum(float(r[1]) for r in rader); b_sum = float(rader[-1][3])
    a_ber = sum(4500 * 0.5 / 1000 * 1000 * 1.02 ** (t - 1) for t in range(1, 11))
    b_ber = sum(sum(5 * 10 * (0.85 * 1.08) ** (t - k - 1) * 0.5 for k in range(1, t)) for t in range(1, 11))
    if abs(a_sum - a_ber) > 0.01 or abs(b_sum - b_ber) > 0.01:
        feil.append(f'06B: CSV ({a_sum:.2f}/{b_sum:.2f}) stemmer ikke med formelen ({a_ber:.2f}/{b_ber:.2f})')

if feil:
    print('KONTROLL FEILET:'); [print(' -', f) for f in feil]; sys.exit(1)
print('Alle kontroller bestått' + (' (inkl. JavaScript-paritet)' if '--js' in sys.argv else '') + '.')
