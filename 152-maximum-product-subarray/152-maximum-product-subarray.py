class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        [2,3,-2,4]
         0 1  2 3
         
         2 6 -2 4 
         
            f(0)
         
         2,f(1)   ,f(1)
         
         
        
        '''
        max_so_far = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        for i in range(1,len(nums)):
            x = max(nums[i], cur_max*nums[i], cur_min*nums[i])
            y = min(nums[i], cur_max*nums[i], cur_min*nums[i]) 
            cur_max = x
            cur_min = y
            max_so_far = max(cur_max,max_so_far)
        return max_so_far