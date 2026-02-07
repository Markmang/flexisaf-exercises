import pandas as pd

# ============================================================
# 1. BUILD THE DATAFRAME (30+ ROWS)
# ============================================================
# Default integer indexing is used at creation to allow
# later positional access with .iloc.

data = {
    "ProjectID": ["P001"] * 10 + ["P002"] * 10 + ["P003"] * 10,
    "Team": (
        ["Backend"] * 5 + ["Frontend"] * 5 +
        ["Backend"] * 5 + ["QA"] * 5 +
        ["Frontend"] * 5 + ["QA"] * 5
    ),
    "Week": list(range(1, 11)) * 3,
    "HoursWorked": [
        38, 40, 42, 36, 45,
        30, 32, 35, 34, 36,
        40, 41, 39, 44, 46,
        28, 30, 31, 29, 33,
        37, 38, 40, 42, 43,
        26, 27, 28, 30, 32
    ],
    "Status": ["Completed", "Completed", "Completed", "Delayed", "Completed"] * 6
}

df = pd.DataFrame(data)


# ============================================================
# 2. SERIES VS DATAFRAME BEHAVIOR
# ============================================================
# Single column label → Series (1D)
# Multiple column labels → DataFrame (2D)

hours_series = df["HoursWorked"]
hours_df = df[["ProjectID", "HoursWorked"]]


# ============================================================
# 3. LABEL-BASED INDEXING (.loc)
# ============================================================
# Used when selection is based on column labels and conditions.

backend_logs = df.loc[df["Team"] == "Backend"]
df.loc[df["HoursWorked"] > 44, "Status"] = "Overtime"


# ============================================================
# 4. POSITION-BASED INDEXING (.iloc)
# ============================================================
# Used for numeric position slicing, independent of labels.

first_five_rows = df.iloc[0:5]
week_hours_subset = df.iloc[0:5, 2:4]


# ============================================================
# 5. ROW AND COLUMN SLICING
# ============================================================
label_slice = df.loc[5:10, ["ProjectID", "Team", "HoursWorked"]]
position_slice = df.iloc[10:15, :]


# ============================================================
# 6. DERIVED COLUMNS
# ============================================================
# Vectorized operations applied column-wise.

df["OvertimeFlag"] = df["HoursWorked"] > 40

df["Workload"] = df["HoursWorked"].apply(
    lambda h: "Heavy" if h >= 40 else "Normal"
)


# ============================================================
# 7. BOOLEAN INDEXING (FILTERING)
# ============================================================
overtime_records = df[df["OvertimeFlag"]]

risk_records = df[
    (df["Status"] == "Delayed") &
    (df["HoursWorked"] < 35)
]


# ============================================================
# 8. SUMMARY STATISTICS
# ============================================================
hours_summary = df["HoursWorked"].describe()


# ============================================================
# 9. GROUPED AGGREGATIONS
# ============================================================
team_average = df.groupby("Team")["HoursWorked"].mean()

project_summary = df.groupby("ProjectID").agg(
    AverageHours=("HoursWorked", "mean"),
    MaxHours=("HoursWorked", "max"),
    TotalWeeks=("Week", "count")
)


# ============================================================
# 10. INTENTIONAL INDEXING MISTAKE
# ============================================================
# ❌ Chained indexing – unreliable update

df[df["Team"] == "QA"]["Status"] = "Review"


# ============================================================
# 11. CORRECTING THE INDEXING MISTAKE
# ============================================================
# ✅ Proper label-based update using .loc

df.loc[df["Team"] == "QA", "Status"] = "Review"


# ============================================================
# 12. FINAL CLEANED DATAFRAME
# ============================================================
final_df = (
    df.sort_values(by=["ProjectID", "Week"])
      .reset_index(drop=True)
)


# ============================================================
# 13. PRINT FINAL RESULTS (ALL DERIVED DATA IN ORDER)
# ============================================================

print("\n" + "="*70)
print("📊 FINAL RESULTS OUTPUT — FULL PIPELINE")
print("="*70)

# 1. Base DataFrame (FIRST derived object)
print("\n1️⃣ Base DataFrame (df):")
print(df)

# 2. Series vs DataFrame
print("\n2️⃣ HoursWorked Series:")
print(hours_series)

print("\n3️⃣ ProjectID & HoursWorked DataFrame:")
print(hours_df)

# 3. Label-based selection
print("\n4️⃣ Backend Team Logs (.loc):")
print(backend_logs)

# 4. Position-based indexing
print("\n5️⃣ First Five Rows (.iloc):")
print(first_five_rows)

print("\n6️⃣ Week & HoursWorked Subset (.iloc):")
print(week_hours_subset)

# 5. Row & column slicing
print("\n7️⃣ Label-Based Slice (Rows 5–10):")
print(label_slice)

print("\n8️⃣ Position-Based Slice (Rows 10–15):")
print(position_slice)

# 6. Derived columns
print("\n9️⃣ DataFrame with Derived Columns (OvertimeFlag, Workload):")
print(df[["ProjectID", "Team", "Week", "HoursWorked", "OvertimeFlag", "Workload"]])

# 7. Boolean indexing results
print("\n🔟 Overtime Records:")
print(overtime_records)

print("\n1️⃣1️⃣ Risk Records (Delayed & Low Hours):")
print(risk_records)

# 8. Summary statistics
print("\n1️⃣2️⃣ HoursWorked Summary Statistics:")
print(hours_summary)

# 9. Grouped aggregations
print("\n1️⃣3️⃣ Average Hours Per Team:")
print(team_average)

print("\n1️⃣4️⃣ Project-Level Summary:")
print(project_summary)

# 10. Final cleaned DataFrame (LAST derived object)
print("\nFINAL CLEANED DATAFRAME (Preview)")
print(final_df.head())

print("\n" + "="*70)
print("✅ END OF FULL DATAFRAME PIPELINE OUTPUT")
print("="*70)
