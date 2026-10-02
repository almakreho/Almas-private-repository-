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

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(DATA)
df["week_start"] = pd.to_datetime(df["week_start"])
print(df.head())
print(df.shape)
print(df.isna().sum())
print("Duplicate building/week records:",
      df.duplicated(["building", "week_start"]).sum())
df["variance_kwh"] = df["energy_kwh"] - df["baseline_kwh"]
df["variance_pct"] = (df["variance_kwh"] / df["baseline_kwh"]) * 100
df["anomaly"] = df["variance_pct"] >= 10.0
building_summary = df.groupby("building").agg(
    total_energy=("energy_kwh", "sum"),
    total_baseline=("baseline_kwh", "sum"),
    avg_variance_percentage=("variance_pct", "mean"),
    anomaly_count=("anomaly", "sum")
).reset_index()
weekly_summary = df.groupby("week_start").agg(
    weekly_energy=("energy_kwh", "sum"),
    weekly_baseline=("baseline_kwh", "sum"),
    anomaly_count=("anomaly", "sum")
).reset_index()
weekly_summary["variance_percentage"] = (
    (weekly_summary["weekly_energy"] - weekly_summary["weekly_baseline"]) / weekly_summary["weekly_baseline"]
) * 100
os.makedirs(TABLES, exist_ok=True)
building_summary.to_csv(os.path.join(TABLES, "building_summary.csv"), index=False)
weekly_summary.to_csv(os.path.join(TABLES, "weekly_summary.csv"), index=False)
anomaly_review_table = df[df["anomaly"]].copy()
anomaly_review_table.to_csv(os.path.join(TABLES, "anomaly_review_table.csv"), index=False)
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.figure(figsize=(10, 5))
weekly_trend = df.groupby("week_start")[["energy_kwh", "baseline_kwh"]].sum().reset_index()
plt.plot(weekly_trend["week_start"], weekly_trend["energy_kwh"], marker='o', color='#d62728', linewidth=2, label='Measured Energy (kWh)')
plt.plot(weekly_trend["week_start"], weekly_trend["baseline_kwh"], marker='s', linestyle='--', color='#1f77b4', linewidth=2, label='Baseline Energy (kWh)')
plt.title("Weekly Measured Energy vs. Baseline Energy", fontsize=14, fontweight='bold')
plt.xlabel("Week Start Date", fontsize=12)
plt.ylabel("Total Consumption (kWh)", fontsize=12)
plt.legend(frameon=True)
plt.tight_layout()
plt.savefig(os.path.join(TABLES, "measured_vs_baseline_weekly.png"), dpi=300)
plt.close()
plt.figure(figsize=(8, 5))
sns.barplot(data=building_summary, x="building", y="avg_variance_percentage", palette="magma")
plt.axhline(0, color='black', linewidth=0.8)
plt.title("Average Energy Variance Percentage by Building", fontsize=14, fontweight='bold')
plt.xlabel("Building Name", fontsize=12)
plt.ylabel("Average Variance (%)", fontsize=12)
for i, val in enumerate(building_summary["avg_variance_percentage"]):
    plt.text(i, val + 0.15, f"{val:.2f}%", ha='center', fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(TABLES, "variance_by_building.png"), dpi=300)
plt.close()
