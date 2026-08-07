"""
=========================================================
NORWAY CASE STUDY
=========================================================
"""

import pandas as pd
import config

from optimization import find_best_temperature


def main():

    # -----------------------------------------------------
    # Load Norwegian electricity prices
    # -----------------------------------------------------

    prices = pd.read_csv(
        "data/Norway.csv",
        sep=";"
    )

    print(prices.columns.tolist())

    # -----------------------------------------------------
    # Convert datetime
    # -----------------------------------------------------

    prices["Datetime (Local)"] = pd.to_datetime(
        prices["Datetime (Local)"]
    )

    # -----------------------------------------------------
    # Keep only year 2025
    # -----------------------------------------------------

    prices = prices[
        prices["Datetime (Local)"].dt.year == 2025
    ].reset_index(drop=True)

    print()
    print(f"Hours available : {len(prices)}")

    # -----------------------------------------------------
    # Boiler operating conditions
    # -----------------------------------------------------

    thermal_power_kw = 5233.3
    methane_initial = 409.57

    results = []

    print()
    print("========================================")
    print("START NORWAY CASE")
    print("========================================")

    # -----------------------------------------------------
    # Loop over all hours
    # -----------------------------------------------------

    for hour in range(len(prices)):

        electricity_price = prices.loc[
            hour,
            "Price (EUR/MWhe)"
        ]

        best = find_best_temperature(
            thermal_power_kw=thermal_power_kw,
            methane_initial=methane_initial,
            electricity_price=electricity_price,
            carbon_price=config.CARBON_TAX,
            verbose=False,
        )

        timestamp = prices.loc[
            hour,
            "Datetime (Local)"
        ]

        results.append({
            "date": timestamp.date(),
            "hour": timestamp.hour,

            "electricity_price": electricity_price,
            "gas_price": config.NATURAL_GAS_PRICE,
            "carbon_price": config.CARBON_TAX,

            "temperature": best["temperature"],

            "methane_kg_h": best["fuel"]["methane_kg_h"],
            "burner_power_kw": best["fuel"]["burner_power_kw"],
            "fuel_power_kw": best["fuel"]["fuel_power_kw"],
            "preheating_effectiveness": best["fuel"]["effectiveness"],
            "effective_preheating_kw": best["fuel"]["effective_preheating"],

            "thermal_power_to_air_kw": best["preheater"]["thermal_power_kw"],
            "electric_power_kw": best["preheater"]["total_electric_power_kw"],

            "co2_kg_h": best["emissions"]["co2_kg_h"],

            "gas_cost": best["economics"]["gas_cost"],
            "electricity_cost": best["economics"]["electricity_cost"],
            "carbon_cost": best["economics"]["carbon_cost"],
            "total_cost": best["economics"]["total_cost"],

            "iterations": best["iterations"],
        })

        if (hour + 1) % 500 == 0:
            print(f"Completed {hour + 1}/{len(prices)} hours")

    # -----------------------------------------------------
    # Save results
    # -----------------------------------------------------

    df = pd.DataFrame(results)

    df.to_csv(
        "results/norway_results.csv",
        index=False,
    )

if __name__ == "__main__":
    main()