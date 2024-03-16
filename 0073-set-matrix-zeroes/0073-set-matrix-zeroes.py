class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        arrI, arrJ = [], []
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    arrI.append(i)
                    arrJ.append(j)
        for i in range(rows):
            for j in range(cols):
                if(i in arrI or j in arrJ):
                    matrix[i][j] = 0