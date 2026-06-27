import json
import os

# -------------------------------
# Function 1: Save students to file
# -------------------------------
def save_students(students_list):
    # Create the data folder if it doesn't exist
    os.makedirs("data", exist_ok=True)

    # Save students to JSON file
    with open("data/students.json", "w") as file:
        json.dump(students_list, file, indent=4)


# -------------------------------
# Function 2: Load students from file
# -------------------------------
def load_students():
    # Check if the file exists
    if not os.path.exists("data/students.json"):
        return []

    # Read and return the student list
    with open("data/students.json", "r") as file:
        return json.load(file)


# -------------------------------
# Function 3: Add a new student
# -------------------------------
def add_student(name, course, price):
    # Load existing students
    students = load_students()

    # Create a new student dictionary
    student = {
        "name": name,
        "course": course,
        "price": price
    }

    # Add the student
    students.append(student)

    # Save the updated list
    save_students(students)


# -------------------------------
# Test the program
# -------------------------------
add_student("Ravi", "Data Science", 5999)
add_student("Priya", "Web Development", 4999)
add_student("Kumar", "Machine Learning", 6999)

# Load and display all students
students = load_students()

print(f"Total students: {len(students)}")

for s in students:
    print(f"{s['name']} - {s['course']}")

