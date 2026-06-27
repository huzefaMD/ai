#Writing to a File

# Open a file and write to it
# "w" means write mode — creates file if not exists
with open("students.txt", "w") as f:
    f.write("Ravi Kumar - Data Science\n")
    f.write("Priya S - Web Development\n")
    f.write("Kumar M - Machine Learning\n")

print("File saved!")



#Reading from a File

# Open and read the whole file
with open("students.txt", "r") as f:
    content = f.read()
    print(content)

# Output:
# Ravi Kumar - Data Science
# Priya S - Web Development
# Kumar M - Machine Learning



#Appending to a File

# Add a new line WITHOUT deleting existing content
with open("students.txt", "a") as f:
    f.write("Anitha R - Python Basics\n")

print("New record added!")


#PART 2: JSON Files

#Saving to JSON

import json

# Your data as a Python dictionary
student = {
    "name":    "Ravi Kumar",
    "course":  "Data Science",
    "price":   5999,
    "active":  True
}

# Save to a JSON file
with open("student.json", "w") as f:
    json.dump(student, f, indent=2)

print("Saved!")


#Loading from JSON


import json

# Load it back
with open("student.json", "r") as f:
    loaded = json.load(f)

# It comes back as a Python dictionary!
print(loaded["name"])    # Ravi Kumar
print(loaded["course"])  # Data Science
print(loaded["price"])   # 5999



