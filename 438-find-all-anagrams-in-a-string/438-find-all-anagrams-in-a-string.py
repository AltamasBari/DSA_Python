class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #s = "cbaebabacd"
        #     0123456789 
        # p = "abc"
        d1 = {}
        d2 = {}
        res = []
        if len(p) > len(s):
            return res
        
        start = 0
        for i in range(len(p)):
            d1[p[i]] = d1.get(p[i],0) + 1
            d2[s[i]] = d2.get(s[i],0) + 1
        
        if d1 == d2:
            res.append(start)

        for i in range(len(p),len(s)):
            if d2[s[start]] == 1:
                  del d2[s[start]]
            else:
                d2[s[start]] -= 1
            d2[s[i]] = d2.get(s[i],0) + 1
            start += 1
            if d1 == d2:
                res.append(start)
        return res
            

        