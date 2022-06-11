#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        i = 0
        j = 0
        sm = 0
        res = 0
        while j < N:
            sm += Arr[j]
            if (j - i + 1) < K:
                j += 1
            elif (j-i+1) == K:
                res = max(res,sm)
                sm -= Arr[i]
                i += 1
                j += 1
        
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