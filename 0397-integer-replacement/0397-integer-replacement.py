class Solution:
    def integerReplacement(self, n):
        res = 0
        while n>1:
            res += 1
            if n&1:
                if n&2 and n>3:
                    n   += 1
                    res += 2
                    n  >>= 2
                else:
                    n  -= 1
            else:
                n >>= 1
        return res