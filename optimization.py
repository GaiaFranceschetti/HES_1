"""
=========================================================
OPTIMIZATION
=========================================================

Evaluate the operating cost of the hybrid boiler for a
given outlet air temperature.
"""
import config
from comparison import solve_preheated_case

from economics.costs import (
    gas_cost,
    electricity_cost,
    total_cost,
)


def evaluate_temperature(
    thermal_power_kw,
    methane_initial,
    outlet_temperature,
    electricity_price,
):
    """
    Evaluate one operating point.
    """

    # Solve the physical model
    result = solve_preheated_case(
        thermal_power_kw,
        methane_initial,
        outlet_temperature,
    )

    methane = result["methane"]
    electric_power = result["preheater"]["electric_power"]

    gas = gas_cost(methane)

    electricity = electricity_cost(
        electric_power,
        electricity_price,
    )

    total = total_cost(
        methane,
        electric_power,
        electricity_price,
    )

    return {
        "temperature": outlet_temperature,
        "methane": methane,
        "electric_power": electric_power,
        "gas_cost": gas,
        "electricity_cost": electricity,
        "cost": total,
        "iterations": result["iterations"],
    }


def find_best_temperature(
    thermal_power_kw,
    methane_initial,
    electricity_price,
):
    """
    Find the outlet air temperature that minimizes
    the hourly operating cost.
    """

    best_result = None
    best_cost = float("inf")

    for temperature in range(
        config.MIN_PREHEAT_TEMPERATURE,
        config.MAX_PREHEAT_TEMPERATURE + 1,
        config.PREHEAT_TEMPERATURE_STEP,
    ):

        result = evaluate_temperature(
            thermal_power_kw,
            methane_initial,
            temperature,
            electricity_price,
        )

        if result["cost"] < best_cost:
            best_cost = result["cost"]
            best_result = result

    return best_result


if __name__ == "__main__":

    result = find_best_temperature(
        thermal_power_kw=5233.3,
        methane_initial=409.57,
        electricity_price=10,
    )

    print()
    print("========================================")
    print("BEST OPERATING POINT")
    print("========================================")

    for key, value in result.items():
        print(f"{key:20s}: {value}")