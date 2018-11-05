#this function
#1) interpolates the arguments into a string
#2) returns the sum of the two arguments
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b
#this function
#1) interpolates the arguments into a string
#2) returns the difference of the two arguments
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b
#this function
#1) interpolates the arguments into a string
#2) multiplies the two arguments and returns
#the result
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

#this function
#1) interpolates the arguments into a string
#2) returns the results of dividing two numbers
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")
#these are arguments within functions taken as arguments
#each function returns one argument
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
#huh when you just concatenate strings with variables
#you can do it just with commas.  Spaces are automatically
#added
print("That becomes: ", what, " Can you do it by hand?")