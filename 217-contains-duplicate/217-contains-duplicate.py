class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for x in nums:
            dict[x] = dict.get(x,0) + 1
        for y in dict:
            if dict[y] > 1:
                return True
        return False
        