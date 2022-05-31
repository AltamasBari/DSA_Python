class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def recursion(opn,close,temp):
            if opn == close == n:
                ans.append(temp)
                return
            
            if(opn < n):
                recursion(opn+1,close,temp + "(")
            
            if(opn > close):
                recursion(opn,close+1,temp + ")")
                
            return
        
        recursion(0,0,"")
        return ans