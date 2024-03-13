class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s)+1):
            dp[i] = any(dp[i-j] and s[i-j:i] in words for j in range(1, i+1))
                
        return dp[-1]