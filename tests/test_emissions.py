from economics.emissions import methane_to_co2


methane = 1000   # kg CH4

co2 = methane_to_co2(methane)


print()
print("========================================")
print("EMISSIONS TEST")
print("========================================")

print(f"Methane : {methane} kg")
print(f"CO2     : {co2:.2f} kg")