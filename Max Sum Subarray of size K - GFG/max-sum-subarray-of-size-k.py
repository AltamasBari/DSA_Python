#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        i = 0
        j = 0
        sm = 0
        res = 0
        while j < N:
            sm += Arr[j]  #calculation on j only
            
            if (j-i+1) == K: #window size achieved
                res = max(res,sm) 
                sm -= Arr[i] # calculations on i
                i += 1  #increment i  - slide the window : start postn
            
            j += 1  #increment j - slide the window : end postn
        
        return res

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends