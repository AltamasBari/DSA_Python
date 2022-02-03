class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        mp = {}

        for x in nums3:
            for y in nums4:
                mp[x + y] = mp.get(x+y,0) + 1


        count = 0 
        for a in nums1:
            for b in nums2:
                x = a + b
                if x and -x in mp:
                    count += mp[-x]
                elif x == 0 and x in mp:
                    count += mp[0]
        return count