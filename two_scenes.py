#right now you can go between two areas in the game
#the central corridor and the lazer weapon armory
#and win the game

from sys import exit
from random import randint
from textwrap import dedent

#this is just a class with an enter function
#all of the scenes used are a subset of this class

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)

#this is the 'Engine' class
#it has a function that takes in parameters of 
#self and scene_map

# a_map = Map('central_corridor')
# a_game = Engine(a_map)
# a_game.play()
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

#Every death has a scene that takes place
class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
         "Your Mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this.",
         "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

#Every location is a subset of a scene
class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
                Central Corridor
             """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
                        You Shoot!  And Die
                  """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
                        You try and dodge... But die.
                  """))
            return 'death'

        elif action == "tell a joke":
            print(dedent("""
                        Joking works!  You find the laser
                        weapon armory...
                  """))
            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
#location is a subset of a scene
class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
                    You are in the Laser Weapon Armory.
                    What is the three diget code?!
              """))

        code = ("111")
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                        Woot, you got the right code.
                        On to the Bridge!
                  """))
            return 'central_corridor'
        else:
            print(dedent("""
                  The lock buzzes one last time and then you hear a
                  sickening melting sound as the mechanism is fused
                  together.  You decide to sit there, and finally the
                  Gothons blow up the ship from their ship and you die.
                  """))
            return 'death'


class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'



#Map takes it its own parameter and the start_scene
#it has a function called 'next_scene' within it
#it also has opening scene as a function
class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
#Everything is dependent on line 145-147
    def opening_scene(self):
        return self.next_scene(self.start_scene)

#huh what is cool about this is that you can 
#start you scene anywhere you want
#nothing is dependent on anything previous to it


#okay everything starts with the definition of an 
#instance of the map
#start_scene is the parameter being used in 
#Map, in this case it is laser_weapon_armory
#the opening_scene passes this parameter as
#the start_scene to the function
#next_scene which takes in the parameter
#and changes it to the variable scene_name
#val = Map.scenes.get(scene_name)
#return val
a_map = Map('laser_weapon_armory')
a_game = Engine(a_map)
a_game.play()