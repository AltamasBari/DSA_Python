class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        n = len(words)
        words.sort(key = len)
        maxm = -1
        
        def compare(x,y):
            p = len(x)
            q = len(y)
            
            if (p - q) != 1:
                return False
            
            i = 0
            j = 0
            count = 0
            while i < p:
                if j < q and x[i] == y[j]:
                    i += 1
                    j += 1
                else:
                    i += 1
                    count += 1
            
            if count == 1:
                return True
            else:
                return False
        
        
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if((compare(words[i],words[j]) and 1 + dp[j] > dp[i])):
                    dp[i] = 1 + dp[j]
            maxm =  max(maxm,dp[i])
        
        return maxm