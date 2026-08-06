"""
=========================================================
CASE COMPARISON
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

    return solve_operating_point(
        thermal_power_kw=thermal_power_kw,
        methane_initial=methane_initial,
        outlet_temperature=outlet_temperature,
        electricity_price=electricity_price,
        carbon_price=carbon_price,
        verbose=False,
    )


def print_comparison(case_a, case_b):

    print()
    print("========================================")
    print("CASE COMPARISON")
    print("========================================")

    print(f"Case A methane        : {case_a:.2f} kg/h")
    print(f"Case B methane        : {case_b['methane']:.2f} kg/h")

    saving = case_a - case_b["methane"]
    saving_percent = saving / case_a * 100

    print(f"Methane saving        : {saving:.2f} kg/h")
    print(f"Methane saving        : {saving_percent:.2f} %")

    print()
    print(f"Electric power        : {case_b['preheater']['total_electric_power_kw']:.2f} kW")

    print(f"CO2 emissions         : {case_b['emissions']['co2_kg_h']:.2f} kg/h")

    print()
    print(f"Gas cost              : {case_b['economics']['gas_cost']:.2f} €/h")
    print(f"Electricity cost      : {case_b['economics']['electricity_cost']:.2f} €/h")
    print(f"Carbon cost           : {case_b['economics']['carbon_cost']:.2f} €/h")
    print(f"Total operating cost  : {case_b['economics']['total_cost']:.2f} €/h")

    print()
    print(f"Iterations            : {case_b['iterations']}")