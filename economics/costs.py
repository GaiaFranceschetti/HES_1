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
    Convert methane consumption [kg/h]
    into thermal energy [MWh/h].
    """

    # LHV_METHANE è in kJ/kg
    energy_kwh_h = methane_kg_h * config.LHV_METHANE / 3600

    return energy_kwh_h / 1000



def gas_cost(methane_kg_h):
    """
    Calculate hourly gas cost [€/h].
    """

    energy = methane_energy(methane_kg_h)

    return energy * config.NATURAL_GAS_PRICE



def electricity_cost(electric_power_kw, electricity_price):
    """
    Calculate hourly electricity cost [€/h].
    """

    electric_energy = electric_power_kw / 1000

    return electric_energy * electricity_price



def carbon_cost(co2_kg, carbon_price):
    """
    Calculate carbon tax cost [€/h].

    Parameters
    ----------
    co2_kg : float
        CO2 emissions [kg/h]

    carbon_price : float
        Carbon price [€/ton CO2]

    Returns
    -------
    float
        Carbon cost [€/h]
    """

    co2_ton = co2_kg / 1000

    return co2_ton * carbon_price


def total_cost(
    methane_kg_h,
    electric_power_kw,
    electricity_price,
    carbon_price=0,
):

    gas = gas_cost(
        methane_kg_h
    )

    electricity = electricity_cost(
        electric_power_kw,
        electricity_price,
    )

    co2_kg = (
        methane_kg_h
        * config.CO2_EMISSION_FACTOR
    )

    carbon = carbon_cost(
        co2_kg,
        carbon_price,
    )

    total = (
        gas
        + electricity
        + carbon
    )

    return {

        "gas_cost": gas,

        "electricity_cost": electricity,

        "carbon_cost": carbon,

        "total_cost": total,

        "co2_kg_h": co2_kg,

    }