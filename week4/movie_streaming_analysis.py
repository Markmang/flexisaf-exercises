import pandas as pd

# =========================================================
# 1️⃣ CREATE DATAFRAMES (WITH INTENTIONAL ISSUES)
# =========================================================

users = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 5, 6],
    "age": [25, 30, None, 22, 40, 30],
    "region": ["Africa", "Europe", "africa", "Asia", "Europe", None],
    "subscription_type": ["Premium", "Basic", "Premium", "Basic", "Premium", "Basic"]
})

movies = pd.DataFrame({
    "movie_id": [101, 102, 103, 104, 105],
    "genre": ["Action", "action", "Drama", "Sci-Fi", "SCI-FI"],
    "release_year": ["2018", "2020", "2019", "2021", "2021"],  # incorrect type
    "duration": [120, 90, 110, 140, 140]
})

watch_history = pd.DataFrame({
    "user_id": [1, 1, 2, 3, 4, 4, 5],
    "movie_id": [101, 101, 102, 103, 104, 104, 105],
    "watch_time": [120, 120, 80, 100, 130, 130, 140],
    "rating": [4.5, 4.5, None, 5, 3.5, 3.5, 4]
})

# =========================================================
# 2️⃣ DATA CLEANING (Modern Best Practice)
# =========================================================

# --- Fix Missing Values (NO inplace) ---
users["age"] = users["age"].fillna(users["age"].mean())
users["region"] = users["region"].fillna("Unknown")
watch_history["rating"] = watch_history["rating"].fillna(
    watch_history["rating"].mean()
)

# --- Standardize Text Columns ---
users["region"] = users["region"].str.capitalize()
movies["genre"] = movies["genre"].str.upper()

# --- Fix Data Types ---
movies["release_year"] = pd.to_numeric(movies["release_year"], errors="coerce")

# --- Remove Duplicates ---
watch_history = watch_history.drop_duplicates().reset_index(drop=True)

# =========================================================
# 3️⃣ INTENTIONAL MERGE ERROR (WRONG JOIN KEY)
# =========================================================

try:
    wrong_merge = watch_history.merge(movies, on="user_id")
except KeyError as e:
    print("Intentional Merge Error:", e)

# ✅ Correct Merge
merged = (
    watch_history
        .merge(movies, on="movie_id", how="left")
        .merge(users, on="user_id", how="left")
)

# =========================================================
# 4️⃣ ANALYSIS
# =========================================================

# --- Genre Insights ---
genre_stats = (
    merged.groupby("genre", as_index=False)
          .agg(
              avg_watch_time=("watch_time", "mean"),
              avg_rating=("rating", "mean"),
              total_views=("movie_id", "count")
          )
)

# --- Subscription Insights ---
subscription_stats = (
    merged.groupby("subscription_type", as_index=False)
          .agg(
              avg_watch_time=("watch_time", "mean"),
              avg_rating=("rating", "mean")
          )
)

# --- Region Insights ---
region_stats = (
    merged.groupby("region", as_index=False)
          .agg(
              avg_rating=("rating", "mean"),
              total_views=("movie_id", "count")
          )
)

# --- Most Watched Genres ---
most_watched_genres = genre_stats.sort_values(
    by="total_views", ascending=False
)

# --- Highest Rated Movies ---
highest_rated_movies = (
    merged.groupby(["movie_id", "genre"], as_index=False)
          .agg(
              avg_rating=("rating", "mean"),
              total_views=("movie_id", "count")
          )
          .sort_values(by="avg_rating", ascending=False)
)

# =========================================================
# 5️⃣ FINAL ANALYSIS-READY DATASET
# =========================================================

final_dataset = (
    merged.sort_values(by=["genre", "subscription_type"])
          .reset_index(drop=True)
)

# =========================================================
# OUTPUT
# =========================================================

print("\n=== FINAL CLEANED DATASET ===\n")
print(final_dataset)

print("\n=== GENRE INSIGHTS ===\n")
print(genre_stats)

print("\n=== SUBSCRIPTION INSIGHTS ===\n")
print(subscription_stats)

print("\n=== REGION INSIGHTS ===\n")
print(region_stats)

print("\n=== MOST WATCHED GENRES ===\n")
print(most_watched_genres)

print("\n=== HIGHEST RATED MOVIES ===\n")
print(highest_rated_movies)
