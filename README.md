# Portfolio V2 (explorations)

- index.html : le site comme sandbox du carré. Un carré = un pixel ; vu de biais, c'est un cube. Dessiner, extruder, gommer, changer la densité ; vues carré, losange, cube. Projets et portrait sont faits des mêmes pixels.
- explo-a.html, explo-b.html, explo-c.html, explo-d.html, identite.html : essais précédents.

## recomposition/ (17 novembre 2026, direction retenue)
- `recomposition/index.html` : accueil à 4 mots (Galerie, Observatoire, Bibliothèque, Profil), module brique 2:1, écran fixe sans défilement.
- `recomposition/data.js` : 72 projets (63 agence depuis agence.json du site, 9 études et concours depuis data.js) + profil et parcours. Champ `nat` déduit du programme, à valider par Yves.
- Liens directs pour tester : `#g-mvt`, `#g-stat`, `#g-big`, `#o`, `#b-date`, `#b-prog`, `#b-statut`, `#b-Logement`, `#p-pres`, `#p-philo`, `#p-parc`, `#p-cv`.
- Script de génération des données : à relancer si agence.json change (voir le fil du projet).
