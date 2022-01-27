class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        i,j = 0,0
        mx = 0
         
        while(j < len(s)):
            if s[j] not in d:
                d.add(s[j])
                mx =  max(mx,len(d))
                j += 1 
            else:
                d.remove(s[i])
                i += 1
        return mx
        
                
        