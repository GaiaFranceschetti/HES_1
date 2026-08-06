import math

from .materials import MATERIALS

from .insulation import INSULATIONS

from .air_properties import (
    air_cp,
    air_conductivity,
    air_viscosity,
    air_prandtl,
)

from .preheater_config import (
    AIR_INLET_TEMPERATURE,
    INDUCTION_EFFICIENCY,
    AMBIENT_PRESSURE,
    FRICTION_FACTOR,
    FAN_EFFICIENCY,
    TUBE_THICKNESS,
    DEFAULT_MATERIAL,
    AMBIENT_TEMPERATURE,
    EXTERNAL_CONVECTION_COEFFICIENT,
    INSULATION_THICKNESS,
)

def design_preheater(
    air_mass_flow,
    outlet_temperature,
    air_velocity=15.0,
    material=DEFAULT_MATERIAL,
    insulation="RockWool"
):

    # ----------------------------------------------------------
    # Material properties
    # ----------------------------------------------------------

    material_data = MATERIALS[material]

    thermal_conductivity = material_data["thermal_conductivity"]

    max_temperature = material_data["max_temperature"]

    emissivity = material_data["emissivity"]

    # ----------------------------------------------------------
    # Insulation properties
    # ----------------------------------------------------------

    insulation_data = INSULATIONS[insulation]

    insulation_k = insulation_data["k"]

    insulation_max_temperature = insulation_data["max_temperature"]

    # ----------------------------------------------------------
    # Temperature rise
    # ----------------------------------------------------------

    delta_T = outlet_temperature - AIR_INLET_TEMPERATURE

    # ----------------------------------------------------------
    # Mean air temperature
    # ----------------------------------------------------------

    mean_temperature = (
        AIR_INLET_TEMPERATURE
        + outlet_temperature
    ) / 2

    temperature_K = mean_temperature + 273.15

    # ----------------------------------------------------------
    # Air properties
    # ----------------------------------------------------------

    cp_air = air_cp(mean_temperature)

    air_k = air_conductivity(mean_temperature)

    air_mu = air_viscosity(mean_temperature)

    prandtl = air_prandtl(mean_temperature)

    # ----------------------------------------------------------
    # Thermal power
    # ----------------------------------------------------------

    thermal_power_kw = (
        air_mass_flow
        * cp_air
        * delta_T
    ) / 1000

    # ----------------------------------------------------------
    # Electric power
    # ----------------------------------------------------------

    electric_power_kw = (
        thermal_power_kw
        / INDUCTION_EFFICIENCY
    )
   
    # ----------------------------------------------------------
    # Air density
    # ----------------------------------------------------------

    air_density = (
        AMBIENT_PRESSURE
        / (
            287
            * temperature_K
        )
    )

    # ----------------------------------------------------------
    # Volume flow
    # ----------------------------------------------------------

    volume_flow = (
        air_mass_flow
        / air_density
    )

    # ----------------------------------------------------------
    # Duct area
    # ----------------------------------------------------------

    duct_area = (
        volume_flow
        / air_velocity
    )

    # ----------------------------------------------------------
    # Duct diameter
    # ----------------------------------------------------------

    duct_diameter = math.sqrt(
        (
            4
            * duct_area
        )
        / math.pi
    )

    outer_diameter = duct_diameter + 2 * TUBE_THICKNESS

    

    # ----------------------------------------------------------
    # Residence time
    # ----------------------------------------------------------

    TARGET_RESIDENCE_TIME = 2.0

    heated_length = (
        air_velocity
        * TARGET_RESIDENCE_TIME
    )

    heated_volume = (
        duct_area
        * heated_length
    )

    # ----------------------------------------------------------
    # Insulation geometry
    # ----------------------------------------------------------
    
    insulation_outer_diameter = (
           outer_diameter
           + 2 * INSULATION_THICKNESS
    )
    
    insulation_external_surface = (
           math.pi
           * insulation_outer_diameter
           * heated_length
    )

    # ----------------------------------------------------------
    # Heat exchange surfaces
    # ----------------------------------------------------------

    internal_surface = (

        math.pi

        * duct_diameter

        * heated_length

    )

    external_surface = (

        math.pi

        * outer_diameter

        * heated_length

    )

    # ----------------------------------------------------------
    # Reynolds number
    # ----------------------------------------------------------

    reynolds = (
        air_density
        * air_velocity
        * duct_diameter
        / air_mu
    )

    if reynolds < 2300:
        flow_regime = "Laminar"
    elif reynolds < 4000:
        flow_regime = "Transition"
    else:
        flow_regime = "Turbulent"

    # ----------------------------------------------------------
    # Nusselt number
    # ----------------------------------------------------------

    if flow_regime == "Turbulent":
       nusselt = (
        0.023
        * reynolds**0.8
        * prandtl**0.4
    )
    else:
       nusselt = None

    # ----------------------------------------------------------
    # Convective heat transfer coefficient
    # ----------------------------------------------------------

    if nusselt is not None:
       heat_transfer_coefficient = (
        nusselt
        * air_k
        / duct_diameter
    )
    else:
       heat_transfer_coefficient = None

    # ----------------------------------------------------------
    # Inner wall temperature
    # ----------------------------------------------------------

    wall_temperature = (
       mean_temperature
       + (
         thermal_power_kw * 1000
       ) / (
        heat_transfer_coefficient
        * internal_surface
       )
    )

    # ----------------------------------------------------------
    # Tube conduction resistance
    # ----------------------------------------------------------

    conduction_resistance = (
        math.log(
          outer_diameter / duct_diameter
        )
        /
        (
          2
          * math.pi
          * thermal_conductivity
          * heated_length
        )
    )

    # ----------------------------------------------------------
    # Insulation thermal resistance
    # ----------------------------------------------------------
