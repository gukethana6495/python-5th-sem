import numpy as np

marks = np.array([85, 45, 92, 67, 78, 55])

print("Original array:")
print(marks)

# Sorting
sorted_marks = np.sort(marks)

print("\nSorted marks:")
print(sorted_marks)

# Filtering
high_marks = marks[marks > 70]

print("\nMarks greater than 70:")
print(high_marks)
print(high_marks)