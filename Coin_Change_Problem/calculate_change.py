def calculate_change(target, coins):
    #Calculate the minimum coins needed using greedy algorithm
    coins = sorted(coins.items(), key=lambda x: -x[1])  # Sort by value descending
    result = {}
    remaining = target
    
    for name, value in coins:
        if remaining >= value:
            count = remaining // value
            result[name] = count
            remaining -= count * value
    
    if remaining != 0:
        return None
    return result