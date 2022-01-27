class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2,nums1
        
        for x in nums1:
            dict[x] = dict.get(x,0) + 1
        res = []
        for x in nums2:
            if x in dict and dict[x]:
                dict[x] -= 1
                res.append(x)
        return res