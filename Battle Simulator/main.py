

import csv
import random

def validate_attribute(value):
    #Verify if the attribute value is between 1-10
    try:
        num = int(value)
        if 1 <= num <= 10:
            return num
        return None
    except ValueError:
        return None

def get_valid_input(prompt, attr_name):
    #get valid input
    while True:
        value = input(f"{prompt} (1-10): ")
        validated = validate_attribute(value)
        if validated is not None:
            return validated
        print(f"Invalid {attr_name}! Please enter 1-10.")

def create_character():
    #Create a new character
    name = input("\nEnter character name: ").strip()
    
    print("\nEnter character attributes:")
    # health = get_valid_input("Health", "health")
    strength = get_valid_input("Strength", "strength")
    defense = get_valid_input("Defense", "defense")
    speed = get_valid_input("Speed", "speed")

    return {
        "name": name,
        "health": 10,
        "strength": strength,
        "defense": defense,
        "speed": speed
    }

def generate_system_character(counter):
    #Generate system character
    maxvalue = 3
    if counter > 3:
        maxvalue = 10
    return {
        "name": f"system_{counter}",
        "health": 10,
        "strength": random.randint(1, maxvalue),
        "defense": random.randint(1, maxvalue),
        "speed": random.randint(1, maxvalue)
    }

def update_character(character):
    #Upgrade character attributes
    print("\nCharacter upgrades:")
    for attr in ["defense", "strength", "speed", "health"]:
        if character[attr] < 10:
            original = character[attr]
            character[attr] = min(10, character[attr] + 1)
            print(f"{attr.capitalize()}: {original} → {character[attr]}")
    return character

def display_character_info(character):
    #Display detailed information of a single character
    print(f"\n=== {character['name'].upper()} ===")
    print(f"Health:   {character['health']}/10")
    print(f"Strength: {character['strength']}/10")
    print(f"Defense:  {character['defense']}/10")
    print(f"Speed:    {character['speed']}/10")
    print("=" * (len(character['name']) + 6))

def save_to_csv(characters, filename):
    #Save characters to CSV
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "health", "strength", "defense", "speed"])
        writer.writeheader()
        writer.writerows(characters)

def load_from_csv(filename):
    #Loading characters from CSV
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            return [{
                "name": row["name"],
                "health": 10,
                "strength": int(row["strength"]),
                "defense": int(row["defense"]),
                "speed": int(row["speed"])
            } for row in reader]
    except FileNotFoundError:
        return []

def battle_loop(user_char, system_char):
    #Battle cycle with turn based
    print("\n=== BATTLE START ===")
    display_character_info(user_char)
    print("\nVS\n")
    display_character_info(system_char)
    
    while True:
        # User's turn to attack
        print("\nYour turn to attack!")
        system_action = random.choice(["defense", "run"])
        print(f"System character chooses to {'defend' if system_action == 'defense' else 'run'}.")
        
        if system_action == "defense":
            if system_char["defense"] >= user_char["strength"]:
                print("System character successfully defended!")
            else:
                damage = user_char["strength"] - system_char["defense"]
                system_char["health"] -= damage
                print(f"System character took {damage} damage! Health: {system_char['health']}")
        elif system_action == "run":
            if system_char["speed"] > user_char["speed"]:
                print("System character successfully ran away!")
            else:
                damage = user_char["strength"]
                system_char["health"] -= damage
                print(f"System character failed to run and took {damage} damage! Health: {system_char['health']}")
        
        if system_char["health"] <= 0:
            print("\nYou win!")
            return True, user_char  # User wins
        
        # System's turn to attack
        print("\nSystem character's turn to attack!")
        user_action = input("Choose action (1: Defend, 2: Run): ").strip()
        
        if user_action == "1":  # User chooses to defend
            if user_char["defense"] >= system_char["strength"]:
                print("You successfully defended!")
            else:
                damage = system_char["strength"] - user_char["defense"]
                user_char["health"] -= damage
                print(f"You took {damage} damage! Health: {user_char['health']}")
        elif user_action == "2":  # User chooses to run
            if user_char["speed"] > system_char["speed"]:
                print("You successfully ran away!")
            else:
                damage = system_char["strength"]
                user_char["health"] -= damage
                print(f"You failed to run and took {damage} damage! Health: {user_char['health']}")
        else:
            print("Invalid action! You lose your turn.")
            continue  # Skip to system's next turn
        
        if user_char["health"] <= 0:
            print("\nYou lose!")
            return False, user_char  # User loses

def main():
    filename = "characters.csv"
    characters = load_from_csv(filename)
    system_counter = 1
    
    if not characters:
        print("No existing characters. Create a new one:")
        new_char = create_character()
        characters.append(new_char)
        save_to_csv(characters, filename)
    
    while True:
        print("\n=== MAIN MENU ===")
        print("1. Show Characters")
        print("2. Start Battle")
        print("3. Create New Character")
        print("4. Exit")
        choice = input("Enter choice: ").strip()
        
        if choice == "1":
            if not characters:
                print("No characters available!")
                continue
            print("\n=== CHARACTER LIST ===")
            for char in characters:
                display_character_info(char)
        
        elif choice == "2":
            if not characters:
                print("No characters available!")
                continue
                
            print("\nSelect your fighter:")
            for idx, char in enumerate(characters, 1):
                print(f"{idx}. {char['name']}")
                
            try:
                selected = int(input("Enter number: ")) - 1
                if 0 <= selected < len(characters):
                    user_char = characters[selected]
                    battle_wins = 0
                    
                    while True:
                        victory, updated_char = battle_loop(user_char, generate_system_character(system_counter))
                        characters[selected] = updated_char  # Update character if upgraded
                        system_counter += 1
                        
                        if victory:
                            battle_wins += 1
                            print(f"\nYou won the battle! Total wins: {battle_wins}")
                            update_character(updated_char)  # Upgrade character after winning
                            save_to_csv(characters, filename)
                            characters[selected]["health"] = 10
                            cont = input("\nContinue battling? (y/n): ").lower()
                            if cont != 'y':
                                break
                        else:
                            print("\nBattle failed! Returning to main menu.")
                            characters[selected]["health"] = 10
                            break
                    
                else:
                    print("Invalid selection!")
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "3":
            new_char = create_character()
            characters.append(new_char)
            save_to_csv(characters, filename)
            print("Character created and saved!")
        
        elif choice == "4":
            save_to_csv(characters, filename)
            print("Data saved. Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
