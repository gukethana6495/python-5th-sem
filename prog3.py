import pandas as pd

data = {
    "Name": ["Asha", "Ravi", "John"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print("Student DataFrame:")
print(df)