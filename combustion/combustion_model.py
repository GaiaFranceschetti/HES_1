"""
=========================================================
COMBUSTION MODEL

First version

This module calculates the methane consumption
required to keep the flame temperature constant.

=========================================================
"""

from config import *


def print_configuration():

    print("========================================")
    print("COMBUSTION MODEL")
    print("========================================")

    print(f"Ambient Pressure : {P_ATM/1000:.1f} kPa")

    print(f"Air Temperature Standard : {T_AIR_STANDARD} °C")

    print(f"Air Temperature Preheated : {T_AIR_PREHEATED} °C")

    print(f"Target Flame Temperature : {TARGET_FLAME_TEMPERATURE} °C")

    print(f"Steam Production : {STEAM_PRODUCTION} kg/h")

    print(f"Steam Pressure : {STEAM_PRESSURE} bar")

    print("========================================")


if __name__ == "__main__":

    print_configuration()
