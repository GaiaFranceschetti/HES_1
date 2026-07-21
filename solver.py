from combustion.mass_balance import calculate_mass_balance
from combustion.air_preheater import calculate_air_preheater
from combustion.fuel_consumption import methane_consumption


def solve_operating_point(
    thermal_power_kw,
    methane_initial,
    tolerance=0.01,
    max_iterations=20,
):
    """
    Solve the coupled system:

    CH4 --> Air --> Air Preheater --> New CH4

    until convergence.
    """

    methane = methane_initial

    for iteration in range(max_iterations):

        # Mass balance
        mass = calculate_mass_balance(methane)

        # Air preheater
        preheater = calculate_air_preheater(mass["air"])

        # New methane consumption
        methane_new = methane_consumption(
            thermal_power_kw,
            preheater["thermal_power"],
        )

        error = abs(methane_new - methane)

        print(
            f"\nIteration {iteration+1:2d}"
            f" | CH4 = {methane_new:.2f} kg/h"
            f" | Error = {error:.4f}"
        )

        if error < tolerance:

            return {
                "methane": methane_new,
                "mass": mass,
                "preheater": preheater,
                "iterations": iteration + 1,
            }

        methane = methane_new

    print("\nWARNING: maximum number of iterations reached.")

    return {
        "methane": methane,
        "mass": mass,
        "preheater": preheater,
        "iterations": max_iterations,
    }