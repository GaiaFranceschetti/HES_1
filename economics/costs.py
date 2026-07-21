"""
=========================================================
ECONOMIC COSTS
=========================================================
Functions to calculate the hourly operating cost
of the hybrid boiler.
=========================================================
"""

import config


def methane_energy(methane_kg_h):
    """
    Convert methane mass flow [kg/h] into energy [MWh/h].
    """

    return methane_kg_h * config.METHANE_LHV_KWH_PER_KG / 1000


def gas_cost(methane_kg_h):
    """
    Calculate hourly gas cost [€/h].
    """

    energy = methane_energy(methane_kg_h)

    return energy * config.GAS_PRICE_EUR_PER_MWH


def electricity_cost(electric_power_kw, electricity_price):
    """
    Calculate hourly electricity cost [€/h].
    """

    electric_energy = electric_power_kw / 1000

    return electric_energy * electricity_price


def total_cost(
    methane_kg_h,
    electric_power_kw,
    electricity_price,
):
    """
    Calculate total hourly operating cost [€/h].
    """

    return (
        gas_cost(methane_kg_h)
        + electricity_cost(
            electric_power_kw,
            electricity_price,
        )
    )