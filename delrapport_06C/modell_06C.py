#!/usr/bin/env python3
"""Delrapport 06C: Forenklet, reproduserbar norsk skatteberegning for 2026.

Beregningen er en dokumentert TYPE D-scenariomodell og IKKE et faktisk
skatteoppgjør eller en anbefaling om skattemessig emigrasjon. Alle beløp NOK.

Antakelser: enslig, direkte eneaksjonær i et unotert norsk AS, ingen privat
formue/gjeld, maksimal kommunal sats 0,35 %, ingen skjermingsfradrag,
full ordinær inntektsskatt på utbytte, netto selskapsformue verdsatt til
selskapsformuesverdi på riktig lovbestemt referansetidspunkt.

Kilder: Skatteetaten, 'Forskuddsutskrivingen 2026', Skatte-ABC A-4 og U-10,
'Skattesats for aksjer 2026' og 'Skattemessig emigrasjon'.
"""
from __future__ import annotations

import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

D = Decimal
ZERO = D("0")
FORMUE_BUNN = D("1900000")
FORMUE_TRINN_2 = D("21500000")
AKSJER_VERDIANDEL = D("0.80")
FORMUE_SATS_1 = D("0.010")
FORMUE_SATS_2 = D("0.011")
AKSJE_SKATT = D("0.3784")
SELSKAP_SKATT = D("0.22")
EXITSKATT_BUNN = D("3000000")


def num(value: object) -> Decimal:
    return D(str(value))


def nok(value: Decimal) -> int:
    """Kun utdataformat; skatteberegning gjøres med full Decimal-presisjon."""
    return int(value.quantize(D("1"), rounding=ROUND_HALF_UP))


def formuesskatt_2026(skattemessig_selskapsnetto: object,
                      eierandel: object = "1",
                      annen_skattepliktig_nettoformue: object = "0") -> Decimal:
    """Illustrert 2026-skatt for person med unoterte norske aksjer.

    'Annen nettoformue' er allerede vurdert til individuell skatteverdi
    etter korrekte rabatter, og negativ privat gjeldsfordeling modelleres IKKE.
    """
    v = max(ZERO, num(skattemessig_selskapsnetto))
    share = num(eierandel)
    if not ZERO <= share <= D("1"):
        raise ValueError("eierandel må ligge mellom 0 og 1")
    total = AKSJER_VERDIANDEL * share * v + num(annen_skattepliktig_nettoformue)
    lower = max(ZERO, min(total, FORMUE_TRINN_2) - FORMUE_BUNN)
    upper = max(ZERO, total - FORMUE_TRINN_2)
    return lower * FORMUE_SATS_1 + upper * FORMUE_SATS_2


def brutto_utbytte_for_formuesskatt(formuesskatt: object) -> Decimal:
    """Uten skjerming, aksjonærlån, kapitaltilbakebetaling eller annen likviditet."""
    return num(formuesskatt) / (D("1") - AKSJE_SKATT)


def skattemessig_resultat_for_utbytte(formuesskatt: object) -> Decimal:
    """NY skattbar bedriftsinntekt før 22 % selskapsskatt, hvis hele utbyttet må nyinntjenes."""
    return brutto_utbytte_for_formuesskatt(formuesskatt) / (D("1") - SELSKAP_SKATT)


def exitskatt_2026(aksjemarkedsverdi: object,
                    inngangsverdi: object = "100000",
                    ovrig_latent_nettogevinst: object = "0") -> Decimal:
    """Forenklet exitskatt ved skattemessig utflytting, en personlig eier.

    Kun latente gevinster opptjent under norsk skattemessig bosted, der
    kvalifiserende øvrige gevinster/tap er samlet netto og lovlig fradragsberettiget.
    Særlige regler, skjerming og EØS/non-EØS tapsforskjeller er utelatt.
    """
    gain = num(aksjemarkedsverdi) - num(inngangsverdi) + num(ovrig_latent_nettogevinst)
    return max(ZERO, gain - EXITSKATT_BUNN) * AKSJE_SKATT


def annual_no_interest_exit_installment(exitskatt: object) -> Decimal:
    return num(exitskatt) / D("12")



