# before this you have to install Anthropic (pip install anthropic)
# create a api key in claude api dashboard and use that key in 11th line
# my_ai_bot.py
# Built at HuzefAI Seminar
# My first real AI application!

import anthropic

# Step 1: Connect to Claude
client = anthropic.Anthropic(
    api_key = "paste-your-key-here"
)

# Step 2: Give Claude a personality
SYSTEM = """You are a helpful friend
who answers questions for engineering
students in Chennai.
Keep all answers short and simple.
Use examples from Indian IT companies."""

# Step 3: The memory — starts empty
messages = []

# Step 4: Welcome screen
print("=" * 40)
print("   My AI Bot — Built by Me!")
print("=" * 40)
print("Type your question and press Enter")
print("Type 'quit' to stop")
print("=" * 40)

# Step 5: Ask for name
name = input("\nWhat is your name? ")
print(f"\nHello {name}! Ask me anything!\n")

# Step 6: The main loop
while True:

    # Get question from user
    question = input(f"{name}: ")

    # Check for quit
    if question.lower() == "quit":
        print(f"\nBye {name}! Keep learning!")
        break

    # Skip empty input
    if question == "":
        continue

    # Add question to memory
    messages.append({
        "role":    "user",
        "content": question
    })

    # Send to Claude and show response
    print("\nAI: ", end="", flush=True)

    full_answer = ""

    with client.messages.stream(
        model      = "claude-sonnet-4-6",
        max_tokens = 200,
        system     = SYSTEM,
        messages   = messages
    ) as stream:
        for word in stream.text_stream:
            print(word, end="", flush=True)
            full_answer += word

    print("\n")

    # Add answer to memory
    messages.append({
        "role":    "assistant",
        "content": full_answer
    })

# Step 7: Show how many messages were sent
print(f"\nYou asked {len(messages) // 2} questions today!")
