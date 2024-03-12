class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        def dfs(node,cur):
            if node == n - 1:
                res.append(cur)
            for a in graph[node]:
                dfs(a, cur+[a])
        dfs(0,[0])
        return res