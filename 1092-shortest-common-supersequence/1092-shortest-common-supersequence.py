class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        dp =[[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        ans = ""
        i = m
        j = n
        while(i > 0 and j > 0):
            if(str1[i-1] == str2[j-1]):
                ans += str1[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]: # up
                    ans += str1[i-1]
                    i -= 1
                else: #left
                    ans += str2[j-1]
                    j -= 1
        while(i):
            ans += str1[i-1]
            i -= 1
        while(j):
            ans += str2[j-1]
            j -= 1
        
        return ans[::-1]