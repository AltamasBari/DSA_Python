class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        
        i = 0
        j = 0
        
        sm = 0
        max_sum = 0
        while j < n:
            sm += nums[j]
            
            if nums[j] in d:
                while i < d[nums[j]] + 1:
                    sm -= nums[i]
                    i += 1
            
            d[nums[j]] = j #insert the  nums[j] or update the value
            max_sum = max(max_sum,sm)
            j += 1
        
        return max_sum
        