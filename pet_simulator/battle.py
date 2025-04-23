#Import from other pages
from pet_actions import view_pets
from pet import Pet

# battle system
def battle(pets):
    if len(pets) < 2:
        print("You need at least two pets to battle!")
        return

    print("\nSelect two pets to battle")
  
    for idx, pet in enumerate(pets, start=1):
        print(f"{idx}. {pet.name}")
    
    pet1_idx = int(input("Choose the first pet: ")) - 1
    pet2_idx = int(input("Choose the second pet: ")) - 1
    
    pet1 = pets[pet1_idx]
    pet2 = pets[pet2_idx]

    print(f"\nBattle between {pet1.name} and {pet2.name}!\n")
    
    # Battle start
    while pet1.is_alive() and pet2.is_alive():
        pet1.attack(pet2)
        if pet2.is_alive():
            pet2.attack(pet1)
    
    # Who won the bttle
    if pet1.is_alive():
        print(f"\n{pet1.name} wins the battle!")
        pet1.gain_experience(50)  # Gain exp when won
    else:
        print(f"\n{pet2.name} wins the battle!")
        pet2.gain_experience(50)  # Gain exp when won
