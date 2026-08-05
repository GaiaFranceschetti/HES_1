"""
Temperature-dependent thermophysical properties of dry air.

Reference temperature range:
20°C - 500°C

The implemented correlations are engineering approximations
suitable for preliminary thermal design.
"""

# ----------------------------------------------------------
# Specific heat
# ----------------------------------------------------------

def air_cp(T):

    """
    Specific heat [J/kgK]

    T in °C
    """

    return 1005 + 0.10 * (T - 20)


# ----------------------------------------------------------
# Thermal conductivity
# ----------------------------------------------------------

def air_conductivity(T):

    """
    Thermal conductivity [W/mK]

    T in °C
    """

    return 0.024 + 0.000075 * T


# ----------------------------------------------------------
# Dynamic viscosity
# ----------------------------------------------------------

def air_viscosity(T):

    """
    Dynamic viscosity [Pa s]

    T in °C
    """

    return 1.81e-5 * ((T + 273.15) / 293.15) ** 0.7


# ----------------------------------------------------------
# Prandtl number
# ----------------------------------------------------------

def air_prandtl(T):

    """
    Prandtl number [-]
    """

    return 0.71