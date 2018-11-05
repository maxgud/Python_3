var = 32
print ("I know how to put variables into strings different ways...")

print(f"here is a variable {var}.  Yup yup.")
print("Here is the same variable", var, "within strings")

#comments!!!

#okay to get an input to be an integer we need the 
#int to surround the input...
a = int(input("First number to add please...\n"))
b = int(input("Second number to add please...\n"))
def add(a, b):
    print(f"ADDING {a} + {b}")
    sum = a + b

    return sum

print (add(a,b), "is the answer.")

#honestly the first 20 exercises are interpolation of 
#variables, escape characters, input 
#reading and writing files
#and function definitions
