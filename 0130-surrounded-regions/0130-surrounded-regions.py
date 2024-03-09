class Solution:
    def solve(self, board: List[List[str]]) -> None:
            def dfs(sv):
                a,b=sv[0],sv[1]
                board[a][b]='Y'
                for r,c in [(a-1,b),(a+1,b),(a,b-1),(a,b+1)]:
                    if 0<=r<m and 0<=c<n and board[r][c]=='O':
                        board[r][c]="Y"
                        dfs((r,c))
            m=len(board)
            n=len(board[0])
            for i in range(m):
                for j in range(n):
                    if i==0 or i==m-1 or j==0 or j==n-1:
                        if board[i][j]=='O':
                            dfs((i,j))
            for i in range(m):
                for j in range(n):
                    if board[i][j]=='O':
                        board[i][j]='X'
                    elif board[i][j]=='Y':
                        board[i][j]='O'