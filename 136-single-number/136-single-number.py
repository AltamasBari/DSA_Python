class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for x in nums:
            dict[x] = dict.get(x,0) + 1;
        for x in dict:
            if dict.get(x) == 1:
                return x