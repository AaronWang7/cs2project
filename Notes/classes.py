# Classes and object notes

# what is a class in Python -buleprint for creating an object
# What is an object- like bob is a object, instance in class
# method is a function specic to a class 
# class can have muti method(treat pokemon, train)
# class make program easy
# def __str__(self):


class pokemon:
    def __init__(self,name,species,dmg,hp):
        self.name = name
        self.species = species
        self.hp = hp
        self.dmg = dmg

    def __str__(self):
        return f"Name:{self.name}\nSpecies:{self.species}\nhp: {self.hp}\ndmg:{self.dmg}"

    def battle(self, opponent):
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= self.dmg
            print(f"{self.name} attacked {opponent.name} for {self.dmg} and {opponent.name} now has {opponent.hp}")
            if opponent.hp > 0:
                self.hp -= opponent.dmg
                print(f"{opponent.name} attacked {self.name} for {opponent.dmg} and {self.name} now has {self.hp}")
                if self.hp <= 0:
                    print(f"{self.name} has been knocked out. {opponent.name} won the battle")
            else:
                print(f"{opponent.name} has been knocked out. {self.name} won the battle")
    
bob = pokemon("Mr.Bob","Charizard", 95, 300)
fluffy = pokemon("Fluffy","Arcanine", 110, 280)

print(bob.species)
print(fluffy.species)

print(bob)
bob.battle(fluffy)
print(fluffy.hp)