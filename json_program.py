import json

student = {
    "name": "Ravi",
    "age": 21,
    "marks": 88
}

# Convert Python object to JSON string
json_text = json.dumps(student, indent=4)

print("JSON Data:")
print(json_text)

# Convert JSON string back to Python object
data = json.loads(json_text)

print("\nStudent Name:", data["name"])
print("Marks:", data["marks"])