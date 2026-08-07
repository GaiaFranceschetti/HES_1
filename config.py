"""
=========================================================
CONFIGURATION FILE
Hybrid Boiler with Induction Air Preheater

All physical constants, operating conditions,
design parameters and economic assumptions.

Author:
Alberto Maso
Gaia Franceschetti
=========================================================
"""

# ==========================================================
# UNIVERSAL CONSTANTS
# ==========================================================

R = 8.314462618                    # J/(mol·K)

# ==========================================================
# ATMOSPHERIC CONDITIONS
# ==========================================================

P_ATM = 101325                     # Pa
AMBIENT_PRESSURE = 101325          # Pa

T_AMBIENT = 25                     # °C
AMBIENT_TEMPERATURE = 25           # °C

# ==========================================================
# STEAM GENERATOR
# ==========================================================

STEAM_PRODUCTION = 8000            # kg/h
STEAM_PRESSURE = 16                # bar

BOILER_EFFICIENCY = 0.92

# ==========================================================
# COMBUSTION
# ==========================================================

EXCESS_AIR = 1.10

TARGET_FLAME_TEMPERATURE = 1900    # °C

# ==========================================================
# METHANE
# ==========================================================

M_CH4 = 16.04e-3                   # kg/mol

LHV_METHANE = 50000.0              # kJ/kg

# ==========================================================
# AIR TEMPERATURES
# ==========================================================

T_AIR_STANDARD = 250               # °C
T_AIR_PREHEATED = 450              # °C

AIR_TEMPERATURE_STANDARD = 250     # °C
AIR_TEMPERATURE_PREHEATED = 450    # °C

AIR_INLET_TEMPERATURE = 25         # °C

# ==========================================================
# AIR PROPERTIES
# ==========================================================

CP_AIR = 1005                      # J/(kg·K)

AIR_CP = 1005                      # J/(kg·K)

AIR_GAS_CONSTANT = 287             # J/(kg·K)

AIR_DYNAMIC_VISCOSITY = 1.85e-5    # Pa·s

CP_CO2 = 844                       # J/(kg·K)
CP_H2O = 1860                      # J/(kg·K)
CP_N2 = 1040                       # J/(kg·K)

# ==========================================================
# AIR COMPOSITION
# ==========================================================

O2_FRACTION = 0.21
N2_FRACTION = 0.79

STOICHIOMETRIC_AIR_FUEL_RATIO = 17.13

# ==========================================================
# PREHEATER
# ==========================================================

INDUCTION_EFFICIENCY = 0.95

DESIGN_AIR_VELOCITY = 15           # m/s

TARGET_RESIDENCE_TIME = 2.0        # s

FRICTION_FACTOR = 0.03

FAN_EFFICIENCY = 0.75

# ==========================================================
# PREHEATER GEOMETRY
# ==========================================================

TUBE_THICKNESS = 0.003             # m

DEFAULT_MATERIAL = "AISI310"

EXTERNAL_CONVECTION_COEFFICIENT = 10.0    # W/(m²·K)

INSULATION_THICKNESS = 0.0         # m

# ==========================================================
# EMISSIONS
# ==========================================================

CO2_EMISSION_FACTOR = 2.744        # kg CO2 / kg CH4

# ==========================================================
# ECONOMICS
# ==========================================================

NATURAL_GAS_PRICE = 45.0           # €/MWh

DEFAULT_ELECTRICITY_PRICE = 100 # €/MWh

CARBON_TAX = 80.0                  # €/tCO2

# ==========================================================
# OPTIMIZATION SETTINGS
# ==========================================================

MIN_PREHEAT_TEMPERATURE = 250      # °C
MAX_PREHEAT_TEMPERATURE = 600      # °C
PREHEAT_TEMPERATURE_STEP = 25      # °C

# ==========================================================
# COMBUSTION IMPROVEMENT
# ==========================================================

REFERENCE_AIR_TEMPERATURE = 250      # °C

EFFICIENCY_GAIN_PER_100C = 0.01

# ==========================================================
# PREHEATING EFFECTIVENESS
# ==========================================================

REFERENCE_AIR_TEMPERATURE = 250      # °C

MAX_PREHEATING_EFFECTIVENESS = 0.90

PREHEATING_CHARACTERISTIC_TEMPERATURE = 120      # °C