def likviditetsgrense_2026(maks_brutto_utbytte: object,
                           eierandel: object = "1",
                           annen_skattepliktig_nettoformue: object = "0") -> Decimal:
    """Selskapsformue der formuesskatten akkurat kan finansieres av et gitt utbytte.

    Basert på at all modellert skatt må dekkes gjennom fullt skattlagt
    utbytte. Dette er ingen juridisk vurdering av lovlig utbyttegrunnlag.
    """
    div = max(ZERO, num(maks_brutto_utbytte))
    share = num(eierandel)
    if not ZERO < share <= D("1"):
        raise ValueError("eierandel må være >0 og <=1")
    kap = div * (D("1") - AKSJE_SKATT)
    trinn1skatt = (FORMUE_TRINN_2 - FORMUE_BUNN) * FORMUE_SATS_1
    if kap <= trinn1skatt:
        upper_wealth = FORMUE_BUNN + kap / FORMUE_SATS_1
    else:
        upper_wealth = FORMUE_TRINN_2 + (kap - trinn1skatt) / FORMUE_SATS_2
    return max(ZERO, (upper_wealth - num(annen_skattepliktig_nettoformue)) /
                      (AKSJER_VERDIANDEL * share))

def _generate() -> None:
    folder = Path(__file__).resolve().parent
    w_values = [2_000_000, 2_375_000, 3_000_000, 5_000_000, 9_000_000,
                10_000_000, 15_000_000, 25_000_000, 26_875_000,
                30_000_000, 50_000_000, 100_000_000]
    with (folder / "scenario_formue_2026.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["skattemessig_selskapsnetto_NOK", "skattemessig_aksjeformue_NOK",
                         "formuesskatt_NOK", "brutto_utbytte_til_skatt_NOK",
                         "ny_resultat_for_utbytte_for_selskapsskatt_NOK", "evidenskategori"])
        for value in w_values:
            tax = formuesskatt_2026(value)
            writer.writerow([value, nok(num(value)*AKSJER_VERDIANDEL), nok(tax),
                             nok(brutto_utbytte_for_formuesskatt(tax)),
                             nok(skattemessig_resultat_for_utbytte(tax)), "D"])

    m_values = [1_000_000, 3_100_000, 4_000_000, 5_000_000,
                10_000_000, 20_000_000, 40_000_000, 100_000_000]
    with (folder / "scenario_exitskatt_2026.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["aksjemarkedsverdi_NOK", "aksjeinngangsverdi_NOK",
                         "illustrert_latent_gevinst_NOK", "exitskatt_NOK",
                         "aarlig_12del_uten_renter_NOK", "evidenskategori"])
        for value in m_values:
            tax = exitskatt_2026(value)
            writer.writerow([value, 100000, value-100000, nok(tax),
                             nok(annual_no_interest_exit_installment(tax)), "D"])



    with (folder / "scenario_likviditetsgrense_2026.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["maks_mulig_aarlig_brutto_utbytte_NOK",
                         "maks_skattemessig_selskapsformue_uten_likviditetsgap_NOK",
                         "formuesskatt_ved_grense_NOK", "evidenskategori"])
        for annual_cash in [0, 25000, 50000, 100000, 200000, 300000, 500000]:
            vmax = likviditetsgrense_2026(annual_cash)
            writer.writerow([annual_cash, nok(vmax),
                             nok(formuesskatt_2026(vmax)), "D"])

def _selftest() -> None:
    assert formuesskatt_2026(2375000) == ZERO
    assert formuesskatt_2026(3000000) == D("5000")
    assert formuesskatt_2026(9000000) == D("53000")
    assert formuesskatt_2026(25000000) == D("181000")
    assert formuesskatt_2026(26875000) == D("196000")
    assert formuesskatt_2026(30000000) == D("223500")
    assert formuesskatt_2026(50000000) == D("399500")
    assert formuesskatt_2026(5000000, eierandel="0.5") == D("1000")
    assert formuesskatt_2026(3000000, annen_skattepliktig_nettoformue=500000) == D("10000")
    assert exitskatt_2026(3100000) == ZERO
    assert exitskatt_2026(4000000) == D("340560.0000")
    assert exitskatt_2026(10000000) == D("2610960.0000")
    assert exitskatt_2026(40000000) == D("13962960.0000")
    assert nok(brutto_utbytte_for_formuesskatt(D("53000"))) == 85264
    assert nok(annual_no_interest_exit_installment(D("13962960"))) == 1163580
    assert nok(likviditetsgrense_2026(0)) == 2375000
    assert nok(likviditetsgrense_2026(50000)) == 6260000
    assert nok(likviditetsgrense_2026(100000)) == 10145000
    assert nok(likviditetsgrense_2026(200000)) == 17915000
    assert nok(likviditetsgrense_2026(500000)) == 39920455

if __name__ == "__main__":
    _selftest()
    _generate()
    print("OK: 20 kontroller bestått; tre scenario-CSV-er opprettet")