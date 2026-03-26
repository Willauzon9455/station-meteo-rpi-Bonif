# Décisions techniques

## Choix des améliorations
Pour ce projet, j’ai choisi trois améliorations principales :

1. **Journalisation CSV avec horodatage**  
   Catégorie **B — Traitement et logique**

2. **Gestion d’erreurs robuste**  
   Catégorie **C — Qualité du code**

3. **Ajout du capteur APDS-9960**  
   Catégorie **A — Acquisition de données**

## Pourquoi ces choix
J’ai choisi ces améliorations parce qu’elles corrigent des faiblesses importantes du code de base et qu’elles respectent bien les contraintes du travail.

La **journalisation CSV avec horodatage** a été choisie pour conserver les mesures dans un fichier au lieu de seulement les afficher dans la console. Cela permet d’avoir un historique des données.

La **gestion d’erreurs robuste** a été choisie pour rendre le programme plus stable. Le code de base pouvait planter si le capteur ne répondait pas ou si une lecture échouait. Avec cette amélioration, le programme réagit mieux aux problèmes.

L’**ajout du capteur APDS-9960** a été choisi pour ajouter un deuxième capteur au projet. Cela permet de lire la proximité, la lumière ambiante et les couleurs RGB. Cette amélioration respecte aussi la contrainte matérielle demandée dans l’énoncé.

## Avantages des choix techniques
Ces choix rendent le projet :
- plus stable
- plus clair
- plus facile à tester
- plus utile pour conserver et analyser les données

## Résumé
Les décisions techniques ont été prises pour améliorer la qualité du code, ajouter de nouvelles fonctionnalités utiles et respecter les exigences du travail.