# while loop — keep going until stop
# This is the heart of every chatbot!

print("=" * 35)
print("  HuzefAI Course Recommender Bot")
print("=" * 35)
print("Type 'quit' to exit")
print()

while True:
    question = input("Ask me anything: ")

    if question == "quit":
        print("Goodbye! Keep learning!")
        break

    if question == "":
        continue

    print(f"You asked: {question}")
    print("Great question! Visit huzefai.com")
    print()
