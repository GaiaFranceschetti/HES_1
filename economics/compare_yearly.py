"""
=========================================================
YEARLY COMPARISON

Comparison between conventional boiler and hybrid boiler
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

    baseline_cost = baseline["total_cost"].sum()
    hybrid_cost = hybrid["total_cost"].sum()

    baseline_methane = baseline["methane"].sum()
    hybrid_methane = hybrid["methane"].sum()

    saving_cost = baseline_cost - hybrid_cost

    saving_percentage = (
        saving_cost / baseline_cost * 100
    )

    methane_saving = (
        baseline_methane - hybrid_methane
    )

    print()
    print("========================================")
    print("YEARLY COMPARISON")
    print("========================================")

    print()

    print(
        f"Baseline cost : {baseline_cost:.2f} €/year"
    )

    print(
        f"Hybrid cost   : {hybrid_cost:.2f} €/year"
    )

    print()

    print(
        f"Cost saving   : {saving_cost:.2f} €/year"
    )

    print(
        f"Saving        : {saving_percentage:.3f} %"
    )

    print()

    print(
        f"Methane saving: {methane_saving/1000:.2f} ton/year"
    )


if __name__ == "__main__":
    main()