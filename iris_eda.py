"""Exploratory Data Analysis (EDA) for the Iris dataset.

Run:
    python iris_eda.py

The script saves summary tables, a correlation matrix, a pair plot, and a
short observations report in the outputs/ directory.
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")  # Allows plots to be saved in non-interactive environments.
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris


PROJECT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)


def main():
    # 1. Load the Iris dataset into a pandas DataFrame.
    iris = load_iris(as_frame=True)
    df = iris.frame.copy()
    df["species"] = df["target"].map(dict(enumerate(iris.target_names)))

    feature_names = list(iris.feature_names)
    readable_names = {
        "sepal length (cm)": "sepal_length_cm",
        "sepal width (cm)": "sepal_width_cm",
        "petal length (cm)": "petal_length_cm",
        "petal width (cm)": "petal_width_cm",
    }
    df = df.rename(columns=readable_names)

    # Save a copy of the dataset used for analysis.
    df.to_csv(OUTPUT_DIR / "iris_dataset.csv", index=False)

    numeric_features = list(readable_names.values())

    # 2. Summary statistics: mean, median, and standard deviation.
    summary = pd.DataFrame({
        "mean": df[numeric_features].mean(),
        "median": df[numeric_features].median(),
        "standard_deviation": df[numeric_features].std(),
        "minimum": df[numeric_features].min(),
        "maximum": df[numeric_features].max(),
    })
    summary.index.name = "feature"
    summary.to_csv(OUTPUT_DIR / "summary_statistics.csv")

    # Save a species-level summary as an additional useful table.
    species_summary = df.groupby("species")[numeric_features].mean().round(3)
    species_summary.to_csv(OUTPUT_DIR / "species_mean_measurements.csv")

    # 3. Correlation matrix.
    correlation = df[numeric_features].corr()
    correlation.to_csv(OUTPUT_DIR / "correlation_matrix.csv")

    # 4. Pairwise scatter plots, colored by species.
    sns.set_theme()
    pair_plot = sns.pairplot(
        df,
        vars=numeric_features,
        hue="species",
        diag_kind="hist",
    )
    pair_plot.fig.suptitle("Iris Dataset: Pairwise Feature Relationships", y=1.02)
    pair_plot.savefig(OUTPUT_DIR / "iris_pairplot.png", dpi=200, bbox_inches="tight")
    plt.close(pair_plot.fig)

    # Additional correlation heatmap.
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation, annot=True, fmt=".2f", square=True)
    plt.title("Iris Feature Correlation Matrix")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "correlation_heatmap.png", dpi=200, bbox_inches="tight")
    plt.close()

    # 5. Create a concise observations report based on the known Iris patterns.
    petal_length_corr = correlation.loc["petal_length_cm", "petal_width_cm"]
    observations = f"""Iris Dataset EDA — Observations
================================

Dataset overview
- Rows: {len(df)}
- Numerical measurement features: {len(numeric_features)}
- Species: {', '.join(iris.target_names)}
- Missing values in the analysis DataFrame: {int(df.isna().sum().sum())}

Key observations
1. Petal length and petal width have a strong positive correlation
   (Pearson correlation: {petal_length_corr:.3f}).
2. Setosa is generally well separated from the other species by petal
   measurements, because its petals are notably smaller.
3. Versicolor and virginica overlap more than setosa in some feature pairs,
   but petal length and petal width help distinguish them.
4. Sepal measurements show useful variation, but they tend to separate the
   three species less clearly than petal measurements.
5. Mean, median, and standard deviation summarize each feature's center and
   spread. Compare summary_statistics.csv and species_mean_measurements.csv
   for overall and species-level measurements.

Files generated
- iris_dataset.csv
- summary_statistics.csv
- species_mean_measurements.csv
- correlation_matrix.csv
- iris_pairplot.png
- correlation_heatmap.png
- observations.txt

Note: These observations describe common patterns in the classic Iris dataset.
Review the saved plots and tables when writing your final project report.
"""
    (OUTPUT_DIR / "observations.txt").write_text(observations, encoding="utf-8")

    print("EDA completed successfully.")
    print(f"Output files saved to: {OUTPUT_DIR}")
    print("\nSummary statistics:")
    print(summary.round(3).to_string())


if __name__ == "__main__":
    main()
