# Norsk Økonomi - Interaktiv forskningsportal v3.1

## Interaktive sider og publisering

- [Hovedside og samlet forskningsrapport](index.html).
- [Delrapport 06B – interaktive tiårsscenarioer](delrapport_06B/index.html).
- [Delrapport 06C – gründer, likviditet, emisjon og utflytting](delrapport_06C/index.html).

Delrapportene 01–12 er innarbeidet i hovedsidens samlede rapport og [Markdown-utgaven](Norsk_Okonomi_Samlet_Forskningsrapport_2026_v2.md). De foreligger ikke som tolv separate HTML-filer her. 06B og 06C har egne HTML-sider og egne rapport-, kilde- og datafiler. Lenker til begge finnes også på hovedsiden. Kildehenvisningene K01–K170 på hovedsiden fører til de tilhørende referansene.

Dette er foreløpige forskningsutkast og eksempler på en åpen forskningsprosess, ikke eksternt fagfellevurderte konklusjoner. Scenarioer er betingede regneeksempler, ikke prognoser, individuell skatterådgivning eller dokumenterte nasjonale årsaksvirkninger.

### Åpne lokalt

HTML-sidene trenger ikke et byggetrinn. Fra repositoryets rot:

```sh
python3 -m http.server 8000
```

Åpne `http://localhost:8000/`, `http://localhost:8000/delrapport_06B/` og `http://localhost:8000/delrapport_06C/`. Modellkontroller og replikasjon av 06C er dokumentert i [replikasjonsveiledningen](delrapport_06C/LES_MEG.md). Modellenes 20 + 31 kontroller er ikke uavhengig juridisk eller vitenskapelig fagfellevurdering.



## Innhold i release v3.1
Avsluttende konklusjon er lagt til som siste kapittel i Markdown og nettside. Interaktive datasett og modeller er beholdt. Normativ vurdering er merket separat fra kausale funn.


## Ny delrapport 06B

[Les delrapport 06B](delrapport_06B/delrapport_06B_kapitalflukt_tiar.md) om formuesskatt, utflytting og verdiskaping over ti år, eller åpne [den interaktive HTML-utgaven](delrapport_06B/index.html). [Kilderegister](delrapport_06B/kilderegister_06B.json), [observasjoner](delrapport_06B/observasjoner_utflytting.csv) og [tiårsscenarioer](delrapport_06B/scenarioer_10_ar.csv) følger med. Scenarioene bygger på antakelser og er ikke samlede norske kausalestimater.

## Ny delrapport 06C – Gründerens skatt, emisjoner og utflytting

[Les delrapport 06C](delrapport_06C/delrapport_06C_grunder_formuesskatt_utflytting_2026.md): et mikroperspektiv på personlige skatter for eiere av unoterte vekstselskaper, bundet varelager, kapitalinnhenting og utflyttingsskatt. [Interaktiv kalkulator](delrapport_06C/index.html), [kilderegister](delrapport_06C/kilderegister_06C.json), [Python-modeller](delrapport_06C/modell_06C_utvidet.py), [scenariodata og replikasjonsveiledning](delrapport_06C/LES_MEG.md) følger med. Modellen inneholder 20 + 31 interne konsistenskontroller. Alle tall om flyttealternativer er betingede scenarioer (D), ikke estimater for konkrete land, gründere eller nasjonale kausale effekter. Forskningsutkast, ikke fagfellevurdert.

---

# Norsk Økonomi 2026

## Oppdatert oppsummering - Norge har råd til å handle, men ikke til å utsette omstillingen

Norge er fortsatt et av verdens rikeste land. Vi har sterke institusjoner, høy levestandard, store naturressurser og en oljefondsformue som gir oss en økonomisk handlefrihet nesten ingen andre land har. Likevel avdekker forskningsprosjektet Norsk Økonomi 2026 alvorlige strukturelle utfordringer som kan undergrave vår framtidige velstand.

Hovedproblemet er ikke at Norge mangler penger. Problemet er at vi risikerer å bruke vår historiske rikdom til å opprettholde en økonomisk struktur som ikke utvikler tilstrekkelig framtidig verdiskaping.

