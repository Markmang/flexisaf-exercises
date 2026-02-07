# Project Hours Analysis (Pandas)

## 📌 Overview

This project demonstrates how to use **pandas** to analyze **project team hours and status** across multiple projects and weeks.  
It applies filtering, aggregation, vectorized operations, and grouping to evaluate workloads, overtime, and risk.

The program shows how to:  
- Store project hours data in a pandas DataFrame  
- Apply label-based (`.loc`) and position-based (`.iloc`) indexing  
- Create derived columns using vectorized operations  
- Filter records using boolean indexing  
- Compute summary statistics and grouped aggregations  
- Intentionally trigger and fix a chained indexing error  
- Sort and reset the final DataFrame for clean output

------------------------------------------------------------------------

## 📊 Data Structure Explanation

- **Rows** represent individual weekly logs for team members across projects  
- **Columns** include:  
  - `ProjectID` → Project identifier  
  - `Team` → Team name (Backend, Frontend, QA)  
  - `Week` → Week number  
  - `HoursWorked` → Number of hours worked  
  - `Status` → Task status  
  - `OvertimeFlag` → True if hours > 40  
  - `Workload` → 'Heavy' or 'Normal'

Example row:

    P001  Backend  1  38  Completed  False  Normal

------------------------------------------------------------------------

## ⚙️ Program Features

### 1️⃣ Build DataFrame

Stores simulated project hours and statuses in a pandas DataFrame.

### 2️⃣ Series vs DataFrame Behavior

Shows difference between single-column Series and multi-column DataFrame.

### 3️⃣ Label-Based Indexing (.loc)

Selects subsets of data based on column labels and conditions.

### 4️⃣ Position-Based Indexing (.iloc)

Selects subsets of data using numeric row/column positions.

### 5️⃣ Row & Column Slicing

Demonstrates slicing with labels and positions.

### 6️⃣ Derived Columns

Creates `OvertimeFlag` and `Workload` using vectorized operations.

### 7️⃣ Boolean Indexing (Filtering)

Filters overtime records and risk records (Delayed & low hours).

### 8️⃣ Summary Statistics

Computes descriptive statistics for `HoursWorked`.

### 9️⃣ Grouped Aggregations

Aggregates data by `Team` and `ProjectID` for mean, max, and counts.

### 🔟 Intentional Indexing Mistake

Shows why chained indexing can fail.

### 1️⃣1️⃣ Correcting the Indexing Mistake

Uses proper `.loc` to update values reliably.

### 1️⃣2️⃣ Final Cleaned DataFrame

Sorts, resets index, and prepares a clean DataFrame for reporting.

------------------------------------------------------------------------

## ▶️ How to Run the Program

### Step 1 — Install Python

Ensure **Python 3.8+** is installed.

### Step 2 — Install Required Library

```bash
pip install pandas
```

### Step 3 — Run the Script

Save your script as:

```bash
project_hours_analysis.py
```

Run it in terminal:

```bash
python project_hours_analysis.py
```

------------------------------------------------------------------------

## 📦 Required Libraries

| Library  | Purpose                                         |
|---------|-------------------------------------------------|
| pandas  | DataFrame manipulation, filtering, aggregation |

Install with:

```bash
pip install pandas
```

------------------------------------------------------------------------

## 🧠 Key Concepts Used

- pandas DataFrames & Series  
- Label-based indexing `.loc`  
- Position-based indexing `.iloc`  
- Vectorized operations  
- Boolean indexing and filtering  
- Grouped aggregations (`.groupby`)  
- Summary statistics (`.describe`)  
- Chained indexing and correct updating  
- Sorting and resetting index

------------------------------------------------------------------------

## 📌 Example Output

- Base DataFrame  
- HoursWorked Series and subset DataFrame  
- Backend Team Logs  
- Row and column slices  
- Derived columns (`OvertimeFlag`, `Workload`)  
- Overtime and risk records  
- Summary statistics for `HoursWorked`  
- Average hours per team and project-level summary  
- Final cleaned and sorted DataFrame

------------------------------------------------------------------------

## ✨ Author

**Udeagha Mark Mang**
