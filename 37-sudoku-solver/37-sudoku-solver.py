class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        
        def isRow(val,i,j):
            for col in range(9):
                if board[i][col] == str(val):
                    return False
            return True
            
        def isCol(val,i,j):
            for row in range(9):
                if board[row][j] == str(val):
                    return False
            return True
            
        def isSub(val,i,j):
            start = 3 * (i//3)
            end = 3 * (j//3)
            for row in range(start,start+3):
                for col in range(end,end+3):
                    if board[row][col] == str(val):
                        return False
            
            return True
        
        
        def isValid(val,i,j):
            return isRow(val,i,j) and isCol(val,i,j) and isSub(val,i,j)
        
        def recursion(i,j):
            
            if i == m:   #end of board
                return True
            
            if j == n - 1: # end of a row, last column , move to next row, start from first col
                next_i = i + 1
                next_j = 0
            else:           # not the end, move to next col
                next_i = i 
                next_j = j + 1
                
            
            if board[i][j] != ".": # cell already filled
                return recursion(next_i,next_j) # move ahead
            
            else: #not filled
                for val in range(1,10): # 1 to 9
                    if(isValid(val,i,j)):
                        board[i][j] = str(val)          #update
                        if(recursion(next_i,next_j)):   #able to fill cell correctly
                            return True
                        else:
                            board[i][j] = '.'           #backtrack, restore previous value
        
        
        recursion(0,0)