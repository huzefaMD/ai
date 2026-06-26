# Single quotes
name1 = 'Python'

# Double quotes
name2 = "Python"

# Triple quotes — for LONG strings like system prompts!
name3 = """Python is a programming
language used for AI, data science,
and web development"""

print(name1)
print(name2)
print(name3)


# The 5 Most Important String Tools

#Tool 1 — .strip() — Removes Extra Spaces

messy_input = "   Ravi Kumar   "
clean_input = messy_input.strip()
print(clean_input)
# Ravi Kumar


#Tool 2 — .lower() — Converts to Lowercase

command = "QUIT"
print(command.lower())
# quit

#Tool 3 — .replace() — Swaps Words

message = "Hello User! Welcome to the platform."
updated = message.replace("User", "Ravi")
print(updated)
# Hello Ravi! Welcome to the platform.


#Tool 4 — in — Checks if a Word Exists

user_message = "I want to learn data science"
if "data" in user_message:
    print("Topic detected: Data Science")
# Topic detected: Data Science


#Tool 5 — len() — Counts Characters
prompt = "What is machine learning?"
print(len(prompt))
# 26



#How These Connect to Claude

# Line 1 — clean user input
user_input = input("You: ").strip()
# Removes accidental spaces the person typed

# Line 2 — check commands case-insensitively
if user_input.lower() == "quit":
    print("Goodbye!")
# Works even if they type QUIT or Quit

# Line 3 — detect topics in their message
if "python" in user_input.lower():
    print("Python topic detected")

# Line 4 — build the actual prompt for Claude
prompt = f"User {name} asks: {user_input}"


#Building Claude Prompts with Strings

# Variables with information
person_name    = "Ravi"
years_exp      = 3
current_role   = "Web Developer"
goal           = "switch to Data Science"

# Build a Claude prompt using f-string
prompt = f"""You are a career advisor.

A person named {person_name} has {years_exp} years
of experience as a {current_role}.
Their goal is to {goal}.

Recommend the best learning path for them."""

print(prompt)

