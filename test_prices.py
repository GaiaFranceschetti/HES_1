from economics.prices import ElectricityPrices

prices = ElectricityPrices(
    "data/20250101_20251231_MGP_PrezziZonali_COUP-2.xlsx"
)

print("Number of hours:", prices.number_of_hours())

print("Hour 1:", prices.get_price(0))
print("Hour 2:", prices.get_price(1))
print("Hour 3:", prices.get_price(2))

print("Date:", prices.get_date(0))
print("Hour of day:", prices.get_hour(0))