"""
=========================================================
ELECTRICITY PRICES
=========================================================
This module loads hourly electricity prices from
an Excel file and provides simple methods to access
them during the optimization.
=========================================================
"""

from pathlib import Path
import pandas as pd


class ElectricityPrices:
    """
    Class to manage hourly electricity prices.
    """

    def __init__(self, filename):
        """
        Load electricity prices from an Excel file.

        Parameters
        ----------
        filename : str
            Path to the Excel file.
        """

        filename = Path(filename)

        if not filename.exists():
            raise FileNotFoundError(
                f"Price file not found: {filename}"
            )

        # Read Excel file
        self.data = pd.read_excel(
            filename,
            sheet_name="MGP-PrezziZonali-COUP"
        )

        # Rename columns
        self.data = self.data.rename(columns={
            "Data": "date",
            "Ora": "hour",
            "€/MWh": "price"
        })

        # Convert price column from Italian format
        # (e.g. "138,70") to float (138.70)
        self.data["price"] = (
            self.data["price"]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .astype(float)
        )

    def get_price(self, hour):
        """
        Return electricity price [€/MWh].

        Parameters
        ----------
        hour : int
            Hour index (0-8759)

        Returns
        -------
        float
        """

        return self.data.loc[hour, "price"]

    def get_date(self, hour):
        """
        Return the date corresponding to the selected hour.
        """

        return self.data.loc[hour, "date"]

    def get_hour(self, hour):
        """
        Return the hour of the day (1-24).
        """

        return self.data.loc[hour, "hour"]

    def number_of_hours(self):
        """
        Return total number of simulated hours.
        """

        return len(self.data)