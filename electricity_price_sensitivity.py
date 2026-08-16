"""
=========================================================
ELECTRICITY PRICE SENSITIVITY

Sensitivity analysis of the hybrid boiler operation
under different electricity-price scenarios.

The Italian 2025 electricity-price profile is used as
reference and scaled by different factors.

All other parameters remain unchanged.
=========================================================
"""

import os
import pandas as pd
import config

from economics.prices import ElectricityPrices
from optimization import find_best_temperature


# =========================================================
# SETTINGS
# =========================================================

PRICE_SCENARIOS = {
    "100%": 1.00,
    "80%": 0.80,
    "60%": 0.60,
    "40%": 0.40,
    "20%": 0.20,
}

THERMAL_POWER_KW = 5233.3
METHANE_INITIAL = 409.57

PRICE_FILE = (
    "data/20250101_20251231_MGP_PrezziZonali_COUP-2.xlsx"
)

OUTPUT_FOLDER = "results/electricity_sensitivity"

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True,
)


# =========================================================
# RUN ONE SCENARIO
# =========================================================

def run_scenario(
    prices,
    price_factor,
    scenario_name,
):

    results = []

    print()
    print("========================================")
    print(f"SCENARIO: {scenario_name}")
    print(
        f"Electricity price factor : "
        f"{price_factor:.0%}"
    )
    print("========================================")

    # -----------------------------------------------------
    # Loop over all hours
    # -----------------------------------------------------

    for hour in range(prices.number_of_hours()):

        original_price = prices.get_price(hour)

        electricity_price = (
            original_price * price_factor
        )

        # -------------------------------------------------
        # Optimization
        # -------------------------------------------------

        best = find_best_temperature(
            thermal_power_kw=THERMAL_POWER_KW,
            methane_initial=METHANE_INITIAL,
            electricity_price=electricity_price,
            carbon_price=config.CARBON_TAX,
            verbose=False,
        )

        # -------------------------------------------------
        # Save hourly result
        # -------------------------------------------------

        results.append({

            "date":
                prices.get_date(hour),

            "hour":
                prices.get_hour(hour),

            "original_electricity_price":
                original_price,

            "electricity_price":
                electricity_price,

            "price_factor":
                price_factor,

            "temperature":
                best["temperature"],

            "methane_kg_h":
                best["fuel"]["methane_kg_h"],

            "electric_power_kw":
                best["preheater"][
                    "total_electric_power_kw"
                ],

            "co2_kg_h":
                best["emissions"]["co2_kg_h"],

            "gas_cost":
                best["economics"]["gas_cost"],

            "electricity_cost":
                best["economics"]["electricity_cost"],

            "carbon_cost":
                best["economics"]["carbon_cost"],

            "total_cost":
                best["economics"]["total_cost"],

            "iterations":
                best["iterations"],
        })

        # -------------------------------------------------
        # Progress
        # -------------------------------------------------

        if (hour + 1) % 500 == 0:

            print(
                f"Completed "
                f"{hour + 1}/"
                f"{prices.number_of_hours()} hours"
            )

    return pd.DataFrame(results)


# =========================================================
# ANALYZE SCENARIO
# =========================================================

def summarize_scenario(
    df,
    scenario_name,
    price_factor,
):

    return {

        "scenario":
            scenario_name,

        "price_factor":
            price_factor,

        "average_electricity_price":
            df["electricity_price"].mean(),

        "average_temperature":
            df["temperature"].mean(),

        "hours_at_250C":
            (df["temperature"] == 250).sum(),

        "hours_at_600C":
            (df["temperature"] == 600).sum(),

        "average_methane_kg_h":
            df["methane_kg_h"].mean(),

        "total_methane_t":
            df["methane_kg_h"].sum() / 1000,

        "total_electricity_MWh":
            df["electric_power_kw"].sum() / 1000,

        "total_co2_t":
            df["co2_kg_h"].sum() / 1000,

        "average_total_cost_eur_h":
            df["total_cost"].mean(),

        "total_operating_cost_eur":
            df["total_cost"].sum(),

        "total_gas_cost_eur":
            df["gas_cost"].sum(),

        "total_electricity_cost_eur":
            df["electricity_cost"].sum(),

        "total_carbon_cost_eur":
            df["carbon_cost"].sum(),
    }


# =========================================================
# MAIN
# =========================================================

