import pandas as pd

# Load your dataset
df = pd.read_csv("dataset_mood_smartphone.csv")

# Calculate missing percentages
total_per_variable = df.groupby("variable")["value"].apply(lambda x: x.notna().sum())
missing_per_variable = df.groupby("variable")["value"].apply(lambda x: x.isna().sum())
missing_pct = (missing_per_variable / (missing_per_variable + total_per_variable)) * 100

# Get descriptive stats
desc = df.groupby("variable")["value"].describe()

# Drop 25% and 75%, rename 50% to 'median'
desc = desc.drop(columns=["25%", "75%"])
desc = desc.rename(columns={"50%": "median"})

# Round and format
# desc = desc.round(3)
desc["count"] = desc["count"].astype(int)
desc["mean"] = desc["mean"].round(3)
desc["median"] = desc["median"].round(3)
desc["max"] = desc["max"].round(3)
desc["min"] = desc["min"].round(3)
desc["median"] = desc["median"].round(3)
desc["std"] = desc["std"].round(3)

desc["% missing"] = missing_pct.round(1).fillna(100.0)

# Reorder columns if needed
desc = desc[["count", "mean", "std", "min", "median", "max", "% missing"]]

# Export to LaTeX
latex_table = desc.to_latex(float_format="%.2f")
print(latex_table)
