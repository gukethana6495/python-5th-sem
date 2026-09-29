try:
    with open("student.txt", "w") as file:
        file.write("Name: Ravi\n")
        file.write("Marks: 88\n")

    print("File written successfully.")

    with open("student.txt", "r") as file:
        content = file.read()
        print("\nFile Content:")
        print(content)

except FileNotFoundError:
    print("File not found.")

except PermissionError:
    print("You do not have permission to access the file.")