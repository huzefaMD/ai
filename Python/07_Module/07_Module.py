#First Function

# Define the function
def greet_student(name):
    print(f"Hello {name}! Welcome to the course!")

# Call it — as many times as you want!
greet_student("Ravi")
greet_student("Priya")
greet_student("Kumar")


#Functions That Give Back a Value — return

def get_total_score(score1, score2):
    total = score1 + score2
    return total

# Store the returned value
math_total = get_total_score(85, 92)
print(f"Total score: {math_total}")
# Total score: 177



#Build a Mini Function Library
# functions_practice.py

# ── Function 1 ─────────────────────────────
def format_message(role, content):
    """Create a message dictionary"""
    return {
        "role":    role,
        "content": content
    }

# ── Function 2 ─────────────────────────────
def get_course_price(course_name):
    """Return price of a course"""
    prices = {
        "Python Basics":       1999,
        "Web Development":     4999,
        "Data Science":        5999,
        "Machine Learning":    6999,
    }
    return prices.get(course_name, 0)

# ── Function 3 ─────────────────────────────
def estimate_tokens(text):
    """Estimate token count from text"""
    return len(text) // 4

# ── Test all 3 ─────────────────────────────
msg = format_message("user", "What is AI?")
print(msg)
# {'role': 'user', 'content': 'What is AI?'}

price = get_course_price("Data Science")
print(f"Price: ₹{price}")
# Price: ₹5999

tokens = estimate_tokens("Explain machine learning briefly")
print(f"Estimated tokens: {tokens}")
# Estimated tokens: 8
