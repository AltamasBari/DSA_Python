class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
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