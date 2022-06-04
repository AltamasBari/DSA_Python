class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d = {}
        m = len(matrix)
        n = len(matrix[0])
        
        for r in range(m):
            for c in range(n):
                if (r-c) in d and d[r-c] != matrix[r][c]:
                    return False
                
                d[r-c] = matrix[r][c]
        
        return True