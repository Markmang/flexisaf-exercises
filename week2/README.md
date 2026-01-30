# Energy Consumption Analysis (NumPy)

## 📌 Overview

This project demonstrates how to use **NumPy** to analyze **daily energy
consumption** across multiple departments and hours.\
It applies broadcasting, normalization, cost scaling, statistical
analysis, and ranking to evaluate energy cost efficiency.

The program shows how to:\
- Store department energy consumption in a NumPy array\
- Normalize hourly consumption using broadcasting\
- Apply hourly cost rates and department adjustment factors\
- Compute total daily cost per department\
- Calculate hourly statistics (mean, min, max, variance)\
- Identify top highest-cost departments\
- Intentionally trigger and fix a broadcasting error\
- Validate and explain array shapes at every step

------------------------------------------------------------------------

## 📊 Data Structure Explanation

-   **Rows** represent **departments**
-   **Columns** represent **hourly energy consumption**

Example row:

    [120.5, 150.2, 98.4, ...] → One department across 24 hours

------------------------------------------------------------------------

## ⚙️ Program Features

### 1️⃣ Create Energy Consumption Matrix

Stores simulated energy data in a NumPy array of shape `(D, H)`.

### 2️⃣ Normalize Hourly Consumption

Divides energy values by hourly totals using broadcasting.

### 3️⃣ Apply Hourly Cost Rates

Multiplies normalized energy by hourly cost values.

### 4️⃣ Trigger Broadcasting Error

Demonstrates an incorrect broadcasting attempt intentionally.

### 5️⃣ Fix Broadcasting Error

Reshapes department adjustment factors to broadcast correctly.

### 6️⃣ Compute Total Daily Cost

Calculates daily energy cost per department.

### 7️⃣ Compute Hourly Statistics

Finds mean, minimum, maximum, and variance per hour.

### 8️⃣ Identify Top 3 Costliest Departments

Ranks departments based on total cost.

### 9️⃣ Explain Array Shapes

Prints and explains dimensions at each major step.

------------------------------------------------------------------------

## ▶️ How to Run the Program

### Step 1 --- Install Python

Ensure **Python 3.8+** is installed.

### Step 2 --- Install Required Library

    pip install numpy

### Step 3 --- Run the Script

Save your script as:

    energy_consumption.py

Run it in terminal:

    python energy_consumption.py

------------------------------------------------------------------------

## 📦 Required Libraries

  Library   Purpose
  --------- ------------------------------------------------------
  numpy     Numerical computing, broadcasting, matrix operations

Install with:

    pip install numpy

------------------------------------------------------------------------

## 🧠 Key Concepts Used

-   NumPy Arrays\
-   Broadcasting\
-   Normalization\
-   Vectorized Computation\
-   Axis-based Aggregation\
-   Statistical Analysis\
-   Shape Validation\
-   Error Handling (Broadcasting Fix)

------------------------------------------------------------------------

## 📌 Example Output

-   Energy Consumption Matrix\
-   Normalized Energy Values\
-   Cost-Adjusted Consumption\
-   Hourly Statistics\
-   Total Cost per Department\
-   Top 3 Highest-Cost Departments\
-   Shape Explanations

------------------------------------------------------------------------

## ✨ Author

**Udeagha Mark Mang**
