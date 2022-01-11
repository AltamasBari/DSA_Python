class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []
        self.recursion(res,temp,n,k)
        return res
    def recursion(self,res,temp,n,k):
        if k == 0:
            res.append(temp.copy())
            return 
        if n == 0:
            return 
        temp.append(n)
        self.recursion(res,temp,n-1,k-1)
        temp.pop()
        self.recursion(res,temp,n-1,k)