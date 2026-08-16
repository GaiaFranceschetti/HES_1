from combustion.mass_balance import (
    calculate_mass_balance,
    print_mass_balance,
)

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
    Solve one operating point of the hybrid boiler.
    """

    methane = methane_initial

    for iteration in range(max_iterations):

        # --------------------------------------------------
        # Mass balance
        # --------------------------------------------------

        mass = calculate_mass_balance(methane)

        if verbose:
            print_mass_balance(mass)

        air_mass_flow = mass["air"] / 3600

        # --------------------------------------------------
        # Air preheater
        # --------------------------------------------------

        preheater = design_preheater(
            air_mass_flow=air_mass_flow,
            outlet_temperature=outlet_temperature,
        )

        if verbose:

            print()
            print("========================================")
            print("PREHEATER DESIGN")
            print("========================================")

            print(f"Air mass flow          : {preheater['air_mass_flow']:.3f} kg/s")
            print(f"Outlet temperature     : {preheater['outlet_temperature']:.1f} °C")
            print(f"Thermal power to air   : {preheater['thermal_power_kw']:.1f} kW")
            print(f"Induction power        : {preheater['electric_power_kw']:.1f} kW")
            print(f"Fan power              : {preheater['fan_power_kw']:.2f} kW")
            print(f"Total electric power   : {preheater['total_electric_power_kw']:.1f} kW")
            print(f"Wall temperature       : {preheater['wall_temperature']:.1f} °C")
            print(f"Pressure drop          : {preheater['pressure_drop_pa']:.1f} Pa")
            print(f"Material OK            : {preheater['material_ok']}")
            print(f"Radiation losses       : {preheater['radiation_losses_kw']:.2f} kW")
            print(f"Convection losses      : {preheater['convection_losses_kw']:.2f} kW")
            print(f"Total losses           : {preheater['total_losses_kw']:.2f} kW")

        # --------------------------------------------------
        # Fuel consumption
        # --------------------------------------------------

        fuel = methane_consumption(
            thermal_power_kw=thermal_power_kw,
            thermal_power_to_air_kw=preheater["thermal_power_kw"],
            air_temperature=outlet_temperature,
            verbose=verbose,
        )

        methane_new = fuel["methane_kg_h"]

        # --------------------------------------------------
        # Emissions
        # --------------------------------------------------

        emissions = methane_to_co2(methane_new)

        # --------------------------------------------------
        # Economics
        # --------------------------------------------------

        economics = total_cost(
            methane_kg_h=methane_new,
            electric_power_kw=preheater["total_electric_power_kw"],
            electricity_price=electricity_price,
            carbon_price=carbon_price,
        )

        if verbose:

            print()
            print("========================================")
            print("ECONOMICS")
            print("========================================")

            print(f"Gas cost              : {economics['gas_cost']:.2f} €/h")
            print(f"Electricity cost      : {economics['electricity_cost']:.2f} €/h")
            print(f"Carbon cost           : {economics['carbon_cost']:.2f} €/h")
            print(f"Total operating cost  : {economics['total_cost']:.2f} €/h")

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

            break

        methane = methane_new

    else:

        if verbose:
            print("\nWARNING: Maximum number of iterations reached.")

    return {

        "methane": methane_new,

        "fuel": fuel,

        "mass": mass,

        "preheater": preheater,

        "emissions": emissions,

        "economics": economics,

        "iterations": iteration + 1,

    }