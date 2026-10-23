#!/usr/bin/env python3
"""Hyporia / Norsk Økonomi, delrapport 06C v0.2.

Reproduserbare illustrasjoner (kategori D), ikke personlig skatterådgivning.
Satsene er låst til norske 2026-regler; reform- og utlandsrater er hypotetiske.
Kjør: python3 modell_06C.py && python3 modell_06C_utvidet.py
"""
from __future__ import annotations

import csv
import json
from decimal import Decimal
from pathlib import Path

from modell_06C import (
    D, ZERO, AKSJE_SKATT, formuesskatt_2026,
    exitskatt_2026, brutto_utbytte_for_formuesskatt, nok,
)

ROOT = Path(__file__).resolve().parent
CAT = "D"


def reformskatt(netto: object, sats: object, andel: object = 1) -> Decimal:
    """NOU 2026:9-type illustrasjon: 2 mill. bunn, ingen aksjerabatt."""
    rate = D(str(sats))
    if not D(0) <= rate <= D(1):
        raise ValueError("sats utenfor 0..1")
    return max(ZERO, D(str(netto)) * D(str(andel)) - D(2000000)) * rate


def emisjon(netto: object, selskapsverdi_for: object,
            ny_kapital: object, grunderandel_for: object = 1) -> dict:
    """Ren primæremisjon til pre-money-pris, uten gründerens aksjesalg."""
    nav, premoney, cash, owner = map(lambda x: D(str(x)),
                                     (netto, selskapsverdi_for, ny_kapital, grunderandel_for))
    if premoney <= 0 or cash < 0 or not (0 < owner <= 1):
        raise ValueError("Ugyldige emisjonsforutsetninger")
    owner_after = owner * premoney / (premoney + cash)
    t_before = formuesskatt_2026(nav, owner)
    t_after = formuesskatt_2026(nav + cash, owner_after)
    return {"nav_for": nav, "nav_etter": nav + cash,
            "andel_for": owner, "andel_etter": owner_after,
            "markedsverdi_for": premoney * owner,
            "markedsverdi_etter": (premoney + cash) * owner_after,
            "skatt_for": t_before, "skatt_etter": t_after,
            "endring": t_after - t_before}


def vekstbane(start_netto: object = 3000000, vekst: object = ".20",
              brutto_utbytte: object = 25000, aar: int = 10,
              diskontering: object = ".05") -> list[dict]:
    start, g, div, r = map(lambda x: D(str(x)),
                            (start_netto, vekst, brutto_utbytte, diskontering))
    if aar <= 0 or g <= -1 or r <= -1:
        raise ValueError("Ugyldige tids-/vekstparametre")
    result = []
    for t in range(1, aar + 1):
        nav = start * (D(1) + g) ** (t - 1)
        tax = formuesskatt_2026(nav)
        gap = max(ZERO, tax - div * (D(1) - AKSJE_SKATT))
        result.append({"aar": 2025 + t, "netto": nav, "skatt": tax,
                       "utbytte": div, "behov": brutto_utbytte_for_formuesskatt(tax),
                       "gap": gap, "nvskatt": tax / (D(1)+r)**t,
                       "nou025": reformskatt(nav, ".0025"),
                       "nou075": reformskatt(nav, ".0075")})
    return result


def utflyttingsplan(tax: object, salgsaar: int = 10) -> list[Decimal]:
    """Forenklet rentefri 12-årsbetaling; restandel ved simulert salg.

    Ikke en juridisk modell for andre akselerasjoner eller skatteavtaler.
    """
    exit_tax = D(str(tax))
    if salgsaar < 1:
        raise ValueError("salgsaar må være >= 1")
    out = []
    remaining = exit_tax
    for year in range(1, salgsaar + 1):
        due = remaining if year == salgsaar else (exit_tax / D(12) if year <= 12 else ZERO)
        out.append(due)
        remaining -= due
    return out


