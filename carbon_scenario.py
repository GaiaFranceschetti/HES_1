"""
=========================================================
CARBON SCENARIOS

Sensitivity analysis of the hybrid boiler under
different carbon tax scenarios.
=========================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

OUTPUT_FOLDER = "results/carbon_scenarios"

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True,
)

from yearly_optimization import main as yearly_optimization


def main():

    # -----------------------------------------------------
    # Carbon tax scenarios [€/tCO2]
    # -----------------------------------------------------

    carbon_prices = [
        0,
        50,
        80,
        100,
        150,
        200,
    ]

    results = []

    print()
    print("========================================")
    print("CARBON TAX SENSITIVITY")
    print("========================================")

    # -----------------------------------------------------
    # Run all scenarios
    # -----------------------------------------------------

    for carbon_price in carbon_prices:

        print()
        print(
            f"Running scenario with carbon tax = "
            f"{carbon_price} €/tCO₂"
        )

        df = yearly_optimization(
            carbon_price=carbon_price,
        )

        results.append({

            "carbon_price":
                carbon_price,

            "average_temperature":
                df["temperature"].mean(),

            "average_methane_kg_h":
                df["methane_kg_h"].mean(),

            "average_electric_power_kw":
                df["electric_power_kw"].mean(),

            "total_methane_t":
                df["methane_kg_h"].sum()/1000,

            "total_co2_t":
                df["co2_kg_h"].sum()/1000,

            "total_electricity_MWh":
                df["electric_power_kw"].sum()/1000,

            "gas_cost":
                df["gas_cost"].sum(),

            "electricity_cost":
                df["electricity_cost"].sum(),

            "carbon_cost":
                df["carbon_cost"].sum(),

            "total_cost":
                df["total_cost"].sum(),

        })

    # -----------------------------------------------------
    # Summary dataframe
    # -----------------------------------------------------

    summary = pd.DataFrame(results)

    # -----------------------------------------------------
    # Savings with respect to zero carbon tax
    # -----------------------------------------------------

    baseline = summary.iloc[0]

    summary["methane_saving_t"] = (
        baseline["total_methane_t"]
        - summary["total_methane_t"]
    )

    summary["co2_reduction_t"] = (
        baseline["total_co2_t"]
        - summary["total_co2_t"]
    )

    summary["additional_cost"] = (
        summary["total_cost"]
        - baseline["total_cost"]
    )

    # -----------------------------------------------------
    # Save results
    # -----------------------------------------------------

    summary.to_csv(
        "results/carbon_scenarios.csv",
        index=False,
    )
    # =====================================================
    # Total operating cost
    # =====================================================

    plt.figure(figsize=(7,5))

    plt.plot(
        summary["carbon_price"],
        summary["total_cost"]/1e6,
        marker="o",
    )

    plt.xlabel("Carbon tax [€/tCO₂]")
    plt.ylabel("Annual operating cost [M€]")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_FOLDER}/cost_vs_carbon_tax.png"
    )

    plt.close()

    # =====================================================
    # Average temperature
    # =====================================================

    plt.figure(figsize=(7,5))

    plt.plot(
        summary["carbon_price"],
        summary["average_temperature"],
        marker="o",
    )

    plt.xlabel("Carbon tax [€/tCO₂]")
    plt.ylabel("Average optimal temperature [°C]")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_FOLDER}/temperature_vs_carbon_tax.png"
    )

    plt.close()

    # =====================================================
    # Methane consumption
    # =====================================================

    plt.figure(figsize=(7,5))

    plt.plot(
        summary["carbon_price"],
        summary["total_methane_t"],
        marker="o",
    )

    plt.xlabel("Carbon tax [€/tCO₂]")
    plt.ylabel("Annual methane consumption [t]")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_FOLDER}/methane_vs_carbon_tax.png"
    )

    plt.close()

    # =====================================================
    # CO2 emissions
    # =====================================================

    plt.figure(figsize=(7,5))

    plt.plot(
        summary["carbon_price"],
        summary["total_co2_t"],
        marker="o",
    )

    plt.xlabel("Carbon tax [€/tCO₂]")
    plt.ylabel("Annual CO₂ emissions [t]")

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        f"{OUTPUT_FOLDER}/co2_vs_carbon_tax.png"
    )

    plt.close()


    # -----------------------------------------------------
    # Print summary
    # -----------------------------------------------------

    print()
    print("========================================")
    print("CARBON SCENARIOS SUMMARY")
    print("========================================")

    print(summary)

    print()
    print(
        "Results saved to "
        "'results/carbon_scenarios.csv'"
    )

    print()
    print("========================================")
    print("PLOTS CREATED")
    print("========================================")
    print(f"Output folder : {OUTPUT_FOLDER}")

if __name__ == "__main__":
    main()