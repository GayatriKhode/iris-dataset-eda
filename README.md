# Iris Dataset — Exploratory Data Analysis (EDA)

A beginner-friendly Python project that explores the classic Iris dataset using **pandas**, **Seaborn**, **Matplotlib**, and **scikit-learn**.

## Project objectives

- Load the Iris dataset into a pandas DataFrame.
- Calculate the mean, median, standard deviation, minimum, and maximum for each numeric feature.
- Create pairwise scatter plots to compare the four measurements across the three Iris species.
- Calculate feature correlations and create a correlation heatmap.
- Save tables, charts, and written observations into an `outputs/` folder.

## Dataset

The dataset is loaded from `sklearn.datasets.load_iris`, so you do not need to download a separate CSV file. It contains 150 observations, four numeric measurements, and three species:

- Setosa
- Versicolor
- Virginica

The measurements are sepal length, sepal width, petal length, and petal width, in centimeters.

## Project structure

```text
iris-eda-github-project/
├── iris_eda.py
├── requirements.txt
├── .gitignore
├── README.md
└── outputs/
    ├── iris_dataset.csv
    ├── summary_statistics.csv
    ├── species_mean_measurements.csv
    ├── correlation_matrix.csv
    ├── iris_pairplot.png
    ├── correlation_heatmap.png
    └── observations.txt
```

## Requirements

- Python 3.9 or later recommended
- pip

## Run the project

### 1. Download or clone the repository

If you are using GitHub, open your repository and copy its URL. Then run:

```bash
git clone YOUR_REPOSITORY_URL
cd iris-eda-github-project
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### 2. Create and activate a virtual environment (recommended)

**Windows (Command Prompt):**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the analysis

```bash
python iris_eda.py
```

The script creates or updates the files inside `outputs/`. It uses a non-interactive plotting backend, so the charts are saved as image files rather than requiring a chart window to open.

## Output files

| File | Description |
|---|---|
| `iris_dataset.csv` | Dataset used for analysis, including the species label |
| `summary_statistics.csv` | Mean, median, standard deviation, minimum, and maximum for each feature |
| `species_mean_measurements.csv` | Average measurements grouped by species |
| `correlation_matrix.csv` | Pearson correlations between numeric features |
| `iris_pairplot.png` | Pairwise scatter plots and feature distributions |
| `correlation_heatmap.png` | Heatmap of feature correlations |
| `observations.txt` | Brief observations and dataset overview |

## Main findings

- Petal length and petal width have a strong positive relationship.
- Setosa is generally easy to distinguish because it has smaller petals.
- Versicolor and virginica overlap in some measurements, but petal measurements help separate them.
- Sepal measurements are useful, although they often separate species less clearly than petal measurements.

Check `outputs/observations.txt` and the saved charts to review the results.

## Tools used

- Python
- pandas
- Matplotlib
- Seaborn
- scikit-learn

## GitHub upload

1. Create a **public** repository on GitHub, for example `iris-dataset-eda`.
2. Extract this project ZIP file.
3. Open a terminal in the extracted project folder.
4. Run the following commands (replace the URL with your repository URL):

```bash
git init
git add .
git commit -m "Add Iris dataset EDA project"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

If Git asks you to sign in, follow GitHub's authentication prompts. Do not put passwords or access tokens into your source files.

## Suggested conclusion

Exploratory Data Analysis of the Iris dataset reveals that petal measurements are particularly useful for distinguishing the three Iris species. Summary statistics describe the distribution of each feature, while pair plots and the correlation matrix show relationships and separation patterns. The saved CSV files and charts provide evidence for these observations.