Rapporten dokumenterer flere utviklingstrekk som, dersom de fortsetter og forsterker hverandre, kan føre til en langvarig svekkelse av norsk konkurransekraft, økonomisk mobilitet og velferdsstatens finansieringsgrunnlag.

### 1. Vi blir rikere på papiret, men skaper ikke nødvendigvis tilsvarende nye verdier

Norsk produktivitetsvekst har avtatt over tid. OECD peker på at vårt produktivitetsforsprang er blitt mindre, samtidig som Norge har utfordringer med å utvikle og skalere nye virksomheter.

En stor del av husholdningenes formue er bundet i eiendom. I 2024 utgjorde primær- og sekundærboliger omtrent 62 prosent av husholdningenes beregnede bruttoformue.

Når eksisterende boliger stiger i verdi, oppstår betydelige formuesgevinster for eierne. Men prisstigning på eksisterende eiendom skaper ikke automatisk flere boliger, høyere produksjonskapasitet eller økt nasjonal produktivitet.

Det gjenstår å fastslå hvor mye investering i produktiv virksomhet som faktisk fortrenges av bolig- og eiendomsmarkedet. Likevel er det grunn til å stille et grunnleggende spørsmål: Har vi utformet et økonomisk system hvor det er mer attraktivt å eie eksisterende verdier enn å skape nye?

### 2. Unge risikerer å arve en stadig høyere økonomisk inngangsbillett

Forskningsmaterialet viser betydelige forskjeller i unges muligheter til å etablere seg på boligmarkedet.

Blant undersøkte årskull hadde 50 prosent av unge med foreldre i de øverste to prosentene av formuesfordelingen vært registrert med boligformue innen fylte 25 år, sammenlignet med 20 prosent av unge med foreldre i nederste formueskvartil.

Dette viser at familiens økonomiske utgangspunkt har stor betydning for muligheten til å etablere seg.

Boligpriser, egenkapitalkrav og gjeld kan også påvirke unges evne til å starte bedrifter, ta økonomisk risiko og etablere familie. Størrelsen på disse årsakssammenhengene er ennå ikke tilstrekkelig kartlagt.

Et samfunn hvor foreldrenes formue får stadig større betydning for barnas økonomiske muligheter, risikerer å svekke nettopp den sosiale mobiliteten som har vært en av Norges største styrker.

### 3. Offentlig sektor må vurderes etter resultatene, ikke bevilgningene

Norge har svært høye offentlige utgifter relativt til fastlandsøkonomien. Noe av dette skyldes omfattende velferdsordninger, høyt lønnsnivå, geografi og en aldrende befolkning.

Dette betyr ikke at offentlig sektor som helhet er ineffektiv. Men det betyr heller ikke at økte bevilgninger automatisk gir bedre tjenester.

Rapporten peker på behovet for å undersøke sammenhengen mellom ressursbruk, produktivitet og faktiske samfunnsresultater langt grundigere.

En velferdsstat blir ikke bærekraftig av å bruke stadig mer penger. Den blir bærekraftig av å levere gode tjenester med en ressursbruk økonomien kan bære over tid.

Norge må derfor flytte oppmerksomheten fra størrelsen på budsjettene til målbare resultater, effektive prosesser og langsiktig samfunnsnytte.

### 4. Demografien vil forsterke de økonomiske utfordringene

Norge står overfor en betydelig aldring av befolkningen.

Fødselstallet per kvinne var 1,48 i 2025, langt under reproduksjonsnivået. Samtidig vil antallet eldre øke kraftig, og behovet for helse- og omsorgstjenester vokse.

Dette skaper en utfordring som ikke kan løses med finansiering alene. Flere eldre trenger tjenester som krever arbeidskraft, samtidig som konkurransen om de yrkesaktive øker.

Dersom produktiviteten ikke forbedres, kan en stadig større andel av arbeidskraften måtte brukes til å opprettholde eksisterende tjenester.

Oljefondet kan betale lønninger, men det kan ikke trylle fram arbeidskraft eller erstatte manglende produktivitetsvekst.

### 5. Oljefondet kan bli en sovepute

Det strukturelle oljekorrigerte underskuddet i forslaget til statsbudsjett for 2027 er 608,4 milliarder kroner.

