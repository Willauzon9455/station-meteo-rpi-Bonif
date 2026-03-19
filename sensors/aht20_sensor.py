"""
Module pour la lecture sécurisée du capteur AHT20.

Ce module fournit des fonctions pour initialiser le capteur et lire
les mesures avec validation et gestion d'erreurs.
"""

from __future__ import annotations

import time
import board
import adafruit_ahtx0


class SensorConnectionError(Exception):
    """Erreur levée si le capteur ne peut pas être initialisé."""


class SensorReadError(Exception):
    """Erreur levée si une lecture du capteur échoue."""


def init_sensor(max_retries: int = 3, retry_delay: float = 2.0):
    """
    Initialise le capteur AHT20 avec quelques tentatives.

    Args:
        max_retries: Nombre maximal de tentatives.
        retry_delay: Délai entre les tentatives en secondes.

    Returns:
        Une instance du capteur AHT20.

    Raises:
        SensorConnectionError: Si le capteur ne peut pas être initialisé.
    """
    for attempt in range(1, max_retries + 1):
        try:
            i2c = board.I2C()
            sensor = adafruit_ahtx0.AHTx0(i2c)
            return sensor
        except Exception as exc:
            if attempt == max_retries:
                raise SensorConnectionError(
                    f"Impossible d'initialiser le capteur AHT20 après {max_retries} tentatives."
                ) from exc
            time.sleep(retry_delay)


def read_temperature(sensor) -> float:
    """
    Lit la température et valide la plage.

    Args:
        sensor: Instance du capteur AHT20.

    Returns:
        Température en Celsius.

    Raises:
        SensorReadError: Si la lecture échoue ou la valeur est invalide.
    """
    try:
        value = sensor.temperature
    except Exception as exc:
        raise SensorReadError("Erreur de lecture de la température.") from exc

    if not (-40 <= value <= 85):
        raise SensorReadError(f"Température hors plage: {value:.2f} °C")

    return value


def read_humidity(sensor) -> float:
    """
    Lit l'humidité relative et valide la plage.

    Args:
        sensor: Instance du capteur AHT20.

    Returns:
        Humidité relative en pourcentage.

    Raises:
        SensorReadError: Si la lecture échoue ou la valeur est invalide.
    """
    try:
        value = sensor.relative_humidity
    except Exception as exc:
        raise SensorReadError("Erreur de lecture de l'humidité.") from exc

    if not (0 <= value <= 100):
        raise SensorReadError(f"Humidité hors plage: {value:.2f} %")

    return value