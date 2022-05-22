class Solution:
    def minCut(self, s: str) -> int:
        #tabultion
        n = len(s)    
        dp = [0 for _ in range(n+1)]
        
        @functools.lru_cache(maxsize=None)
        def isPalindrome(i,j):
            if i > j:
                return True

            if s[i] != s[j]:
                return False
            return isPalindrome(i+1,j-1)

        for i in reversed(range(n)):
            min_cost = float('inf')
            for j in range(i,n):
                if(isPalindrome(i,j)):
                    cost = 1 + dp[j+1]
                    min_cost = min(min_cost,cost)

            dp[i] = min_cost
            
        return dp[0] - 1 
        
        '''
        #memoization tle
        n = len(s)    
        dp = [-1 for _ in range(n)]
        #racecar
        #i     j
        def isPalindrome(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        def recursion(i):
            if i == n:
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            min_cost = float('inf')
            for j in range(i,n):
                if(isPalindrome(i,j)):
                    cost = 1 + recursion(j+1)
                    min_cost = min(min_cost,cost)
            
            dp[i] = min_cost
            return min_cost
            
            
        return recursion(0) - 1 # A|B|C| extra partition at end so -1
        '''