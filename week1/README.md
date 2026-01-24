# Intern Scores Analysis (NumPy)

## 📌 Overview

This project demonstrates how to use **NumPy** to analyze intern
assessment scores.\
It performs slicing, filtering, averaging, validation, and normalization
to compare intern performance across multiple assessments.

The program shows how to: - Store intern scores in a NumPy array -
Extract rows, columns, and sub-arrays - Compute overall and
per-assessment averages - Clean low scores using boolean indexing -
Normalize scores using broadcasting - Validate array shapes before
normalization

------------------------------------------------------------------------

## 📊 Data Structure Explanation

-   **Rows** represent **one intern's scores across multiple exams**
-   **Columns** represent **one exam's scores across all interns**

Example row: ''' \[78, 85, 90, 88\] → One intern across 4 exams '''

------------------------------------------------------------------------

## ⚙️ Program Features

### 1️⃣ Create Score Matrix

Stores intern scores in a NumPy array of shape `(6, 4)`.

### 2️⃣ Slice Data

Extracts specific rows, columns, and sub-arrays for analysis.

### 3️⃣ Compute Overall Average

Calculates the mean score across all interns and exams.

### 4️⃣ Filter Low Scores

Replaces values below 50 with 0 while preserving original data.

### 5️⃣ Compute Average per Assessment

Finds column-wise averages to understand exam difficulty.

### 6️⃣ Normalize Scores

Scales each score relative to its exam's average using broadcasting.

### 7️⃣ Validate Before Broadcasting

Ensures array dimensions match to prevent incorrect normalization.

------------------------------------------------------------------------

## ▶️ How to Run the Program

### Step 1 --- Install Python

Ensure **Python 3.8+** is installed.

### Step 2 --- Install Required Library

''' pip install numpy '''

### Step 3 --- Run the Script

Save your script as: ''' intern_scores.py '''

Run it in terminal: ''' python intern_scores.py '''

------------------------------------------------------------------------

## 📦 Required Libraries

  Library   Purpose
  --------- -------------------------------------------
  numpy     Numerical computing and matrix operations

Install with: ''' pip install numpy '''

------------------------------------------------------------------------

## 🧠 Key Concepts Used

-   NumPy Arrays
-   Indexing & Slicing
-   Boolean Masking
-   Axis-based Mean Calculation
-   Broadcasting
-   Data Normalization

------------------------------------------------------------------------

## 📌 Example Output

-   Original Scores
-   Filtered Scores
-   Overall Average
-   Assessment Averages
-   Normalized Scores

------------------------------------------------------------------------

## ✨ Author

**Udeagha Mark Mang**
