class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pt_0 = 0
        pt_1 = 0
        pt_2 = len(nums) - 1
        
        while pt_1 <= pt_2:
            if(nums[pt_1] == 0):
                nums[pt_0],nums[pt_1] = nums[pt_1],nums[pt_0]
                pt_1 += 1
                pt_0 += 1
            elif(nums[pt_1] == 1):
                pt_1 += 1
            elif(nums[pt_1] == 2):
                nums[pt_1],nums[pt_2] = nums[pt_2],nums[pt_1]
                pt_2 -= 1
        
        
        return nums