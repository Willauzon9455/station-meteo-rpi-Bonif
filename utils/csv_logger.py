from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path


class CSVDataLogger:
    """Journalise les mesures météo dans un fichier CSV."""

    def __init__(self, data_dir: str = "data") -> None:
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(exist_ok=True)
        self.file_path = self.data_dir / f"meteo_data_{datetime.now():%Y-%m-%d}.csv"

        if not self.file_path.exists():
            with open(self.file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["timestamp", "temperature_c", "humidity_percent"])

    def log_data(self, temperature: float, humidity: float) -> None:
        """Ajoute une mesure au fichier CSV."""
        with open(self.file_path, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                datetime.now().isoformat(timespec="seconds"),
                f"{temperature:.2f}",
                f"{humidity:.2f}",
            ])