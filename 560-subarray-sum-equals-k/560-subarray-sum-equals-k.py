class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        dict = {}
        count = 0
        sm = 0
        dict[sm] = 1
        for x in nums:
            sm += x
            if sm-k in dict:
                count += dict[sm-k]
                            
            dict[sm] = dict.get(sm,0) + 1
        return count
        