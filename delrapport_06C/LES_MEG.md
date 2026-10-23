# Delrapport 06C v0.2 – Gründerens skattemessige flyttepunkt

**Hyporia / Norsk Økonomi / 22. oktober 2026**

## Hva pakken undersøker

1. Norsk formuesskatt og likviditetsbelastning for eier av unotert norsk AS.
2. Separate skattemessige selskapsverdier og markedsverdier ved utflyttingsskatt.
3. Skattekommisjonens satsalternativer 0,25–0,75 %, som **ikke** er vedtatt lov.
4. En tiårig modell for skattebelastning og udekket personlig likviditet.
5. En *hypotetisk* nåverdianalyse av å bli skattemessig bosatt i Norge eller flytte ut og selge aksjene på et senere tidspunkt. Utenlandsk skatteregime er ikke knyttet til et bestemt land.
6. Kapitalinnhenting som kan endre gründerens formuesskatt uten privat aksjesalg.
7. Forholdet mellom rapporterte skattedrevne utflyttinger og empiriske nullfunn om foretaksinvestering.

## Viktige resultater i grunnscenarioene (D)

- NOK 3 mill. i skattemessig selskapsformue, 20 % nominell årlig NAV-vekst og 25 000 kroner i tilgjengelig brutto utbytte gir **433 008 kroner** samlet 10-årig formuesskatt, **293 888 kroner** i hypotetisk samlet udekket personlig beløp. Skatteår 2026–2035, faste 2026-regler.
- Skattekommisjonens foreslåtte 0,75 %-scenario med null aksjerabatt gir i den forenklede modellen høyere årlig formuesskatt enn 2026-modellen for enkelte eiere med skattemessig selskapsformue under 8 mill. kroner. Kryssingspunktet er matematisk 8 mill. kroner.
- Nåverdianalyse med valgte forutsetninger har paritet rundt **37,7 %** hypotetisk utenlandsk aksjegevinstskatt på verdistigning *etter* utflytting. Dette er **ikke** en faktisk utenlandsk skattesats eller et råd om utflytting.

## Filer

| Fil | Rolle |
|---|---|
| `delrapport_06C_grunder_formuesskatt_utflytting_2026.md` | Full norsk forskningsanalyse inkl. kapitler 9–16 i v0.2 |
| `index.html` | Interaktiv selvstendig HTML-modell, uten eksterne avhengigheter |
| `modell_06C.py` | V0.1 grunnmodell med 20 tester, produserer 3 CSV |
| `modell_06C_utvidet.py` | V0.2 utvidet modell med 31 tester, produserer 5 nye CSV og JSON |
| `scenario_formue_2026.csv` | Årlige nivåer og utbyttebehov |
| `scenario_exitskatt_2026.csv` | Markedsverdier og hypotetisk utflyttingsskatt |
| `scenario_likviditetsgrense_2026.csv` | Årlig utdelingsgrense mot skatteverdi |
| `scenario_kommisjonsreform.csv` | Statisk alternativ sammenlikning med NOU 2026:9 |
| `scenario_emisjon_og_eierskatt.csv` | Emisjon, eierutvanning og økt formuesskatt uten personlig realisasjon |
| `scenario_vekst_likviditet.csv` | Ti år med skatte- og likviditetsbane |
| `scenario_flyttebeslutning_naverdi.csv` | Hypotetisk nåverdiforskjell etter utenlandsk gevinstskattesats |
| `scenario_betaling_og_tid.csv` | Årlig tabell for skatt og betaling av utflyttingsskatt |
| `modellresultater_06C_v02.json` | Kontrollverdier for Python/HTML-paritet |
| `kilderegister_06C.json` | Lov-, NOU- og forskningskilder samt merknad om kildekonflikt |
| `SHA256SUMS.txt` | Integritetskontroll for filene i pakken |

## Reproduksjon

```bash
python3 modell_06C.py
python3 modell_06C_utvidet.py
sha256sum -c SHA256SUMS.txt
```

Ved regenerering av CSV/JSON kan plattformspesifikke linjeskift (CRLF/LF) forandre SHA256 uten at tallene er endret. Sammenlign derfor også CSV-data og modellkontroller hvis det skjer.

## Faglig avgrensning og evidens

- **A:** Kilder til faktisk gjeldende rett per 22. oktober 2026.
- **B/C-kandidat:** Publiserte forskningsartikler og arbeidsnotater (må valideres etter hver studies design).
- **D:** Hypotetiske beregninger og scenarioer, ikke observert individuell eller nasjonal kausal effekt.
- Det finnes ingen universell rasjonell utflyttingsdato. Beslutningen avhenger av land, kontantstrøm, forventninger, skattestatus, skatteavtaler og fremtidige faktiske regler.
- Norsk utflyttingsskatt på samme opparbeidede gevinst sammenliknes med fremtidig norsk gevinstskatt som *alternative* rettslige scenarioer, ikke som to additive norske gevinsskatter.
- Fagansvarlig skattejurist og samfunnsøkonom bør gjennomgå regulatorisk tolkning og data før offisiell publisering.

## Særskilt kildekontroll

Skatte-ABC F-20-13 oppgir 2025 som virkningstidspunkt for betalingsutsettelse, men **lovvedtak 13 (2025–2026) del IV og regjeringens regelendringsoversikt fastslår 2026**. Opplysningen er bevart som kildekonflikt. Se `kilderegister_06C.json`.

## Forslag til GitHub-integrasjon

Legg mappen i `Hyporia-org/norwegian-economy` som `delrapport_06C/`. Oppdater rotens `README.md`, og legg lenker i portalen fra delrapport 05, 06, 06B og kildekontroll/metode 01. Ikke skriv inn scenariene som kausalt estimerte nasjonale tap.

## KI-bruk

OpenAI ChatGPT (GPT-6) brukt til kildegjennomgang, modellering, kode, rapportutkast og konsistenskontroll. Opplysningene er verifisert så langt offentlige kilder og kontrollberegninger tillater. Ingen uavhengig fagfellevurdering er gjennomført.