"""
=========================================================
FUEL CONSUMPTION

=========================================================
"""

import config


def methane_consumption(thermal_power_kw):

    fuel_power_kw = thermal_power_kw / config.BOILER_EFFICIENCY

    methane_kg_s = fuel_power_kw / config.LHV_METHANE

    methane_kg_h = methane_kg_s * 3600

    print()
    print("========================================")
    print("FUEL CONSUMPTION")
    print("========================================")

    print(f"Boiler efficiency      : {config.BOILER_EFFICIENCY:.2f}")
    print(f"Fuel thermal power     : {fuel_power_kw:.1f} kW")
    print(f"Methane consumption    : {methane_kg_s:.4f} kg/s")
    print(f"Methane consumption    : {methane_kg_h:.1f} kg/h")

    return methane_kg_h 