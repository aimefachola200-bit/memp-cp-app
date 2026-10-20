# Application CP — MEMP Bénin

![Emblème](assets/embleme-memp.png)

Application web installable (PWA), **hors ligne**, pour les **Conseillers Pédagogiques (CP)** et **Chefs de Circonscription Scolaire (CCS)** du Ministère des Enseignements Maternel et Primaire.

**Conception : Maître Aimé FACHE — Tél. 01 96 51 03 33**

## Fonctions
- **Nouveau (1.8)** : menu **« Saisie manuelle (sans Excel) »** — fiches de chaque école créées et remplies à l'écran (identification et personnel enseignant repris), état nominatif du personnel d'une école en tableau (directeur, adjoints, enseignants, secrétaires, comptables, agents de saisie, plantons, gardiens, chauffeurs, agents d'entretien, cuisiniers), personnel de la circonscription, noms et contacts des directeurs de toutes les écoles en un seul tableau ; le CCS peut lui-même remplir une fiche.
- **Nouveau (1.4)** : **effectifs des apprenants** (fiche de recensement annuel par école : EP rubrique 7, EM rubrique 3 ; remplie depuis les fiches de collecte, totaux et contrôles, consolidation par zone et par circonscription, PDF, Excel, import / export Excel, circuit Brouillon → Transmise → Validée), réuni avec toutes les fonctions des versions 1.1 à 1.3 ; bandeau d'installation (PC, Android, tablette, iPhone / iPad).
- **Nouveau (1.3.1)** : documents officiels de SCOLARIS et GESCOL (fiches d'évaluation ACE et des directeurs, certificats de présence au poste, de travail, de prise de service, de prise en charge, attestation de direction, certificat de scolarité ; textes de référence : AOF des services de la DDEMP, arrêté du calendrier, emplois du temps, planifications, règlement intérieur signé, thèmes 2026-2027) ; mise à jour sans mélange de versions.
- **Nouveau (1.3)** : cachet rond (même dessin que SCOLARIS / GESCOL, bleu ou rouge, textes modifiables) sur tous les PDF signés ; tableau synoptique du CP présenté comme celui des directeurs (identité de la zone et du CP, écoles et directeurs, unités pédagogiques avec RUP / Co-RUP, personnel, textes officiels), PDF complet signé.
- **Nouveau (1.2)** : espace de travail de chaque CP de zone (écoles, personnel, fiches, activités, bilans, retraites, outils) ; module du personnel identique à SCOLARIS/GESCOL (carrière, anciennetés, départ à la retraite : A 60 ans, B 58 ans, C 55 ans, 1er jour du trimestre suivant la naissance ; fiche de carrière, départs par horizon, effectifs) ; planification annuelle de la maternelle (petits, grands) et du primaire.
- **Nouveau (1.1)** : personnel enseignant par zone (ajouter, modifier, supprimer, import du cahier de contrôle), écoles par zone, fiche de rapport de rentrée EP, emplois du temps officiels modifiables, calendrier scolaire 2026-2027, règlement intérieur en texte modifiable, canevas statistiques à télécharger.
- Fiches EM (rentrée, fin d'année) et EP (fin d'année), planification CI→CM2, thèmes 2026-2027, règlement intérieur, fiches de recensement (PDF).
- **Bilans trimestriels (T1/T2/T3) et annuels** : niveau zone (CP) et CS (CCS), calculs automatiques, consolidation, analyses pré-rédigées, difficultés, **photos (caméra avant/arrière)**.
- Boutons **Charger / Télécharger (PDF, PDF signé, Excel, JSON) / Réinitialiser / Supprimer**.
- Circuit : Brouillon → Transmise → Validée / À corriger ; échange hors ligne CP↔CCS par paquet `.memp.json` signé (SHA-256).
- Signature, cachet, QR de vérification ; emblème du ministère sur chaque document.

## Déploiement sur GitHub Pages
Le workflow `.github/workflows/pages.yml` publie automatiquement l'application sur la branche `gh-pages` à chaque envoi
sur `main` : elle est en ligne à `https://<utilisateur>.github.io/<depot>/` (ici https://aimefachola200-bit.github.io/memp-cp-app/).

## Installation
### Android (téléphone ou tablette)
1. Ouvrir **Chrome** (avec Internet pour la première fois).
2. Aller à **https://aimefachola200-bit.github.io/memp-cp-app/** et attendre l'écran de connexion.
3. Toucher le menu **⋮** (en haut à droite) → **« Installer l'application »** (ou « Ajouter à l'écran d'accueil » → **Installer**).
4. L'icône **Application CP** apparaît sur l'écran d'accueil ; l'application s'ouvre en plein écran et **fonctionne ensuite sans Internet**.
5. Les mises à jour s'installent seules quand l'application est ouverte avec Internet.

### PC et autres
- **PC (Chrome/Edge)** : ouvrir l'adresse, icône « Installer » dans la barre d'adresse.
- **iPad / iPhone (Safari)** : Partager → Sur l'écran d'accueil.
La caméra exige HTTPS (fourni par GitHub Pages).

### Application jumelle d'une circonscription
`node tools/creer-jumelle.mjs pobe ../memp-cp-pobe` crée l'application de la **CS de Pobè** (écoles et personnel par zone,
données locales séparées) : https://aimefachola200-bit.github.io/memp-cp-pobe/

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

## Application DOSP (dossier `dosp/`) — version 1.8.0

Application jumelle pour la **Division de l'Organisation Scolaire et de la Prévision** de la circonscription scolaire
(AOF, article 13 : réceptionner et acheminer les points de rentrée et les rapports de fin d'année ; préparer les
documents de suivi et évaluation ; renforcer les capacités des acteurs locaux). Elle reprend toute l'application CP
(tableau de bord, fiches de recensement / rentrée / fin d'année EP et EM, remplissage automatique, synthèse et tableau
synoptique, effectifs par âge, par sexe et par cours, maternelles par section, infrastructures et mobilier, écoles,
CEP, public et privé à part, rapports, bilans, documents officiels, personnel et **gestion de carrière**) et ajoute :
mon espace de travail (tâches, agenda, bloc-notes, documents), réception et acheminement des fiches (relances,
bordereau d'envoi à la DDEMP), prévisions de l'année suivante, besoins et écarts, suivi-évaluation, renforcement des
capacités (liste de présence, attestations, rapport), plan d'action, documents officiels de la DOSP (note de service,
convocation, PV, soit-transmis, relance, rapport d'activités, compte rendu) — tous signés, cachetés, avec QR.

En ligne : https://aimefachola200-bit.github.io/memp-cp-app/dosp/ — comptes de départ `dosp / dosp123`, `ccs / ccs123`,
`cp / cp123`, `admin / admin123` (à changer). Régénérer : `node tools/creer-jumelle.mjs dosp dosp`.

Fiche d'importation du personnel au format EducMaster : bouton « 📄 Fiche d'importation (EducMaster) » dans
*Personnel enseignant* ; le fichier rempli s'importe par « ⬆ Importer Excel » (colonnes EducMaster reconnues : Matricule,
NPI, Code établissement, Établissement, Statut, Grade, Indices, dates de prise de service…).
