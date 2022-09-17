class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        lookup = {w:i for i,w in enumerate(words)}
        res = []
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                pre, pos = w[:j], w[j:]
                if pre==pre[::-1] and pos[::-1] != w \
                    and pos[::-1] in lookup:
                        res.append([lookup[pos[::-1]], i])
                if j != len(w) and pos==pos[::-1] \
                    and pre[::-1] != w and pre[::-1] in lookup:
                        res.append([i, lookup[pre[::-1]]])
        return res