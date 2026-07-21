"""
=========================================================
CASE COMPARISON

Comparison between:

Case A -> Standard combustion air
Case B -> Preheated combustion air

=========================================================
"""

import config


def methane_with_preheated_air(
        thermal_power_kw,
        air_flow_kg_h):

    air_flow_kg_s = air_flow_kg_h / 3600

    delta_t = (
        config.AIR_TEMPERATURE_PREHEATED
        - config.AIR_TEMPERATURE_STANDARD
    )

    q_air = (
        air_flow_kg_s
        * config.CP_AIR
        * delta_t
    )

    q_burner = thermal_power_kw - q_air

    fuel_power = q_burner / config.BOILER_EFFICIENCY

    methane_kg_h = (
        fuel_power
        / config.LHV_METHANE
        * 3600
    )

    return {

        "q_air": q_air,

        "q_burner": q_burner,

        "methane": methane_kg_h

    }


def print_comparison(case_a, case_b):

    print()
    print("========================================")
    print("CASE COMPARISON")
    print("========================================")

    print(f"Case A methane : {case_a:.2f} kg/h")

    print(f"Case B methane : {case_b['methane']:.2f} kg/h")

    saving = case_a - case_b["methane"]

    saving_percent = saving / case_a * 100

    print(f"Saving          : {saving:.2f} kg/h")

    print(f"Saving          : {saving_percent:.2f} %")