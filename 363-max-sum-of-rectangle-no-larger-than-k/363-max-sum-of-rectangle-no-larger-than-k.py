class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        row = len(matrix)
        col = len(matrix[0])
        
        res = -math.inf
        
        for i in range(row):
            colsum = [0] * col
            for j in range(i,row):
                for c in range(col):
                    colsum[c] += matrix[j][c]
                res = max(res,self.maxrowsum(colsum,k))
        
        return res
    def maxrowsum(self,arr,k):
        cur_sum = 0
        max_so_far = -math.inf
        sum_set = [0]
        
        for i in range(len(arr)):
            cur_sum += arr[i]
            it = bisect.bisect_left(sum_set,cur_sum - k)
            if(it != len(sum_set)):
                max_so_far = max(max_so_far,cur_sum - sum_set[it])
            insort(sum_set,cur_sum)
            
        return max_so_far
        
        