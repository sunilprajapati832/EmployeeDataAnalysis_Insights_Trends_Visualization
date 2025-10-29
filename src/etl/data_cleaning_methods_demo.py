"""
Demonstration of classic data cleaning techniques
based on EmployeeDataAnalysis1.py, adapted for unified dataset.
"""

from pathlib import Path
import pandas as pd

# --- Paths ---
BASE_DIR = Path(__file__).resolve().parents[2]
PROCESSED = BASE_DIR / "data" / "processed" / "employees_unified.csv"

# --- Load data ---
print(f"📂 Loading processed data from: {PROCESSED}")
df = pd.read_csv(PROCESSED)
print(f"✅ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns\n")

# --- Show initial overview ---
print("Initial missing values:\n", df.isnull().sum())

# --- 1️⃣ Remove missing values ---
def drop_missing_rows():
    df_dropped = df.dropna()
    print(f"\n🧹 After dropping missing rows: {df_dropped.shape[0]} rows remain.")
    return df_dropped

# --- 2️⃣ Fill missing values with mean ---
def fill_missing_mean():
    df_filled = df.fillna(df.mean(numeric_only=True))
    print("\n📈 Missing numeric values filled with column mean.")
    return df_filled

# --- 3️⃣ Forward fill missing values ---
def forward_fill():
    df_ffill = df.ffill()
    print("\n🔁 Forward filled missing values (propagated previous).")
    return df_ffill

# --- 4️⃣ Check duplicates ---
def count_duplicates():
    dup_count = df.duplicated().sum()
    print(f"\n📊 Total duplicate rows: {dup_count}")
    return dup_count

# --- 5️⃣ Remove duplicates (keep first) ---
def remove_duplicates_first():
    df_nodup = df.drop_duplicates()
    print(f"\n✅ Removed duplicates (kept first). New shape: {df_nodup.shape}")
    return df_nodup

# --- 6️⃣ Remove duplicates (keep last) ---
def remove_duplicates_last():
    df_nodup = df.drop_duplicates(keep='last')
    print(f"\n✅ Removed duplicates (kept last). New shape: {df_nodup.shape}")
    return df_nodup

# --- 7️⃣ Standardize text columns ---
def standardize_text_columns():
    df_clean = df.copy()
    if "first_name" in df_clean.columns:
        df_clean["first_name_cleaned"] = (
            df_clean["first_name"]
            .astype(str)
            .str.strip()
            .str.lower()
            .str.replace(r"\s+", " ", regex=True)
        )
        print("\n🧩 Standardized 'first_name' formatting:")
        print(df['first_name'].unique())
    else:
        print("\n⚠️ Column 'first_name' not found.")
    return df_clean


# --- Run all steps sequentially for demo ---
if __name__ == "__main__":
    drop_missing_rows()
    fill_missing_mean()
    forward_fill()
    count_duplicates()
    remove_duplicates_first()
    remove_duplicates_last()
    standardize_text_columns()

    print("\n🎯 Data Cleaning Demo Completed Successfully!")