Oljefondet gir Norge muligheten til å finansiere omfattende velferdsordninger og håndtere økonomiske omstillinger. Men det gjør oss også mindre utsatt for de umiddelbare økonomiske konsekvensene av svak produktivitetsvekst og kostnadsøkninger.

Det er foreløpig ikke empirisk dokumentert at oljefondet faktisk fører til at nødvendige reformer blir utsatt. Likevel representerer denne mulige mekanismen en vesentlig langsiktig risiko.

Et land med mindre finansielle reserver ville måttet håndtere ubalanser raskere. Norge kan fortsette lenger uten å foreta de samme tilpasningene.

Vi risikerer dermed å bruke oljefondet til å finansiere problemene i stedet for å løse dem.

Og jo lenger nødvendige tilpasninger utsettes, desto mindre kan handlingsrommet bli når endringene til slutt må gjennomføres.

### 6. Små justeringer er neppe tilstrekkelig dersom problemene er strukturelle

Norsk økonomisk politikk preges ofte av årlige omfordelinger, mindre endringer i skatter og avgifter og nye støtteordninger.

Slike tiltak kan ha legitime og viktige formål. Men dersom utfordringene skyldes grunnleggende insentiver i kapitalmarkedet, boligsystemet, arbeidsmarkedet og offentlig styring, vil marginale budsjettendringer alene neppe være tilstrekkelige.

Forskningsrapporten peker derfor på behovet for å undersøke mer omfattende reformer som kan:

- Gjøre investering i ny produktiv virksomhet mer attraktivt.
- Redusere unges økonomiske etableringsbarrierer og avhengighet av arv.
- Gjøre skattesystemet enklere, mer forutsigbart og mindre vridende.
- Øke produktiviteten og resultatansvaret i offentlig sektor.
- Styrke arbeidstilbudet og gjøre det lettere for unge å komme inn i arbeidslivet.
- Sikre at framtidige generasjoners interesser får større vekt i dagens økonomiske beslutninger.

Reformenes virkninger må dokumenteres før de gjennomføres i stor skala. Store reformer er ikke automatisk gode reformer.

## Samlet konklusjon: Velstand er ikke det samme som bærekraft

Norge er ikke i økonomisk kollaps. Vi har fortsatt betydelige fortrinn, og flere indikatorer viser positiv utvikling. Men nettopp dagens rikdom kan gjøre det vanskelig å se hvor alvorlige langsiktige utfordringer som bygger seg opp.

Produktivitet, kapitalallokering, boligmarked, entreprenørskap, demografi og offentlige finanser kan ikke behandles som uavhengige problemer. De påvirker hverandre og kan skape selvforsterkende utviklingsforløp.

Forskningen har ennå ikke fastslått hvor sterke alle disse mekanismene er. Men vi vet nok til å slå fast at det vil være risikabelt å basere framtidens velstand på en videreføring av dagens utvikling uten betydelige tilpasninger.

Den største risikoen for norsk økonomi er ikke et plutselig sammenbrudd. Det er en langsom svekkelse der vi opprettholder levestandarden med stadig større finansielle overføringer, mens grunnlaget for framtidig verdiskaping og økonomisk selvstendighet gradvis blir svakere.

Vi kan ende med å overlate til kommende generasjoner en økonomi med høye kostnader, store offentlige forpliktelser, krevende etableringsvilkår og et stadig større behov for finansiering fra oppspart petroleumsformue.

Det er ikke mangel på økonomiske ressurser som hindrer Norge i å endre kurs. Vi har kapitalen, kompetansen, institusjonene og tiden som trengs.

Norge har råd til å gjennomføre omstillingen nå. Spørsmålet er hvor lenge vi har råd til å la være.

Oljefondets viktigste oppgave bør ikke være å gjøre det mulig å opprettholde dagens økonomiske modell lengst mulig. Det bør være å gi oss tid og handlingsrom til å bygge en økonomi med sterkere produktivitet, større økonomisk mobilitet og et mer robust grunnlag for framtidig velferd.

Vi må slutte å forveksle oppspart rikdom med framtidig verdiskaping.

Det er dette veivalget som vil avgjøre hvilken norsk økonomi neste generasjon overtar.
