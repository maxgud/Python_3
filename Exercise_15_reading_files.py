#these first two lines import the first two arguments given
#after python3
#The script-name and an argument
from sys import argv
script, filename = argv

#this opens the file given and sets it equal to the 
#variable txt
txt = open(filename)

#this just interpolates the filename
print(f"Here's your file {filename}:")
#this actually prints out what is in the file!
print(txt.read())
#This second part asks for the file within the program
#it doesn't take it as a command prompt argument
print("Type the filename again:")
#these next lines set the file to a variable name
file_again = input("> ")
#open the file and set it to a new variable
txt_again = open(file_again)
#prints the new variable
print(txt_again.read())