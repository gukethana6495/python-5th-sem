import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "John"],
    "Marks": [80, 90, 75]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Selecting a column
print("\nSelected Name column:")
print(df["Name"])

# Modifying data
df["Marks"] = df["Marks"] + 5

print("\nAfter modifying Marks:")
print(df)

# Adding a new column
df["Grade"] = ["A", "A+", "B"]

print("\nAfter adding Grade:")
print(df)