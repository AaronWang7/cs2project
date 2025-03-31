def show_result(country, amount, coins_used):
    #Result display screen
    print("\n" + "="*50)
    print("RESULT".center(50))
    print("="*50)
    print(f"\nCountry: {country}")
    print(f"Amount: {amount}")
    
    if amount == 0:
        print("\nNo coins needed for amount 0.")
    elif not coins_used:
        print("\nCannot make exact change with available denominations.")
    else:
        total_coins = sum(coins_used.values())
        print(f"\nMinimum coins needed: {total_coins}")
        print("Coins used:")
        for coin, count in coins_used.items():
            print(f"  {coin}: {count}")
    
    input("\nPress Enter to continue...")
