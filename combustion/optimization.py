best_cost = 1e20

for power in powers:

    result = simulate(power)

    if result["cost"] < best_cost:

        best = result