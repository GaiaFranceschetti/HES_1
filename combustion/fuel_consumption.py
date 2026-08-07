"""
=========================================================
FUEL CONSUMPTION
=========================================================
"""

import math
import config


def methane_consumption(
    thermal_power_kw,
    thermal_power_to_air_kw=0,
    air_temperature=None,
    verbose=True,
):
    """
    Calculate methane consumption required to produce the
    requested steam thermal power.
    """

    # -----------------------------------------------------
    # Preheating effectiveness
    # -----------------------------------------------------

    if air_temperature is None:

        effectiveness = 0.0

    else:

        delta_T = (
            air_temperature
            - config.REFERENCE_AIR_TEMPERATURE
        )

        delta_T = max(delta_T, 0)

        effectiveness = (
            config.MAX_PREHEATING_EFFECTIVENESS
            * (
                1
                - math.exp(
                    -delta_T
                    / config.PREHEATING_CHARACTERISTIC_TEMPERATURE
                )
            )
        )

    # -----------------------------------------------------
    # Effective thermal contribution of the preheater
    # -----------------------------------------------------

    effective_preheating = (
        effectiveness
        * thermal_power_to_air_kw
    )

    burner_power_kw = (
        thermal_power_kw
        - effective_preheating
    )

    burner_power_kw = max(burner_power_kw, 0)

    # -----------------------------------------------------
    # Fuel thermal power
    # -----------------------------------------------------

    fuel_power_kw = (
        burner_power_kw
        / config.BOILER_EFFICIENCY
    )

    # -----------------------------------------------------
    # Methane consumption
    # -----------------------------------------------------

    methane_kg_s = (
        fuel_power_kw
        / config.LHV_METHANE
    )

    methane_kg_h = methane_kg_s * 3600

    # -----------------------------------------------------
    # Print
    # -----------------------------------------------------

    if verbose:

        print()
        print("========================================")
        print("FUEL CONSUMPTION")
        print("========================================")

        print(f"Steam thermal power    : {thermal_power_kw:.1f} kW")
        print(f"Thermal power to air   : {thermal_power_to_air_kw:.1f} kW")
        print(f"Effectiveness          : {effectiveness:.3f}")
        print(f"Effective preheating   : {effective_preheating:.1f} kW")
        print(f"Burner thermal power   : {burner_power_kw:.1f} kW")
        print(f"Boiler efficiency      : {config.BOILER_EFFICIENCY:.2f}")
        print(f"Fuel thermal power     : {fuel_power_kw:.1f} kW")
        print(f"Methane consumption    : {methane_kg_s:.4f} kg/s")
        print(f"Methane consumption    : {methane_kg_h:.1f} kg/h")

    return {
        "methane_kg_h": methane_kg_h,
        "methane_kg_s": methane_kg_s,
        "burner_power_kw": burner_power_kw,
        "fuel_power_kw": fuel_power_kw,
        "effectiveness": effectiveness,
        "effective_preheating": effective_preheating,
    }