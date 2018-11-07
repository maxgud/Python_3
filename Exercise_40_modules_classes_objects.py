#okay so to use a module you need the name of the file
#then the name of the file dot function
#ex40_mystuff.apple()

import ex40_mystuff
ex40_mystuff.apple()


#this doesn't just work for functions
#it works for variables as well
print(ex40_mystuff.tangerine)

print (ex40_mystuff.dictionary['apple'])
# get apple from dict
#file_name.dictionary_name['key']
ex40_mystuff.dictionary['apple'] = "WHoa" 
#so this changes the definition temporarly, probably
#just in memory.
#the actualy file is unchanged
print (ex40_mystuff.dictionary['apple'])
# get apple from the module
ex40_mystuff.apple() 



class Woot(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")

#I am defining an object of Class Woot here:        
thing = Woot()
#now I am using that object to use variables
#and functions within the class
thing.apple()
print(thing.tangerine)

class Inventory(object):

    def __init__(self):
        self.name

    def __init__(self):
        self.price

    def __init__(self):
        self.amount

#Here is a basic way to create inventory items using
#classes and objects
#here banana has a name, price, and quantity
#this is much better than an array or a dictionary
#because you can create as many attributes as you 
#want with a class and store these attributes
#without an issue.

banana = Inventory
banana.name = "Banana"
banana.price = 1.50
banana.amount = 40

apple = Inventory
apple.name = "Apple"
apple.price = 2.75
apple.amount = 30

print(banana.name)
print(banana.price)
print(banana.amount)

print(apple.name)
print(apple.price)
print(apple.amount)


#different methods, dictionary, module, class

# dict style (if dictionary is in a different file) 
#1) import file_name
#2)/file_name/dictionary_name/['key']
print (ex40_mystuff.dictionary['apple'])

# module style 
# function
#1) import file_name
#2) file_name.function_name()
ex40_mystuff.apple()
# variable
#1) import file_name
#2) file_name.variable
print(ex40_mystuff.tangerine)

# class style
#object defined by class
thing = Woot()
#object_name.function
thing.apple()
#object_name.variable
print(thing.tangerine)




class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

#there is a for-loop in this function
#so it will print each line given
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
hmm = Song(["hmm"])

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
print(happy_bday.lyrics)

hmm.sing_me_a_song()