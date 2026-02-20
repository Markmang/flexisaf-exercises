import pandas as pd
from pathlib import Path


print("\n===================================================")
print("        USER DATA CLEANING PIPELINE")
print("===================================================\n")

# Get project root directory safely
BASE_DIR = Path(__file__).resolve().parent

data_path = BASE_DIR / "dirty_user_dataset.csv"

# --------------------------------
# 1. Load Dirty Dataset
# --------------------------------
df = pd.read_csv(data_path)

print("📌 STEP 1: DIRTY DATASET LOADED")
print("Initial Shape:", df.shape)
print("\nDirty Dataset Preview:")
print(df.head())
print("\n---------------------------------------------------\n")

# --------------------------------
# 2. DETECT & FLAG ISSUES
# --------------------------------

print("📌 STEP 2: DETECTING DATA QUALITY ISSUES\n")

issue_counts = {}

# Convert dates
df["registration_date"] = pd.to_datetime(df["registration_date"], errors="coerce")
df["last_login_date"] = pd.to_datetime(df["last_login_date"], errors="coerce")

# Flag Missing
missing_mask = df.isnull()
missing_counts = missing_mask.sum()
issue_counts["Missing Values"] = missing_counts[missing_counts > 0].to_dict()

# Flag Invalid Ages
invalid_age_mask = (df["age"].notnull()) & (
    (df["age"] < 0) | (df["age"] > 120)
)
issue_counts["Invalid Ages"] = int(invalid_age_mask.sum())

# Flag Invalid Emails
email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
email_valid = df["email"].astype(str).str.match(email_pattern, na=False)
invalid_email_mask = ~email_valid & df["email"].notnull()
issue_counts["Invalid Emails"] = int(invalid_email_mask.sum())

# Flag Impossible Dates
today = pd.Timestamp.today()
future_registration = df["registration_date"] > today
login_before_registration = (
    df["last_login_date"] < df["registration_date"]
)

issue_counts["Future Registration Dates"] = int(future_registration.sum())
issue_counts["Login Before Registration"] = int(login_before_registration.sum())

# Flag Duplicates
duplicate_mask = df.duplicated()
issue_counts["Duplicate Rows"] = int(duplicate_mask.sum())

print("Detected Issues:")
for k, v in issue_counts.items():
    print(f"{k}: {v}")

print("\n---------------------------------------------------\n")

# --------------------------------
# 3. SEPARATE CLEAN VS PROBLEMATIC RECORDS
# --------------------------------

print("📌 STEP 3: SEPARATING CLEAN VS PROBLEMATIC RECORDS\n")

problem_mask = (
    invalid_age_mask |
    invalid_email_mask |
    future_registration |
    login_before_registration |
    duplicate_mask
)

df_problematic = df[problem_mask]
df_clean_initial = df[~problem_mask]

print("Clean Records (Before Fixes):", df_clean_initial.shape)
print("Problematic Records:", df_problematic.shape)

print("\nSample Problematic Records:")
print(df_problematic.head())

print("\n---------------------------------------------------\n")

# --------------------------------
# 4. APPLY CLEANING STRATEGIES
# --------------------------------

print("📌 STEP 4: APPLYING CLEANING STRATEGIES\n")

df_clean = df.copy()

# 4.1 Remove Duplicates
df_clean = df_clean.drop_duplicates()
print("✔ Duplicates Removed")

# 4.2 Fix Invalid Ages (Median Imputation)
invalid_age_mask = (df_clean["age"].notnull()) & (
    (df_clean["age"] < 0) | (df_clean["age"] > 120)
)
median_age = df_clean.loc[~invalid_age_mask, "age"].median()
df_clean.loc[invalid_age_mask, "age"] = median_age
print("✔ Invalid Ages Replaced with Median:", median_age)

# 4.3 Remove Invalid Emails
email_valid = df_clean["email"].astype(str).str.match(email_pattern, na=False)
df_clean = df_clean[email_valid | df_clean["email"].isnull()]
print("✔ Invalid Emails Removed")

# 4.4 Remove Impossible Dates
future_registration = df_clean["registration_date"] > today
login_before_registration = (
    df_clean["last_login_date"] < df_clean["registration_date"]
)
df_clean = df_clean[~future_registration & ~login_before_registration]
print("✔ Impossible Date Records Removed")

# 4.5 Standardize Categorical Labels
df_clean["country"] = df_clean["country"].str.title()
df_clean["status"] = df_clean["status"].str.title()
print("✔ Categorical Labels Standardized")

# 4.6 Fill Missing Categoricals
df_clean["country"] = df_clean["country"].fillna("Unknown")
df_clean["status"] = df_clean["status"].fillna("Unknown")
print("✔ Missing Categoricals Filled with 'Unknown'")

print("\nShape After Cleaning:", df_clean.shape)

print("\n---------------------------------------------------\n")

# --------------------------------
# 5. FINAL CLEANED DATA
# --------------------------------

print("📌 STEP 5: FINAL CLEANED DATA PREVIEW\n")
print(df_clean.head())

# --------------------------------
# 6. SUMMARY REPORT
# --------------------------------

print("\n===================================================")
print("               FINAL SUMMARY REPORT")
print("===================================================\n")

print("Total Records (Original):", df.shape[0])
print("Total Records (Cleaned):", df_clean.shape[0])
print("Total Removed:", df.shape[0] - df_clean.shape[0])

print("\nIssues Detected:")
for k, v in issue_counts.items():
    print(f"{k}: {v}")

print("\nRationale for Cleaning Decisions:")
print("- Duplicates removed to prevent analytical distortion.")
print("- Invalid ages replaced with median to preserve distribution.")
print("- Invalid emails removed (critical identifier field).")
print("- Impossible dates removed (logical inconsistency).")
print("- Categorical labels standardized for grouping consistency.")
print("- Missing categorical values filled to retain records.")

print("\n✔ Data Cleaning Pipeline Completed Successfully.\n")
