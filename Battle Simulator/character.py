import csv
import random
import os

# Define CSV file path
CSV_FOLDER = "Battle Simulator/data"  # Folder name (with space)
CSV_FILE = os.path.join(CSV_FOLDER, "characters.csv")  # File path

# Ensure the folder exists
if not os.path.exists(CSV_FOLDER):
    os.makedirs(CSV_FOLDER)

def create_character():
    """
    Creates a new character with random
