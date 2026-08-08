prices = [7,2,1,5,6,4,8]

def Stock_Buy_Sell_Optimal(prices):
    n = len(prices)
    buy = prices[0]
    max_profit = 0
    for i in range(1,n):
        if buy > prices[i]:
            buy = prices[i]
        else:
            if max_profit < prices[i] - buy:
                max_profit =  prices[i] - buy
    return max_profit

print(Stock_Buy_Sell_Optimal(prices))
