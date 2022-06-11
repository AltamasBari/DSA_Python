#User function Template for python3


class Solution:
    def Countpair (self, arr, n, sum) : 
        #Complete the function
        n = len(arr)
        i = 0
        j = n - 1
        count = 0
        while i < j:
            if(arr[i] + arr[j] == sum):
                count += 1
                i += 1
                j -= 1
            elif arr[i] + arr[j] > sum:
                j -= 1 
            else:
                i += 1
        
        count = count if count else -1
        return count

#{ 
#  Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    K = int(input())
    res = Solution().Countpair(arr, n, K)
    print(res)



# } Driver Code Ends