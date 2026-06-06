# Variables — store information in a box
name    = "Ravi Kumar"
college = "Anna University"
year    = 4
cgpa    = 8.5

# f-strings — combine variable with text
print(f"My name is {name}")
print(f"I study at {college}")
print(f"I am in year {year}")
print(f"My CGPA is {cgpa}")

# THIS is how Claude prompts are built
course = "AWS"
prompt = f"Teach me {course} for complete beginners"
print(prompt)
