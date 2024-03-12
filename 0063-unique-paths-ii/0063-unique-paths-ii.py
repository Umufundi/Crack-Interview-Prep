class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1 for i in range(n)] for j in range(m)]

        def move(r,c):
            if r >=m or c >=n:
                return 0

            if obstacleGrid[r][c] == 1:
                return 0

            if r == m-1 and c == n-1:
                return 1

            if dp[r][c] != -1:
                return dp[r][c]
                
            dp[r][c] = move(r+1,c) + move(r,c+1)
            return dp[r][c]

        return move(0,0)