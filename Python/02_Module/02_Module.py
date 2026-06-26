# Creating variables — just write name = value
product_name = "Wireless Headphones"
product_price = 2999
in_stock = True
rating = 4.6

#The 4 Core Data Types

#Type 1: String (str) — Text

# Strings are text — always in quotes
city       = "Bangalore"
language   = "Python"
api_key    = "sk-ant-api03-xxxx"  # Your API key is a string!

print(type(city))   # <class 'str'>


#Type 2: Integer (int) — Whole Numbers

# Integers are whole numbers — no decimal point
students    = 120
max_seats   = 30
quantity    = 5
max_tokens  = 1024     # You use this in EVERY Claude API call!

print(type(students))  # <class 'int'>

#Type 3: Float (float) — Decimal Numbers

# Floats have decimal points
rating      = 4.6
cost_usd    = 0.0089
percentage  = 85.5

print(type(rating))    # <class 'float'>


#Type 4: Boolean (bool) — True or False

# Booleans are only True or False (capital T and F!)
is_logged_in = True
is_full      = False
has_paid     = True

print(type(is_logged_in))  # <class 'bool'>


#Working with Variables

# Math with numbers
price     = 2999
quantity  = 50
revenue   = price * quantity
print(revenue)           # 149950

# Combining strings
first = "Open"
last  = "AI"
name  = first + last
print(name)              # OpenAI

# Updating a variable
total_cost  = 0.0
total_cost  = total_cost + 0.05
print(total_cost)        # 0.05



#f-Strings — Super Important!


name      = "Ravi"
subject   = "Python"
score     = 95

# Old way (bad):
message = "Hello " + name + " your score in " + subject

# f-string way (use this always):
message = f"Hello {name}! Your score in {subject} is {score}"
print(message)
# Hello Ravi! Your score in Python is 95



