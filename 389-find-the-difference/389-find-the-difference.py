class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mp = {}
        
        for char in s:
            mp[char] = mp.get(char,0) + 1
        
        for char in t:
            if char not in mp:
                return char
            else:
                mp[char] -= 1
                if(mp[char] == 0):
                    del mp[char]