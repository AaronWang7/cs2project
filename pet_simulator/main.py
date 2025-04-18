
import random
import csv
print("welacome to the pet simulator!")
with open('pet_simulator\pet.csv','r') as f:
    if f:
        print("You have played this game before!")
    else:
        print("Would you like to create your fist pet?")
        class pets:
            def __init__(self,name,species,dmg,hp):
                self.name = input("Enter your pet's name:")
                self.species = random.choice(species)
                self.trait = random.choice(trait)
                self.attack = random.randint(10, 90)
                self.health = random.randint(230, 330)



            
trait = ["red","yellow","green","bule"]
species = {"dog",'cat','wolf', 'dragon'}
if species == "dog":
    print("species:", species['species'], 
      "\nhealth:",species['health'],
      "\nacttack:",species['attack'],
      "\ntrait:",species['trait'])
elif species == "cat":
        print("species:", species['species'], 
      "\nhealth:",species['health'],
      "\nacttack:",species['attack'],
      "\ntrait:",species['trait'])


        
    
bob = pets("Mr.Bob","Charizard", 95, 300)
fluffy = pets("Fluffy","Arcanine", 110, 280)

print(bob.species)
print(fluffy.species)

print(bob)
bob.battle(fluffy)