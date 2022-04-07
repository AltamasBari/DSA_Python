class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        
        dp =[[-1 for j in range(n)] for i in range(m)]
        
        def recursion(i,j):
            if (i<0 and j <0):
                return True
            
            if i < 0 and j >= 0:
                for x in range(j+1):
                    if p[x] != '*':
                        return False
                return True
            
            if j < 0 and i >= 0:
                return False
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if(s[i] == p[j] or p[j] == '?'):
                dp[i][j] = recursion(i-1,j-1)
                return dp[i][j]
            
            if(p[j] == '*'):
                dp[i][j] = recursion(i,j-1) or recursion(i-1,j)
                return dp[i][j]
            
            dp[i][j] = False
            return False
        
        return recursion(m-1,n-1)