# /// script
# requires-python = ">=3.11"
# dependencies = ["adafruit-circuitpython-ahtx0", "adafruit-blinka", "RPi.GPIO"]
# ///
"""
Station météo basique avec capteur AHT20
Version minimale - À améliorer par les étudiants

LACUNES INTENTIONNELLES :
1. Pas de gestion d'erreurs si le capteur se déconnecte
2. Pas de validation des plages de valeurs
3. Affichage brut sans formatage ni unités claires
4. Pas d'horodatage des mesures
5. Fréquence codée en dur (pas configurable)
6. Pas de gestion de Ctrl+C propre
7. Code monolithique (difficile d'ajouter des capteurs)
8. Documentation minimale
"""
import time
import board
import adafruit_ahtx0

from utils.csv_logger import CSVDataLogger


def main():
    """Point d'entrée principal de la station météo."""
    i2c = board.I2C()
    sensor = adafruit_ahtx0.AHTx0(i2c)
    logger = CSVDataLogger(data_dir="data")

    print("Station météo - AHT20")
    print("Journalisation CSV activée")
    print("Ctrl+C pour arrêter")
    print()

    while True:
        temperature = sensor.temperature
        humidity = sensor.relative_humidity

        print(f"Température: {temperature:.2f} C")
        print(f"Humidité: {humidity:.2f} %")
        print()

        logger.log_data(temperature, humidity)

        time.sleep(5)


if __name__ == "__main__":
    main()
