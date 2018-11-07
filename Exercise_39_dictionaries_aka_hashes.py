# create a mapping of state to abbreviation
#'Oregon' is the key
#'OR' is the value
#these are the hash pairs, or dictionary pairs
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
# this time 'CA' is the key
#and 'San Francisco' is the value
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
#this is how you add additional key value pairs
#to the dictionary cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
#cities['NY'] is refering to a key and returns the
#value
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
#this is the same, referring to the keys in states
#and returning the values
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
#this is just embedded values
#the key for the value states['Michigan']
#ends up being the key for the cities which returns
#Detroit
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
#this is a for loop for hashes/dictionaries
#this
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

#I am a little confused about how get works...
print('-' * 10)
#hmm I guess it is like a test case, if it isn't
#available
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")