"""
=========================================================
YEARLY COMPARISON

Comparison between conventional boiler and hybrid boiler.

=========================================================
"""

import pandas as pd


def main():

    baseline = pd.read_csv(
        "results/baseline_results.csv"
    )

    hybrid = pd.read_csv(
        "results/yearly_results.csv"
    )


    # =====================================================
    # Annual values
    # =====================================================

    baseline_cost = baseline["total_cost"].sum()
    hybrid_cost = hybrid["total_cost"].sum()

    baseline_methane = (
        baseline["methane"].sum()
        / 1000
    )

    hybrid_methane = (
        hybrid["methane"].sum()
        / 1000
    )

    baseline_co2 = (
        baseline["co2_emissions"].sum()
        / 1000
    )

    hybrid_co2 = (
        hybrid["co2_emissions"].sum()
        / 1000
    )


    # =====================================================
    # Savings
    # =====================================================

    cost_saving = baseline_cost - hybrid_cost

    methane_saving = (
        baseline_methane - hybrid_methane
    )

    co2_saving = (
        baseline_co2 - hybrid_co2
    )


    cost_saving_percent = (
        cost_saving
        / baseline_cost
        * 100
    )

    co2_saving_percent = (
        co2_saving
        / baseline_co2
        * 100
    )


    # =====================================================
    # Print results
    # =====================================================

    print()

    print("========================================")
    print("YEARLY COMPARISON")
    print("========================================")


    print()

    print("COST")

    print(
        f"Baseline : {baseline_cost:.2f} €/year"
    )

    print(
        f"Hybrid   : {hybrid_cost:.2f} €/year"
    )

    print(
        f"Saving   : {cost_saving:.2f} €/year"
    )

    print(
        f"Saving   : {cost_saving_percent:.3f} %"
    )


    print()

    print("METHANE CONSUMPTION")

    print(
        f"Baseline : {baseline_methane:.2f} ton/year"
    )

    print(
        f"Hybrid   : {hybrid_methane:.2f} ton/year"
    )

    print(
        f"Saving   : {methane_saving:.2f} ton/year"
    )


    print()

    print("CO2 EMISSIONS")

    print(
        f"Baseline : {baseline_co2:.2f} ton/year"
    )

    print(
        f"Hybrid   : {hybrid_co2:.2f} ton/year"
    )

    print(
        f"Saving   : {co2_saving:.2f} ton/year"
    )

    print(
        f"Saving   : {co2_saving_percent:.3f} %"
    )


if __name__ == "__main__":
    main()