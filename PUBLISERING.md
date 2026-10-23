# Publisering av Norsk Økonomi v3.2 til GitHub og hyporia.wiki

Instruks for den som publiserer (menneske eller KI-agent med tilgang til GitHub og webserveren).

## Mål

1. Endringene i v3.2 ligger på `main` i `Hyporia-org/norwegian-economy`, med release-tagg `v3.2`.
2. https://hyporia.wiki/norsk-okonomi/ viser v3.2, inkludert mappen `assets/`.

## Leveranse

- `norwegian-economy-v3.2.patch` – én commit laget med `git format-patch` mot `b788ce4` (siste commit på `main` 23. oktober 2026).
- `norwegian-economy-v3.2.zip` – hele repoet etter endringene, uten `.git`. Brukes hvis patchen ikke kan legges på.

## 1. GitHub

```sh
git clone https://github.com/Hyporia-org/norwegian-economy.git
cd norwegian-economy
git log -1 --format=%H          # skal være b788ce40aa8482c066c19a225d9ea4e16ccb300e
git am --keep-cr ../norwegian-economy-v3.2.patch   # --keep-cr er nødvendig: flere filer har CRLF-linjeskift
python3 tools/kontroll.py --js  # skal skrive «Alle kontroller bestått (inkl. JavaScript-paritet).»
(cd delrapport_06C && sha256sum -c SHA256SUMS.txt)
git push origin main
git tag -a v3.2 -m "Norsk Økonomi v3.2 – 23. oktober 2026"
git push origin v3.2
```

Hvis `main` har fått nye commits siden `b788ce4`: kjør `git am --keep-cr --3way`. Ved konflikter i `index.html`, behold begge sider og kjør kontrollen på nytt. Ikke bruk `--force`.

Hvis patchen ikke kan legges på: pakk ut zip-filen over en fersk klon (overskriv filer, ikke slett andre), kjør kontrollene og commit med meldingen fra patchen.

Lag deretter en GitHub-release fra taggen `v3.2` med teksten i `CHANGELOG.md` under «v3.2».

## 2. Nettsiden hyporia.wiki/norsk-okonomi/

1. Finn ut hvordan siden publiseres i dag. Sjekk i denne rekkefølgen: GitHub Pages-innstillinger for repoet, arbeidsflyter i `.github/workflows/` i dette eller et annet Hyporia-repo, og hosting-oppsettet for domenet hyporia.wiki (f.eks. Cloudflare Pages, Netlify eller egen server). Ikke gjett; spør eieren hvis det ikke kan avgjøres.
2. Publiser disse filene og mappene til `/norsk-okonomi/` med samme struktur:
   - `index.html`, `assets/felles.css`, `assets/felles.js`
   - `delrapport_06B/` og `delrapport_06C/` (alle filer)
   - `Norsk_Okonomi_Samlet_Forskningsrapport_2026_v2.md`, `VITENSKAPELIG_KVALITETSSIKRING.md`, `README.md`, `CHANGELOG.md`
3. `assets/` er ny og må med; uten den mangler meny, hjelpetekster, mørk visning og forhåndsvalg.
4. Tøm CDN-hurtigbuffer for `/norsk-okonomi/*` hvis siden ligger bak Cloudflare eller tilsvarende.

## 3. Kontroll etter publisering

Åpne og kontroller (også på mobil, under 960 px bredde):

- https://hyporia.wiki/norsk-okonomi/ – overskriften sier «versjon 3.2», nøkkeltallet for underskudd viser 608,4 mrd., og «Bruk av KI» står i statusboksen.
- https://hyporia.wiki/norsk-okonomi/?preset=rapport#stresstest – fondsverdi 15 962.
- https://hyporia.wiki/norsk-okonomi/?preset=nb2027#stresstest – fondsverdi 31 437.
- https://hyporia.wiki/norsk-okonomi/delrapport_06B/ – modell A viser 2,25 / 2,69 / 24,64 mrd. kr; `?preset=b-rapport` viser 163,7 og 911,1 mill. kr.
- https://hyporia.wiki/norsk-okonomi/delrapport_06C/?preset=kap10 – tabellen viser 5 000 kr i 2026 og 9 800 kr i 2027.
- Menyknappen («Meny») åpner og lukker menyen på mobil; «Mørk visning» virker og huskes ved ny innlasting; (?)-knappene viser forklaringer.
- Nettleserkonsollen viser ingen feil, og `assets/felles.js` og `assets/felles.css` gir HTTP 200.

Rapporter tilbake: commit-hash på `main`, lenke til release, hvordan nettsiden ble publisert, og resultatet av hvert punkt over.
