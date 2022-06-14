#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, A, N, K) : 
        #Complete the function

        d = {}
        cumm_sm = 0
        d[cumm_sm] = 0
        
        max_len = 0
        
        for i in range(N):
            cumm_sm += A[i]
            
            if (cumm_sm - K) in d:
                max_len = max(max_len, i + 1 - d[cumm_sm - K] )
                            
            if cumm_sm not in d:
                d[cumm_sm] = i + 1
        
        return max_len


#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, K = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, K))




# } Driver Code Ends