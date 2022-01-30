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

        prev = []
        for i in range(rowIndex+1):
            curr = []
            for j in range(i+1):
                if j == 0 or j == i:
                    curr.append(1)
                else:
                    curr.append(prev[j]+prev[j-1])
            prev = curr
        return prev
        
            