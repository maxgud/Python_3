from sys import exit
from random import randint
from textwrap import dedent

global health , attack
health = 100
attack = 7
#this is just a template for all other Scenes 
#which will be called.  Every Scene that 
#will be created and called will have an 
#enter function that will be called
#the template Scene is never actually used
class Scene(object):

    def enter(self):
        print("This scene is a template.")
        print("This is never actually displayed.")
        exit(1)

class Engine(object):
#when Engine is called it takes in two parameters
#the name of the object/self and the scene map
#The entire gameplay is run here calling different
#scenes with the map
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
class Forest_Goblin(Scene):

    def enter(self):
        global health, attack
        forest_g_health = 45
        forest_g_attack = 3
        print("Health: ", health)
        print("Forest Goblin Health:", forest_g_health)  
        while health > 0:   
            if forest_g_health < 1:
                attack = attack + 15
                return 'forest' 
            print(dedent("""
                    1: Attack
                    2: Flee
                 """))

            action = input("> ")

            if action == "1":
                health = health - forest_g_attack
                forest_g_health = forest_g_health - attack 
                print("Your Health:", health)
                print("Forest Goblin Health:", forest_g_health)
                                  
            elif action == "2":
                print("Running back to the forest.")
                return 'forest'

            else:
                print("Wrong Input")
                return 'forest_goblin'


class Forest(Scene):
    def monster_encounter():
            monster_encounter = randint(0,3)
            return monster_encounter


    def enter(self):
        print("Health: ", health)
        print("Attack: ", attack)        
        print(dedent("""
                Forest
                Path 1: left
                Path 2: straight
                Path 3: right
             """))

        action = input("> ")

        if action == "1":
                return 'forest_goblin'
        elif action == "2":
            print(dedent("""
                        2
                  """))
            return 'forest'
        elif action == "3":
            print(dedent("""
                        3
                  """))
            return 'forest'                        

        else:
            print("DOES NOT COMPUTE!")
            return 'forest'
#location is a subset of a scene
class Map(object):

    scenes = {
        'forest': Forest(),
        'forest_goblin': Forest_Goblin(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):

        val = Map.scenes.get(scene_name)
        return val
#Everything is dependent on line 145-147
    def opening_scene(self):
        return self.next_scene(self.start_scene)   


a_map = Map('forest')
a_game = Engine(a_map)
a_game.play()             