#
 #   insulation_resistance = (
  #     math.log(
   #        insulation_outer_diameter / outer_diameter
    #   )
     #  /
      # (
       #   2
        #  * math.pi
         # * insulation_k
          #* heated_length
       #)
    #)
    # ----------------------------------------------------------
    # Outer wall temperature
    # ----------------------------------------------------------

    outer_wall_temperature = (
        wall_temperature
        + (
          thermal_power_kw
          * 1000
          * conduction_resistance
        )
    ) 

    # ----------------------------------------------------------
    # Outer insulation temperature
    # ----------------------------------------------------------

#    outer_insulation_temperature = (
#       outer_wall_temperature
#       - (
#          thermal_power_kw
#          * 1000
#          * insulation_resistance
#       )
#    )

    # ----------------------------------------------------------
    # Material verification
    # ----------------------------------------------------------

    SAFETY_MARGIN = 50      # °C

    material_ok = (
       wall_temperature
       <= max_temperature - SAFETY_MARGIN
    )
 
    # ----------------------------------------------------------
    # Radiation heat losses
    # ----------------------------------------------------------

    STEFAN_BOLTZMANN = 5.670374419e-8

    wall_temperature_K = wall_temperature + 273.15

    ambient_temperature_K = AIR_INLET_TEMPERATURE + 273.15

    radiation_losses_kw = (
        emissivity
        * STEFAN_BOLTZMANN
        * external_surface
        * (
           wall_temperature_K**4
           - ambient_temperature_K**4
        )
    ) / 1000

    # ----------------------------------------------------------
    # External convection losses
    # ----------------------------------------------------------

    convection_losses_kw = (
       EXTERNAL_CONVECTION_COEFFICIENT
       * external_surface
       * (
          outer_wall_temperature
          - AMBIENT_TEMPERATURE
       )
    ) / 1000

    total_losses_kw = (
    radiation_losses_kw
    + convection_losses_kw
    )

    # ----------------------------------------------------------
    # Required induction power
    # ----------------------------------------------------------

    required_induction_power_kw = (
       thermal_power_kw
       + total_losses_kw
    )

    electric_power_kw = (
       required_induction_power_kw
       / INDUCTION_EFFICIENCY
    )

    # ----------------------------------------------------------
    # Pressure drop
    # ----------------------------------------------------------

    pressure_drop_pa = (
        FRICTION_FACTOR
        * heated_length
        / duct_diameter
        * (
            air_density
            * air_velocity**2
            / 2
        )
    )

    # ----------------------------------------------------------
    # Fan power
    # ----------------------------------------------------------

    fan_power_kw = (
        pressure_drop_pa
        * volume_flow
        / FAN_EFFICIENCY
    ) / 1000

    # ----------------------------------------------------------
    # Total electric power
    # ----------------------------------------------------------

    total_electric_power_kw = (
        electric_power_kw
        + fan_power_kw
    )

    # ----------------------------------------------------------
    # Results
    # ----------------------------------------------------------

    return {

        "air_mass_flow": air_mass_flow,

        "air_density": air_density,

        "volume_flow": volume_flow,

        "air_velocity": air_velocity,

        "duct_area": duct_area,

        "duct_diameter": duct_diameter,

        "material": material,

        "material": material,

        "tube_thickness": TUBE_THICKNESS,

        "outer_diameter": outer_diameter,

        "internal_surface": internal_surface,

        "external_surface": external_surface,

        "thermal_conductivity": thermal_conductivity,

        "max_material_temperature": max_temperature,

        "emissivity": emissivity,

        "delta_T": delta_T,

        "outlet_temperature": outlet_temperature,

        "outlet_temperature": outlet_temperature,

        "thermal_power_kw": thermal_power_kw,

        "electric_power_kw": electric_power_kw,

        "heated_length": heated_length,

        "heated_volume": heated_volume,

        "residence_time": TARGET_RESIDENCE_TIME,

        "reynolds": reynolds,

        "flow_regime": flow_regime,

        "cp_air": cp_air,

        "air_conductivity": air_k,

        "air_viscosity": air_mu,

        "prandtl": prandtl,

        "nusselt": nusselt,

        "heat_transfer_coefficient": heat_transfer_coefficient,

        "wall_temperature": wall_temperature,

        "material_ok": material_ok,

        "insulation": insulation,

        "insulation_k": insulation_k,

        "insulation_max_temperature": insulation_max_temperature,

        "insulation_outer_diameter": insulation_outer_diameter,

        "insulation_external_surface": insulation_external_surface,

        "radiation_losses_kw": radiation_losses_kw,

        "convection_losses_kw": convection_losses_kw,

        "total_losses_kw": total_losses_kw,

        "required_induction_power_kw": required_induction_power_kw,

        "conduction_resistance": conduction_resistance,

        "outer_wall_temperature": outer_wall_temperature,

#        "insulation_resistance": insulation_resistance,

#        "outer_insulation_temperature": outer_insulation_temperature,

        "pressure_drop_pa": pressure_drop_pa,

        "fan_power_kw": fan_power_kw,

        "total_electric_power_kw": total_electric_power_kw,
    }