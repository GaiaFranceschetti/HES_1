"""
=========================================================
STOICHIOMETRY MODULE

Calculates the stoichiometric combustion of methane.

Author:
Alberto Maso
Gaia Franceschetti
=========================================================
"""

import config

# --------------------------------------------------------
# Molecular weights [kg/mol]
# --------------------------------------------------------

MW_CH4 = 16.04e-3
MW_O2 = 32.00e-3
MW_N2 = 28.0134e-3
MW_CO2 = 44.01e-3
MW_H2O = 18.015e-3

# --------------------------------------------------------
# Air composition
# --------------------------------------------------------

O2_MOLAR_FRACTION = 0.21
N2_MOLAR_FRACTION = 0.79

N2_O2_RATIO = N2_MOLAR_FRACTION / O2_MOLAR_FRACTION


def calculate_stoichiometry(fuel_mass_kg=1.0):
    """
    Calculate the stoichiometric combustion of methane.

    Parameters
    ----------
    fuel_mass_kg : float
        Methane mass [kg]

    Returns
    -------
    dict
        Stoichiometric results.
    """

    # ----------------------------
    # Fuel moles
    # ----------------------------

    n_ch4 = fuel_mass_kg / MW_CH4

    # ----------------------------
    # Oxygen
    # ----------------------------

    n_o2 = 2.0 * n_ch4

    # ----------------------------
    # Nitrogen
    # ----------------------------

    n_n2 = N2_O2_RATIO * n_o2

    # ----------------------------
    # Products
    # ----------------------------

    n_co2 = n_ch4

    n_h2o = 2.0 * n_ch4

    # ----------------------------
    # Masses
    # ----------------------------

    m_o2 = n_o2 * MW_O2

    m_n2 = n_n2 * MW_N2

    m_air = m_o2 + m_n2

    m_co2 = n_co2 * MW_CO2

    m_h2o = n_h2o * MW_H2O

    air_fuel_ratio = m_air / fuel_mass_kg

    results = {

        "fuel": fuel_mass_kg,

        "oxygen": m_o2,

        "nitrogen": m_n2,

        "air": m_air,

        "co2": m_co2,

        "h2o": m_h2o,

        "air_fuel_ratio": air_fuel_ratio

    }

    return results

def print_stoichiometry():

    fuel_mass = 1.0

    results = calculate_stoichiometry(fuel_mass)    

    print()
    print("========================================")
    print("STOICHIOMETRY")
    print("========================================")

    print(f"Fuel               : {results['fuel']:.3f} kg")
    print(f"Oxygen required    : {results['oxygen']:.3f} kg")
    print(f"Nitrogen           : {results['nitrogen']:.3f} kg")
    print(f"Total air          : {results['air']:.3f} kg")
    print(f"CO2 produced       : {results['co2']:.3f} kg")
    print(f"H2O produced       : {results['h2o']:.3f} kg")
    print(f"Air/Fuel ratio     : {results['air_fuel_ratio']:.3f}")