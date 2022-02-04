class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        c = 0
        mp = {0:-1}
        mx = 0
        for i, x in enumerate(nums):
            if x == 0:
                c += 1
            elif x == 1:
                c -= 1
            
            if c in mp:
                mx = max(i-mp[c],mx)
            else:
                mp[c] = i
        return mx