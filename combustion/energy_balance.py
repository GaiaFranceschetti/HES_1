"""
=========================================================
ENERGY BALANCE

Calculates the thermal power required to generate steam.

Author:
Alberto Maso
Gaia Franceschetti
=========================================================
"""

import config
from thermodynamics import steam_properties


def calculate_thermal_power():

    steam_flow_kg_h = config.STEAM_PRODUCTION
    steam_flow_kg_s = steam_flow_kg_h / 3600

    delta_h = (
        steam_properties.H_STEAM
        - steam_properties.H_FEEDWATER
    )

    thermal_power_kw = steam_flow_kg_s * delta_h
    thermal_power_mw = thermal_power_kw / 1000

    return {
        "steam_flow_kg_h": steam_flow_kg_h,
        "delta_h": delta_h,
        "thermal_power_kw": thermal_power_kw,
        "thermal_power_mw": thermal_power_mw,
    }


def print_energy_balance(results):

    print()
    print("========================================")
    print("ENERGY BALANCE")
    print("========================================")

    print(f"Steam production      : {results['steam_flow_kg_h']:.0f} kg/h")
    print(f"Feedwater enthalpy    : {steam_properties.H_FEEDWATER:.1f} kJ/kg")
    print(f"Steam enthalpy        : {steam_properties.H_STEAM:.1f} kJ/kg")
    print(f"Enthalpy increase     : {results['delta_h']:.1f} kJ/kg")
    print(f"Thermal power         : {results['thermal_power_kw']:.1f} kW")
    print(f"Thermal power         : {results['thermal_power_mw']:.3f} MW")