# Vitenskapelig kvalitetssikring - Norsk Økonomi 2026

**Dato:** 13. oktober 2026  
**Revisjonstype:** Dokument-, proveniens- og registerkontroll; begrenset innholdsmessig metoderevisjon.  
**Konklusjon:** Fullstendig rapportpakke samlet, men ikke vitenskapelig sluttgodkjent.

## 1. Kontrollert materiale

- Originale delrapporter 01 - 09 fra brukerens opplastede ZIP, inkludert originale data, kode, kilde- og evidensregistre.
- Delrapportene 10 - 12 fra nåværende prosjektfiler.
- Hovedrapport 1.1.0 fra originalpakken er beholdt som originalt referansedokument.
- Samlet ny rapport er en **redaksjonell integrasjon**: bevarer originalenes innhold og dokumenterer integrerte tillegg.

## 2. Maskinell kontroll av evidensregister 01 - 09

| Spor | Poster | Unike ID-er | Tomme primærkildefelt |
|---|---:|---:|---:|
| 01 | 24 | 24 | 0 |
| 02 | 23 | 23 | 0 |
| 03 | 28 | 28 | 0 |
| 04 | 25 | 25 | 0 |
| 05 | 30 | 30 | 0 |
| 06 | 34 | 34 | 0 |
| 07 | 40 | 40 | 0 |
| 08 | 32 | 32 | 0 |
| 09 | 40 | 40 | 0 |
| **Sum** | **276** | **276** | **0** |

Det er kontrollert at registrene kan leses, at ID-er er unike *innen hvert spor*, og at primærkildefeltene ikke er tomme. Kontroll av lenkers relevans, originaltabellenes faktiske verdier, ID-unikhet på tvers av alle registre og reproduksjon av hver analyse er **ikke** fullført. Spor 06 bruker komma som CSV-separator; de øvrige registrene bruker semikolon.

## 3. Faglige vurderinger

| Kontroll | Resultat | Status |
|---|---|---|
| Omfang 01 - 12 | Alle 12 delrapportfiler til stede | Bestått |
| Rågrunnlag 01 - 09 | Data og kildekode bevart | Bestått |
| Hypoteser og motmodeller | Beskrevet i delrapporter, ikke uavhengig testet | Delvis |
| Evidensregister 10 - 12 | Foreligger som tekstlige tabeller; ikke harmonisert med CSV-skjema | Åpen |
| Kausale analyser | Ingen uavhengig replikasjon gjennomført her | Åpen |
| Sammenlikning mellom definisjoner/årsvintager | Vesentlige ulikheter identifisert; ikke uttømmende tallrevisjon | Delvis |
| Samlet proveniens / SHA-256 | Nytt manifest produseres for distribusjon | Bestått |
| Ekstern fagfellevurdering | Ikke foretatt | Åpen |

## 4. Vesentlige forskningsforbehold

1. **Produktivitet:** Felles internasjonal panelanalyse av norsk markedsrettet fastlandsproduktivitet mot valgte land må reproduseres.
2. **Bolig og kapital:** Koblingen fra boligpris og gjeld til fortrengning av produktive investeringer krever identifiserbar kausal metode.
3. **Generasjoner:** Full kohortanalyse 1945 - 2005 med alder 25/30/35/40 er fortsatt ikke ferdigstilt.
4. **Skatt og mobilitet:** Formelle utflyttinger, kapitalbevegelser, latente gevinster og investeringsendringer er ulike størrelser.
5. **Offentlig ressursbruk:** Høy utgiftsandel alene identifiserer ikke ineffektivitet; Baumol-effekter, demografi og kvalitet må modelleres.
6. **Petroleum og statsfinanser:** Strukturelt underskudd, kontantuttak, fondets verdi og langsiktige inndekningsbehov skal holdes adskilt.
7. **Demografi:** SSB-framskrivinger er betingede, ikke sikre prognoser; regional boligfrigjøring er utestet.
8. **Systemmodell og reformer:** Tilbakekoblinger og radikale reformer er delvis hypoteser og scenarioer uten validert effektstørrelse.

## 5. Prioriterte oppgaver før vitenskapelig sluttpublisering

**P0:** Reproduser tallseriegrunnlaget og generer uavhengig analysekode; opprett samlet evidensregister for 01 - 12 med kildereferanse på hvert tall; harmoniser år, prisnivå og definisjoner; få uavhengig statistisk metodegjennomgang.

**P1:** Gjennomfør faktisk kausal identifikasjon for bolig/foreldrehjelp, skattevirkninger og arbeidsmarkedsmekanismer; bygg mikro- og makroscenarier med sensitivitetsintervaller; dokumenter kontrafaktiske modeller.

