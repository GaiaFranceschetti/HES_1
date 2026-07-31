"""
=========================================================
CONFIGURATION FILE
Hybrid Steam Generator Project

All physical constants are stored here.

Author:
Alberto Maso
Gaia Franceschetti
=========================================================
"""

# =========================================================
# UNIVERSAL CONSTANTS
# =========================================================

R = 8.314462618          # Universal Gas Constant [J/mol K]

# =========================================================
# ATMOSPHERIC CONDITIONS
# =========================================================

P_ATM = 101325           # Pa

T_AMBIENT = 25           # °C

AMBIENT_PRESSURE = 101.325       # kPa

# =========================================================
# AIR TEMPERATURES
# =========================================================

T_AIR_STANDARD = 250     # °C

T_AIR_PREHEATED = 450    # °C

# =========================================================
# METHANE PROPERTIES
# =========================================================

LHV_CH4 = 50e6           # J/kg

M_CH4 = 16.04e-3         # kg/mol

# =========================================================
# AIR PROPERTIES
# =========================================================

CP_AIR = 1005            # J/kg K

CP_CO2 = 844             # J/kg K

CP_H2O = 1860            # J/kg K

CP_N2 = 1040             # J/kg K

# =========================================================
# AIR COMPOSITION
# =========================================================

O2_FRACTION = 0.21

N2_FRACTION = 0.79

# =========================================================
# COMBUSTION
# =========================================================

EXCESS_AIR = 1.10

TARGET_FLAME_TEMPERATURE = 1900      # °C

# =========================================================
# EVAPORATOR
# =========================================================

STEAM_PRODUCTION = 8000              # kg/h

STEAM_PRESSURE = 16                  # bar

# =========================================================
# PREHEATER
# =========================================================

PREHEATER_EFFICIENCY = 0.95

# --------------------------------------------------------
# Boiler efficiency
# --------------------------------------------------------

BOILER_EFFICIENCY = 0.92      # 92%
# --------------------------------------------------------
# Fuel properties
# --------------------------------------------------------

LHV_METHANE = 50000.0      # kJ/kg

# --------------------------------------------------------
# Air properties
# --------------------------------------------------------

CP_AIR = 1.05          # kJ/(kg·K)

AIR_TEMPERATURE_STANDARD = 250.0   # °C

AIR_TEMPERATURE_PREHEATED = 450.0  # °C

INDUCTION_EFFICIENCY = 0.95

# ==========================================================
# AIR PREHEATER
# ==========================================================

# Air properties
AIR_CP = 1005                    # J/kg/K
AIR_GAS_CONSTANT = 287           # J/kg/K
AIR_DYNAMIC_VISCOSITY = 1.85e-5  # Pa*s

# Ambient conditions
AIR_INLET_TEMPERATURE = 25       # °C
AMBIENT_PRESSURE = 101325        # Pa

# Induction
INDUCTION_EFFICIENCY = 0.95

# Design assumptions
DESIGN_AIR_VELOCITY = 15         # m/s
TARGET_RESIDENCE_TIME = 2.0      # s

# Pressure losses
FRICTION_FACTOR = 0.03

# Fan
FAN_EFFICIENCY = 0.75

# ----------------------------------------------------------
# PREHEATER GEOMETRY
# ----------------------------------------------------------

TUBE_THICKNESS = 0.003          # m

DEFAULT_MATERIAL = "AISI310"

# ----------------------------------------------------------
# Ambient conditions
# ----------------------------------------------------------

AMBIENT_TEMPERATURE = 25          # °C

EXTERNAL_CONVECTION_COEFFICIENT = 8.0   # W/m²K

# ----------------------------------------------------------
# Thermal insulation
# ----------------------------------------------------------

DEFAULT_INSULATION = "RockWool"

INSULATION_THICKNESS = 0.05      # m (5 cm)