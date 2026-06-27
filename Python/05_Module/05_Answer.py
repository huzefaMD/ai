# Simple learning path recommender

# Get information from the user
name = input("What is your name? ")
years = int(input("Years of coding experience? "))
knows_python = input("Do you know Python? (yes/no) ").lower()

# Recommend a learning path
if years == 0 and knows_python == "no":
    path = "Python Basics (start here!)"

elif years == 0 and knows_python == "yes":
    path = "Data Structures"

elif years <= 3:
    path = "Web Development"

else:
    path = "Machine Learning"

# Display the recommendation
print(f"\nHello {name}! We recommend: {path}")
