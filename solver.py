from combustion.mass_balance import calculate_mass_balance
from combustion.fuel_consumption import methane_consumption

from economics.emissions import methane_to_co2
from economics.costs import total_cost

from preheater.design import design_preheater


def solve_operating_point(
    thermal_power_kw,
    methane_initial,
    outlet_temperature,
    electricity_price,
    carbon_price=0,
    tolerance=0.01,
    max_iterations=20,
    verbose=True,
):
    """
    Solve the coupled hybrid boiler model.

    CH4
      ↓
    Mass balance
      ↓
    Air preheater design
      ↓
    Updated methane consumption
      ↓
    Repeat until convergence
    """

    methane = methane_initial

    for iteration in range(max_iterations):

        # --------------------------------------------------
        # Mass balance
        # --------------------------------------------------

        mass = calculate_mass_balance(methane)

        air_mass_flow = mass["air"] / 3600

        # --------------------------------------------------
        # Air preheater
        # --------------------------------------------------

        preheater = design_preheater(
            air_mass_flow=air_mass_flow,
            outlet_temperature=outlet_temperature,
        )

        thermal_power_to_air = preheater["thermal_power_kw"]

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
        # Emissions
        # --------------------------------------------------

        emissions = methane_to_co2(
            methane_new
        )

        # --------------------------------------------------
        # Economics
        # --------------------------------------------------

        economics = total_cost(
            methane_kg_h=methane_new,
            electric_power_kw=preheater["total_electric_power_kw"],
            electricity_price=electricity_price,
            carbon_price=carbon_price,
        )

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

                "emissions": emissions,

                "economics": economics,

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

        "emissions": emissions,

        "economics": economics,

        "iterations": max_iterations,

    }