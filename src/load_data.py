"""
Phase 1 — Data Acquisition Script
Downloads and loads the Kaggle House Prices dataset.
If the CSV is not present, prints instructions to download it.
"""

import pandas as pd
import numpy as np
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'raw')
TRAIN_PATH = os.path.join(DATA_DIR, 'train.csv')
TEST_PATH = os.path.join(DATA_DIR, 'test.csv')


def load_data():
    """Load train and test CSVs. Prints error if files are not found."""
    if not os.path.exists(TRAIN_PATH):
        print(f"ERROR: {TRAIN_PATH} not found.")
        print("Download train.csv and test.csv from:")
        print("  https://www.kaggle.com/c/house-prices-advanced-regression-techniques/data")
        print("Place both files in the data/raw/ directory.")
        return None, None

    train = pd.read_csv(TRAIN_PATH)
    test = pd.read_csv(TEST_PATH) if os.path.exists(TEST_PATH) else None
    return train, test


def describe_dataset(df):
    """Print shape, dtypes, null counts, basic statistics."""
    print(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns\n")

    print("=== Data Types ===")
    dtypes = df.dtypes.value_counts()
    for dt, count in dtypes.items():
        print(f"  {dt}: {count} columns")
    print()

    print("=== Null Counts (columns with > 0 nulls) ===")
    nulls = df.isnull().sum()
    nulls = nulls[nulls > 0].sort_values(ascending=False)
    if len(nulls) == 0:
        print("  No missing values.")
    else:
        for col, count in nulls.items():
            print(f"  {col}: {count} missing ({count/len(df)*100:.1f}%)")
    print()

    print("=== Basic Statistics (numeric features) ===")
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    print(df[numeric_cols].describe())
    print()

    print("=== Target Variable: SalePrice ===")
    if 'SalePrice' in df.columns:
        print(df['SalePrice'].describe())
    else:
        print("  (Not in this dataset — test set has no SalePrice)")


if __name__ == "__main__":
    train, test = load_data()
    if train is not None:
        describe_dataset(train)
