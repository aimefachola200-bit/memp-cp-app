# Application CP — MEMP Bénin

![Emblème](assets/embleme-memp.png)

Application web installable (PWA), **hors ligne**, pour les **Conseillers Pédagogiques (CP)** et **Chefs de Circonscription Scolaire (CCS)** du Ministère des Enseignements Maternel et Primaire.

**Conception : Maître Aimé FACHE — Tél. 01 96 51 03 33**

## Fonctions
- **Effectifs des apprenants** (v1.1) : fiche de recensement annuel par école (EP rubrique 7, EM rubrique 3), remplie automatiquement (identification de l'école, effectifs repris des fiches de collecte, totaux et ENSEMBLE calculés, contrôles de cohérence), consolidation par **zone pédagogique** et par **circonscription scolaire**, export **PDF** et **Excel**, **import / export Excel** réimportable (feuilles « Saisie EP » / « Saisie EM »), circuit Brouillon → Transmise → Validée.
- Fiches EM (rentrée, fin d'année) et EP (fin d'année), planification CI→CM2, thèmes 2026-2027, règlement intérieur, fiches de recensement (PDF).
- **Bilans trimestriels (T1/T2/T3) et annuels** : niveau zone (CP) et CS (CCS), calculs automatiques, consolidation, analyses pré-rédigées, difficultés, **photos (caméra avant/arrière)**.
- Boutons **Charger / Télécharger (PDF, PDF signé, Excel, JSON) / Réinitialiser / Supprimer**.
- Circuit : Brouillon → Transmise → Validée / À corriger ; échange hors ligne CP↔CCS par paquet `.memp.json` signé (SHA-256).
- Signature, cachet, QR de vérification ; emblème du ministère sur chaque document.

## Déploiement sur GitHub Pages
Le workflow `.github/workflows/pages.yml` publie automatiquement l'application sur la branche `gh-pages` à chaque envoi
sur `main` : https://aimefachola200-bit.github.io/memp-cp-app/ (aucun réglage de Pages nécessaire).
La version précédente (1.3.1 : personnel, espace CP, tableau synoptique du CP, cachet rond…) est conservée dans la branche `sauvegarde-1.3.1`.

## Installation
- **PC (Chrome/Edge)** : ouvrir l'adresse, icône « Installer » dans la barre d'adresse.
- **Android (Chrome)** : menu ⋮ → « Installer l'application » / « Ajouter à l'écran d'accueil ».
- **Tablette** : idem selon le navigateur (iPad : Partager → Sur l'écran d'accueil).
L'application fonctionne ensuite sans connexion. La caméra exige HTTPS (fourni par GitHub Pages).

## Comptes par défaut (à changer dès la première connexion)
| Rôle | Identifiant | Mot de passe |
|---|---|---|
| Administrateur | admin | admin123 |
| CP | cp | cp123 |
| CCS | ccs | ccs123 |

## Développement
Aucune dépendance. Test local : `python3 -m http.server 8099`. Après toute modification de fichier : `node tools/gen-assets.mjs` (met à jour le cache hors ligne).

## Données
Stockées localement (IndexedDB) sur l'appareil. Faire des sauvegardes régulières (menu Sauvegarde).
