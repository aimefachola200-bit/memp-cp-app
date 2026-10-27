# -*- coding: utf-8 -*-
"""CS Pobè — intègre au jeu de départ (seed.json, repris par l'application DOSP) les données officielles de la circonscription :
zones pédagogiques I, II, III ; 27 unités pédagogiques (RUP, co-RUP, écoles) ; pour chaque école : zone, UP, année de création,
classes autorisées, personnel (FE, ACDPE, AME, autres) et effectifs par cours ou section (G, F).
Source : pobe_up.json, produit par outils/pobe_up/{extraire,consolider}.py à partir du document Word « Les Unités Pédagogiques
par Zone » (1er décembre 2023) et du classeur « Les écoles de la CS par zone » (classes autorisées 2024-2025).
Usage : python3 -I tools/jumelles/pobe/integrer-up.py <pobe_up.json>
Le bloc « officiel » du seed sert au premier lancement, à la mise à jour des installations existantes (cases vides seulement)
et aux boutons « ♻ Réinitialiser ». Matricules, téléphones et dates de naissance : aucun (seulement les noms des RUP et co-RUP)."""
import json
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
SEED = ICI / "seed.json"
ROMAIN = {1: "I", 2: "II", 3: "III"}
STATUT = {"Privé": "Privé laïc"}


def main(src):
    P = json.load(open(src, encoding="utf-8"))
    S = json.load(open(SEED, encoding="utf-8"))
    ecoles = {s["nom"]: s for s in S["schools"]}
    # 1. nouvelles écoles (citées dans les UP, absentes du référentiel)
    n = max(int(s["id"].split("-e")[1]) for s in S["schools"])
    for x in P["nouvelles"]:
        if x["nom"] in ecoles:
            continue
        n += 1
        s = {"id": f"pobe-e{n:03d}", "code": "", "nom": x["nom"], "cycle": x["cycle"], "secteur": STATUT.get(x["secteur"], x["secteur"]), "type": "Classique",
             "departement": "PLATEAU", "codeCs": "CSPOBE", "nomCs": "POBE", "numZone": "", "codeZone": "", "commune": "Pobè", "arrondissement": "",
             "localite": "", "up": "", "directeur": "", "contact": "", "anneeCreation": "", "classesAutorisees": ""}
        S["schools"].append(s)
        ecoles[s["nom"]] = s
    # 2. zones du référentiel
    for r in S["ref"]:
        if r["type"] == "zone":
            r["nom"] = "Zone pédagogique " + ROMAIN[int(r["numero"])]
    # 3. écoles : zone, UP, création, classes, personnel, effectifs (jeu officiel + valeurs de départ)
    off_ec = {}
    for e in P["ecoles"]:
        s = ecoles.get(e["nom"])
        if not s:
            raise SystemExit("école inconnue : " + e["nom"])
        z = e["zone"]
        o = {"numZone": str(z) if z else "", "codeZone": f"CSPOBE-ZP0{z}" if z else "", "up": e["up"] or "",
             "anneeCreation": str(e["annee_creation"]) if e["annee_creation"] else "", "classesAutorisees": e["classes_autorisees"] if e["classes_autorisees"] is not None else ""}
        if e["personnel"] and any(v is not None for v in e["personnel"].values()):
            p = e["personnel"]
            o["personnelFichier"] = {"FE": p["fe"] or 0, "ACDPE": p["acdpe"] or 0, "AME": p["ame"] or 0, "Autres": p["autres"] or 0,
                                     "total": p["total"] if p["total"] is not None else sum((p[k] or 0) for k in ("fe", "acdpe", "ame", "autres"))}
        eff = e["effectifs"] or {}
        data = {}
        if s["cycle"] == "Maternelle":
            for g, c in (("petits", "pet"), ("grands", "gra")):
                for x in ("G", "F"):
                    v = (eff.get(g) or {}).get(x)
                    if v is not None:
                        data[f"dir.{c}.{x}"] = v
        else:
            for c in ("CI", "CP", "CE1", "CE2", "CM1", "CM2"):
                for x in ("G", "F"):
                    v = (eff.get(c) or {}).get(x)
                    if v is not None:
                        data[f"dir.{c}.{x}"] = v
        if data:
            o["effectifs"] = data
        off_ec[s["id"]] = o
        for k in ("numZone", "codeZone", "up"):
            s[k] = o[k]
        for k in ("anneeCreation", "classesAutorisees"):
            if o[k] not in ("", None):
                s[k] = o[k]
        if "personnelFichier" in o:
            s["personnelFichier"] = o["personnelFichier"]
    nom_id = {s["nom"]: s["id"] for s in S["schools"]}
    ups = []
    for u in P["ups"]:
        z = u["zone"]
        ups.append({"id": f"pobe-up-z{z}-{'m' if u['cycle'] == 'Maternelle' else 'p'}{u['numero']:02d}", "zone": z, "codeZone": f"CSPOBE-ZP0{z}",
                    "cycle": u["cycle"], "numero": u["numero"], "up": u["nom"], "rup": u["rup"], "corup": u["corup"], "arrondissement": u["arrondissement"],
                    "ecoleIds": [nom_id[n] for n in u["ecoles"]], "ecoles": ", ".join(u["ecoles"]),
                    # UP ajoutée par la CS sans écoles (ex. Agbarou) : ses écoles sont rattachées à la main, une réinitialisation ne les détache pas
                    **({"ajoutee": True} if u.get("ajoutee") or not u["ecoles"] else {})})
    S["officiel"] = {"version": 1, "annee": "2026-2027", "anneeSource": P["annee"],
                     "source": P["source"], "noteEffectifs": "fichier de la CS (classes autorisées 2024-2025)",
                     "zones": [{"code": f"CSPOBE-ZP0{z['numero']}", "numero": str(z["numero"]), "nom": "Zone pédagogique " + ROMAIN[z["numero"]]} for z in P["zones"]],
                     "ups": ups, "ecoles": off_ec}
    S["source"] = S["source"].split(" Zones pédagogiques (3) à renseigner")[0] + " Zones pédagogiques I, II, III et unités pédagogiques (RUP, co-RUP) : document de la CS du 1er décembre 2023 ; effectifs et personnel par école : classeur « Les écoles de la CS par zone » (2024-2025)."
    json.dump(S, open(SEED, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(S['schools'])} écoles, {len(ups)} UP, {sum(1 for o in off_ec.values() if 'effectifs' in o)} écoles avec effectifs, "
          f"{sum(1 for s in S['schools'] if not s['codeZone'])} sans zone")


if __name__ == "__main__":
    main(sys.argv[1])
