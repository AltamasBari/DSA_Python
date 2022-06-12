#User function Template for python3

class Solution:
    def nthFibonacci(self, n):
        # code here 
        '''
                                sec_prev prev  cur
        0               1     1    2     3     5 8 13 21 ..........
        
        1st             2nd   3rd  4th  5th       ....nth series
        
        0               1      2    3    4     5  6
        '''
        mod = 1000000007
        second_prev = 0
        prev = 1
        
        
        if n == 1:
            return 0
            
        if n == 2:
            return 1
        
        for i in range(2,n+1): #2,3
            cur = (prev + second_prev) % mod
            
            second_prev  = prev % mod
            prev = cur % mod
        
        return cur % mod
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthFibonacci(n))
# } Driver Code Ends