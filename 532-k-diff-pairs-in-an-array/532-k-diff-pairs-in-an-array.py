class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        res = 0
        mp = {}
        
        for x in nums:
            mp[x] = mp.get(x,0) + 1

        for key in mp:
            if k > 0 and key + k in mp or k == 0 and mp[key] > 1:
                res += 1
        return res