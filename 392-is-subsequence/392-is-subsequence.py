class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        
        if n > m:
            return False
        
        if not s:
            return True
        
        i = 0
        j = 0
        
        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
            
            if i == n:
                return True
            j += 1
            
        return False