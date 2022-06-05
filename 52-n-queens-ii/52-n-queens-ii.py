class Solution:
    def totalNQueens(self, n: int) -> int:
    # check whether nth queen can be placed in that column
        def valid(nums, lastcol):
            for c in range(lastcol):
                if abs(nums[c] - nums[lastcol]) == lastcol - c:  # same digonal, r - c equal, r1 - r2 = c1 - c2
                    return False
                if nums[c] == nums[lastcol]:  # same column
                    return False
            return True
    
    
    # nums is a one-dimension array, like [1, 3, 0, 2] means
    # first queen is placed in column 1, second queen is placed
    # in column 3, etc.
    
    #index = row number
        def dfs(nums, curRow,res):
            if curRow == n:
                res[0] += 1
                return  # backtracking
            for i in range(n): # i : col number
                nums[curRow] = i
                if valid(nums, curRow):  # pruning   
                    dfs(nums, curRow + 1, res)
        
        res = [0]
        dfs([-1]*n, 0, res)
        return res[0]
