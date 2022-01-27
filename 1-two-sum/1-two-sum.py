class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i,x in enumerate(nums):
            if target-x in dict:
                return [dict[target-x],i]
            dict[x] = i