class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        mod = 10**9 + 7
        def threeSum(nums: List[int],target) -> List[List[int]]:
            nums.sort()
            final = 0
            for i,x in enumerate(nums[0:len(nums)-2]):
                tar = target - x
                final = (final + twoSum(nums[i+1:],tar))%mod

            return final%mod

        def twoSum(nums: List[int], target: int) -> List[int]:
            dict = {}
            res = 0
            for i,x in enumerate(nums):
                if target-x in dict:
                    res = (res + dict[target-x])%mod
                dict[x] = dict.get(x,0) + 1

            return res%mod
        
        return threeSum(arr,target)