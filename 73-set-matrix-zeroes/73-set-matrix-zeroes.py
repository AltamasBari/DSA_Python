class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        
        i_set = set()
        j_set = set()
        
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    i_set.add(i)
                    j_set.add(j)
        
        for i in range(n):
            for j in range(m):
                if i in i_set or j in j_set:
                    matrix[i][j] = 0