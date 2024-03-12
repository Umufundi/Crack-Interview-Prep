class Leaderboard:

    def __init__(self):
        self.scoreboard = collections.defaultdict(int)        

    def addScore(self, playerId: int, score: int) -> None:
        self.scoreboard[playerId] += score
        
    def top(self, K: int) -> int:
        ans = 0
        top_score = sorted(self.scoreboard.values(), reverse=1)
        for i in range(K):
            ans += top_score[i]
        return ans
        
    def reset(self, playerId: int) -> None:
        del self.scoreboard[playerId]
        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)