#!/usr/bin/env python3

"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character:
    def alive (self):
        while self.health > 0:
            return True
        else:
            return False 
    def attack(self,enemy):
        enemy.health -= self.power
        print("{} does {} damage to {}".format(self.name,self.power,enemy.name))
        if enemy.health <=0:
            print("{} is dead".format(enemy.name))
        elif bob.health <= 0:
            print("You are dead")        
    def print_status(self):
        print("{} has {} health and {} power.".format(self.name,self.health, self.power))

class Goblin(Character):
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power  
class Hero(Character):
    def __init__(self,name,health,power):
        self.name = name
        self.health = health
        self.power = power

bob = Hero("Bob",10,5)
gob = Goblin("The goblin",6,2)
def main():
    while gob.alive() and bob.alive():
        bob.print_status()
        gob.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ", end=' ')
        inpt = input()
        if inpt  =="1":
            bob.attack(gob)
        elif inpt == "2":
            pass
        elif inpt == "3":
            print("You got away safely!")
            break
        else:
            print("Invalid inpt {}".format(inpt))

        if gob.health > 0:
            gob.attack(bob)
            # Goblin attacks hero        
            

if __name__ == "__main__":
  main()
