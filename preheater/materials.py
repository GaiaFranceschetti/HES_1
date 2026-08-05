"""
Material properties used for the induction preheater.
Values are representative engineering values.
"""

MATERIALS = {

    "AISI304": {
        "thermal_conductivity": 16.2,
        "density": 8000,
        "cp": 500,
        "emissivity": 0.65,
        "max_temperature": 870
    },

    "AISI316": {
        "thermal_conductivity": 14.0,
        "density": 8000,
        "cp": 500,
        "emissivity": 0.62,
        "max_temperature": 900
    },

    "AISI321": {
        "thermal_conductivity": 16.3,
        "density": 7900,
        "cp": 500,
        "emissivity": 0.65,
        "max_temperature": 900
    },

    "AISI310": {
        "thermal_conductivity": 14.2,
        "density": 7900,
        "cp": 500,
        "emissivity": 0.72,
        "max_temperature": 1100
    },

    "RA330": {
        "thermal_conductivity": 15.0,
        "density": 7900,
        "cp": 460,
        "emissivity": 0.75,
        "max_temperature": 1140
    },

    "Inconel600": {
        "thermal_conductivity": 14.9,
        "density": 8470,
        "cp": 444,
        "emissivity": 0.70,
        "max_temperature": 1150
    },

    "Inconel601": {
        "thermal_conductivity": 15.3,
        "density": 8100,
        "cp": 450,
        "emissivity": 0.72,
        "max_temperature": 1200
    },

    "Inconel625": {
        "thermal_conductivity": 9.8,
        "density": 8440,
        "cp": 435,
        "emissivity": 0.68,
        "max_temperature": 980
    }

}