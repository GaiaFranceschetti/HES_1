"""
=========================================================
EMISSIONS MODEL

CO2 emissions calculation from methane consumption.
=========================================================
"""

import config


def methane_to_co2(methane_kg_h):
    """
    Calculate CO2 emissions.

    Parameters
    ----------
    methane_kg_h : float
        Methane consumption [kg/h]

    Returns
    -------
    dict
        CO2 emissions.
    """

    co2_kg_h = methane_kg_h * config.CO2_EMISSION_FACTOR

    return {
        "methane_kg_h": methane_kg_h,
        "co2_kg_h": co2_kg_h,
    }
