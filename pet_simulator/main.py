#Import from other pages
from pet_actions import create_pet, view_pets, load_pet_data
from battle import battle
from pet import Pet

# Main menu for actions
def main_menu():
    print("\nWelcome to the Pet Simulator")
    print("1. Create a new pet")
    print("2. View pets")
    print("3. Battle pets")
    print("4. Exit")
    choice = input("Please choose one: ")
    return choice

# Main function
def main():
    pets = load_pet_data()  # Load pet data
    pet_objects = []  # Store data
    while True:
        choice = main_menu()

        if choice == '1':
            # create new pet
            new_pet = create_pet()
            pet_objects.append(new_pet)
        elif choice == '2':
            # view pet
            pet_objects = view_pets(pet_objects)
        elif choice == '3':
            # battle
            battle(pet_objects)
        elif choice == '4':
            print("goodbye!")
            break
        else:
            print("please try again.")

if __name__ == "__main__":
    main()

