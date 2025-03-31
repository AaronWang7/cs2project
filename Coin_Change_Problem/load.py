import csv
def load_denominations(country):
    #Load denominations for the selected country
    with open("Coin_Change_Problem/coin_denominations.csv", mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == country.lower():
                coins = [item.split('-') for item in row[1:]]
                return {name: int(value) for name, value in coins}
    return None
