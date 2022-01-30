class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        row_begin = 0
        col_begin = 0
        row_end = n-1
        col_end = n-1
        res = [[0 for i in range(n)] for j in range(n)]
        count = 0
        while (row_begin <= row_end and col_begin <= col_end):
            for i in range(col_begin,col_end+1):
                count += 1
                res[row_begin][i] = count
            row_begin += 1
            for i in range(row_begin,row_end+1):
                count += 1
                res[i][col_end] = count
            col_end -= 1
            if (row_begin <= row_end):
                for i in range(col_end,col_begin-1,-1):
                    count += 1
                    res[row_end][i] = count
                row_end -= 1
            if (col_begin <= col_end):
                for i in range(row_end,row_begin-1,-1):
                    count += 1
                    res[i][col_begin] = count
                col_begin += 1
        return res