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
from utils.csv_logger import CSVDataLogger
from sensors.aht20_sensor import (
    init_sensor,
    read_temperature,
    read_humidity,
    SensorConnectionError,
    SensorReadError,
)

def main():
    """Point d'entrée principal de la station météo."""
    print("Station météo - AHT20")
    print("Journalisation CSV activée")
    print("Gestion d'erreurs activée")
    print("Ctrl+C pour arrêter proprement")
    print()

    try:
        sensor = init_sensor()
    except SensorConnectionError as exc:
        print(f"Erreur d'initialisation: {exc}")
        return

    logger = CSVDataLogger(data_dir="data")

    try:
        while True:
            try:
                temperature = read_temperature(sensor)
                humidity = read_humidity(sensor)

                print(f"Température: {temperature:.2f} C")
                print(f"Humidité: {humidity:.2f} %")
                print()

                logger.log_data(temperature, humidity)

            except SensorReadError as exc:
                print(f"Erreur de lecture: {exc}")
                print("Nouvelle tentative dans 5 secondes...\n")

            time.sleep(5)

    except KeyboardInterrupt:
        print("\nArrêt propre demandé par l'utilisateur.")


if __name__ == "__main__":
    main()
