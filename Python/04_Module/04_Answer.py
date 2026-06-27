# Step 1: Create empty conversation
conversation = []

# Step 2: Add these 3 messages using .append()
conversation.append({
    "role": "user",
    "content": "What subjects are available?"
})

conversation.append({
    "role": "assistant",
    "content": "Math, Physics, and Computer Science"
})

conversation.append({
    "role": "user",
    "content": "How much does the Math course cost?"
})

# Step 3: Print the results
print(f"Total messages in conversation: {len(conversation)}")
print(f"First speaker: {conversation[0]['role']}")
print(f"Last question: {conversation[2]['content']}")
