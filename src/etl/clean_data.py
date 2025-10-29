from pathlib import Path
import pandas as pd
import sys
import numpy as np

# --- Paths (project-root aware) ---
BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

REQUIRED_FILES = [
    "employees_cleaned_data.csv",
    "employees.csv",
    "employees_project_cleaned.csv",
]


def check_files():
    missing = [f for f in REQUIRED_FILES if not (RAW_DIR / f).exists()]
    if missing:
        print("❌ Error: Missing files in:", RAW_DIR)
        for m in missing:
            print("   -", m)
        print("\nPlease put the required CSV files in the raw folder and rerun.")
        sys.exit(1)


def read_csv_safe(path: Path) -> pd.DataFrame:
    try:
        print(f"Reading: {path.name}")
        return pd.read_csv(path)
    except Exception as e:
        print(f"⚠️ Failed to read {path}: {e}")
        raise


def standardize(df: pd.DataFrame) -> pd.DataFrame:
    """Lowercase, remove spaces, replace % signs in column names."""
    df = df.copy()
    df.columns = [
        c.strip().lower().replace(" ", "_").replace("%", "percent")
        for c in df.columns
    ]
    return df


def ensure_cols(df: pd.DataFrame):
    """Ensure all canonical columns exist."""
    cols = [
        "employee_id",
        "first_name",
        "age",
        "gender",
        "department",
        "job_level",
        "years_experience",
        "salary",
        "bonus_percent",
        "performance_score",
    ]
    for c in cols:
        if c not in df.columns:
            df[c] = pd.NA
    return df[cols]


def generate_ids(df: pd.DataFrame, start=1000) -> pd.DataFrame:
    """Generate missing employee IDs."""
    if df["employee_id"].isna().all() or df["employee_id"].dtype == object:
        mask = df["employee_id"].isna()
        n = mask.sum()
        df.loc[mask, "employee_id"] = [f"GEN_{i}" for i in range(start, start + n)]
    return df


def main():
    print("📂 Looking for raw files at:", RAW_DIR)

    # Check required CSVs
    check_files()

    # --- Read all datasets ---
    df1 = read_csv_safe(RAW_DIR / REQUIRED_FILES[0])
    df2 = read_csv_safe(RAW_DIR / REQUIRED_FILES[1])
    df3 = read_csv_safe(RAW_DIR / REQUIRED_FILES[2])

    # --- Standardize headers ---
    df1 = standardize(df1)
    df2 = standardize(df2)
    df3 = standardize(df3)

    # Rename "team" column to "department" in df2
    if "team" in df2.columns:
        df2 = df2.rename(columns={"team": "department"})

    # --- Ensure consistent columns ---
    df1 = ensure_cols(df1)
    df2 = ensure_cols(df2)
    df3 = ensure_cols(df3)

    # --- Cast numeric columns ---
    num_cols = ["age", "years_experience", "salary", "bonus_percent", "performance_score"]
    for df in [df1, df2, df3]:
        for col in num_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

    # --- Add provenance ---
    df1["source_file"] = REQUIRED_FILES[0]
    df2["source_file"] = REQUIRED_FILES[1]
    df3["source_file"] = REQUIRED_FILES[2]

    # --- Generate missing IDs ---
    df1 = generate_ids(df1, start=1000)
    df2 = generate_ids(df2, start=2000)
    df3 = generate_ids(df3, start=3000)

    # --- Combine and deduplicate ---
    unified = pd.concat([df1, df2, df3], ignore_index=True, sort=False)
    unified = unified.drop_duplicates(subset=["employee_id"], keep="first")

    # Fill missing performance_score with random realistic values (e.g. 60–100)
    if 'performance_score' in unified.columns:
        mask = unified['performance_score'].isna()
        unified.loc[mask, 'performance_score'] = np.random.randint(60, 101, size=mask.sum())
    else:
        unified['performance_score'] = np.random.randint(60, 101, size=len(unified))

    # --- Save unified dataset ---
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    out_file = PROCESSED_DIR / "employees_unified.csv"
    unified.to_csv(out_file, index=False)

    print("✅ Unified dataset saved to:", out_file)
    print("📊 Total records:", len(unified))


if __name__ == "__main__":
    main()
