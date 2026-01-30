import numpy as np

# -----------------------------
# 1. Simulate Energy Consumption Data
# -----------------------------

D = 6   # Number of departments
H = 24  # Number of hours in a day

np.random.seed(42)

# 2D array: Daily energy consumption per department per hour
energy = np.random.uniform(50, 300, size=(D, H))

# 1D array: Hourly cost rates
hourly_cost = np.random.uniform(0.1, 0.5, size=(H,))

# 1D array: Department adjustment factors
dept_adjustment = np.random.uniform(0.8, 1.2, size=(D,))

print("Energy shape:", energy.shape)                  # (D, H)
print("Hourly cost shape:", hourly_cost.shape)        # (H,)
print("Department adjustment shape:", dept_adjustment.shape)  # (D,)

# -----------------------------
# 2. Normalize Hourly Consumption (Broadcasting)
# -----------------------------

hourly_totals = energy.sum(axis=0)  # total energy per hour (H,)
normalized_energy = energy / hourly_totals

print("\nHourly totals shape:", hourly_totals.shape)  # (H,)
print("Normalized energy shape:", normalized_energy.shape)  # (D, H)

# -----------------------------
# 3. Apply Hourly Cost Rates (Broadcasting)
# -----------------------------

cost_applied = normalized_energy * hourly_cost

print("\nCost-applied shape:", cost_applied.shape)  # (D, H)

# -----------------------------
# 4. Intentionally Trigger Broadcasting Error
# -----------------------------

try:
    wrong_adjustment = cost_applied * dept_adjustment
except ValueError as e:
    print("\nBroadcasting Error Triggered:", e)

# -----------------------------
# 5. Fix Broadcasting Error Properly
# -----------------------------

dept_adjustment_fixed = dept_adjustment[:, np.newaxis]
adjusted_cost = cost_applied * dept_adjustment_fixed

print("\nFixed department adjustment shape:", dept_adjustment_fixed.shape)  # (D, 1)
print("Final adjusted cost shape:", adjusted_cost.shape)  # (D, H)

# -----------------------------
# 6. Compute Total Daily Cost Per Department
# -----------------------------

total_daily_cost = adjusted_cost.sum(axis=1)

print("\nTotal daily cost per department shape:", total_daily_cost.shape)  # (D,)

# -----------------------------
# 7. Hourly Statistics Across Departments
# -----------------------------

hourly_mean = adjusted_cost.mean(axis=0)
hourly_min = adjusted_cost.min(axis=0)
hourly_max = adjusted_cost.max(axis=0)
hourly_variance = adjusted_cost.var(axis=0)

print("\nHourly stats shape:", hourly_mean.shape)  # (H,)

# -----------------------------
# 8. Identify Top 3 Highest-Cost Departments
# -----------------------------

top_3_departments = np.argsort(total_daily_cost)[-3:][::-1]

print("\nTop 3 highest-cost departments:", top_3_departments)

# -----------------------------
# 9. Print Final Results
# -----------------------------

print("\nTotal Daily Cost Per Department:")
print(total_daily_cost)

print("\nHourly Mean Cost:")
print(hourly_mean)

print("\nHourly Min Cost:")
print(hourly_min)

print("\nHourly Max Cost:")
print(hourly_max)

print("\nHourly Variance:")
print(hourly_variance)