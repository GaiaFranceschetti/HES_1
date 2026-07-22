"""
=========================================================
EMISSIONS MODEL

CO2 emissions calculation from methane consumption.
=========================================================
"""

import config


def methane_to_co2(methane_kg):
    """
    Calculate CO2 emissions from methane consumption.

    Parameters
    ----------
    methane_kg : float
        Methane consumption [kg]

    Returns
    -------
    float
        CO2 emissions [kg]
    """

    return methane_kg * config.CO2_EMISSION_FACTOR
