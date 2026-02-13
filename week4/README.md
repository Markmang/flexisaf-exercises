# Movie Streaming Analytics (Pandas)

## 📌 Overview

This project demonstrates how to use **pandas** to simulate and analyze
a **movie streaming platform dataset**.\
It covers data creation, cleaning, merging, aggregation, and error
handling to generate meaningful insights from user watch history.

The program shows how to:\
- Create multiple pandas DataFrames from scratch\
- Clean missing values and inconsistent data\
- Fix incorrect data types\
- Remove duplicate records\
- Merge datasets using appropriate join types\
- Perform grouped aggregations for insights\
- Intentionally trigger and fix a merge error\
- Produce a final structured analysis-ready dataset

------------------------------------------------------------------------

## 📊 Data Structure Explanation

The project uses three main DataFrames:

### 1️⃣ Users

-   `user_id` → Unique user identifier\
-   `age` → User age\
-   `region` → Geographic region\
-   `subscription_type` → Basic or Premium

### 2️⃣ Movies

-   `movie_id` → Unique movie identifier\
-   `genre` → Movie genre\
-   `release_year` → Year released\
-   `duration` → Movie duration (minutes)

### 3️⃣ WatchHistory

-   `user_id` → Linked to Users table\
-   `movie_id` → Linked to Movies table\
-   `watch_time` → Minutes watched\
-   `rating` → User rating

Example merged row:

    1  101  120  4.5  ACTION  2018  120  Africa  Premium

------------------------------------------------------------------------

## ⚙️ Program Features

### 1️⃣ Build DataFrames

Creates Users, Movies, and WatchHistory DataFrames manually with
simulated data.

### 2️⃣ Data Cleaning

-   Handles missing values using mean imputation\
-   Standardizes inconsistent genre names\
-   Fixes incorrect data types\
-   Removes duplicate watch records

### 3️⃣ Intentional Merge Error

Attempts to merge on the wrong column to demonstrate a common mistake.

### 4️⃣ Correct Merge

Uses proper join keys (`movie_id`, `user_id`) and left joins to preserve
watch history.

### 5️⃣ Derived Insights

Computes: - Average watch time by genre\
- Average rating by genre\
- Average watch time by subscription type\
- Average rating by region\
- Most-watched genres\
- Highest-rated movies

### 6️⃣ Grouped Aggregations

Uses `.groupby()` with multiple aggregations including mean and count.

### 7️⃣ Final Analysis Dataset

Sorts and structures a clean DataFrame ready for reporting or dashboard
integration.

------------------------------------------------------------------------

## ▶️ How to Run the Program

### Step 1 --- Install Python

Ensure **Python 3.8+** is installed.

### Step 2 --- Install Required Library

``` bash
pip install pandas
```

### Step 3 --- Run the Script

Save your script as:

``` bash
movie_streaming_analysis.py
```

Run it in terminal:

``` bash
python movie_streaming_analysis.py
```

------------------------------------------------------------------------

## 📦 Required Libraries

  Library   Purpose
  --------- --------------------------------------------------------
  pandas    DataFrame manipulation, cleaning, merging, aggregation

Install with:

``` bash
pip install pandas
```

------------------------------------------------------------------------

## 🧠 Key Concepts Used

-   pandas DataFrames\
-   Handling missing values (`fillna`)\
-   Removing duplicates (`drop_duplicates`)\
-   Data type conversion (`astype`)\
-   String normalization\
-   Merging DataFrames (`merge`)\
-   Grouped aggregations (`groupby`, `agg`)\
-   Sorting and resetting index\
-   Error handling in merges

------------------------------------------------------------------------

## 📌 Example Output

-   Cleaned Users, Movies, and WatchHistory tables\
-   Merged analysis-ready dataset\
-   Genre-level watch statistics\
-   Subscription-level engagement metrics\
-   Region-based rating insights\
-   Most-watched genres\
-   Highest-rated movies

------------------------------------------------------------------------

## ✨ Author

**Udeagha Mark Mang**
