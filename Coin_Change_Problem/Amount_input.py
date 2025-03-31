def enter_amount():
    #Amount input screen
    print("\n" + "="*50)
    print("ENTER AMOUNT".center(50))
    print("="*50)
    
    while True:
        try:
            amount = int(input("\nEnter the amount to make (0 to return): "))
            if amount >= 0:
                return amount
            print("Amount cannot be negative.")
        except ValueError:
            print("Please enter a whole number.")