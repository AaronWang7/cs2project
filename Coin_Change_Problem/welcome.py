import csv
import os
def display_welcome():
    #Show welcome screen
    # Display welcome screen
    print("\n" + "="*50)
    print("COIN CHANGE PROBLEM SOLVER".center(50))
    print("="*50)
    print("\nThis program helps you make change using the fewest coins possible.")
    print("First, select a country, then enter the amount you need to make.")
    #only continue if press enter
    input("\nPress Enter to continue...")
