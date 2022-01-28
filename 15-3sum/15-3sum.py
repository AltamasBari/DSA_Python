class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        for i,x in enumerate(nums[0:len(nums)-2]):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            tar = -(x)
            subres = self.twoSum(nums[i+1:],tar)

            for lst in subres:
                lst.append(x)
                final.append(lst)

        return final
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        res = []
        for i,x in enumerate(nums):
            if target-x in dict:
                res.append([target-x,x])
            dict[x] = i
        res = [list(item) for item in set(tuple(row) for row in res)]
        return res