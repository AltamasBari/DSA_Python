class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:    
    # check whether nth queen can be placed in that column
        def valid(nums, idx):
            for i in range(idx):
                if abs(nums[i]-nums[idx]) == idx-i or nums[i] == nums[idx]:
                    return False
            return True
    
    
    # nums is a one-dimension array, like [1, 3, 0, 2] means
    # first queen is placed in column 1, second queen is placed
    # in column 3, etc.
    
    #index = row number
        def dfs(nums, index, path, res):
            if index == n:
                res.append(path)
                return  # backtracking
            for i in range(n): # i : col number
                nums[index] = i
                if valid(nums, index):  # pruning
                    tmp = "." * n # temp = "...."   
                    dfs(nums, index+1, path+[tmp[:i]+"Q"+tmp[i+1:]], res)
        
        res = []
        dfs([-1]*n, 0, [], res)
        return res
