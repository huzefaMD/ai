# A list uses square brackets [ ]
subjects = ["Math", "Physics", "Chemistry", "Computer Science"]
scores   = [85, 92, 78, 95]
empty    = []    # Empty list — you start with this for conversation history!

print(subjects)
# ['Math', 'Physics', 'Chemistry', 'Computer Science']

#Getting Items from a List

subjects = ["Math", "Physics", "Chemistry", "Computer Science"]

print(subjects[0])    # Math                ← first item (index 0)
print(subjects[1])    # Physics             ← second item
print(subjects[-1])   # Computer Science    ← last item
print(len(subjects))  # 4                   ← how many items

#Adding to a List — .append()

# Start with empty list
messages = []

# Add items one by one
messages.append("Hello")
messages.append("Hi there!")

print(messages)
# ['Hello', 'Hi there!']
print(len(messages))
# 2


#Dictionaries

# A dictionary uses { }
# Each item has a key and a value
# key : value

person = {
    "name":    "Ravi Kumar",
    "subject": "Computer Science",
    "score":   92,
    "active":  True
}

print(person)


#Getting Values from a Dictionary

person = {
    "name":    "Ravi Kumar",
    "subject": "Computer Science",
    "score":   92
}

# Get values using the key
print(person["name"])     # Ravi Kumar
print(person["subject"])  # Computer Science
print(person["score"])    # 92

# Add a new key
person["city"] = "Bangalore"
print(person["city"])     # Bangalore

# Update an existing value
person["subject"] = "Data Science"
print(person["subject"])  # Data Science




