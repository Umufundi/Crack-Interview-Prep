class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def divide(x, y, visited):
            if x == y: # find the last node, then return 1.0
                return 1.0
            visited.add(x)
            for n in graph[x]:
                if n not in visited:
                    visited.add(n)
                    d = divide(n, y, visited)
                    if d > 0:
                        # return the weighted edge multiply
                        return d * graph[x][n] 
            return -1.0

        graph = defaultdict(dict)
        # zip can take multiple iterable objects
        # iterate x, y in equations, value in values
        for (x, y), value in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1.0 / value
        
        ans = []
        for x, y in queries:
            if x in graph and y in graph:
                ans.append(divide(x, y, set()))
            else:
                ans.append(-1.0)
        
        return ans
        