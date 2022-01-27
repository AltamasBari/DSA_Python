class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        sets = set()
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '.':
                    continue
                else:
                    s = board[i][j] + ": row" + str(i)
                    t = board[i][j] + ": col" + str(j) 
                    r = board[i][j] + ": sub-box" + str(i//3) + str(j//3)
                    if s in sets or t in sets or r in sets:
                        return False
                    else:
                        sets.add(s)
                        sets.add(t)
                        sets.add(r)
        return True
                
        