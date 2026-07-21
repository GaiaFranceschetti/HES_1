"""
=========================================================
YEARLY OPTIMIZATION

Annual optimization of hybrid boiler operation
using hourly electricity prices.
=========================================================
"""

import pandas as pd

from economics.prices import ElectricityPrices
from optimization import find_best_temperature


def main():

    # Load electricity prices
    prices = ElectricityPrices(
        "data/20250101_20251231_MGP_PrezziZonali_COUP-2.xlsx"
    )

    # Boiler operating conditions
    thermal_power_kw = 5233.3
    methane_initial = 409.57

    results = []

    print()
    print("========================================")
    print("START YEARLY OPTIMIZATION")
    print("========================================")

    # Loop over all hours
    for hour in range(prices.number_of_hours()):

        electricity_price = prices.get_price(hour)

        best = find_best_temperature(
            thermal_power_kw,
            methane_initial,
            electricity_price,
        )

        results.append(
            {
                "date": prices.get_date(hour),
                "hour": prices.get_hour(hour),
                "electricity_price": electricity_price,
                "temperature": best["temperature"],
                "methane": best["methane"],
                "electric_power": best["electric_power"],
                "gas_cost": best["gas_cost"],
                "electricity_cost": best["electricity_cost"],
                "total_cost": best["cost"],
            }
        )

        if hour % 500 == 0:
            print(f"Completed hour {hour}/{prices.number_of_hours()}")

    # Convert results to dataframe
    df = pd.DataFrame(results)

    # Save results
    df.to_csv(
        "results/yearly_results.csv",
        index=False,
    )

    print()
    print("========================================")
    print("YEARLY OPTIMIZATION COMPLETED")
    print("========================================")

    print(f"Hours simulated : {len(df)}")

    print()
    print("First results:")
    print(df.head())


if __name__ == "__main__":
    main()