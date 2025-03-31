from Amount_input import *
from Country_selection import *
from Result_display import *
from welcome import *
from load import *
from calculate_change import *
import os
import csv
def main():
    #Main program flow
    if not os.path.exists("coin_denominations.csv"):
        create_denominations()
    
    display_welcome()
    
    while True:
        country = select_country()
        if not country:
            break
        
        denominations = load_denominations(country)
        if not denominations:
            print(f"Error: No denominations found for {country}")
            continue
        
        while True:
            amount = enter_amount()
            if amount == 0:
                break
            
            coins_used = calculate_change(amount, denominations)
            show_result(country, amount, coins_used)

    print("\nThank you for using the Coin Change Problem Solver!")

def create_denominations():
    #Create the coin denominations file if it doesn't exist
    data = [
        ["USA", "Penny-1", "Nickel-5", "Dime-10", "Quarter-25"],
        ["UK", "Penny-1", "TwoPence-2", "FivePence-5", "TenPence-10", 
         "TwentyPence-20", "FiftyPence-50", "Pound-100"],
        ["Canada", "Penny-1", "Nickel-5", "Dime-10", "Quarter-25", 
         "Loonie-100", "Toonie-200"],
        ["Japan", "OneYen-1", "FiveYen-5", "TenYen-10", "FiftyYen-50", 
         "HundredYen-100", "FiveHundredYen-500"]
    ]
    with open("Coin_Change_Problem/coin_denominations.csv",'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

if __name__ == "__main__":
    main()