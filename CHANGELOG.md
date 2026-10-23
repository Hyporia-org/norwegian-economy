# Endringslogg

## v3.2 – 23. oktober 2026

### Rettet
- Nøkkeltallet «Strukturelt oljekorrigert underskudd» viste 579 mrd. (RNB 2026). Viser nå 608,4 mrd. (2027) og 583,4 mrd. (2026) fra Nasjonalbudsjettet 2027 [K138].
- 87 duplikate id-er på hovedsiden: kapitteloverskrifter (`kap-xx` → `kap-xx-h`), kort kildeliste i tråd 05 (`kxx` → `kxx-kort`) og underhypoteser H07-01–H07-14.
- Delrapport 10 brukte egne kildenumre K01–K07 som kolliderte med hovedrapportens K-numre. Disse heter nå D10-K01–D10-K07 og er lenket.
- YAML-metadata for delrapport 10 ble vist som overskrift (hovedside, Markdown og 06B). Erstattet med en lesbar metadataboks.
- Én H1 per side; del- og delrapporttitler er H2.
- Versjonsnummer samlet til 3.2 i forside, JSON-LD, Open Graph, fotnote, rapporthode og README.
- Hypotesefilteret telte forslag som åpne hypoteser; ny kategori «Forslag og simuleringsplaner». Ugyldig status for H10 rettet. Hypotesekortene lenker til riktig hypotese.
- Stolpediagrammer fremhever Norge (eller siste periode), ikke alltid første stolpe. Faste desimaler per indikator.
- 06B: desimalpunktum i tekst, manglende BOM i CSV, aktiv fane uten markering, manglende y-akse.
- 06C: engelske akseforkortelser («1.2m», «53k»), `lang="no"`, skrivefeil «reproducerbar».
- 06C-rapporten nevnte et konkret selskap ved navn; anonymisert.

### Nytt
- Felles toppmeny (`assets/felles.css`, `assets/felles.js`) på alle sider, med mobilmeny, nedtrekk for alle delrapporter, brødsmuler og «til toppen».
- Mørk visning følger systeminnstillingen og huskes mellom besøk, også i 06B og 06C.
- (?)-hjelpeknapper med forklaring, kilde og evidensklasse for nøkkeltall og alle modellparametere. Begrepsliste på forsiden.
- Forhåndsvalg i alle modeller som gjenskaper rapportens eksempler, og delbare scenarioer via adressen (`?preset=nb2027`, `?r=3&g=2` osv.).
- Fondsmodellen: uttak første år, uttaksregel (fast realvekst eller andel av fondet), petroleumsinnskudd, tømmeår, y-akse og uttaksandel.
- Boligmodellen: gjeld som andel av boligverdien før og etter fall.
- 06B: forhåndsvalg for faktisk toppsatsøkning 2022 (+0,25 pp), effektiv sats på aksjer (+0,4 pp), samlet BNP og Rings nullfunn. Kalenderår på aksen.
- 06C: forhåndsvalg for kapittel 10 og 11, merking av hvilke avsnitt hvert felt påvirker, kolonne for betalingsutsettelse og paritetsrad i sensitivitetstabellen.
- Innholdsfortegnelse og kapittelvelger gruppert etter del; titler gjort entydige (D10 · Sammendrag osv.).
- Nakne nettadresser i rapportteksten er gjort klikkbare.
- Tilleggskapittel «Tillegg v3.2» og kildene K171–K176 (Copenhagen Economics 2026, IMF Article IV 2025, OECD 2026, NOU 2015:1, Stortingets utredningsnotat om formuesskatt, Norsk Petroleum).
- Tydelig erklæring om bruk av LLM-basert KI øverst på alle sider og i README.
- `tools/kontroll.py` og GitHub Actions-arbeidsflyt for automatisk kontroll.

### Ikke endret
- Originaltekst i Del I og delrapport 10–12 er beholdt; tall som viser til RNB 2026 er forklart i tilleggskapitlet.
- Beregningene i 06B og 06C er uendret og gir samme kontrolltall som før.
