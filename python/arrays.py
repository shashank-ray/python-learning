def buy_and_sell_stock_once(prices):
    if not prices or len(prices) < 2:
        return 0 

    min_price = prices[0]  
    max_profit = 0  

    for price in prices[1:]:
        
        current_profit = price - min_price

        
        max_profit = max(max_profit, current_profit)

        
        min_price = min(min_price, price)

    return max_profit


stock_prices = [7, 1, 5, 3, 6, 4]
result = buy_and_sell_stock_once(stock_prices)
print(result)