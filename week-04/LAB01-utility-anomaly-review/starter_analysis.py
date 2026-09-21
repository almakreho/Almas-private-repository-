from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).parent
DATA = ROOT / "data" / "utility_weekly.csv"
OUTPUTS = ROOT / "outputs"
CHARTS = OUTPUTS / "charts"
TABLES = OUTPUTS / "tables"
CHARTS.mkdir(parents=True, exist_ok=True)
TABLES.mkdir(parents=True, exist_ok=True)

# 1. Load the data.
df = pd.read_csv(DATA)

# 2. Convert the date field.
df["week_start"] = pd.to_datetime(df["week_start"])

# 3. Inspect the data.
print(df.head())
print(df.shape)
print(df.isna().sum())
print("Duplicate building/week records:",
      df.duplicated(["building", "week_start"]).sum())

# 4. Create variance fields.
# TODO: calculate variance_kwh and variance_pct.

# 5. Create a transparent anomaly rule.
# TODO: create an "anomaly" Boolean field and explain your rule.

# 6. Create the building summary.
# TODO: calculate total energy, total baseline,
# average variance percentage, and anomaly count.

# 7. Create the weekly summary.
# TODO: calculate weekly energy, baseline, variance percentage,
# and anomaly count.

# 8. Save the required tables.
# TODO: save the building summary, weekly summary,
# and anomaly review table to TABLES.

# 9. Create the required charts.
# TODO: chart measured energy compared with baseline by week.
# TODO: chart average variance percentage by building.

print("Complete the TODO sections, save outputs, and write decision_note.md.")
