class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        n=len(graph)
        grp=defaultdict(list)
        for i,g in enumerate(graph):
            for node in g:
                grp[i].append(node)
       
        
        q=[]
        heapq.heappush(q,(0))
        
        visit=set()

        def dfs(node,res):
            
            if node==n-1:
                    ans.append(res)
                   
            for nei in graph[node]:
                    dfs(nei,res+[nei])
            return 
            
        dfs(0,[0])
        return ans 