def flytte_sammenligning(utenlandsk_gevinstrate: object = ".20", *,
                         netto: object = 9000000, verdi: object = 10000000,
                         inngangsverdi: object = 100000,
                         aar: int = 10, netto_vekst: object = ".10",
                         verdi_vekst: object = ".12", diskontering: object = ".05",
                         flytting_engang: object = 300000,
                         flytting_aarlig: object = 100000,
                         utenlandsk_formuesrate: object = "0") -> dict:
    """Kostnads-NPV, landløst tankeeksperiment, ikke faktisk skatteposisjon."""
    rate, nav, mv, basis, gnav, gmv, disc, fixed, annual, fw = (
        D(str(x)) for x in (utenlandsk_gevinstrate, netto, verdi,
                           inngangsverdi, netto_vekst, verdi_vekst,
                           diskontering, flytting_engang, flytting_aarlig,
                           utenlandsk_formuesrate))
    if aar < 1 or min(gnav,gmv,disc) <= -1 or rate < 0 or fw < 0:
        raise ValueError("Ugyldige sammenlikningsparametre")
    exit_tax = exitskatt_2026(mv, basis)
    dues = utflyttingsplan(exit_tax, aar)
    pv_stay = ZERO
    pv_move = fixed
    pv_wealth = ZERO
    by_year = []
    for t in range(1, aar+1):
        nt = nav * (D(1)+gnav)**(t-1)
        mt = mv * (D(1)+gmv)**(t-1)
        wealth = formuesskatt_2026(nt)
        factor = (D(1)+disc)**t
        pv_stay += wealth / factor
        pv_wealth += wealth / factor
        pv_move += (dues[t-1]+annual+mt*fw)/factor
        by_year.append((2025+t, t, nt, wealth, dues[t-1], annual))
    end_value = mv * (D(1)+gmv)**aar
    pv_stay += max(ZERO, end_value - basis)*AKSJE_SKATT/(D(1)+disc)**aar
    gain_post = max(ZERO, end_value-mv)
    pv_move += gain_post*rate/(D(1)+disc)**aar
    pv_post = gain_post/(D(1)+disc)**aar
    parity = (pv_stay - (pv_move-pv_post*rate))/pv_post if pv_post else None
    return {"stay": pv_stay, "move": pv_move, "difference": pv_move-pv_stay,
            "exit_tax": exit_tax, "pv_wealth":pv_wealth,
            "parity":parity,"years":by_year,"end_value":end_value}


def _csv(name: str, heading: list[str], rows: list[list[object]]) -> None:
    with (ROOT/name).open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(heading)
        writer.writerows(rows)


def _tests() -> int:
    checks = [
      reformskatt(2100000,".0025") == D(250),
      reformskatt(2100000,".0075") == D(750),
      reformskatt(2375000,".0075") == D(2812.5),
      reformskatt(3000000,".0025") == D(2500),
      reformskatt(3000000,".0075") == D(7500),
      reformskatt(5000000,".0025") == D(7500),
      reformskatt(5000000,".0075") == D(22500),
      reformskatt(8000000,".0075") == formuesskatt_2026(8000000),
      reformskatt(9000000,".0025") == D(17500),
      reformskatt(9000000,".0075") == D(52500),
      reformskatt(15000000,".0075") == D(97500),
      reformskatt(25000000,".0025") == D(57500),
      emisjon(5000000,40000000,0)["endring"] == ZERO,
      emisjon(5000000,40000000,10000000)["andel_etter"] == D(".8"),
      emisjon(5000000,40000000,10000000)["markedsverdi_etter"] == D(40000000),
      emisjon(5000000,40000000,10000000)["skatt_for"] == D(21000),
      emisjon(5000000,40000000,10000000)["skatt_etter"] == D(77000),
      emisjon(5000000,40000000,20000000)["endring"] > D(90000),
      nok(vekstbane()[0]["skatt"]) == 5000,
      nok(vekstbane()[2]["gap"]) == 20,
      nok(vekstbane()[9]["skatt"]) == 104835,
      nok(sum(r["skatt"] for r in vekstbane())) == 433008,
      nok(sum(r["gap"] for r in vekstbane())) == 293888,
      nok(sum(r["nvskatt"] for r in vekstbane())) == 301477,
      sum(utflyttingsplan(D(2610960),10)) == D(2610960),
      nok(utflyttingsplan(D(2610960),10)[-1]) == 652740,
      nok(flytte_sammenligning(0)["stay"]) == 7898050,
      nok(flytte_sammenligning(0)["move"]) == 3019419,
      nok(flytte_sammenligning(".20")["move"]) == 5605035,
      nok(flytte_sammenligning(".20")["pv_wealth"]) == 706246,
      abs(flytte_sammenligning()["parity"]-D(".3773669446")) < D(".00000001"),
    ]
    if not all(checks):
        raise AssertionError("Manglende samsvar i kontroll # " + ",".join(str(i+1) for i,v in enumerate(checks) if not v))
    return len(checks)


