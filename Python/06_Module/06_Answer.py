# Simple AI Chatbot with History Feature

conversation = []

print("=== Simple AI Chatbot ===")
print("Type 'exit' to quit.")
print("Type 'history' to view the conversation.\n")

while True:
    # Get user input
    user_input = input("You: ")

    # Store user message
    conversation.append({
        "role": "user",
        "content": user_input
    })

    # Exit command
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # FEATURE 1: Show conversation history
    elif user_input.lower() == "history":
        print(f"\nTotal messages in conversation: {len(conversation)}")
        print("-" * 40)

        for message in conversation:
            print(f"{message['role'].capitalize()}: {message['content']}")

        print("-" * 40)

    # FEATURE 2: Greeting detection
    elif "hello" in user_input.lower() or "hi" in user_input.lower():
        reply = "Hello! How can I help you today?"
        print(f"Bot: {reply}")

        conversation.append({
            "role": "assistant",
            "content": reply
        })

    # Default reply
    else:
        reply = "I'm still learning. Can you ask something else?"
        print(f"Bot: {reply}")

        conversation.append({
            "role": "assistant",
            "content": reply
        })
