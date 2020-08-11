def max_profit(prices):
    if len(prices) == 0:
        return 0
    smallest = prices[0]
    for p in prices:
        if p < smallest:
            smallest = p
    try:
        possible_buys = prices[prices.index(smallest)+1:]
        biggest = possible_buys[0]
        for i in possible_buys:
            if i > biggest:
                biggest = i
        return biggest - smallest
    except IndexError:
        return 0

if __name__ == '__main__':
    print( max_profit([7,1,5,3,6,4]) ) # should be 5
    print( max_profit([7,6,4,3,1]) ) # should be 0