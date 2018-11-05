from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
#this opens the file name with 'writing' privledges
#as opposed to 'r' reading privledges
target = open(filename, 'w')

print("Truncating the file.  Goodbye!")
#this erases everything in the file
target.truncate()

print("Now I'm going to ask you for three lines.")
#these are three varaibles being defined by input
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
#these are writing the variables to the files
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#then the files closes
print("And finally, we close it.")
target.close()