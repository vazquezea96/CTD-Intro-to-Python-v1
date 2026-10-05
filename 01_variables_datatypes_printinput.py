# variables
name = "Jazmine"
age = 28
height = 5.8

print("Name: ", name)
print("Age: ", age)
print("Height: ", height)
print(name, "is", age, "and is", height)
score = 10
print(score) # Output: 10

score = 25
print(score) # Output: 25

# Data Types
is_student = True # Boolean
balance = 1000.75 # Float
first_name = "Eduardo" # String
number_of_days = 7 # Integer

print(type(is_student))
print(type(balance))
print(type(first_name))
print(type(number_of_days))

# Collecting Input with input()

# name = input("What is your name? ")
# print("Hello,", name)

# This will NOT work the way you expect
# age = input("Enter your age: ")
# next_year = age + 1 # TypeError! You can't add a number to a string

# This WILL work
# age = input("Enter your age: ")
# age = int(age) # Convert the string to an integer
# # age = int(input("Enter your age: "))
# next_year = age + 1
# print("Next year you will be", next_year)

# Implicit vs. Explicit Conversion
result = 3 + 2.5 # Python converts 3 to 3.0 automatically
print(result) # Output: 5.5
print(type(result)) # Output: <class 'float'>

result = int(2.8) + 3 # You explicitly convert 2.8 to 2 (drops the decimal)
print(result)

# Operators
# Operators are symbols that perform operations on values. Python has three main types.

# Arithmetic Operators
# These do math:
# + - * / // % **

# / always gives you a float, even when the answer is a whole number: 9 / 3 gives you 3.0
# // drops the decimal part: 7 // 2 gives 3, not 3.5

# % gives you the remainder after division: 7 % 3 gives 1 because 7 divided by 3 is 2 with a remainder 1

total = 10 + 5
print(total)

remainder = 10 % 3
print(remainder)

squared = 4 ** 2
print(squared)

# Comparison Operators
# These compare two values and give you a boolean (True or False):
# == (equal), != (NOT), < (less), > (greater), <=, >=
# Note the difference: = assigns a value, == checks if two values are equal.

age = 30
print(age > 18)
print(age == 25)

# Logical Operators
# These combine conditions
# and, or, not

age = 30
has_id = True
print(age >= 18 and has_id) # Output: True (both conditions are met)
print(age >= 21 or has_id) # Output: True (at least one is met)

# Combining Strings
# You can join strings together using the + operator. This is called string concatenation:
first = "Code"
second = "the Dream"
combined = first + " " + second
print(combined) 

age = 30
message = "I am " + str(age) + " years old."
print(message)

# Formatted Strings (f-strings)
# An f-string is a convenient way to put variables inside a string. You add the letter f before the opening quote, then put variable names inside curly braces {}.

print(f"My name is {name} and I am {age} years old.")

# You can also do math inside the curly braces:
price = 5
quantity = 3
print(f"Total: {price * quantity} items")

print(0.1 + 0.2)
# To display a clean number with a specific number of decimal places, use :.Nf where N is the number of places you want:
total = 0.1 + 0.2
print(f"Total: {total:.2f}") # Output: Total: 0.30

# String Methods
# Strings come with built-in tools called methods that let you transform and work with text. You use them by adding a dot (.) and the method name after the string or variable.

# Changing Case
greeting = "Hello, World!"

print(greeting.lower()) 
print(greeting.upper())

# Removing Extra Whitespace
# strip() removes spaces (and other whitespace) from the beginning and end of a string. This is especially useful when working with user input:

user_input = "   hello   "
print(user_input.strip())     # Output: hello

# Replacing Text
# replace() swaps one piece of text for another:
message = "I like cats"
new_message = message.replace("cats", "dogs")
print(new_message)

# Splitting Text into a List
# split() breaks a string into a list of smaller strings at each space (or at a character you specify):
sentence = "Code the Dream"
words = sentence.split()
print(words)

data = "apple,banana,cherry"
fruits = data.split(",")
print(fruits)

# Joining Text Together
# join() does the opposite of split() - it takes a list of strings and combines them:
words = ["Code", "the", "Dream"]
combined = " ".join(words)
print(combined)
