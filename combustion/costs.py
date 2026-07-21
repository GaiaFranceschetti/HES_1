"""
=========================================================
OPERATING COSTS

Calculates hourly operating costs.

=========================================================
"""

import config


def calculate_costs(
    methane_kg_h,
    electric_power_kw,
):

    methane_energy_kwh = (
        methane_kg_h
        * config.LHV_METHANE
    )

    gas_cost = (
        methane_energy_kwh
        * config.GAS_PRICE
    )

    electric_cost = (
        electric_power_kw
        * config.ELECTRICITY_PRICE
    )

    total_cost = gas_cost + electric_cost

    return {

        "gas_cost": gas_cost,

        "electric_cost": electric_cost,

        "total_cost": total_cost,

    }


def print_costs(results):

    print()
    print("========================================")
    print("OPERATING COSTS")
    print("========================================")

    print(f"Gas cost         : {results['gas_cost']:.2f} €/h")
    print(f"Electricity cost : {results['electric_cost']:.2f} €/h")
    print(f"Total cost       : {results['total_cost']:.2f} €/h")
    