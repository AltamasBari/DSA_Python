class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
              1
             1 1
            1 2 1
           1 3 3 1
          1 4 6 4 1
         1 5 10 10 5 1
        1 6 15 20 15 6 1
        
        '''

        res = []
        for i in range(rowIndex+1):
            temp = []
            for j in range(i+1):
                if j == 0 or j == i:
                    temp.append(1)
                else:
                    temp.append(res[-1][j]+res[-1][j-1])
            res.append(temp)
        return res[-1]
        
            