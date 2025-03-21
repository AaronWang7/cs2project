import random

def battle(character1, character2):
    # turn based battle between two characters.
    print(f"\nBattle Start: {character1['name']} VS {character2['name']}")

    # attack turn tracker
    def attack_turn(attacker, defender):
        # Simulates an attack turn between two characters.
        # Calculates damage based on attacker's attack and defender's defense.
        damage = random.randint(int(attacker['attack'] * 0.8), attacker['attack']) - defender['defense']
        damage = max(0, damage)  # Ensure damage is not negative
        defender['hp'] -= damage
        print(f"{attacker['name']} attacks {defender['name']} for {damage} damage! Remaining HP: {defender['hp']}")

    # Check if a character is defeated
    def is_defeated(character):
        # Checks if a character's HP is less than or equal to 0.
        return character['hp'] <= 0

    # experience to the winner
    def award_experience(winner, loser):
        # experience to the winner based on the loser's level.
        # If experience reaches 100, the winner levels up.
        experience_gain = loser['level'] * 10
        winner['experience'] += experience_gain
        print(f"{winner['name']} gains {experience_gain} experience points!")
        if winner['experience'] >= 100:
            winner['level'] += 1
            winner['experience'] = 0
            winner['hp'] += 20
            winner['attack'] += 5
            winner['defense'] += 5
            winner['speed'] += 1
            print(f"{winner['name']} leveled up to level {winner['level']}!")

    # Battle loop
    while True:
        if character1['speed'] >= character2['speed']:
            attack_turn(character1, character2)
            if is_defeated(character2):
                award_experience(character1, character2)
                print(f"{character2['name']} is defeated! {character1['name']} wins!\n")
                break
            attack_turn(character2, character1)
            if is_defeated(character1):
                award_experience(character2, character1)
                print(f"{character1['name']} is defeated! {character2['name']} wins!\n")
                break
        else:
            attack_turn(character2, character1)
            if is_defeated(character1):
                award_experience(character2, character1)
                print(f"{character1['name']} is defeated! {character2['name']} wins!\n")
                break
            attack_turn(character1, character2)
            if is_defeated(character2):
                award_experience(character1, character2)
                print(f"{character2['name']} is defeated! {character1['name']} wins!\n")
                break
