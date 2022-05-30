class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #Tabulation
        
        m = len(s)
        n = len(p)
        
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        
        dp[0][0] = True
        
        for i in range(1,m+1):   #if j < 0 and i >= 0: return False -> j == 0 and i > 0
            dp[i][0] = False
        
        
        for j in range(1,n+1):
            flag = True
            for idx in range(1,j+1):
                if p[idx-1] != '*':
                    flag = False
                    break
            dp[0][j] = flag
            
        for i in range(1,m+1):
            for j in range(1,n+1):
                if(s[i-1] == p[j-1] or p[j-1] == '?'):
                    dp[i][j] = dp[i-1][j-1]

                elif(p[j-1] == '*'):
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                
                else:
                    dp[i][j] = False
        
        return dp[m][n]
            
        
        '''
        #recursion memoization
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
        '''