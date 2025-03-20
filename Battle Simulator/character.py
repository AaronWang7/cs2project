import csv
import random

def create_character():

    #Creates a new character with random stats. Returns a dictionary containing the character's attributes.
    name = input("Enter character name: ")
    hp = random.randint(80, 120)
    attack = random.randint(10, 20)
    defense = random.randint(5, 15)
    speed = random.randint(1, 10)
    level = 1
    experience = 0
    return {
        'name': name,
        'hp': hp,
        'attack': attack,
        'defense': defense,
        'speed': speed,
        'level': level,
        'experience': experience
    }

def save_character(character)

    #Saves a character's data to a CSV file.

    with open('characters.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            character['name'],
            character['hp'],
            character['attack'],
            character['defense'],
            character['speed'],
            character['level'],
            character['experience']
        ])

def load_characters():
    #Loads characters from a CSV file. Returns a list of character dictionaries.
    characters = []
    try:
        with open('characters.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    characters.append({
                        'name': row[0],
                        'hp': int(row[1]),
                        'attack': int(row[2]),
                        'defense': int(row[3]),
                        'speed': int(row[4]),
                        'level': int(row[5]),
                        'experience': int(row[6])
                    })
    except FileNotFoundError:
        pass
    return characters
