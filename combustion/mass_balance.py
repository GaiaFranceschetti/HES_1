"""
=========================================================
MASS BALANCE

Calculates the mass flow rates of reactants and products
starting from the methane consumption.

Author:
Alberto Maso
Gaia Franceschetti
=========================================================
"""

from combustion.stoichiometry import calculate_stoichiometry


def calculate_mass_balance(methane_kg_h):
    """
    Calculates the real mass flow rates of the combustion process.

    Parameters
    ----------
    methane_kg_h : float
        Methane consumption [kg/h]

    Returns
    -------
    dict
    """

    stoich = calculate_stoichiometry(1.0)

    results = {

        "methane": methane_kg_h,

        "oxygen": stoich["oxygen"] * methane_kg_h,

        "nitrogen": stoich["nitrogen"] * methane_kg_h,

        "air": stoich["air"] * methane_kg_h,

        "co2": stoich["co2"] * methane_kg_h,

        "h2o": stoich["h2o"] * methane_kg_h

    }

    return results


def print_mass_balance(results):

    print()
    print("========================================")
    print("MASS BALANCE")
    print("========================================")

    print(f"Methane         : {results['methane']:.2f} kg/h")
    print(f"Air             : {results['air']:.2f} kg/h")
    print(f"Oxygen          : {results['oxygen']:.2f} kg/h")
    print(f"Nitrogen        : {results['nitrogen']:.2f} kg/h")
    print(f"CO2             : {results['co2']:.2f} kg/h")
    print(f"H2O             : {results['h2o']:.2f} kg/h")