class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        pointer = 1
        for i in range(2,len(nums)):
            if nums[i] != nums[pointer-1]:
                pointer += 1
                nums[pointer] = nums[i]
        return pointer + 1  