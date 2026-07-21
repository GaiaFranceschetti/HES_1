"""
=========================================================
CASE COMPARISON
=========================================================
"""

from solver import solve_operating_point


def solve_preheated_case(
    thermal_power_kw,
    methane_initial,
):
    return solve_operating_point(
        thermal_power_kw,
        methane_initial,
    )


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
    print(f"Iterations      : {case_b['iterations']}")