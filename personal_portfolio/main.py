#Import os, random and functions from other pages
import os
import random
from cal import *
from to_do import *
from rps import *
from shopping_list import *
from tic_tac import *
from guess_number import *
#Clears the screen based on OS
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#Press Enter to continue
def pause():
    input("\nPress Enter to continue...")
#Display how to use the program
# Display main menu(projects user can pick)
def show_menu():
    print("""
(Enter 0-6):
1. Calculator
2. Rock Paper Scissors 
3. To Do List
4. Number Guessing Game
5. tic tac toe game
6. shopping list
0. Exit
""")
#Data/Inforamtion stored(title, desc, process, learned, group)
def show_description(index):
    descriptions = [
        {
            "title": "Calculator",
            "desc": "Performs basic math operations like addition, subtraction, multiplication, and division.",
            "process": "Created functions for each operation and added input validation.",
            "learned": "How to define and use functions effectively.",
            "group": "Individual project"
        },
        {
            "title": "Rock Paper Scissors",
            "desc": "Play Rock Paper Scissors against the computer.",
            "process": "Used the `random` module to simulate computer choices.",
            "learned": "How to use `random.randint()` and handle user input for game logic.",
            "group": "Individual project"
        },
        {
            "title": "To-Do List",
            "desc": "Create, view, and manage tasks stored in a text file.",
            "process": "Used string handling and file operations (`with open`) to read/write tasks.",
            "learned": "File handling in Python and working with persistent data.",
            "group": "Individual project"
        },
        {
            "title": "Guess the Number",
            "desc": "Guess a random number between 1 and 100 with hints after each guess.",
            "process": "Implemented a `while` loop to keep the game running until the correct guess.",
            "learned": "How to use loops and conditional logic to manage game flow.",
            "group": "Individual project"
        },
        {
            "title": "Tic Tac Toe",
            "desc": "Play Tic Tac Toe against the computer in the terminal.",
            "process": "Used lists to create the board and random choices for computer moves.",
            "learned": "Game logic and turn-based control using functions and conditionals.",
            "group": "Individual project"
        },
        {
            "title": "Shopping List",
            "desc": "Add, view, and remove items from your shopping list.",
            "process": "Handled user inputs with strings and list operations.",
            "learned": "Managing user input, updating lists, and basic operations.",
            "group": "Individual project"
        }
    ]
    proj = descriptions[index - 1]
    print(f"\n{proj['title']}")
    print(f"Description: {proj['desc']}")
    print(f"Process: {proj['process']}")
    print(f"What I learned: {proj['learned']}")
    print(f"Role: {proj['group']}\n")


def run_project(choice):
    print(f"\nRunning {choice}...")
    # Project code goes here
    print("(Project runs here)\n")
#Main function handles user choice
def main():
    while True:
        clear_screen()
        show_menu()
        
        try:
            choice = input("Your choice (0-6): ")
            
            if choice == "0":
                print("Goodbye!")
                break
            elif choice == "1":
                cal()
            elif choice == "2":
                rps_game()
            elif choice == "3":
                load_tasks()
            elif choice == "4":
                play_game()
            elif choice == "5":
                play_tic_tac_toe()
            elif choice == "6":
                shopping()




            else:
                print("Please enter 0-6")
                pause()
        except:
            print("Invalid input")
            pause()

if __name__ == "__main__":
    main()