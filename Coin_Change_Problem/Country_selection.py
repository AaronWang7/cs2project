
def select_country():
    #Country selection screen
    print("\n" + "="*50)
    print("SELECT COUNTRY".center(50))
    print("="*50)
    print("\nAvailable countries:")
    print("1. USA\n2. UK\n3. Canada\n4. Japan\n5. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-5): ")
        if choice == '1': return "USA"
        if choice == '2': return "UK"
        if choice == '3': return "Canada"
        if choice == '4': return "Japan"
        if choice == '5': return None
        print("Invalid choice. Please enter 1-5.")