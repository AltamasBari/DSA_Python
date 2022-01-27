class Solution:
    def firstUniqChar(self, s: str) -> int:
        od = OrderedDict()
        for i,x in enumerate(s):
            if x in od:
                od[x] = -1
            else:
                od[x] = i
        for x in od:
            if od[x] != -1:
                return od[x]
        return -1