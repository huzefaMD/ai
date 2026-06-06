# if/else — make a decision
years = input("Years of IT experience: ")
years = int(years)

if years == 0:
    print("Best course: Python for AI")
    print("Start from the beginning!")

elif years <= 2:
    print("Best course: AWS Fundamentals")
    print("Great entry point!")

elif years <= 5:
    print("Best course: DevOps Bootcamp")
    print("High demand skill!")

else:
    print("Best course: Generative AI")
    print("Cutting edge technology!")

print("See you at HuzefAI!")
