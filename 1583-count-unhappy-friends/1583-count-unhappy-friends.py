class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        res = 0
        closest = {}
        for x,y in pairs:
            closest[x] = preferences[x][:preferences[x].index(y)]
            closest[y] = preferences[y][:preferences[y].index(x)]
            
        for c in closest:
            for x in closest[c]:
                if c in closest[x]:
                    res += 1
                    break
        return res