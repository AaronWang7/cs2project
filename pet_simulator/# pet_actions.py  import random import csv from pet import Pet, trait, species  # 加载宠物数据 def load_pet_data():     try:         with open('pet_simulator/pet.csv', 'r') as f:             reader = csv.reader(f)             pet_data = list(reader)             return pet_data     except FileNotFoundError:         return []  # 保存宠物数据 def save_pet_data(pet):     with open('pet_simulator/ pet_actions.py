#Import from other pages
#Import random and csv
import random
import csv
from pet import Pet, trait, species

# Load pets information
def load_pet_data():
    try:
        with open('pet_simulator/pet.csv', 'r') as f:
            reader = csv.reader(f)
            pet_data = list(reader)
            return pet_data
    except FileNotFoundError:
        return []

# Save pets information
def save_pet_data(pet):
    with open('pet_simulator/pet.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([pet.name, pet.species, pet.trait, pet.dmg, pet.hp, pet.level, pet.experience])

# create new pet
def create_pet():
    pet_name = input("Enter your pet's name: ")
    pet_species = random.choice(list(species))  # random species
    pet_trait = random.choice(trait)  # random trait
    pet_dmg = random.randint(5, 50)  # random dmg
    pet_hp = random.randint(250, 350)  # random health

    new_pet = Pet(pet_name, pet_species, pet_trait, pet_dmg, pet_hp)
    print(f"Your new pet: {new_pet}")
    save_pet_data(new_pet)
    return new_pet

# see stats
def view_pets(pets):
    if not pets:
        print("You don't have any pets yet!")
        return []
    print("\n=== Your Pets ===")
    for idx, pet in enumerate(pets, start=1):
        print(f"{idx}. {pet}")
    print("\n")
    return pets
