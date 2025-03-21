# Import functions from different pages
from character import create_character, load_characters, save_character
from battle import battle

def show_characters():
    # Displays a list of all characters loaded from the CSV file.
    characters = load_characters()
    if not characters:
        print("No characters found.")
    else:
        for i, c in enumerate(characters):
            print(f"{i+1}. {c['name']} (HP: {c['hp']}, Attack: {c['attack']}, Defense: {c['defense']}, Speed: {c['speed']}, Level: {c['level']})")

def main():
    # Main function to run the Battle Simulator program.
    # Displays a menu for user interaction
    while True:
        print("\n=== Battle Simulator ===")
        print("1. Create Character")
        print("2. Show Characters")
        print("3. Start Battle")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            character = create_character()
            save_character(character)
            print(f"Character {character['name']} created and saved!")
        elif choice == '2':
            show_characters()
        elif choice == '3':
            characters = load_characters()
            if len(characters) < 2:
                print("Not enough characters to battle")
            else:
                show_characters()
                c1_index = int(input("Choose first character (number): ")) - 1
                c2_index = int(input("Choose second character (number): ")) - 1
                battle(characters[c1_index], characters[c2_index])
        elif choice == '4':
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
