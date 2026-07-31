import pandas as pd
import matplotlib.pyplot as plt

from design import design_preheater

temperatures = [
    250,
    300,
    350,
    400,
    450,
    500,
    550,
    600
]

results = []

for T in temperatures:

    data = design_preheater(
        air_mass_flow=1.5,
        outlet_temperature=T
    )

    results.append(data)

df = pd.DataFrame(results)

print(
    df[
        [
            "outlet_temperature",
            "thermal_power_kw",
            "electric_power_kw",
            "fan_power_kw",
            "total_electric_power_kw",
            "wall_temperature",
            "pressure_drop_pa",
            "heated_length",
            "heat_flux",
        ]
    ]
)

df.to_excel(
    "study_outlet_temperature.xlsx",
    index=False
)   

plt.figure(figsize=(8,5))

plt.plot(
    df["outlet_temperature"],
    df["total_electric_power_kw"],
    marker="o"
)

plt.xlabel("Outlet temperature [°C]")
plt.ylabel("Total electric power [kW]")
plt.title("Effect of outlet temperature on total electric power")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "total_electric_power_vs_temperature.png",
    dpi=300
)

plt.show()