**P2:** Ekstern fagfellevurdering, DOI/arkivering, replikasjonspakke og publiseringsversjon etter revisjon.

## 6. Bruk av KI

Flere AI-verktøy og modeller kan inngå i forskningsprogrammets opprinnelige prosess, slik originalenes KI-erklæringer beskriver. Denne sammenstillingen er gjennomført med OpenAI ChatGPT til organisering, skriving av syntese, maskinell konsistenskontroll og pakking. KI har ikke utført uavhengig fagfellevurdering, verifisert alle primærkilder eller validert kausalestimatene. Endelig faglig ansvar og godkjenning må ligge hos navngitte menneskelige forfattere/fagkontrollører.

## 7. Integrasjon av delrapport 06C (23. oktober 2026)

**Omfang:** Nytt selvstendig mikroscenariokapittel om eierbeskatning av norske unoterte aksjer, kapitalbinding, emisjoner og hypotetiske utflyttingsalternativer. Tillegget utvider forskningstråd 05/06 og utfyller 06B; det erstatter ikke noen av 06Bs kausale forbehold.

**Replikasjon:** `delrapport_06C/modell_06C.py` og `delrapport_06C/modell_06C_utvidet.py` har henholdsvis 20 og 31 interne konsistenskontroller. De genererer åtte CSV-filer og et maskinlesbart sammendrag. `delrapport_06C/SHA256SUMS.txt` inneholder integritetsverdier for GitHub-innholdet. Sjekksummer kan avvike ved lokal linjeskiftkonvertering; kjør i et miljø med LF.

**Dokumentasjonsstatus:** A = dokumenterte regler fra offisielle rettskilder (tolkningen må kontrolleres av fagperson); D = illustrasjoner, nåverdier og scenarioer. Ingen observert individuell investeringsrespons eller norsk samlet kausaleffekt er beregnet. Den hypotetiske utenlandske beskatningen representerer ikke et identifisert land. `kilderegister_06C.json` skiller forslag fra gjeldende rett og logger en kildekonflikt om ikrafttredelsesår for formuesskatteutsettelse (2025/2026).

**Åpen kvalitetssikringsoppgave:** Verifiser rettsforståelsen mot full lovtekst og individuell skatteposisjon; dobbeltsjekk datakilder for satser og tidsgrenser; gjennomfør uavhengig reproduksjon og ekstern skattejuridisk og samfunnsøkonomisk vurdering før vitenskapelig sluttpublisering. Unngå å oversette likviditetsgap i D-modellen til anslått tap av investeringer, sysselsetting eller BNP uten kausal identifikasjon.

**KI-bruk:** OpenAI ChatGPT GPT-6 har bistått med utforming av rapport, beregningskode, kontrolltester, kildekatalog og GitHub-integrasjon; dette er ikke en uavhengig fagfellevurdering.

## 8. Redaksjonell revisjon v3.2 (23. oktober 2026)

**Omfang:** Teknisk og redaksjonell revisjon av nettsidene, ikke ny empirisk analyse. Ingen modellformler i 06B eller 06C er endret.

**Kontrollert mot primærkilder:** SPU 21 268 mrd. kroner ved utgangen av 2025 (NBIM); strukturelt underskudd 583,4 mrd. (2026) og 608,4 mrd. (2027) samt uttak 2,7 % (Nasjonalbudsjettet 2027); fruktbarhet 1,48 (2025) og 1,44 (2024) og alder ved første fødsel 30,4 år (SSB); formuesskattesatser, bunnfradrag 1,9 mill. og aksjerabatt 20 % for 2026 (Skatteetaten); 3 mill. kroner bunnfradrag for utflyttingsskatt (Finansdepartementet); satser og aksjerabatter 2021–2023 (Stortingets utredningsseksjon). Norges skatteandel 40,2 % (OECD 2024) er ikke kontrollert på nytt fordi landnotatet ikke var tilgjengelig.

**Maskinell kontroll:** `tools/kontroll.py --js` kontrollerer unike id-er, interne ankre, kildehenvisninger, at nøkkeltall er lik datasettet, versjonsnummer, at 06C-kalkulatoren i nettleseren gir samme tall som `modellresultater_06C_v02.json` (433 008 kr, 293 888 kr, 7 898 050 kr, 5 605 035 kr og paritet 37,74 %), og at 06B-scenariofilen stemmer med formlene i kapittel 5 og 6.

**KI-bruk:** Revisjonen er gjennomført med hjelp av en stor språkmodell (Anthropic Claude). Den har ikke utført fagfellevurdering. Endelig faglig ansvar ligger hos navngitte menneskelige forfattere og fagkontrollører.

**Gjenstår:** Punktene i kapittel 5 (P0–P2) er uendret.
