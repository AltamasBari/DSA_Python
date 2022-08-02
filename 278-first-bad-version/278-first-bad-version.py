# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l = 1
        h = n
        
        while l <= h:
            
            mid = l + (h-l) // 2
            
            if(isBadVersion(mid)):               
                h = mid - 1
            else:
                l = mid + 1
        
        return l
        