class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        sign = 1
        if x < 0: # If -ve
            sign = -1
            x = x * -1
        
        # Reverse Digits by using While Loop & Modulo Operator
        rev = 0
        while x != 0:
            remainder = x % 10
            rev = rev * 10 + remainder
            x = x // 10

        if INT_MIN < rev < INT_MAX:
            return sign * rev
        else:
            return 0