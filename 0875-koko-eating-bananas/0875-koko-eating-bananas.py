class Solution:
    def f(self,p,k):
        t = 0
        for i in p:
            t+=ceil(i/k)
        return t
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s = 1
        e = max(piles)

        while(s<=e):
            m = s + (e-s)//2
            if self.f(piles,m)>h:
                s = m+1
            else:
                e = m-1
        return s