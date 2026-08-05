"""
=========================================================
CARBON TAX SCENARIOS

Analysis of hybrid boiler operation under different
carbon prices.
=========================================================
"""

import pandas as pd
import config

from yearly_optimization import main as run_yearly


def analyse_results(carbon_price):

    df = pd.read_csv(
        "results/yearly_results.csv"
    )

    total_cost = df["total_cost"].sum()

    co2 = (
        df["co2_emissions"].sum()
        / 1000
    )

    electricity = (
        df["electric_power"].sum()
        / 1000
    )

    active_hours = (
        df["temperature"] == 450
    ).sum()

    return {
    "carbon_price": carbon_price,
    "cost": total_cost,
    "co2": co2,
    "co2_saving": None,
    "electricity": electricity,
    "active_hours": active_hours,
}



def main():

    scenarios = [
        0,
        50,
        100,
        150,
        200,
    ]

    results = []


    print()

    print("========================================")
    print("CARBON TAX SCENARIOS")
    print("========================================")


    for carbon_price in scenarios:

        print()
        print(
            f"Running scenario: "
            f"{carbon_price} €/ton"
        )


        # Update carbon price
        config.CARBON_PRICE_EUR_PER_TON = carbon_price


        # Run yearly optimization
        run_yearly()


        result = analyse_results(
            carbon_price
        )

        results.append(result)


    df_results = pd.DataFrame(results)


    df_results.to_csv(
        "results/carbon_scenarios.csv",
        index=False,
    )
    baseline_co2 = (
    df_results.loc[
        df_results["carbon_price"] == 0,
        "co2"
    ].values[0]
)

    df_results["co2_saving"] = (
    baseline_co2 - df_results["co2"]
)
    summary = df_results.copy()

    summary["cost_MEUR"] = (
    summary["cost"] / 1e6
)

    summary = summary[
    [
        "carbon_price",
        "cost_MEUR",
        "co2",
        "co2_saving",
        "electricity",
        "active_hours",
    ]
]


    summary.to_csv(
    "results/carbon_summary.csv",
    index=False,
    )
    print()

    print("========================================")
    print("RESULTS")
    print("========================================")

    print(df_results)



if __name__ == "__main__":
    main()