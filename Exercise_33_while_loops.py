#defining a variable
i = 0
#defining an array
numbers = []

#while loop condition
while i < 6:
	#interpolation of the variable i in a string
    print(f"At the top i is {i}")
    #this is adding the variable i to the array
    #numbers
    numbers.append(i)

    #this increases the variable by one
    i = i + 1
    #this shows what is put in the numbers array
    print("Numbers now: ", numbers)
    #this shows what happened to the variable 
    #by showing its value
    print(f"At the bottom i is {i}")


print("The numbers: ")
#this prints each element in the array numbers
for num in numbers:
    print(num)

#this prints the array numbers
print(numbers)    