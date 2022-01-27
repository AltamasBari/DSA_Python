class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if(m*n != r*c):
            return mat
        
        arr = []
        for i in range(m):
            for j in range(n):
                arr.append(mat[i][j])
        
        res = []
        x = 0
        while(r):
            res.append(arr[x:x+c])
            x = x + c
            r -= 1
        return res