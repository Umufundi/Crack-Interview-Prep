class Solution:
    def lastRemaining(self, n: int) -> int:
        arr = range(n,0,-1)
        while len(arr)>1:
            arr = arr[-2::-2]       
        return arr[0]