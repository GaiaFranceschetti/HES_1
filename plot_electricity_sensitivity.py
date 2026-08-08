"""
=========================================================
ELECTRICITY PRICE SENSITIVITY PLOT

Average optimal temperature as a function of the
average electricity price.
=========================================================
"""

import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------------------------------
# Files
# -----------------------------------------------------

INPUT_FILE = (
    "results/electricity_sensitivity/"
    "electricity_price_sensitivity_summary.csv"
)

OUTPUT_FILE = (
    "results/electricity_sensitivity/"
    "average_temperature_vs_electricity_price.png"
)


# -----------------------------------------------------
# Load results
# -----------------------------------------------------

df = pd.read_csv(INPUT_FILE)


# -----------------------------------------------------
# Sort by electricity price
# -----------------------------------------------------

df = df.sort_values(
    "average_electricity_price"
)


# -----------------------------------------------------
# Create plot
# -----------------------------------------------------

plt.figure(figsize=(8, 5))


plt.plot(
    df["average_electricity_price"],
    df["average_temperature"],
    marker="o",
    linewidth=1.5,
)


# -----------------------------------------------------
# Labels
# -----------------------------------------------------

plt.xlabel(
    "Average electricity price [€/MWh]"
)

plt.ylabel(
    "Average optimal air temperature [°C]"
)

plt.title(
    "Optimal Preheating Temperature vs Electricity Price"
)


# -----------------------------------------------------
# Grid
# -----------------------------------------------------

plt.grid(
    True,
    alpha=0.3
)


# -----------------------------------------------------
# Layout
# -----------------------------------------------------

plt.tight_layout()


# -----------------------------------------------------
# Save
# -----------------------------------------------------

plt.savefig(
    OUTPUT_FILE,
    dpi=300,
)


plt.close()


print()
print("========================================")
print("PLOT CREATED")
print("========================================")

print(
    f"Output : {OUTPUT_FILE}"
)