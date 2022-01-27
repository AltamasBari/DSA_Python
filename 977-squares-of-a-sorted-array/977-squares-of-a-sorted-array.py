class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        low = 0
        high = len(nums) - 1
        res = [0] * len(nums)
        for p in reversed(range(len(nums))):
            if(abs(nums[low]) > abs(nums[high])):
                res[p] = nums[low] * nums[low]
                low += 1
            else:
                res[p] = nums[high] * nums[high]
                high -= 1
        return res