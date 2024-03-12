class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        if not mat1 or not mat2:
            return []
        ma, na = len(mat1), len(mat1[0])
        mb, nb = len(mat2), len(mat2[0])
        res = [ [0]*nb for i in range(ma) ]
        pa, pb = [], []
        for i in range(ma):
            for j in range(na):
                if mat1[i][j] != 0:
                    pa.append((i, j, mat1[i][j]))
        for i in range(mb):
            for j in range(nb):
                if mat2[i][j] != 0:
                    pb.append((i, j, mat2[i][j]))
        for i, j, v1 in pa:
            for k, l, v2 in pb:
                if j == k:
                    res[i][l] += v1 * v2
        return res 