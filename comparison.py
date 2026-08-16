"""
=========================================================
CASE COMPARISON
=========================================================
Compare two operating points of the hybrid boiler.
=========================================================
"""

import config

from solver import solve_operating_point


def solve_preheated_case(
    thermal_power_kw,
    methane_initial,
    outlet_temperature,
    electricity_price=config.DEFAULT_ELECTRICITY_PRICE,
    carbon_price=config.CARBON_TAX,
):
    """
    Solve one operating point.
    """

    return solve_operating_point(
        thermal_power_kw=thermal_power_kw,
        methane_initial=methane_initial,
        outlet_temperature=outlet_temperature,
        electricity_price=electricity_price,
        carbon_price=carbon_price,
        verbose=False,
    )


def print_comparison(reference, hybrid):
    """
    Compare two operating points.
    """

    methane_ref = reference["fuel"]["methane_kg_h"]
    methane_hybrid = hybrid["fuel"]["methane_kg_h"]

    methane_saving = methane_ref - methane_hybrid
    methane_saving_percent = 100 * methane_saving / methane_ref

    co2_ref = reference["emissions"]["co2_kg_h"]
    co2_hybrid = hybrid["emissions"]["co2_kg_h"]

    print()
    print("========================================")
    print("CASE COMPARISON")
    print("========================================")

    print()
    print("Fuel")
    print("----------------------------------------")
    print(f"Reference methane      : {methane_ref:.2f} kg/h")
    print(f"Hybrid methane         : {methane_hybrid:.2f} kg/h")
    print(f"Saving                 : {methane_saving:.2f} kg/h")
    print(f"Saving                 : {methane_saving_percent:.2f} %")

    print()
    print("Electricity")
    print("----------------------------------------")
    print(
        f"Preheater power        : "
        f"{hybrid['preheater']['total_electric_power_kw']:.2f} kW"
    )

    print()
    print("Emissions")
    print("----------------------------------------")
    print(f"Reference CO₂          : {co2_ref:.2f} kg/h")
    print(f"Hybrid CO₂             : {co2_hybrid:.2f} kg/h")
    print(f"Reduction              : {co2_ref-co2_hybrid:.2f} kg/h")

    print()
    print("Economics")
    print("----------------------------------------")
    print(f"Gas cost               : {hybrid['economics']['gas_cost']:.2f} €/h")
    print(f"Electricity cost       : {hybrid['economics']['electricity_cost']:.2f} €/h")
    print(f"Carbon cost            : {hybrid['economics']['carbon_cost']:.2f} €/h")
    print(f"Operating cost         : {hybrid['economics']['total_cost']:.2f} €/h")

    print()
    print("Solver")
    print("----------------------------------------")
    print(f"Iterations             : {hybrid['iterations']}")