class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = m+n-1
        while i >= 0 and j>=0:
            if nums1[i]>nums2[j]:
                nums1[k]=nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k]=nums2[j]
                j -= 1
                k -= 1
        
        while i>= 0:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        
        
        '''
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                nums1[i],nums2[j] = nums2[j],nums1[i]
                i += 1
                nums2.sort()
        while i < m+n and j < n :
            nums1[i] = nums2[j]
            i += 1
            j += 1
        '''
                
        