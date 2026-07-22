"""
=========================================================
ANALYSE RESULTS

Analysis of yearly hybrid boiler optimization results.
=========================================================
"""

import pandas as pd


def main():

    df = pd.read_csv(
        "results/yearly_results.csv"
    )

    print()
    print("========================================")
    print("YEARLY RESULTS ANALYSIS")
    print("========================================")

    print()

    # Total costs
    total_cost = df["total_cost"].sum()

    print("Total operating cost:")
    print(f"{total_cost:.2f} €/year")

    print()

    # Methane consumption
    methane = df["methane"].sum()

    print("Total methane consumption:")
    print(f"{methane/1000:.2f} ton/year")

    print()

        # CO2 emissions
    co2 = df["co2_emissions"].sum()

    print()

    print("Total CO2 emissions:")
    print(f"{co2/1000:.2f} ton/year")

    # Electricity consumption
    electricity = df["electric_power"].sum()

    print("Total electricity consumption:")
    print(f"{electricity/1000:.2f} MWh/year")

    print()

    # Average optimal temperature
    avg_temperature = df["temperature"].mean()

    print("Average optimal temperature:")
    print(f"{avg_temperature:.1f} °C")

    print()

    # Temperature distribution
    print("Temperature distribution:")

    print(
        df["temperature"]
        .value_counts()
        .sort_index()
    )

    print()

    # Electricity price when preheater is active
    print("Electricity price when preheater is ON:")

    active_hours = df[
        df["temperature"] == 450
    ]

    print(
        active_hours["electricity_price"]
        .describe()
    )


if __name__ == "__main__":
    main()