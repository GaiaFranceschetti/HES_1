"""
=========================================================
MAIN - HYBRID BOILER SINGLE OPERATING POINT

Hybrid boiler model including:

- Steam generation
- Combustion
- Mass balance
- Detailed induction air preheater design
- Coupled methane / air iteration
- Comparison with conventional boiler

=========================================================
"""

import config

from combustion.combustion_model import print_configuration
from combustion.stoichiometry import print_stoichiometry

from combustion.energy_balance import (
    calculate_thermal_power,
    print_energy_balance,
)

from combustion.fuel_consumption import methane_consumption
from combustion.mass_balance import (
    calculate_mass_balance,
    print_mass_balance,
)

import preheater
from preheater.design import design_preheater

from comparison import (
    solve_preheated_case,
    print_comparison,
)


def main():

    print()
    print("========================================")
    print("HYBRID BOILER SINGLE POINT MODEL")
    print("========================================")

    # --------------------------------------------------
    # Physical configuration
    # --------------------------------------------------

    print_configuration()

    # --------------------------------------------------
    # Stoichiometry
    # --------------------------------------------------

    print_stoichiometry()

    # --------------------------------------------------
    # Steam thermal power
    # --------------------------------------------------

    energy = calculate_thermal_power()

    print_energy_balance(energy)

    # --------------------------------------------------
    # Conventional boiler
    # --------------------------------------------------

    fuel = methane_consumption(
        thermal_power_kw=energy["thermal_power_kw"],
        verbose=True,
    )

    methane = fuel["methane_kg_h"]

    mass = calculate_mass_balance(methane)

    print_mass_balance(mass)

    # --------------------------------------------------
    # Detailed induction preheater
    # --------------------------------------------------

    preheater = design_preheater(
        air_mass_flow=mass["air"] / 3600,
        outlet_temperature=config.AIR_TEMPERATURE_PREHEATED,
    )

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
    print(f"Radiation losses     : {preheater['radiation_losses_kw']:.2f} kW")
    print(f"Convection losses    : {preheater['convection_losses_kw']:.2f} kW")
    print(f"Total losses         : {preheater['total_losses_kw']:.2f} kW")

    # --------------------------------------------------
    # Hybrid operating point
    # --------------------------------------------------

    comparison = solve_preheated_case(
        thermal_power_kw=energy["thermal_power_kw"],
        methane_initial=methane,
        outlet_temperature=config.AIR_TEMPERATURE_PREHEATED,
    )

    print_comparison(
        methane,
        comparison,
    )


if __name__ == "__main__":
    main()
    