class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        lst = [[0]]
        
        for i in range(1,numRows+1):
            temp = []
            for j in range(i):
                if j == 0:
                    temp.append(1)
                    continue
                if j != i-1:
                    temp.append(lst[i-1][j] + lst[i-1][j-1])
                    continue
                if j == i-1:
                    temp.append(1)
            lst.append(temp)
        
        return lst[1:]
                