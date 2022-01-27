class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for x in magazine:
            dict[x] = dict.get(x,0) + 1
        for x in ransomNote:
            if x not in dict:
                return False
            else:
                dict[x] -= 1
            if dict[x] < 0:
                return False
        return True
