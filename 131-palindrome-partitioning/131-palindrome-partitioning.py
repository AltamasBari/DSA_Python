class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        n = len(s)
        
        def recursion(idx,ds):
            
            if idx == n:
                ans.append(ds.copy())
                return
            
            for i in range(idx,n):
                left = s[idx:i+1]
                
                if left == left[::-1]:
                    ds.append(left)
                    recursion(i+1,ds)
                    ds.pop()
            
            return
            
        recursion(0,[])
        return ans