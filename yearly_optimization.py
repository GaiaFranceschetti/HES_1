"""
=========================================================
YEARLY OPTIMIZATION

Annual optimization of the hybrid boiler operation
using hourly electricity prices.
=========================================================
"""

import pandas as pd
import config

from economics.prices import ElectricityPrices
from optimization import find_best_temperature


def main(
    carbon_price=None,
):

    if carbon_price is None:
        carbon_price = config.CARBON_TAX

    # -----------------------------------------------------
    # Load hourly electricity prices
    # -----------------------------------------------------

    prices = ElectricityPrices(
        "data/20250101_20251231_MGP_PrezziZonali_COUP-2.xlsx"
    )

    # -----------------------------------------------------
    # Boiler operating conditions
    # -----------------------------------------------------

    thermal_power_kw = 5233.3
    methane_initial = 409.57

    results = []

    print()
    print("========================================")
    print("START YEARLY OPTIMIZATION")
    print("========================================")

    # -----------------------------------------------------
    # Loop over the entire year
    # -----------------------------------------------------

    for hour in range(prices.number_of_hours()):

        electricity_price = prices.get_price(hour)

        best = find_best_temperature(
            thermal_power_kw=thermal_power_kw,
            methane_initial=methane_initial,
            electricity_price=electricity_price,
            carbon_price=carbon_price,
            verbose=False,
        )

        results.append({

            # -------------------------------------------------
            # Time
            # -------------------------------------------------

            "date": prices.get_date(hour),
            "hour": prices.get_hour(hour),

            # -------------------------------------------------
            # Market
            # -------------------------------------------------

            "electricity_price": electricity_price,
            "gas_price": config.NATURAL_GAS_PRICE,
            "carbon_price": carbon_price,

            # -------------------------------------------------
            # Optimal operating point
            # -------------------------------------------------

            "temperature": best["temperature"],

            # -------------------------------------------------
            # Fuel
            # -------------------------------------------------

            "methane_kg_h":
                best["fuel"]["methane_kg_h"],

            "burner_power_kw":
                best["fuel"]["burner_power_kw"],

            "fuel_power_kw":
                best["fuel"]["fuel_power_kw"],

            "preheating_effectiveness":
                best["fuel"]["effectiveness"],

            "effective_preheating_kw":
                best["fuel"]["effective_preheating"],

            # -------------------------------------------------
            # Preheater
            # -------------------------------------------------

            "thermal_power_to_air_kw":
                best["preheater"]["thermal_power_kw"],

            "electric_power_kw":
                best["preheater"]["total_electric_power_kw"],

            # -------------------------------------------------
            # Emissions
            # -------------------------------------------------

            "co2_kg_h":
                best["emissions"]["co2_kg_h"],

            # -------------------------------------------------
            # Economics
            # -------------------------------------------------

            "gas_cost":
                best["economics"]["gas_cost"],

            "electricity_cost":
                best["economics"]["electricity_cost"],

            "carbon_cost":
                best["economics"]["carbon_cost"],

            "total_cost":
                best["economics"]["total_cost"],

            # -------------------------------------------------
            # Solver
            # -------------------------------------------------

            "iterations":
                best["iterations"],

        })

        if (hour + 1) % 500 == 0:

            print(
                f"Completed {hour + 1}/{prices.number_of_hours()} hours"
            )

    # -----------------------------------------------------
    # Save results
    # -----------------------------------------------------

    df = pd.DataFrame(results)

    df.to_csv(
        "results/yearly_results.csv",
        index=False,
    )

    # -----------------------------------------------------
    # Temperature distribution
    # -----------------------------------------------------

    distribution = (
        df["temperature"]
        .value_counts()
        .sort_index()
    )

    # -----------------------------------------------------
    # Print summary
    # -----------------------------------------------------

    print()
    print("========================================")
    print("YEARLY OPTIMIZATION COMPLETED")
    print("========================================")

    print(f"Hours simulated : {len(df)}")

    print()
    print(df.head())

    print()
    print("========================================")
    print("TEMPERATURE DISTRIBUTION")
    print("========================================")

    for temperature, hours in distribution.items():

        percentage = 100 * hours / len(df)

        print(
            f"{temperature:3.0f} °C : "
            f"{hours:5d} h "
            f"({percentage:5.1f} %)"
        )

    print()
    print("========================================")
    print("YEARLY SUMMARY")
    print("========================================")

    print(
        f"Average electricity price : "
        f"{df['electricity_price'].mean():.2f} €/MWh"
    )

    print(
        f"Average temperature       : "
        f"{df['temperature'].mean():.1f} °C"
    )

    print(
        f"Average methane           : "
        f"{df['methane_kg_h'].mean():.2f} kg/h"
    )

    print(
        f"Average electric power    : "
        f"{df['electric_power_kw'].mean():.2f} kW"
    )

    print(
        f"Average total cost        : "
        f"{df['total_cost'].mean():.2f} €/h"
    )

    print(
        f"Total methane            : "
        f"{df['methane_kg_h'].sum()/1000:.2f} t"
    )

    print(
        f"Total CO₂               : "
        f"{df['co2_kg_h'].sum()/1000:.2f} t"
    )

    print(
        f"Total operating cost     : "
        f"{df['total_cost'].sum():.2f} €"
    )

    print()
    print("========================================")
    print("OPERATING RANGE")
    print("========================================")

    print(
        f"Electricity price : "
        f"{df['electricity_price'].min():.2f}"
        f" - "
        f"{df['electricity_price'].max():.2f} €/MWh"
    )

    print(
        f"Temperature       : "
        f"{df['temperature'].min():.0f}"
        f" - "
        f"{df['temperature'].max():.0f} °C"
    )

    print(
        f"Operating cost    : "
        f"{df['total_cost'].min():.2f}"
        f" - "
        f"{df['total_cost'].max():.2f} €/h"
    )

    return df


if __name__ == "__main__":
    main()