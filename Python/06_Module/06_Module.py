#PART 1: The For Loop

# For loop over a list
subjects = ["Math", "Physics", "Chemistry", "Computer Science"]

for subject in subjects:
    print(f"Studying: {subject}")


#Loop with Numbers — range()

# range(4) gives numbers 0, 1, 2, 3
for i in range(4):
    print(f"Round number {i + 1}")

#Loop with Index — enumerate()

subjects = ["Math", "Physics", "Chemistry", "Computer Science"]

for i, subject in enumerate(subjects):
    print(f"{i + 1}. {subject}")

#Loop Over a Dictionary

scores = {
    "Math":              92,
    "Physics":           85,
    "Computer Science":  95
}

for subject, score in scores.items():
    print(f"{subject}: {score}")

#PART 2: The While Loop

#Your First While Loop

# While loop — keeps running until user says quit
while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "quit":
        print("Goodbye!")
        break          # ← EXIT the loop immediately

    print(f"You said: {user_input}")



#Putting It All Together — Mini Chatbot


# mini_chatbot.py
# Uses: variables, strings, lists, dicts, if/else, loops

# Topic information
topics = {
    "Math":              "Algebra, Calculus, Statistics",
    "Physics":           "Mechanics, Optics, Thermodynamics",
    "Computer Science":  "Algorithms, Data Structures, AI"
}

# Conversation history — empty list to start
conversation = []

print("=" * 40)
print("   Mini Study Assistant")
print("=" * 40)
print("Type 'topics' to see subjects")
print("Type 'quit' to exit")
print("=" * 40)

# The main loop — keeps chatbot running
while True:

    # Get user input
    user_input = input("\nYou: ").strip()

    # Skip empty input
    if not user_input:
        continue

    # Check for quit command
    if user_input.lower() == "quit":
        print("Bot: See you next time! 👋")
        break

    # Check for topics command
    elif user_input.lower() == "topics":
        print("\nBot: Available subjects:")
        for subject, details in topics.items():
            print(f"  • {subject}: {details}")

    # Check if asking about a specific subject
    elif "math" in user_input.lower():
        print(f"Bot: Math covers: {topics['Math']}")

    # Default reply
    else:
        # Add to conversation history
        conversation.append({
            "role":    "user",
            "content": user_input
        })
        print(f"Bot: Thanks for your message!")

print(f"\nTotal messages in session: {len(conversation)}")



