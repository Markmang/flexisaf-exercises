# User Data Cleaning Pipeline (Pandas)

## 📌 Overview

This project demonstrates how to use **pandas** to build and run a
**user data cleaning pipeline**.\
It covers data loading, issue detection, record separation, cleaning
strategies, and summary reporting to produce a reliable, analysis-ready
dataset from a dirty CSV file.

The program shows how to:\
- Load a raw CSV dataset using pandas\
- Detect and flag multiple categories of data quality issues\
- Separate clean records from problematic ones\
- Apply targeted cleaning strategies per issue type\
- Standardize categorical fields for consistency\
- Produce a structured summary report of all actions taken

---

## 📊 Data Structure Explanation

The project works with a single flat CSV dataset:

### 1️⃣ dirty_user_dataset.csv

-   `user_id` → Unique user identifier\
-   `age` → User age\
-   `email` → User email address\
-   `country` → User's country\
-   `status` → Account status\
-   `registration_date` → Date the user registered\
-   `last_login_date` → Date of the user's most recent login

Example cleaned row:

    1  34  user@example.com  Nigeria  Active  2021-03-15  2023-08-10

---

## ⚙️ Program Features

### 1️⃣ Load Dirty Dataset

Reads the raw CSV file from the project directory and previews its
initial shape and contents.

### 2️⃣ Detect & Flag Issues

Scans the dataset for:\
- Missing values across all columns\
- Invalid ages (below 0 or above 120)\
- Invalid email formats (regex-based validation)\
- Future registration dates\
- Last login dates occurring before registration dates\
- Duplicate rows

### 3️⃣ Separate Clean vs Problematic Records

Splits the dataset into two subsets — records that passed all checks
and records that failed at least one — for transparent auditing.

### 4️⃣ Apply Cleaning Strategies

Applies targeted fixes including:\
- Duplicate removal\
- Median imputation for invalid ages\
- Removal of records with invalid emails\
- Removal of records with impossible dates\
- Title-case standardization of categorical labels\
- Filling missing categoricals with `"Unknown"`

### 5️⃣ Final Cleaned Data Preview

Displays a preview of the cleaned dataset with its updated shape after
all transformations have been applied.

### 6️⃣ Summary Report

Produces a final report showing:\
- Original vs cleaned record counts\
- Total records removed\
- All detected issue counts by category\
- Rationale for each cleaning decision made

---

## ▶️ How to Run the Program

### Step 1 — Install Python

Ensure **Python 3.8+** is installed.

### Step 2 — Install Required Library

```bash
pip install pandas
```

### Step 3 — Add Your Dataset

Place your raw CSV file in the same directory as the script and name it:

```bash
dirty_user_dataset.csv
```

### Step 4 — Run the Script

Save your script as:

```bash
data_cleaning_pipeline.py
```

Run it in terminal:

```bash
python data_cleaning_pipeline.py
```

---

## 📦 Required Libraries

  Library   Purpose
  --------- --------------------------------------------------------
  pandas    DataFrame loading, cleaning, validation, and reporting
  pathlib   Safe cross-platform file path resolution

Install with:

```bash
pip install pandas
```

---

## 🧠 Key Concepts Used

-   pandas DataFrames\
-   Loading CSV files (`read_csv`)\
-   Date parsing and comparison (`to_datetime`)\
-   Missing value detection (`isnull`, `fillna`)\
-   Regex-based validation (`str.match`)\
-   Boolean masking for filtering\
-   Removing duplicates (`drop_duplicates`)\
-   Median imputation (`median`)\
-   String normalization (`str.title`)\
-   Issue counting and summary reporting

---

## 📌 Example Output

-   Dirty dataset shape and preview\
-   Detected issue counts by category\
-   Clean vs problematic record split\
-   Confirmation of each cleaning step applied\
-   Final cleaned dataset preview\
-   Summary report with removal counts and cleaning rationale

---

## ✨ Author

**Udeagha Mark Mang**
