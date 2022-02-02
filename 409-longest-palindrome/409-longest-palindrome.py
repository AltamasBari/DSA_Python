class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for x in s:
            d[x] = d.get(x,0) + 1
        
        count = 0 
        for x in d:
            if d[x] > 1:
                count += ((d[x]//2)*2)
                
        if count % 2 == 0 and count < len(s):
            return count + 1
        else:
            return count