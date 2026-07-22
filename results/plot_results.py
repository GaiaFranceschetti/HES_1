"""
=========================================================
PLOT RESULTS

Visualization of yearly hybrid boiler optimization.

=========================================================
"""

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path


def main():

    df = pd.read_csv(
        "results/yearly_results.csv"
    )

    # Create folder for figures

    output_folder = Path(
        "results/figures"
    )

    output_folder.mkdir(
        exist_ok=True
    )


    # =====================================================
    # 1) Temperature vs electricity price
    # =====================================================

    plt.figure(figsize=(8,5))

    plt.scatter(
        df["electricity_price"],
        df["temperature"],
        s=10
    )

    plt.xlabel(
        "Electricity price [€/MWh]"
    )

    plt.ylabel(
        "Optimal air temperature [°C]"
    )

    plt.title(
        "Optimal operating temperature vs electricity price"
    )

    plt.grid()

    plt.savefig(
        output_folder / "temperature_vs_price.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()





    # =====================================================
    # 2) Operating mode distribution
    # =====================================================

    temperature_hours = (
        df["temperature"]
        .value_counts()
        .sort_index()
    )

    plt.figure(figsize=(7,5))

    bars = plt.bar(
        temperature_hours.index.astype(str),
        temperature_hours.values
    )


    total_hours = len(df)


    for bar, value in zip(
        bars,
        temperature_hours.values
    ):

        percentage = (
            value / total_hours * 100
        )

        plt.text(
            bar.get_x() + bar.get_width()/2,
            value,
            f"{percentage:.1f}%",
            ha="center",
            va="bottom"
        )


    plt.xlabel(
        "Optimal air temperature [°C]"
    )

    plt.ylabel(
        "Operating hours"
    )

    plt.title(
        "Annual distribution of operating modes"
    )

    plt.grid(
        axis="y"
    )


    plt.savefig(
        output_folder / "operating_modes.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()





    # =====================================================
    # 3) Activation price distribution
    # =====================================================

    active_hours = df[
        df["temperature"] == 450
    ]


    plt.figure(figsize=(8,5))


    plt.hist(
        active_hours["electricity_price"],
        bins=20
    )


    plt.xlabel(
        "Electricity price [€/MWh]"
    )

    plt.ylabel(
        "Number of activation hours"
    )

    plt.title(
        "Electricity price distribution during preheater activation"
    )

    plt.grid()


    plt.savefig(
        output_folder / "activation_price_distribution.png",
        dpi=300,
        bbox_inches="tight"
    )


    plt.show()



if __name__ == "__main__":
    main()


    