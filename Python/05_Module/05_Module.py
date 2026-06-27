#The Basic Structure

if something_is_true:
    do this
else:
    do this instead

#Your First If/Else — Try This!

seats_left = 5

if seats_left > 0:
    print("Seats available! Enroll now.")
else:
    print("Sorry, fully booked.")

#Multiple Choices — elif

score = 78

if score >= 90:
    print("Grade: A")
elif score >= 75:
    print("Grade: B")
elif score >= 60:
    print("Grade: C")
else:
    print("Grade: F")


#and — BOTH must be true

students   = 28
seats_left = 2

if students > 0 and seats_left > 0:
    print("Batch running with seats available!")

#or — ONE is enough

subject = "Math"
if subject == "Math" or subject == "Physics":
    print("Science stream subject selected")

#in — The Shortcut for Multiple or Checks

# Instead of:
if command == "quit" or command == "exit" or command == "q":
    print("Goodbye!")

# Write:
command = "quit"
if command in ["quit", "exit", "q"]:
    print("Goodbye!")


