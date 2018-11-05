# Here's some new strange stuff, remember type it exactly.
#This wasn't working in python 2....
#so python 3 recognizes newline escape sequences, good

name = "Max"
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#I am a little confused, so when adding a variable
#after a string you can just comma after the string
#if you are interpolating you need the 
#print(f"string string {variable} string")
print("Here are the days: ", days)
print("Here are the months: ", months)

print(f"""
There's something going on here.
With the {name} three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

#cool i understand!