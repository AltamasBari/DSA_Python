class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = 0
        mul = 1
        for x in nums:
            if x:
                mul *= x
        
        if 0 in nums:
            for i,x in enumerate(nums):
                if x == 0:
                    count += 1
            if count == 1:
                for i,x in enumerate(nums):
                    if x:
                        nums[i] = 0
                    else:
                        nums[i] = mul
            else:
                return [0]*len(nums)
        else:
            for i,x in enumerate(nums):
                nums[i] = mul//x
        
        return nums