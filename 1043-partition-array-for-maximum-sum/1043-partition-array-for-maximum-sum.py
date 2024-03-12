class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [arr[0]] + [0]*((n:=len(arr)) -1)
        currmax = arr[0]

        for i in range(1, k):
            if arr[i] > currmax:
                currmax = arr[i]
            dp[i] = currmax * (i + 1)

        for i in range(k, n):
            curr = 0
            currmax = -1
            for j in range(1, k + 1):
                if arr[i - j + 1] > currmax:
                    currmax = arr[i - j + 1]

                curr = dp[i-j] + (j*currmax)

                if curr > dp[i]:
                    dp[i] = curr
                    
        return dp[n - 1]