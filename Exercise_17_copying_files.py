from sys import argv
from os.path import exists

#this takes in 3 arguments
#1) Name of the script to run
#2) The file to copy
#3) The file to copy to
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

#each character is a byte and len just counts
#the characters
print(f"The input file is {len(indata)} bytes long")

#checks to see if the file being copied to exists
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()