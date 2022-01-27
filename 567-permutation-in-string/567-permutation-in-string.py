class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = {}
        d2 = {}
        
        if len(s1) > len(s2):
            return False
        
        for x in s1:
            d1[x] = d1.get(x,0) + 1
        
        for i in range(len(s1)):
            d2[s2[i]] = d2.get(s2[i],0) + 1
        
        if d1 == d2:
            return True
        else:
            j = 0
            for i in range(len(s1),len(s2)):
                d2[s2[i]] = d2.get(s2[i],0) + 1
                if d2[s2[j]] > 1:
                    d2[s2[j]] -= 1
                else:
                    del d2[s2[j]]
                j += 1
                if d1 == d2:
                    return True
            return False