class Solution:
    def rotate(self, mat: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(mat)
        for i in range(n):
            for j in range(i):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
        
        for r in range(n):
            i, j = 0, n-1
            while i<=j:
                mat[r][i], mat[r][j] = mat[r][j], mat[r][i]
                i+=1
                j-=1