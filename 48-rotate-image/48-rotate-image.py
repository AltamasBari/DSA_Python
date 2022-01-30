class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
            0 1 2 
        0 [[1,2,3]
        1  [4,5,6]
        2  [7,8,9]]
        '''
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        '''
           0  1  2        
        0 [1, 4, 7]
        1 [2, 5, 8]
        2 [3, 6, 9]]
        '''
        for i in range(m):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-1-j] = matrix[i][n-1-j],matrix[i][j]
        return matrix