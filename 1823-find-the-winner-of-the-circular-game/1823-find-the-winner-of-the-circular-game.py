class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n==1: 
            return 1
        elif k==1:
            return n
        elif n>=k:
            next_n = n - n//k
            z = self.findTheWinner(next_n, k) - 1
            x = (z-n%k + next_n) % next_n
            return x + x//(k-1) + 1
        else:
            return (k + self.findTheWinner(n-1, k) -1) % n + 1
        