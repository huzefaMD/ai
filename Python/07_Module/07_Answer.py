# Function to return the course price
def get_course_price(course_name):
    course_prices = {
        "Python": 9999,
        "Data Science": 5999,
        "Machine Learning": 8999,
        "Web Development": 4999
    }

    return course_prices.get(course_name, 0)


# Function 1: Greet a student
def greet_student(name, course):
    return f"Hello {name}! Your {course} batch starts Monday!"


# Function 2: Check if a course is full
def is_course_full(enrolled, max_seats):
    return enrolled >= max_seats


# Function 3: Calculate total revenue
def calculate_revenue(course_name, students):
    price = get_course_price(course_name)
    return price * students


# -------------------------
# Test Cases
# -------------------------

# Function 1
print(greet_student("Ravi", "Data Science"))

# Function 2
print(is_course_full(30, 30))   # True
print(is_course_full(25, 30))   # False

# Function 3
print(calculate_revenue("Data Science", 50))   # 299950
