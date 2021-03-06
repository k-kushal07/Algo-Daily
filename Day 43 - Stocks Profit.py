def max_profit(stocks):
    n = len(stocks)
    cost = 0
    max_price = 0
    if (len(stocks) == 0):
        return 0
    min_price = stocks[0]
    for i in range(len(stocks)):
        min_price = min(min_price, stocks[i])
        cost = stocks[i] - min_price
        max_price = max(max_price, cost)
    return max_price

inpArr = [int(ele) for ele in input().split()]
print(max_profit(inpArr))
