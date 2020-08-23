def maxProfit(prices) -> int:
    min_buy_price = float('inf')
    max_profit = 0

    for p in prices:
        if p < min_buy_price:
            min_buy_price = p
        elif p - min_buy_price > max_profit:
            max_profit = p - min_buy_price
    return max_profit

if __name__ == '__main__':
    print(maxProfit([7,1,5,3,6,4]))