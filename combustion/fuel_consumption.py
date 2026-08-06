"""
=========================================================
FUEL CONSUMPTION
=========================================================
"""

import config


def methane_consumption(
    thermal_power_kw,
    thermal_power_to_air_kw=0,
    verbose=True,
):
    """
    Calculate methane consumption required to produce the
    requested steam thermal power.

    Parameters
    ----------
    thermal_power_kw : float
        Thermal power required by the steam generator.

    thermal_power_to_air_kw : float
        Thermal power transferred to the combustion air by
        the induction preheater.

    verbose : bool
        Print results.

    Returns
    -------
    dict
        Dictionary containing methane consumption and
        burner/fuel powers.
    """

    # Thermal power still required from the burner
    burner_power_kw = thermal_power_kw - thermal_power_to_air_kw

    if burner_power_kw < 0:
        burner_power_kw = 0

    # Fuel thermal power
    fuel_power_kw = burner_power_kw / config.BOILER_EFFICIENCY

    # Methane consumption
    methane_kg_s = fuel_power_kw / config.LHV_METHANE
    methane_kg_h = methane_kg_s * 3600

    if verbose:
        print()
        print("========================================")
        print("FUEL CONSUMPTION")
        print("========================================")

        print(f"Steam thermal power    : {thermal_power_kw:.1f} kW")
        print(f"Thermal power to air   : {thermal_power_to_air_kw:.1f} kW")
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
    }