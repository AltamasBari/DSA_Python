class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        #TC: O(m*n)
        #SC: O(1) 
        m = len(matrix)
        n = len(matrix[0])
        for r in range(m-1):
            for c in range(n-1):
                if r+1 < m and c+1 < n and matrix[r][c] != matrix[r+1][c+1] :
                    return False

        return True
        '''
        TC: O(m*n)
        SC: O(n+2) : n col(n diag) + 2 corner
        d = {}
        m = len(matrix)
        n = len(matrix[0])
        
        for r in range(m):
            for c in range(n):
                if (r-c) in d and d[r-c] != matrix[r][c]:
                    return False
                
                d[r-c] = matrix[r][c]
        
        return True
        '''