class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = False
        if x == 1:
            return x
        if n == 0:
            return 1
        elif n<0:
            negative = True
            n=abs(n)
        ans = 1
        while n>1:
            if n % 2 == 1:
                ans = ans * x
                n=n-1
            x= x*x
            n=n/2
        if negative == True:
            return 1/(ans*x)
        else:
            return ans * x