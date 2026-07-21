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

from combustion.air_preheater import (
    calculate_air_preheater,
    print_air_preheater,
)

from comparison import (
    solve_preheated_case,
    print_comparison,
)

import comparison

def main():

    print_configuration()

    print_stoichiometry()

    energy = calculate_thermal_power()

    print_energy_balance(energy)

    methane =  methane_consumption(energy["thermal_power_kw"])

    mass = calculate_mass_balance(methane)
    
    print_mass_balance(mass)

    preheater = calculate_air_preheater(mass["air"])

    print_air_preheater(preheater)

    comparison = solve_preheated_case(
    energy["thermal_power_kw"],
    methane
)

    print_comparison(
    methane,
    comparison
)
    

if __name__ == "__main__":
    main() 