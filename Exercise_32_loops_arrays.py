the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
# the pattern for the for loop is
#for index in name_of_array:

for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []
attributes = []
# then use the range function to do 0 to 6 counts
for i in range(0, 7):
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)

for i in range (23, 32):
	#i isn't the index it is the actual number in the range...
	print(f"The number {i} is being added to attributes...")
	attributes.append(i)

print (attributes)
# now we can print them out too
for i in elements:
    print(f"Element was: {i}")