from combustion.mass_balance import calculate_mass_balance
from combustion.fuel_consumption import methane_consumption

from preheater.design import design_preheater


def solve_operating_point(
    thermal_power_kw,
    methane_initial,
    outlet_temperature,
    tolerance=0.01,
    max_iterations=20,
    verbose=True,
):
    """
    Solve the coupled system:

        CH4
          ↓
    Mass balance
          ↓
    Air preheater design
          ↓
    Updated methane
          ↓
    Repeat until convergence
    """

    methane = methane_initial

    for iteration in range(max_iterations):

        # --------------------------------------------------
        # Mass balance
        # --------------------------------------------------

        mass = calculate_mass_balance(methane)

        # Convert air flow from kg/h to kg/s
        air_mass_flow = mass["air"] / 3600

        # --------------------------------------------------
        # Detailed preheater design
        # --------------------------------------------------

        preheater = design_preheater(
            air_mass_flow=air_mass_flow,
            outlet_temperature=outlet_temperature,
        )

        # Useful quantities
        thermal_power_to_air = preheater["thermal_power_kw"]
        electric_power = preheater["total_electric_power_kw"]

        # --------------------------------------------------
        # Fuel consumption
        # --------------------------------------------------

        fuel = methane_consumption(
            thermal_power_kw=thermal_power_kw,
            thermal_power_to_air_kw=thermal_power_to_air,
            verbose=verbose,
        )

        methane_new = fuel["methane_kg_h"]

        # --------------------------------------------------
        # Convergence
        # --------------------------------------------------

        error = abs(methane_new - methane)

        if verbose:
            print(
                f"\nIteration {iteration + 1:2d}"
                f" | CH4 = {methane_new:.2f} kg/h"
                f" | Error = {error:.4f}"
            )

        if error < tolerance:
            return {
                "methane": methane_new,
                "fuel": fuel,
                "mass": mass,
                "preheater": preheater,
                "iterations": iteration + 1,
            }

        methane = methane_new

    if verbose:
        print("\nWARNING: Maximum number of iterations reached.")

    return {
        "methane": methane,
        "fuel": fuel,
        "mass": mass,
        "preheater": preheater,
        "iterations": max_iterations,
    }