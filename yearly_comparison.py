"""
=========================================================
YEARLY COMPARISON

Comparison between:

Scenario A
- Conventional boiler
- Fixed combustion air temperature

Scenario B
- Hybrid boiler
- Hourly optimized air preheating

=========================================================
"""

import config

from economics.prices import ElectricityPrices

from solver import solve_operating_point
from optimization import find_best_temperature


def main():

    # -----------------------------------------------------
    # Electricity prices
    # -----------------------------------------------------

    prices = ElectricityPrices(
        "data/20250101_20251231_MGP_PrezziZonali_COUP-2.xlsx"
    )

    # -----------------------------------------------------
    # Boiler operating conditions
    # -----------------------------------------------------

    thermal_power_kw = 5233.3
    methane_initial = 409.57

    # -----------------------------------------------------
    # Annual totals
    # -----------------------------------------------------

    reference = {

        "methane": 0.0,
        "electricity": 0.0,
        "co2": 0.0,
        "gas_cost": 0.0,
        "electricity_cost": 0.0,
        "carbon_cost": 0.0,
        "total_cost": 0.0,

    }

    hybrid = {

        "methane": 0.0,
        "electricity": 0.0,
        "co2": 0.0,
        "gas_cost": 0.0,
        "electricity_cost": 0.0,
        "carbon_cost": 0.0,
        "total_cost": 0.0,

    }

    print()
    print("========================================")
    print("START YEARLY COMPARISON")
    print("========================================")

    # -----------------------------------------------------
    # Loop over all hours
    # -----------------------------------------------------

    for hour in range(prices.number_of_hours()):

        electricity_price = prices.get_price(hour)

        # -------------------------------------------------
        # Scenario A
        # -------------------------------------------------

        conventional = solve_operating_point(

            thermal_power_kw=thermal_power_kw,

            methane_initial=methane_initial,

            outlet_temperature=config.MIN_PREHEAT_TEMPERATURE,

            electricity_price=electricity_price,

            carbon_price=config.CARBON_TAX,

            verbose=False,

        )

        # -------------------------------------------------
        # Scenario B
        # -------------------------------------------------

        optimized = find_best_temperature(

            thermal_power_kw=thermal_power_kw,

            methane_initial=methane_initial,

            electricity_price=electricity_price,

            carbon_price=config.CARBON_TAX,

            verbose=False,

        )

        # -------------------------------------------------
        # Accumulate reference
        # -------------------------------------------------

        reference["methane"] += conventional["fuel"]["methane_kg_h"]

        reference["electricity"] += (
            conventional["preheater"]["total_electric_power_kw"]
            / 1000
        )

        reference["co2"] += conventional["emissions"]["co2_kg_h"]

        reference["gas_cost"] += conventional["economics"]["gas_cost"]

        reference["electricity_cost"] += conventional["economics"]["electricity_cost"]

        reference["carbon_cost"] += conventional["economics"]["carbon_cost"]

        reference["total_cost"] += conventional["economics"]["total_cost"]

        # -------------------------------------------------
        # Accumulate hybrid
        # -------------------------------------------------

        hybrid["methane"] += optimized["fuel"]["methane_kg_h"]

        hybrid["electricity"] += (
            optimized["preheater"]["total_electric_power_kw"]
            / 1000
        )

        hybrid["co2"] += optimized["emissions"]["co2_kg_h"]

        hybrid["gas_cost"] += optimized["economics"]["gas_cost"]

        hybrid["electricity_cost"] += optimized["economics"]["electricity_cost"]

        hybrid["carbon_cost"] += optimized["economics"]["carbon_cost"]

        hybrid["total_cost"] += optimized["economics"]["total_cost"]

        if (hour + 1) % 500 == 0:

            print(
                f"Completed {hour+1}/{prices.number_of_hours()} hours"
            )

    # -----------------------------------------------------
    # Final comparison
    # -----------------------------------------------------

    print()
    print("========================================")
    print("YEARLY COMPARISON")
    print("========================================")

    methane_saved = reference["methane"] - hybrid["methane"]

    co2_saved = reference["co2"] - hybrid["co2"]

    net_saving = reference["total_cost"] - hybrid["total_cost"]

    print()

    print("NATURAL GAS")

    print("----------------------------------------")

    print(f"Reference : {reference['methane']/1000:.2f} t")

    print(f"Hybrid    : {hybrid['methane']/1000:.2f} t")

    print(f"Saving    : {methane_saved/1000:.2f} t")

    print(
        f"Saving    : "
        f"{100*methane_saved/reference['methane']:.2f} %"
    )

    print()

    print("ELECTRICITY")

    print("----------------------------------------")

    print(
        f"Hybrid consumption : "
        f"{hybrid['electricity']:.2f} MWh"
    )

    print()

    print("CO2")

    print("----------------------------------------")

    print(f"Reference : {reference['co2']/1000:.2f} t")

    print(f"Hybrid    : {hybrid['co2']/1000:.2f} t")

    print(f"Reduction : {co2_saved/1000:.2f} t")

    print()

    print("ECONOMICS")

    print("----------------------------------------")

    print(f"Reference cost : {reference['total_cost']:.2f} €")

    print(f"Hybrid cost    : {hybrid['total_cost']:.2f} €")

    print(f"Net saving     : {net_saving:.2f} €")

    print()

    print("Gas cost saving")

    print(
        f"{reference['gas_cost']-hybrid['gas_cost']:.2f} €"
    )

    print()

    print("Carbon cost saving")

    print(
        f"{reference['carbon_cost']-hybrid['carbon_cost']:.2f} €"
    )

    print()

    print("Additional electricity cost")

    print(
        f"{hybrid['electricity_cost']-reference['electricity_cost']:.2f} €"
    )


if __name__ == "__main__":

    main()