"""AIDA 1141 Week 5 Graded Lab 2 starter.

Complete the marked TODOs. This file is a starter, not a finished solution.
"""

from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier


LAB_DIR = Path(__file__).resolve().parent
DATA_DIR = LAB_DIR / "data"
OUTPUT_DIR = LAB_DIR / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

FEATURE_COLUMNS = [
    "units_sold_last_week",
    "stock_on_hand",
    "days_until_delivery",
]


def main() -> None:
    # Load labelled historical examples and the new products to predict.
    history = pd.read_csv(DATA_DIR / "bookstore_history.csv")
    new_products = pd.read_csv(DATA_DIR / "new_products.csv")

    print("Historical examples:")
    print(history.head().to_string(index=False))
    print(f"\nNumber of historical examples: {len(history)}")
    print("\nNew products:")
    print(new_products.to_string(index=False))

    # GUIDED PART A — CLASSIFICATION (3%)
    # Predict a category: should the bookstore consider a reorder (Yes/No)?

    # TODO 1: Put the feature columns from history into X_class.
    # Hint: use history[FEATURE_COLUMNS].
    X_class = None

    # TODO 2: Put the known classification answer into y_class.
    # Hint: the label column is "reorder_now".
    y_class = None

    if X_class is None or y_class is None:
        print("\nComplete Guided Part A TODOs 1 and 2, then run this file again.")
        return

    classifier = DecisionTreeClassifier(max_depth=2, random_state=42)

    # TODO 3: Train the classifier using X_class and y_class with .fit(...).
    # Example pattern: model.fit(input_data, known_answers)
    # Add your code below.

    # TODO 4: Use the trained classifier to predict for new_products.
    # Use new_products[FEATURE_COLUMNS] as the input.
    classification_predictions = None

    if classification_predictions is None:
        print("\nComplete Guided Part A TODOs 3 and 4, then run this file again.")
        return

    classification_output = new_products.copy()
    classification_output["predicted_reorder_now"] = classification_predictions
    classification_path = OUTPUT_DIR / "classification_predictions.csv"
    classification_output.to_csv(classification_path, index=False)
    print("\nClassification predictions:")
    print(classification_output.to_string(index=False))
    print(f"Saved: {classification_path.relative_to(LAB_DIR)}")

    # INDEPENDENT PART B — REGRESSION (2%)
    # Predict a number: suggested order units.

    # TODO 5: Put the units_sold_last_week column from history into X_regression.
    # Use this one numeric feature to keep the first regression model simple.
    X_regression = None

    # TODO 6: Put the known numeric answer into y_regression.
    # Hint: the label column is "recommended_order_units".
    y_regression = None

    if X_regression is None or y_regression is None:
        print("\nComplete Independent Part B TODOs 5 and 6, then run this file again.")
        return

    regressor = LinearRegression()

    # TODO 7: Train the regressor using X_regression and y_regression.
    # Add your .fit(...) code below.

    # TODO 8: Predict recommended order units for new_products.
    # Use new_products[["units_sold_last_week"]] as input, then round to 1 decimal.
    regression_predictions = None

    if regression_predictions is None:
        print("\nComplete Independent Part B TODOs 7 and 8, then run this file again.")
        return

    regression_output = new_products.copy()
    regression_output["predicted_order_units"] = regression_predictions
    regression_path = OUTPUT_DIR / "regression_predictions.csv"
    regression_output.to_csv(regression_path, index=False)
    print("\nRegression predictions:")
    print(regression_output.to_string(index=False))
    print(f"Saved: {regression_path.relative_to(LAB_DIR)}")
    print("\nReminder: predictions are estimates, not automatic ordering decisions.")


if __name__ == "__main__":
    main()
