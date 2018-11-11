from random import randint

global health, attack, goblin_attack, goblin_health
health = 100
attack = 7

#		monster_encounter = randint(0,3)

def treasure():
	print("You found a treasure!  Attack increased!")
	attack = attack + 15

def monster_encounter(hp,att):
		monster_encounter = 2
		if monster_encounter == 2:
				goblin_attack = 3
				goblin_health = 45
				print("You encountered a monster")

				while hp > 0:
					if goblin_health < 1:	
							print("Monster is dead!")	
							health = hp
							attack = att 	
							treasure()				
							break

					print("1:Attck or 2:flee?")
					action = input(">")
					if action == "1":
							goblin_health = goblin_health - att
							hp = hp - goblin_attack
							print("Goblin Health:", goblin_health)
							print("Your Health:",hp)
					elif action == "2":
							print("2")
					else:
							print("Wrong input!")





monster_encounter(health, attack)