class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums1 = None
        nums2 = None
        c1 = 0
        c2 = 0
        
        for num in nums:
            if num == nums1:
                c1 += 1
            elif num == nums2:
                c2 += 1
            
            elif c1 == 0:
                nums1 = num
                c1 = 1
            
            elif c2 == 0:
                nums2 = num
                c2 = 1
            
            else:
                c1 -= 1
                c2 -= 1
        
        ans = []
        n = len(nums)
        c1 = 0
        c2 = 0
        for num in nums:
            if num == nums1:
                c1 += 1
            elif num == nums2:
                c2 += 1
        if c1 > n//3:
            ans.append(nums1)
        if c2 > n//3:
            ans.append(nums2)    
        
        return ans
        