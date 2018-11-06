print("Let's practice everything.")
#easy escape characters / sequences
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')
#defining strings over multiple lines with escape
#sequences
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
#prints the variable 'poem'
print("--------------")
print(poem)
print("--------------")

#does some math and sets it to a variable
five_var = 10 - 2 + 3 - 6
#interpolates the variable in a string
print(f"This should be five: {five_var}")

#defines a function which takes in 1 argument 
#and uses it to create other variables/values
#which are returned
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
#jelly_beans is now set to the beans variable
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
#this is another way to interpolate
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))