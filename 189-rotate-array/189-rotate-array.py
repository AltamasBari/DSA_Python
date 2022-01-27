class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums.reverse()
        start = 0
        end = k - 1
        
        while (start < end):
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1
        
        start = k
        end = len(nums) - 1
        
        while (start < end):
            nums[start],nums[end] = nums[end],nums[start]
            start += 1
            end -= 1