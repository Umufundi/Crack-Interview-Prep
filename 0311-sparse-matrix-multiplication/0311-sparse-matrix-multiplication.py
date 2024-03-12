class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        mat1_rows = len(mat1) 
        mat1_cols = len(mat1[0])

        mat2_cols = len(mat2[0])

        result = [[0 for _ in range(mat2_cols)] for _ in range(mat1_rows)]

        for i in range(mat1_rows):
            for j in range(mat1_cols):
                if mat1[i][j] != 0:
                    for k in range(mat2_cols):
                        if mat2[j][k] != 0:
                            result[i][k] += mat1[i][j] * mat2[j][k] 
        return result