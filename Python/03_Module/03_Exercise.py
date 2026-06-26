# A user typed this messy message
user_message = "   I WANT TO LEARN DATA SCIENCE   "

# Step 1: Clean it up
# Use .strip() to remove extra spaces
# Use .lower() to make it lowercase
clean_message = user_message.strip().lower()
print(f"Cleaned: {clean_message}")

# Step 2: Check what they want
# Use "in" to check if "data" is in the message
if "data" in clean_message:
    print("Recommending: Data Science Fundamentals")

# Step 3: Build a prompt for Claude
person_name = "Ravi"
prompt = f"""You are an assistant.
User {person_name} said: {clean_message}
Give them a short learning recommendation."""

print(f"\nPrompt ready to send to Claude:")
print(prompt)
