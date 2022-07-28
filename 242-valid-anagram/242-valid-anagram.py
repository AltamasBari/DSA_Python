class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0 for _ in range(26)]
        
        for x in s:
            arr[ord(x)-ord('a')] += 1
        
        for x in t:
            if arr[ord(x)-ord('a')]:
                arr[ord(x)-ord('a')] -= 1
            else:
                return False
        
        for x in arr:
            if x != 0:
                return False
        return True