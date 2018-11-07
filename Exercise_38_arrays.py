#this is just a variable that is equal to a string
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")
#this turns the variable into an array
#it splits the array where ever there is a ' ' aka space
stuff = ten_things.split(' ')
#this is a second array
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

#while the number of elements in stuff does not equal 10
#run the following lines of code
while len(stuff) != 10:
	#this .pop() takes the last element off of the array
	#more_stuff
	#you can set this to a variable which is done
    next_one = more_stuff.pop()
    #this prints the variable being added to the
    #stuff array
    print("Adding: ", next_one)
    stuff.append(next_one)
    #this interpolates how many elements are in the 
    #array stuff
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

#this prints the second element in stuff
print(stuff[1])
#this prints the last element in stuff
print(stuff[-1]) # whoa! fancy
#this removes the last element in stuff and prints it
print(stuff.pop())
#this joins all the elements in stuff with a space
#this can be used to turn an array into a string
print(' '.join(stuff)) # what? cool!
#this joins all the elements in stuff into a string
#joining them with a hash#
print('#'.join(stuff)) # super stellar!
#this joins only the 4th and 5th elements in the array
#stuff with a hash
print('#'.join(stuff[3:5]))