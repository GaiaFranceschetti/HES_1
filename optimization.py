"""
=========================================================
OPTIMIZATION
=========================================================

Search for the outlet air temperature that minimizes
the hourly operating cost of the hybrid boiler.
=========================================================
"""

import config

from solver import solve_operating_point


def find_best_temperature(
    thermal_power_kw,
    methane_initial,
    electricity_price,
    carbon_price=0,
    verbose=True,
):
    """
    Find the outlet air temperature that minimizes
    the total operating cost.
    """

    best_result = None
    best_cost = float("inf")

    for temperature in range(
        config.MIN_PREHEAT_TEMPERATURE,
        config.MAX_PREHEAT_TEMPERATURE + 1,
        config.PREHEAT_TEMPERATURE_STEP,
    ):

        result = solve_operating_point(
            thermal_power_kw=thermal_power_kw,
            methane_initial=methane_initial,
            outlet_temperature=temperature,
            electricity_price=electricity_price,
            carbon_price=carbon_price,
            verbose=False,
        )

        cost = result["economics"]["total_cost"]

        if verbose:
            print(
                f"T = {temperature:3d} °C | "
                f"CH4 = {result['fuel']['methane_kg_h']:.2f} kg/h | "
                f"P_el = {result['preheater']['total_electric_power_kw']:.2f} kW | "
                f"Cost = {cost:.2f} €/h"
            )

        if cost < best_cost:

            best_cost = cost
            best_result = result

            # Store optimal temperature
            best_result["temperature"] = temperature

    return best_result


if __name__ == "__main__":

    result = find_best_temperature(
        thermal_power_kw=5233.3,
        methane_initial=409.57,
        electricity_price=config.DEFAULT_ELECTRICITY_PRICE,
        carbon_price=config.CARBON_TAX,
        verbose=True,
    )

    print()
    print("========================================")
    print("BEST OPERATING POINT")
    print("========================================")

    print(f"Optimal temperature      : {result['temperature']} °C")
    print(f"Methane consumption      : {result['fuel']['methane_kg_h']:.2f} kg/h")
    print(f"Electric power           : {result['preheater']['total_electric_power_kw']:.2f} kW")
    print(f"CO₂ emissions            : {result['emissions']['co2_kg_h']:.2f} kg/h")
    print(f"Gas cost                 : {result['economics']['gas_cost']:.2f} €/h")
    print(f"Electricity cost         : {result['economics']['electricity_cost']:.2f} €/h")
    print(f"Carbon cost              : {result['economics']['carbon_cost']:.2f} €/h")
    print(f"Total operating cost     : {result['economics']['total_cost']:.2f} €/h")