"""AIDA 1141 Graded Lab 3 starter: model training and validation.

Complete the TODOs in order. The program intentionally does not contain a
completed analysis. It saves a Part A checkpoint before you start Part B.
"""

from pathlib import Path

import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split


LAB_DIR = Path(__file__).resolve().parent
DATA_FILE = LAB_DIR / "data" / "event_setups.csv"
OUTPUT_DIR = LAB_DIR / "outputs"


def main() -> None:
    history = pd.read_csv(DATA_FILE)
    print("Loaded event setup rows:", len(history))
    print(history.head())

    # PART A — GUIDED CHECKPOINT (3%)
    # TODO A1: Set X_a to the room_area_sqm feature column.
    X_a = None

    # TODO A2: Set y to the setup_minutes target column.
    y = None

    if X_a is None or y is None:
        raise NotImplementedError("Complete TODOs A1 and A2 before running Part A.")

    # TODO A3: Split X_a and y. Use test_size=0.25 and random_state=42.
    # Assign all four outputs in this order:
    # X_train, X_valid, y_train, y_valid = train_test_split(...)
    X_train = X_valid = y_train = y_valid = None
    # Replace the None values above with your train_test_split call.
    if X_train is None:
        raise NotImplementedError("Complete TODO A3 with the specified reproducible split.")

    # TODO A4: Create and fit a DummyRegressor(strategy="mean") on training rows.
    # Then use it to predict X_valid. Save predictions as baseline_predictions.
    baseline_predictions = None

    # TODO A5: Create and fit LinearRegression() on the Part A training rows.
    # Then predict X_valid. Save predictions as part_a_predictions.
    part_a_predictions = None

    if baseline_predictions is None or part_a_predictions is None:
        raise NotImplementedError("Complete TODOs A4 and A5 before calculating scores.")

    # TODO A6: Calculate both MAE values against y_valid.
    baseline_mae = None
    part_a_mae = None
    if baseline_mae is None or part_a_mae is None:
        raise NotImplementedError("Complete TODO A6 using mean_absolute_error.")

    # TODO A7: Build this row-level results table and save it to
    # part_a_validation.csv. Include event_id, known setup_minutes,
    # baseline_predictions, and part_a_predictions.
    # Also save a two-row model/validation_mae_minutes score table as
    # part_a_model_comparison.csv so your two scores are recorded.
    OUTPUT_DIR.mkdir(exist_ok=True)
    part_a_rows = None
    if part_a_rows is None:
        raise NotImplementedError("Complete TODO A7 and save outputs/part_a_validation.csv.")
    part_a_rows.to_csv(OUTPUT_DIR / "part_a_validation.csv", index=False)
    part_a_scores = None
    if part_a_scores is None:
        raise NotImplementedError("TODO A7: save the Part A baseline and model MAE values.")
    part_a_scores.to_csv(OUTPUT_DIR / "part_a_model_comparison.csv", index=False)

    print("\nPart A validation MAE (minutes):")
    print(f"Baseline: {baseline_mae:.2f}")
    print(f"Room area model: {part_a_mae:.2f}")
    print("Saved outputs/part_a_validation.csv and outputs/part_a_model_comparison.csv")

    # PART B — INDEPENDENT EXTENSION (2%)
    # First commit your Part A checkpoint. Then finish these TODOs.
    # TODO B1: Set X_b to BOTH room_area_sqm and equipment_items.
    X_b = None
    if X_b is None:
        print("\nPart A is complete. For Part B, complete TODOs B1–B4.")
        return

    # TODO B2: Fit a new LinearRegression on X_b.loc[X_train.index] and y_train.
    # Keep the exact same training and validation row indices used in Part A.
    # Then predict X_b.loc[X_valid.index] and name them part_b_predictions.
    part_b_predictions = None
    if part_b_predictions is None:
        raise NotImplementedError("Complete TODO B2 with the same train/validation rows.")

    # TODO B3: Calculate Part B validation MAE against y_valid.
    part_b_mae = None
    if part_b_mae is None:
        raise NotImplementedError("Complete TODO B3 using mean_absolute_error.")

    # TODO B4: Save a two-row comparison with columns model and validation_mae_minutes.
    # Include the Part A room-area model and Part B two-feature model.
    comparison = None
    if comparison is None:
        raise NotImplementedError("Complete TODO B4 and save part_b_model_comparison.csv.")
    comparison.to_csv(OUTPUT_DIR / "part_b_model_comparison.csv", index=False)

    print("\nSaved outputs/part_b_model_comparison.csv")
    print(comparison.to_string(index=False))
    print("\nInterpret the results cautiously; the supplied records are fictional.")


if __name__ == "__main__":
    main()
