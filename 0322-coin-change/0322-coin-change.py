class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        coins = [c for c in coins if c<=amount]
        if not coins: return -1
        if len(coins) < 2:
            ret = amount // coins[0]
            return -1 if amount-ret*coins[0] else ret
        
        if amount & 1 and not any(c & 1 for c in coins):
            return -1
        
        seen = 1 << amount
        for step in range(1, amount):
            cur = seen
            for coin in coins:
                cur |= seen >> coin
            if cur & 1:
                return step
            if cur == seen:
                return -1      
            seen = cur