"""
=========================================================
PLOT CARBON TAX SCENARIOS

Visualization of hybrid boiler response to carbon price.

Outputs:
- Operating cost
- CO2 emissions
- Flexibility activation
- CO2 savings

=========================================================
"""

import pandas as pd
import matplotlib.pyplot as plt


# =========================================================
# LOAD RESULTS
# =========================================================

df = pd.read_csv(
    "results/carbon_scenarios.csv"
)


# =========================================================
# 1) OPERATING COST
# =========================================================

plt.figure(figsize=(8,5))

plt.plot(
    df["carbon_price"],
    df["cost"] / 1e6,
    marker="o",
)

plt.xlabel(
    "Carbon price [€/ton CO$_2$]"
)

plt.ylabel(
    "Annual operating cost [M€/year]"
)

plt.title(
    "Impact of carbon pricing on operating cost"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "results/carbon_cost.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()



# =========================================================
# 2) CO2 EMISSIONS
# =========================================================

plt.figure(figsize=(8,5))

plt.plot(
    df["carbon_price"],
    df["co2"],
    marker="o",
)

plt.xlabel(
    "Carbon price [€/ton CO$_2$]"
)

plt.ylabel(
    "CO$_2$ emissions [ton/year]"
)

plt.title(
    "Impact of carbon pricing on CO$_2$ emissions"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "results/carbon_emissions.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()



# =========================================================
# 3) FLEXIBILITY ACTIVATION
# =========================================================

plt.figure(figsize=(8,5))

plt.plot(
    df["carbon_price"],
    df["active_hours"],
    marker="o",
)

plt.xlabel(
    "Carbon price [€/ton CO$_2$]"
)

plt.ylabel(
    "Preheater activation [h/year]"
)

plt.title(
    "Impact of carbon pricing on hybrid boiler flexibility"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "results/carbon_flexibility.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()



# =========================================================
# 4) CO2 SAVINGS
# =========================================================

baseline_co2 = df.loc[
    df["carbon_price"] == 0,
    "co2"
].values[0]


df["co2_saving"] = (
    baseline_co2 - df["co2"]
)


plt.figure(figsize=(8,5))

plt.plot(
    df["carbon_price"],
    df["co2_saving"],
    marker="o",
)

plt.xlabel(
    "Carbon price [€/ton CO$_2$]"
)

plt.ylabel(
    "CO$_2$ reduction [ton/year]"
)

plt.title(
    "Impact of carbon pricing on CO$_2$ reduction"
)

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "results/carbon_savings.png",
    dpi=300,
    bbox_inches="tight",
)

plt.show()



# =========================================================
# PRINT SUMMARY TABLE
# =========================================================

print()

print("========================================")
print("CARBON TAX SUMMARY")
print("========================================")

print()

print(
    df[
        [
            "carbon_price",
            "cost",
            "co2",
            "co2_saving",
            "active_hours"
        ]
    ]
)