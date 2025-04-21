
import random
import csv
trait = ["red","yellow","green","bule"]
species = {"dog",'cat','wolf', 'dragon'}
print("welacome to the pet simulator!")
with open('pet_simulator\pet.csv','r') as f:
    if f:
        try:

            print("Would you like to create a new pet?(press 0 if no, 1 for crate a pet)")
            new_pet = int(input(":"))
            if new_pet == 0:
                 print("Ok")
            elif new_pet == 1:
                class pets:
                    def __init__(self,name,species,dmg,hp):
                        self.name = name
                        self.species = species
                        self.trait = trait
                        self.dmg = dmg
                        self.hp = hp
                        print(f"Name:{self.name}\nSpecies:{self.species}\nTrait:{self.trait}\nAtack:{self.dmg}\nHelth:{self.hp}")
                        def __str__(self):
                             return f"Name:{self.name}\nSpecies:{self.species}\ntrait:{self.trait}\nhp: {self.hp}\ndmg:{self.dmg}"
       
        except ValueError:
                print("Enter 1 or 0")
pets_system = pets(input("Enter your pet's name"),random.choice(species), random.choice(trait), random.randint(5, 50),random.randint(250, 350))
        


            

