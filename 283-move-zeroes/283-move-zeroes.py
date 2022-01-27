class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        for j,x in enumerate(nums):
            if x == 0:
                continue
            else:
                nums[j] = 0
                nums[i] = x
                
                i += 1
        
        return nums
        