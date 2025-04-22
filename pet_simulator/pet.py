#Import random
import random

trait = ["red", "yellow", "green", "blue"]
species = {"dog", "cat", "wolf", "dragon"}

class Pet:
    def __init__(self, name, species, trait, dmg, hp):
        self.name = name
        self.species = species
        self.trait = trait
        self.dmg = dmg
        self.hp = hp
        self.level = 1  # stating level = 1
        self.experience = 0  #Stating exp = 0
        self.max_hp = hp  # Record health
    # return info
    def __str__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nTrait: {self.trait}\nLevel: {self.level}\nHP: {self.hp}/{self.max_hp}\nDMG: {self.dmg}\nExperience: {self.experience}"
    
    def attack(self, other_pet):
        damage = random.randint(0, self.dmg)
        other_pet.hp -= damage
        print(f"{self.name} attacks {other_pet.name} for {damage} damage!")

    def gain_experience(self, exp):
        #Gain exp
        self.experience += exp
        print(f"{self.name} gained {exp} experience!")
        self.level_up()

    def level_up(self):
        # check level up
        required_exp = 100 * self.level  # Needed exp 
        while self.experience >= required_exp:
            self.experience -= required_exp
            self.level += 1
            self.dmg += random.randint(5, 10)  # Gain dmg
            self.hp += random.randint(10, 20)  # Gain health when level up
            self.max_hp = self.hp  # Update max health
            print(f"{self.name} leveled up to Level {self.level}!")
            required_exp = 100 * self.level  # Next level needed xp

    def is_alive(self):
        return self.hp > 0
