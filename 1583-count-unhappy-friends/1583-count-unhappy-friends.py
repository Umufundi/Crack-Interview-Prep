class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        ranks = {}
        for person, pref in enumerate(preferences):
            ranks[person] = defaultdict(lambda: n)
            for rank, peer in enumerate(pref):
                ranks[person][peer] = rank
        partner = {}        
        for p1, p2 in pairs:
            partner[p1] = p2
            partner[p2] = p1
        ans = 0
        for p1, p2 in pairs:
            for peer in preferences[p1]:
                if (ranks[p1][peer] < ranks[p1][p2] and
                    ranks[peer][p1] < ranks[peer][partner[peer]]):
                    ans += 1
                    break
            for peer in preferences[p2]:
                if (ranks[p2][peer] < ranks[p2][p1] and
                    ranks[peer][p2] < ranks[peer][partner[peer]]):
                    ans += 1
                    break
        return ans 