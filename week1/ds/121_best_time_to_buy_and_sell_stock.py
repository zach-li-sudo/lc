def maxProfit(prices):
    min_buy = 100000000
    max_profit = 0

    for p in prices:
        min_buy = min(p, min_buy) # update min buy price
        profit = p - min_buy # current step profit
        max_profit = max(max_profit, profit)
    
    return max_profit

    


# prices = [7,1,5,3,6,4]
prices = [7,6,4,3,1]
# prices = [2, 1]
print(maxProfit(prices))