def _generate(count: int) -> None:
    _csv("scenario_kommisjonsreform.csv",
         ["selskapsnetto_NOK","formuesskatt_2026_NOK","nOu_025_NOK","nOu_075_NOK","kategori"],
         [[v,nok(formuesskatt_2026(v)),nok(reformskatt(v,".0025")),nok(reformskatt(v,".0075")),CAT]
          for v in [2100000,2375000,3000000,5000000,8000000,9000000,15000000,25000000,30000000,50000000]])
    _csv("scenario_emisjon_og_eierskatt.csv",
         ["ny_egenkapital_NOK","nav_for_NOK","nav_etter_NOK","eierandel_for_prosent","eierandel_etter_prosent","personlig_markedsverdi_for_NOK","personlig_markedsverdi_etter_NOK","skatt_for_NOK","skatt_etter_NOK","aarlig_skatteendring_NOK","kategori"],
         [[cash, nok(a["nav_for"]), nok(a["nav_etter"]),nok(a["andel_for"]*100),nok(a["andel_etter"]*100),nok(a["markedsverdi_for"]),nok(a["markedsverdi_etter"]),nok(a["skatt_for"]),nok(a["skatt_etter"]),nok(a["endring"]),CAT]
          for cash in [0,1000000,5000000,10000000,20000000] for a in [emisjon(5000000,40000000,cash)]])
    _csv("scenario_vekst_likviditet.csv",
         ["aar","selskapsformue_NOK","formuesskatt_NOK","fritt_bruttoutbytte_NOK","nodvendig_bruttoutbytte_NOK","personlig_likviditetsgap_NOK","naaverdi_formuesskatt_NOK","nOu_025_NOK","nOu_075_NOK","kategori"],
         [[a["aar"],nok(a["netto"]),nok(a["skatt"]),nok(a["utbytte"]),nok(a["behov"]),nok(a["gap"]),nok(a["nvskatt"]),nok(a["nou025"]),nok(a["nou075"]),CAT] for a in vekstbane()])
    examples=[(i,flytte_sammenligning(i)) for i in ("0",".1",".2",".3",".4",".5")]
    _csv("scenario_flyttebeslutning_naverdi.csv",
         ["utenlandsk_post_move_sats","merket_land","naaverdi_bli_NOK","naaverdi_flytte_NOK","differanse_flytt_minus_bli_NOK","utflyttingsskatt_NOK","formuesskatt_NPV_bli_NOK","kategori"],
         [[str(D(rate)),"hypotetisk – ikke et bestemt land",nok(a["stay"]),nok(a["move"]),nok(a["difference"]),nok(a["exit_tax"]),nok(a["pv_wealth"]),CAT]
          for rate,a in examples])
    a=flytte_sammenligning(".2")
    _csv("scenario_betaling_og_tid.csv",
         ["aar","skattet_ar_nr","nav_NOK","no_formuesskatt_NOK","utflyttingsskatt_avdrag_NOK","aarlig_flyttekostnad_NOK","kategori"],
         [[year,t,nok(n),nok(w),nok(inst),nok(cost),CAT] for year,t,n,w,inst,cost in a["years"]])
    summary={"type":"scenario_D","report":"06C v0.2","tax_rules_year":2026,"not_individual_advice":True,
             "internal_tests":count,"wealth_tax_total_10_years":nok(sum(x["skatt"] for x in vekstbane())),
             "unfunded_private_liquidity_total":nok(sum(x["gap"] for x in vekstbane())),
             "pv_stay":nok(a["stay"]),"pv_move_at_20_percent_foreign":nok(a["move"]),
             "pv_wealth_stay":nok(a["pv_wealth"]),"parity_foreign_capital_gain_rate":float(a["parity"]),
             "current_law_vs_hypotheticals":"NOU and foreign tax assumptions are not enacted Norwegian or foreign rules"}
    (ROOT/"modellresultater_06C_v02.json").write_text(json.dumps(summary,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")


if __name__=="__main__":
    n=_tests()
    _generate(n)
    print(f"OK: {n} interne kontroller bestått; fem scenario-CSV-er og JSON generert")