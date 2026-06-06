# ─────────────────────────────────────────────
# MY FIRST AI CHATBOT
# Built at HuzefAI Seminar
# ─────────────────────────────────────────────

# Step 1: Course information
courses = {
    "AWS":    "Rs.4999 — 6 weeks — Cloud computing",
    "DevOps": "Rs.7999 — 8 weeks — Build and deploy apps",
    "GenAI":  "Rs.9999 — 8 weeks — Build AI applications",
    "Python": "Rs.3999 — 5 weeks — Programming basics"
}

# Step 2: The AI personality
bot_name = "HuzefAI Bot"
bot_personality = "friendly and helpful"

# Step 3: Memory — starts empty
chat_history = []

# Step 4: Welcome screen
print("=" * 45)
print(f"   Welcome to {bot_name}!")
print(f"   I am {bot_personality}.")
print("=" * 45)
print("Commands:")
print("  'courses' — see all courses")
print("  'history' — see chat history")
print("  'clear'   — clear history")
print("  'quit'    — exit")
print("=" * 45)

# Step 5: Get student name
name = input("\nYour name: ").strip()
if name == "":
    name = "Student"

print(f"\nHello {name}! How can I help you?")
print()

# Step 6: The main chatbot loop
while True:

    # Get student message
    message = input(f"{name}: ").strip()

    # Skip empty messages
    if message == "":
        continue

    # Command: quit
    if message.lower() == "quit":
        print(f"\n{bot_name}: Goodbye {name}!")
        print(f"You had {len(chat_history)} messages.")
        print("Visit huzefai.com to enroll!")
        break

    # Command: show courses
    elif message.lower() == "courses":
        print(f"\n{bot_name}: Here are our courses:\n")
        for course, details in courses.items():
            print(f"  {course}: {details}")
        print()

    # Command: show history
    elif message.lower() == "history":
        if len(chat_history) == 0:
            print(f"\n{bot_name}: No messages yet!\n")
        else:
            print(f"\n{bot_name}: Your {len(chat_history)} messages:\n")
            for i, msg in enumerate(chat_history):
                print(f"  {i+1}. {msg}")
            print()

    # Command: clear history
    elif message.lower() == "clear":
        chat_history = []
        print(f"\n{bot_name}: Chat cleared!\n")

    # Check if asking about a specific course
    elif "aws" in message.lower():
        chat_history.append(message)
        print(f"\n{bot_name}: Great choice {name}!")
        print(f"AWS Fundamentals: {courses['AWS']}")
        print("This is perfect for cloud careers!")
        print("Type 'courses' to see all options.\n")

    elif "devops" in message.lower():
        chat_history.append(message)
        print(f"\n{bot_name}: Excellent choice {name}!")
        print(f"DevOps Bootcamp: {courses['DevOps']}")
        print("DevOps engineers are in high demand!\n")

    elif "genai" in message.lower() or "ai" in message.lower():
        chat_history.append(message)
        print(f"\n{bot_name}: Amazing choice {name}!")
        print(f"Generative AI: {courses['GenAI']}")
        print("This is the hottest skill right now!\n")

    elif "python" in message.lower():
        chat_history.append(message)
        print(f"\n{bot_name}: Smart starting point {name}!")
        print(f"Python for AI: {courses['Python']}")
        print("Python is the language of AI!\n")

    elif "price" in message.lower() or "cost" in message.lower():
        chat_history.append(message)
        print(f"\n{bot_name}: Here are our prices {name}:\n")
        for course, details in courses.items():
            print(f"  {course}: {details.split('—')[0].strip()}")
        print()

    elif "hello" in message.lower() or "hi" in message.lower():
        chat_history.append(message)
        print(f"\n{bot_name}: Hello {name}! Great to meet you!")
        print("Ask me about our courses or type 'courses'!\n")

    # Default reply
    else:
        chat_history.append(message)
        print(f"\n{bot_name}: Thanks for your message {name}!")
        print("I can help with course information.")
        print("Type 'courses' to see what we offer.")
        print("Or WhatsApp Huzefa for personal help!\n")
