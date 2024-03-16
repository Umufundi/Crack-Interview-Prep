class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        friends_unhappy = set([])
        existing_pairs = {}
        for pair in pairs:
            p1,p2 = pair
            existing_pairs[p1] = p2
            existing_pairs[p2] = p1
        for pair in pairs:
            p1,p2 = pair
            for i in range(preferences[p1].index(p2)-1,-1,-1):
                if preferences[p1][i] in existing_pairs and preferences[preferences[p1][i]].index(p1) < preferences[preferences[p1][i]].index(existing_pairs[preferences[p1][i]]):
                    friends_unhappy.add(p1)
                    break   
            for i in range(preferences[p2].index(p1)-1,-1,-1):
                if preferences[p2][i] in existing_pairs and preferences[preferences[p2][i]].index(p2) < preferences[preferences[p2][i]].index(existing_pairs[preferences[p2][i]]):
                    friends_unhappy.add(p2)
                    break   
        return len(friends_unhappy)