#User function Template for python3
mod = 1003
class Solution:
    def countWays(self, N, S):
        # code here
        dp = [[[-1 for _ in range(2)] for _ in range(N)] for _ in range(N)]
        def recursion(i,j,isTrue):
            if i > j:
                return 0
            
            if i == j:
                if(isTrue):
                    return 1 if S[i] == 'T' else 0
                else:
                    return 1 if S[i] == 'F' else 0
            
            if dp[i][j][isTrue] != -1:
                return dp[i][j][isTrue]
            
            ways = 0
            for idx in range(i+1,j,2):
                left_T = recursion(i,idx-1,1) 
                left_F = recursion(i,idx-1,0) 
                right_T = recursion(idx+1,j,1)
                right_F = recursion(idx+1,j,0) 
                
                if S[idx] == '&':
                    if(isTrue):
                        ways = (ways + (left_T * right_T)%mod) % mod
                    else:
                        ways = (ways + (left_F * right_F)%mod + (left_F * right_T)%mod + (left_T * right_F)%mod) %mod
                
                elif S[idx] == '|':
                    if(isTrue):
                        ways = (ways + (left_T * right_T)%mod + (left_T * right_F)%mod + (left_F * right_T)%mod) %mod
                    else:
                        ways = (ways + (left_F * right_F)%mod) %mod
                
                else:
                    if(isTrue):
                        ways = (ways + (left_T * right_F)%mod + (left_F * right_T)%mod) %mod
                    else:
                        ways = (ways + (left_T * right_T)%mod + (left_F * right_F)%mod) %mod
            
            dp[i][j][isTrue] = ways
            return ways
        
        return recursion(0,N-1,1)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        
        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends