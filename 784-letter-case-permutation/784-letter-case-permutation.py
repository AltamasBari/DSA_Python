class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:                
        res = []
        self.backtrack("",0,s,res)
        return res
    
    def backtrack(self,sub, i,s,res):
        if len(sub) == len(s):
            res.append(sub)
        else:
            if s[i].isalpha():
                self.backtrack(sub + s[i].swapcase(), i + 1,s,res)
            self.backtrack(sub + s[i], i + 1,s,res)