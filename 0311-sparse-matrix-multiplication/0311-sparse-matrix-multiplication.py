
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])

        def matrixCompress(mat):
            compressed = [[] for _ in range(len(mat))]
            for row in range(len(mat)):
                for col in range(len(mat[0])):
                    if mat[row][col]:
                        compressed[row].append([mat[row][col], col])
            return compressed


        res = [[0 for j in range(n)] for i in range(m)] 
        A = matrixCompress(mat1)
        B = matrixCompress(mat2)

        for m1_row in range(m):
            for element1, m1_col in A[m1_row]:
                for element2, m2_col in B[m1_col]:
                    res[m1_row][m2_col] += element1 * element2
        return res