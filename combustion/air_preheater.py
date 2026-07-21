"""
=========================================================
AIR PREHEATER

Calculates the electric power required to preheat
the combustion air.

=========================================================
"""

import config


def calculate_air_preheater(air_flow_kg_h):

    air_flow_kg_s = air_flow_kg_h / 3600

    delta_t = (
        config.AIR_TEMPERATURE_PREHEATED
        - config.AIR_TEMPERATURE_STANDARD
    )

    thermal_power_kw = (
        air_flow_kg_s
        * config.CP_AIR
        * delta_t
    )

    electric_power_kw = (
        thermal_power_kw
        / config.INDUCTION_EFFICIENCY
    )

    return {

        "air_flow": air_flow_kg_h,

        "thermal_power": thermal_power_kw,

        "electric_power": electric_power_kw,

        "delta_t": delta_t

    }


def print_air_preheater(results):

    print()
    print("========================================")
    print("AIR PREHEATER")
    print("========================================")

    print(f"Air flow               : {results['air_flow']:.1f} kg/h")
    print(f"Temperature increase   : {results['delta_t']:.1f} °C")
    print(f"Heat to air            : {results['thermal_power']:.1f} kW")
    print(f"Electric power         : {results['electric_power']:.1f} kW")