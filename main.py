# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "adafruit-circuitpython-ahtx0",
#   "adafruit-blinka",
#   "RPi.GPIO",
#   "adafruit-circuitpython-apds9960"
# ]
# ///

"""
Station météo améliorée avec AHT20 et APDS-9960.

Fonctionnalités :
- Lecture température/humidité (AHT20)
- Journalisation CSV avec horodatage
- Gestion d'erreurs robuste avec tentative de reconnexion
- Lecture proximité + RGB (APDS-9960)
"""

import time
import board
import busio
import adafruit_apds9960.apds9960

from utils.csv_logger import CSVDataLogger
from sensors.aht20_sensor import (
    init_sensor,
    read_temperature,
    read_humidity,
    SensorConnectionError,
    SensorReadError,
)


def init_apds():
    """Initialise le capteur APDS-9960."""
    try:
        i2c = busio.I2C(board.SCL, board.SDA)
        apds = adafruit_apds9960.apds9960.APDS9960(i2c)
        apds.enable_proximity = True
        apds.enable_color = True
        return apds
    except Exception as exc:
        print(f"Erreur d'initialisation du APDS-9960 : {exc}")
        return None


def read_apds_data(apds):
    """Lit proximité et couleurs RGB+C du APDS-9960."""
    if apds is None:
        return None

    try:
        proximity = apds.proximity

        # attendre que les données couleur soient prêtes
        wait_count = 0
        while not apds.color_data_ready and wait_count < 20:
            time.sleep(0.01)
            wait_count += 1

        r, g, b, c = apds.color_data

        return {
            "proximity": proximity,
            "red": r,
            "green": g,
            "blue": b,
            "clear": c,
        }
    except Exception as exc:
        print(f"Erreur de lecture du APDS-9960 : {exc}")
        return None


def main():
    """Point d'entrée principal de la station météo."""
    print("Station météo améliorée - AHT20 + APDS-9960")
    print("Journalisation CSV activée")
    print("Gestion d'erreurs activée")
    print("Ctrl+C pour arrêter proprement")
    print()

    try:
        sensor = init_sensor()
    except SensorConnectionError as exc:
        print(f"Erreur d'initialisation AHT20 : {exc}")
        return

    apds = init_apds()
    logger = CSVDataLogger(data_dir="data")

    try:
        while True:
            # ----- AHT20 -----
            try:
                temperature = read_temperature(sensor)
                humidity = read_humidity(sensor)

                print(f"Température: {temperature:.2f} C")
                print(f"Humidité: {humidity:.2f} %")

                logger.log_data(temperature, humidity)

            except SensorReadError as exc:
                print(f"Erreur de lecture AHT20 : {exc}")
                print("Tentative de reconnexion du AHT20...")

                try:
                    sensor = init_sensor()
                    print("Reconnexion AHT20 réussie.")
                except SensorConnectionError as reconnect_exc:
                    print(f"Échec de reconnexion AHT20 : {reconnect_exc}")

            # ----- APDS-9960 -----
            apds_data = read_apds_data(apds)
            if apds_data is not None:
                print(f"Proximité: {apds_data['proximity']}")
                print(
                    f"RGB+C: "
                    f"{apds_data['red']} "
                    f"{apds_data['green']} "
                    f"{apds_data['blue']} "
                    f"{apds_data['clear']}"
                )
            else:
                print("APDS-9960 non disponible ou lecture impossible.")

            print()
            time.sleep(5)

    except KeyboardInterrupt:
        print("\nArrêt propre demandé par l'utilisateur.")


if __name__ == "__main__":
    main()