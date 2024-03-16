class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        na,nb = len(word1),len(word2)
        if not word1 or not word2:
            return max(na,nb)
        q = deque([(0,0)])
        steps = 0
        seen = set()
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                while i<na and j<nb and word1[i] == word2[j]:
                    i += 1
                    j += 1 
                if i == na and j == nb: return steps
                for da,db in [(0,1),(1,0),(1,1)]:
                    ni,nj = i+da,j+db
                    if ni<=na and nj<=nb and (ni,nj) not in seen:
                        seen.add((ni,nj))
                        q.append((ni,nj))
            steps+=1
        return steps