def main():

    print()
    print("========================================")
    print("ELECTRICITY PRICE SENSITIVITY")
    print("========================================")

    print()
    print(
        "Reference electricity prices:"
    )

    print(PRICE_FILE)

    # -----------------------------------------------------
    # Load Italian electricity prices
    # -----------------------------------------------------

    prices = ElectricityPrices(
        PRICE_FILE
    )

    print()
    print(
        f"Hours available : "
        f"{prices.number_of_hours()}"
    )

    summaries = []

    # -----------------------------------------------------
    # Run all scenarios
    # -----------------------------------------------------

    for scenario_name, price_factor in PRICE_SCENARIOS.items():

        df = run_scenario(
            prices=prices,
            price_factor=price_factor,
            scenario_name=scenario_name,
        )

        # -------------------------------------------------
        # Save hourly results
        # -------------------------------------------------

        output_file = (
            f"{OUTPUT_FOLDER}/"
            f"sensitivity_{scenario_name.replace('%', '')}.csv"
        )

        df.to_csv(
            output_file,
            index=False,
        )

        # -------------------------------------------------
        # Summary
        # -------------------------------------------------

        summary = summarize_scenario(
            df=df,
            scenario_name=scenario_name,
            price_factor=price_factor,
        )

        summaries.append(summary)

    # =====================================================
    # SUMMARY DATAFRAME
    # =====================================================

    summary_df = pd.DataFrame(
        summaries
    )

    # -----------------------------------------------------
    # Save summary
    # -----------------------------------------------------

    summary_df.to_csv(
        f"{OUTPUT_FOLDER}/"
        "electricity_price_sensitivity_summary.csv",
        index=False,
    )

    # =====================================================
    # PRINT RESULTS
    # =====================================================

    print()
    print("========================================")
    print("SENSITIVITY ANALYSIS COMPLETED")
    print("========================================")

    print()

    for _, row in summary_df.iterrows():

        print(
            f"{row['scenario']:>4} | "
            f"Price = "
            f"{row['average_electricity_price']:7.2f} €/MWh | "
            f"T = "
            f"{row['average_temperature']:6.1f} °C | "
            f"CH4 = "
            f"{row['total_methane_t']:8.2f} t | "
            f"CO2 = "
            f"{row['total_co2_t']:8.2f} t | "
            f"Cost = "
            f"{row['total_operating_cost_eur']/1e6:6.3f} M€"
        )

    # =====================================================
    # DETAILED TABLE
    # =====================================================

    print()
    print("========================================")
    print("SUMMARY TABLE")
    print("========================================")

    display_columns = [

        "scenario",

        "average_electricity_price",

        "average_temperature",

        "hours_at_250C",

        "hours_at_600C",

        "total_methane_t",

        "total_electricity_MWh",

        "total_co2_t",

        "total_operating_cost_eur",

        "total_gas_cost_eur",

        "total_electricity_cost_eur",

        "total_carbon_cost_eur",
    ]

    print(
        summary_df[
            display_columns
        ].to_string(
            index=False
        )
    )

    # =====================================================
    # SAVING RELATIVE TO 100% SCENARIO
    # =====================================================

    baseline_cost = summary_df.loc[
        summary_df["price_factor"] == 1.00,
        "total_operating_cost_eur"
    ].iloc[0]

    baseline_methane = summary_df.loc[
        summary_df["price_factor"] == 1.00,
        "total_methane_t"
    ].iloc[0]

    baseline_co2 = summary_df.loc[
        summary_df["price_factor"] == 1.00,
        "total_co2_t"
    ].iloc[0]

    summary_df["cost_saving_vs_100_percent_eur"] = (
        baseline_cost
        - summary_df["total_operating_cost_eur"]
    )

    summary_df["methane_reduction_vs_100_percent_t"] = (
        baseline_methane
        - summary_df["total_methane_t"]
    )

    summary_df["co2_reduction_vs_100_percent_t"] = (
        baseline_co2
        - summary_df["total_co2_t"]
    )

    # -----------------------------------------------------
    # Save updated summary
    # -----------------------------------------------------

    summary_df.to_csv(
        f"{OUTPUT_FOLDER}/"
        "electricity_price_sensitivity_summary.csv",
        index=False,
    )

    # =====================================================
    # FINAL RESULTS
    # =====================================================

    print()
    print("========================================")
    print("EFFECT OF LOWER ELECTRICITY PRICES")
    print("========================================")

    for _, row in summary_df.iterrows():

        print()
        print(
            f"Scenario: {row['scenario']}"
        )

        print(
            f"Average temperature : "
            f"{row['average_temperature']:.1f} °C"
        )

        print(
            f"CH4 reduction       : "
            f"{row['methane_reduction_vs_100_percent_t']:.2f} t"
        )

        print(
            f"CO2 reduction       : "
            f"{row['co2_reduction_vs_100_percent_t']:.2f} t"
        )

        print(
            f"Cost saving         : "
            f"{row['cost_saving_vs_100_percent_eur']:.2f} €"
        )

    print()
    print("========================================")
    print("FILES SAVED")
    print("========================================")

    print(
        f"Output folder : "
        f"{OUTPUT_FOLDER}"
    )


if __name__ == "__main__":
    main()