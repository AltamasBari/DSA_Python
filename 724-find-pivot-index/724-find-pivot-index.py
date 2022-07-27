class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        
        cumm_sum = 0
        for i in range(n):
            cumm_sum += nums[i]
        
        sm = 0
        for i in range(n):
            cumm_sum -= nums[i]
            if sm == cumm_sum:
                return i
            sm += nums[i]
        return -1