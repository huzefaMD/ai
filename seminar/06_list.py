# List — remember multiple things
chat_history = []

print("Simple chat — type quit to stop")
print()

while True:
    message = input("You: ")

    if message == "quit":
        break

    if message == "":
        continue

    chat_history.append(message)
    print(f"Bot: Got your message!")
    print()

print(f"\nYou sent {len(chat_history)} messages:")
for i, msg in enumerate(chat_history):
    print(f"  {i+1}. {msg}")
