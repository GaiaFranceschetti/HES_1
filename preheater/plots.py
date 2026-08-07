"""
=========================================================
PLOTS

Generate all figures from yearly_results.csv
=========================================================
"""

import os

import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------------------------------
# Create output folder
# -----------------------------------------------------

OUTPUT_FOLDER = "results/plots"

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True,
)

# -----------------------------------------------------
# Load results
# -----------------------------------------------------

df = pd.read_csv(
    "results/yearly_results.csv"
)

plt.rcParams["figure.dpi"] = 200

# -----------------------------------------------------
# Prepare additional variables
# -----------------------------------------------------

df["datetime"] = pd.to_datetime(
    df["date"],
    format="%d/%m/%Y"
)

df["month"] = df["datetime"].dt.month

# =====================================================
# Temperature distribution
# =====================================================

plt.figure(figsize=(8,5))

plt.hist(
    df["temperature"],
    bins=15,
)

plt.xlabel("Optimal air temperature [°C]")
plt.ylabel("Hours")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/temperature_distribution.png"
)

plt.close()


# =====================================================
# Temperature vs electricity price
# =====================================================

plt.figure(figsize=(8,5))

plt.scatter(
    df["electricity_price"],
    df["temperature"],
    s=6,
)

plt.xlabel("Electricity price [€/MWh]")
plt.ylabel("Optimal air temperature [°C]")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/temperature_vs_price.png"
)

plt.close()


# =====================================================
# Methane vs electricity price
# =====================================================

plt.figure(figsize=(8,5))

plt.scatter(
    df["electricity_price"],
    df["methane_kg_h"],
    s=6,
)

plt.xlabel("Electricity price [€/MWh]")
plt.ylabel("Methane consumption [kg/h]")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/methane_vs_price.png"
)

plt.close()


# =====================================================
# Operating cost vs electricity price
# =====================================================

plt.figure(figsize=(8,5))

plt.scatter(
    df["electricity_price"],
    df["total_cost"],
    s=6,
)

plt.xlabel("Electricity price [€/MWh]")
plt.ylabel("Operating cost [€/h]")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/operating_cost_vs_price.png"
)

plt.close()


# =====================================================
# Electricity price distribution
# =====================================================

plt.figure(figsize=(8,5))

plt.hist(
    df["electricity_price"],
    bins=30,
)

plt.xlabel("Electricity price [€/MWh]")
plt.ylabel("Hours")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/electricity_price_distribution.png"
)

plt.close()


# =====================================================
# Methane consumption during the year
# =====================================================

plt.figure(figsize=(12,5))

plt.plot(
    df["methane_kg_h"],
    linewidth=0.8,
)

plt.xlabel("Hour of the year")
plt.ylabel("Methane consumption [kg/h]")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/yearly_methane.png"
)

plt.close()


# =====================================================
# Operating cost during the year
# =====================================================

plt.figure(figsize=(12,5))

plt.plot(
    df["total_cost"],
    linewidth=0.8,
)

plt.xlabel("Hour of the year")
plt.ylabel("Operating cost [€/h]")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_FOLDER}/yearly_cost.png"
)

plt.close()


print()

print("========================================")
print("PLOTS CREATED")
print("========================================")

print(f"Output folder : {OUTPUT_FOLDER}")

