# You are given the test scores of 5 students across
# 3 subjects in a 2D Numpy array. Each row represents
# a student, and each collumn a subject

import numpy as np
scores = np.array([
    [78, 85, 90],
    [88, 79, 92],
    [84, 76, 88],
    [90, 93, 94],
    [75, 80, 70]
])
# Avg of each student
row_avg = np.mean(scores, axis=1)
print(f"Student avg of each student {row_avg}")
# Avg of each subject
col_avg = np.mean(scores, axis=0)
print(f"Avg of subjects: {col_avg}")
# Index of highest score
highest_index = np.argmax(row_avg)
print(f"Student with highest score is student {highest_index}")
# +5 points on the 3rd subject
new_score = scores[:, 2] + 5
print(f"New score of the 3rd subject {new_score}")
