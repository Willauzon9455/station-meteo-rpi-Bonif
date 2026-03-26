# Analyse du code initial

## Description du code de base
Le code de base permet de lire la température et l’humidité du capteur **AHT20** et d’afficher les résultats dans la console à toutes les 5 secondes.

## Forces du code initial
- Le programme est simple à comprendre.
- Le capteur AHT20 est bien initialisé.
- Les lectures de température et d’humidité fonctionnent.
- Le code donne une bonne base de départ pour une station météo IoT.

## Lacunes intentionnelles du code de base
1. **Pas de gestion d’erreurs**  
   Le programme peut crash si le capteur se déconnecte.

2. **Pas de validation des données**  
   Aucune vérification des plages de valeurs.

3. **Affichage brut**  
   Pas de formatage, unités peu claires.

4. **Pas d’horodatage**  
   Impossible de savoir quand les mesures ont été prises.

5. **Configuration codée en dur**  
   Fréquence de lecture non configurable.

6. **Pas d’arrêt propre**  
   `Ctrl+C` fait crasher le programme.

7. **Code monolithique**  
   Difficile d’ajouter des capteurs.

8. **Documentation minimale**  
   Le README ne décrit pas l’installation ni l’usage.

## Améliorations choisies
Pour améliorer le projet, j’ai choisi les trois améliorations suivantes :

1. **Journalisation CSV avec horodatage**  
   Catégorie **B — Traitement et logique**

2. **Gestion d’erreurs robuste**  
   Catégorie **C — Qualité du code**

3. **Ajout du capteur APDS-9960**  
   Catégorie **A — Acquisition de données**

## Justification des choix
J’ai choisi ces améliorations parce qu’elles corrigent directement plusieurs faiblesses du code initial.  
La journalisation CSV permet de conserver un historique des mesures.  
La gestion d’erreurs rend le programme plus stable et plus fiable.  
L’ajout du capteur APDS-9960 permet d’ajouter de nouvelles données et de respecter la contrainte matérielle demandée dans l’évaluation.

## Résumé
Le code initial était fonctionnel, mais très minimal. Les améliorations choisies rendent la station météo plus complète, plus stable et plus utile.