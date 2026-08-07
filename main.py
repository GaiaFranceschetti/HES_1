"""
=========================================================
MAIN - HYBRID BOILER SINGLE OPERATING POINT
=========================================================
"""

import config

from combustion.combustion_model import print_configuration
from combustion.stoichiometry import print_stoichiometry

from combustion.energy_balance import (
    calculate_thermal_power,
    print_energy_balance,
)

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
    # Configuration
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
    # Initial methane guess
    # --------------------------------------------------

    methane_initial = 410.0

    # --------------------------------------------------
    # Conventional boiler
    # --------------------------------------------------

    reference = solve_preheated_case(
        thermal_power_kw=energy["thermal_power_kw"],
        methane_initial=methane_initial,
        outlet_temperature=config.AIR_TEMPERATURE_STANDARD,
    )

    # --------------------------------------------------
    # Hybrid boiler
    # --------------------------------------------------

    hybrid = solve_preheated_case(
        thermal_power_kw=energy["thermal_power_kw"],
        methane_initial=methane_initial,
        outlet_temperature=config.AIR_TEMPERATURE_PREHEATED,
    )

    # --------------------------------------------------
    # Comparison
    # --------------------------------------------------

    print_comparison(
        reference,
        hybrid,
    )


if __name__ == "__main__":
    main()

