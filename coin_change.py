class Solution:
    def coinChange(self, coins, amount):
        total = amount
        count = 0
        while len(coins) > 0:
            max_coins = max(coins)
            while max_coins <= total:
                count += 1
                total -= max_coins
            coins.pop(coins.index(max(coins)))
        return count

if __name__ == "__main___":
    print( Solution.coinChange( [1, 2, 5], 11) ) # Should be 3, 11 = 5 + 5 + 1