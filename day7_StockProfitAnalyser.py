prices = list(map(int, input("Enter stock prices: ").split()))
min_price = prices[0]
max_profit = 0
buy_day = 0
sell_day = 0
for i in range(1, len(prices)):
    # Check if we found a lower buying price
    if prices[i] < min_price:
        min_price = prices[i]
        buy_day = i
    # Calculate profit if we sell today
    profit = prices[i] - min_price
    # Check if this is the best profit so far
    if profit > max_profit:
        max_profit = profit
        sell_day = i
print("Maximum profit:", max_profit)
if max_profit > 0:
    print("Buy on day:", buy_day + 1)
    print("Sell on day:", sell_day + 1)
    print("Buy price:", prices[buy_day])
    print("Sell price:", prices[sell_day])
else:
    print("No profit can be made.")
