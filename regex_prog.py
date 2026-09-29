import re

text = "My marks are 85 and my attendance is 92"

# Find all numbers
numbers = re.findall(r"\d+", text)

print("Numbers found:", numbers)