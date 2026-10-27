/* République du Bénin — MEMP — Application CP — Configuration
   Conception : Maître Aimé FACHE — Tél. 01 96 51 03 33 */
export const APP = {
  name: 'Application CP',
  full: 'Application CP — Gestion pédagogique',
  version: '1.20.1',
  republique: 'RÉPUBLIQUE DU BÉNIN',
  ministere: 'MINISTÈRE DES ENSEIGNEMENTS MATERNEL ET PRIMAIRE',
  concepteur: 'Maître Aimé FACHE',
  concepteurTel: '01 96 51 03 33',
  concepteurTelRaw: '0196510333',
};
/* Variante de l'application. L'application jumelle d'une circonscription (ex. CS Pobè) remplace ce bloc
   (tools/creer-jumelle.mjs) : nom, base de données locale distincte, données de départ (écoles, personnel, zones). */
export const VARIANT = {
  id: 'general',
  titre: '',
  base: 'memp-cp-app',
  seed: null,
  comptes: [['admin', 'admin123'], ['cp', 'cp123'], ['ccs', 'ccs123']],
};
export const CREDIT = `Conçu par ${APP.concepteur} · Tél. ${APP.concepteurTel}`;
