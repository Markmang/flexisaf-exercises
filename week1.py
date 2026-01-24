import numpy as np

scores = np.array([
    [78, 85, 90, 88],
    [45, 60, 55, 70],
    [92, 95, 93, 97],
    [30, 50, 45, 40],
    [88, 82, 84, 86],
    [70, 75, 80, 78]
])

# Slicing examples
rows = scores[:2] #returns first and second rows
cols = scores[:, 1] # returns 2nd column
sub_array = scores[1:4, 1:3] # Sub-array of middle rows and columns

# Overall average
overall_avg = scores.mean()

# Preserve original & replace below 50
filtered_scores = scores.copy()
filtered_scores[filtered_scores < 50] = 0

# Average per assessment
assessment_avg = scores.mean(axis=0)

# Validation before broadcasting
if scores.shape[1] == assessment_avg.shape[0]:
    normalized_scores = scores / assessment_avg
else:
    raise ValueError("Broadcasting mismatch")

print("Original Scores:\n", scores)
print(f'the shape of this array is {scores.shape}')
print("Selected Rows:\n", rows)
print("Selected Column:\n", cols)
print("Sub-array:\n", sub_array)
print(f"Overall Average: {overall_avg:.2f}")
print("Filtered Scores:\n", filtered_scores)
print("Assessment Averages:\n", assessment_avg)
print("Normalized Scores:\n", normalized_scores)
