class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        
        def isIsomorphic(s, t):
            mapS = {}
            mapT = {}

            n = len(s)

            for i in range(n):
                if s[i] not in mapS and t[i] not in mapT:
                    mapS[s[i]] = t[i]
                    mapT[t[i]] = s[i]

                elif mapS.get(s[i]) != t[i] or mapT.get(t[i]) != s[i]:
                    return False

            return True
        
        for word in words:
            if isIsomorphic(pattern,word):
                ans.append(word)
        
        return ans