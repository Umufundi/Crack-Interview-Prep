class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
                
        graph = {i:[] for i in range(n)}
        for start, finish, cost in flights:
            graph[start].append((finish,cost))       
        q = deque([(src,0)])
        visited=[-1]*n
        while q and K > -1:
            s=len(q)
            while s > 0:
                city,cost = q.popleft()

                for i,j in graph[city]:
                    if visited[i] == -1 or j+cost < visited[i]:
                        q.append((i,j+cost))
                        visited[i]=j+cost
                s -= 1
            K -= 1
        return visited[dst]