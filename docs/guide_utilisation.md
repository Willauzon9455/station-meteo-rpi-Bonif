# Guide d’utilisation

## Prérequis

Pour utiliser le projet, il faut :

- un Raspberry Pi configuré avec Raspberry Pi OS
- le capteur **AHT20**
- le capteur **APDS-9960**
- I²C activé sur le Raspberry Pi
- les dépendances Python installées

## Activation de I²C

Pour activer I²C :

```bash
sudo raspi-config nonint do_i2c 0

Pour vérifier les capteurs :

i2cdetect -y 1

Le AHT20 devrait apparaître à l’adresse 0x38 et le APDS-9960 à l’adresse 0x39.

Installation des dépendances

Pour installer les dépendances du projet :

uv sync

Si une bibliothèque manque, on peut aussi utiliser :

uv add adafruit-circuitpython-apds9960
Lancer le programme principal

Pour exécuter la station météo :

uv run main.py

Le programme affiche :

la température
l’humidité
les mesures du capteur APDS-9960 selon l’amélioration ajoutée
Journalisation CSV

Les mesures sont enregistrées dans le dossier :

data/

Un fichier CSV est créé avec :

la date et l’heure
la température
l’humidité
Arrêt du programme

Pour arrêter le programme, utiliser :

Ctrl+C

Le programme effectue un arrêt propre.

Tests

Pour tester un capteur individuellement, il est possible d’utiliser les fichiers de test dans le dossier :

tests/

Exemple :

python3 tests/test_apds.py