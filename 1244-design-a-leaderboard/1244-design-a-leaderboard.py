from heapq import heappush, heappop
from collections import defaultdict

class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        # maintain k-heap
        h = []
        for score in self.scores.values():
            heappush(h, score)
            if len(h) > K:
                heappop(h)
        return sum(h)

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)