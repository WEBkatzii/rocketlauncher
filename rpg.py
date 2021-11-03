#import libraries
import os
from os import system, name 
import random

#clearing definition
def clear(): 
      # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear')

#player controller
class character:

    #getting character stats
    def __init__(self, name, hp, armor):
        self.name = name
        self.hp = hp
        self.arrows = 100
        self.weaponlist = []
        self.armor = armor

    #set the characters emeny
    def setenemy(self, enemy):
        self.enemy = enemy
        self.enemy.enemy = self

    #set the characters weapon
    def setweapon(self, weapon):
        self.weapon = weapon

    #attack the characters enemy
    def attack(self):
        self.enemy.hp = self.enemy.hp - self.weapon.damage * (self.weapon.strength // self.enemy.armor)
        self.arrows = self.arrows - self.weapon.usedarrows

#weapon controller
class weapon:

    #getting weapon stats
    def __init__(self, name, damage, usedarrows, strength):
        self.name = name
        self.damage = damage
        self.usedarrows = usedarrows
        self.strength = strength

#battlecontroller
class battle:
    
    def __init__(self):
        pass

    def start(self, enemy):
        clear()
        self.enemyalive = True
        self.enemy = enemy
        player.setenemy(self.enemy)
        input(player.enemy.name + " started a fight against you!")
        while self.enemyalive == True:
            #player weapon chooser
            for i in range(len(player.weaponlist)):
                print(str(i)+":", player.weaponlist[i].name)
            print(str(len(player.weaponlist)+1)+": health potion")
            self.weapon = input("Choose weapon:")
            if self.weapon.isdigit() == True:
                if int(self.weapon) <= len(player.weaponlist):
                    clear()
                    player.setweapon(player.weaponlist[int(self.weapon)])
                    print("You chose:", player.weapon.name)
                    player.attack()
                    if player.enemy.hp <= 0:
                        self.enemyalive = False
                        input("You killed " + player.enemy.name +"!")
                        
                    else:
                        input(player.enemy.name + " has " + str(player.enemy.hp) + " hp left!")
                
                elif int(self.weapon) == len(player.weaponlist) + 1:
                    clear()
                    player.hp = player.hp + 25
                    print("You chose health potion!")
                    input("You now have " + str(player.hp) + "hp!")
            
            #enemy action controller
            if self.enemyalive == True:
                clear()
                player.enemy.setweapon(enemy.weaponlist[random.randint(0, len(self.enemy.weaponlist)-1)])
                enemy.attack()
                print(player.enemy.name + " used " + player.enemy.weapon.name + "!")
                input("You have " + str(player.hp) + " hp left!")

#setup characters
player = character("player", 100, 2)
giant = character("Giant", 250, 3)
orc = character("Orc",100, 2)
undead = character("Undead", 50, 1)

#setup weapons
sword = weapon("sword", 10, 0, 2)
axe = weapon("axe", 15, 0, 3)
bow = weapon("bow", 10, 1, 2)
dagger = weapon("dagger", 5, 0, 2)
crossbow = weapon("crossbow", 15, 1, 3)
powerwand = weapon("power wand", 5, 0, 10)

#give player weapons
player.weaponlist = [sword, bow, powerwand]

#give undead weapons
undead.weaponlist = [dagger]
orc.weaponlist = [dagger, axe]


fight = battle()
fight.start(undead)
fight.start(orc)