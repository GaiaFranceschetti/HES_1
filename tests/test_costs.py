from economics.costs import (
    methane_energy,
    gas_cost,
    electricity_cost,
    total_cost,
)

methane = 379.86          # kg/h
electric_power = 300      # kW
electricity_price = 120   # €/MWh

print("Methane energy:", methane_energy(methane), "MWh/h")

print("Gas cost:", gas_cost(methane), "€/h")

print(
    "Electricity cost:",
    electricity_cost(
        electric_power,
        electricity_price,
    ),
    "€/h",
)

print(
    "Total cost:",
    total_cost(
        methane,
        electric_power,
        electricity_price,
    ),
    "€/h",
)