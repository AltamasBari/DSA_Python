class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        #O(rows * log (columns))
        for row in matrix:
            low = 0
            high = len(row) - 1
            if target >= row[0] and target <= row[-1]:
                while low <= high:
                    mid =  (low + high)//2
                    if row[mid] > target:
                        high = mid - 1
                    elif row[mid] < target:
                        low = mid + 1
                    elif row[mid] == target:
                        return True
        return False
        '''
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        j = m - 1
        while(i >= 0 and i < n and j >= 0 and j < m):
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False