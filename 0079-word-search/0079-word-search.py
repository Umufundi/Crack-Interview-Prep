class Solution:
    res = [False]
    def exist(self, board: List[List[str]], word: str) -> bool:
        # res = [False]
        if word[0]*(len(word)//2)==word[:(len(word)//2)]:
            word=word[::-1]
        

        characters=[]
        directs = [[-1,0],[1,0],[0,-1],[0,1]]
        def dfs(i,j,idx):
            if idx==len(word):
                # print('enter')
                self.res = [True]
                return
            if self.res==[True]:
                return
            c = board[i][j]
            board[i][j]='.'
            for x,y in directs:
                newI,newJ = i+x, j+y
                if 0<=newI<m and 0<=newJ<n and board[newI][newJ]==word[idx] and board[newI][newJ]!='.':
                    dfs(newI,newJ,idx+1)
            board[i][j]=c
            
        m = len(board)
        n = len(board[0])
        c = word[0]
        for i in range(m):
            for j in range(n):
                c1 = board[i][j]
                if c == c1:
                    dfs(i,j, 1)

        return self.res[0]