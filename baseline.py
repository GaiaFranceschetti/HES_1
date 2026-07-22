"""
=========================================================
BASELINE CASE

Conventional boiler operation:
- Natural gas only
- No electric preheating
=========================================================
"""

import pandas as pd

from economics.prices import ElectricityPrices
from combustion.fuel_consumption import methane_consumption
from economics.costs import gas_cost


def main():

    prices = ElectricityPrices(
        "data/20250101_20251231_MGP_PrezziZonali_COUP-2.xlsx"
    )

    thermal_power_kw = 5233.3

    # Conventional boiler:
    # no electric preheater
    methane = methane_consumption(
        thermal_power_kw,
        preheater_power_kw=0,
        verbose=False,
    )

    results = []

    for hour in range(prices.number_of_hours()):

        cost = gas_cost(methane)

        results.append(
            {
                "date": prices.get_date(hour),
                "hour": prices.get_hour(hour),
                "methane": methane,
                "electric_power": 0,
                "gas_cost": cost,
                "electricity_cost": 0,
                "total_cost": cost,
            }
        )


    df = pd.DataFrame(results)


    df.to_csv(
        "results/baseline_results.csv",
        index=False,
    )


    print()
    print("========================================")
    print("BASELINE RESULTS")
    print("========================================")

    print(
        f"Annual cost: {df['total_cost'].sum():.2f} €/year"
    )

    print(
        f"Methane consumption: "
        f"{df['methane'].sum()/1000:.2f} ton/year"
    )


if __name__ == "__main__":
    main()
    