#User function Template for python3

class Solution:
    def printUniqueSubset(self, nums):
        # Code here
                
        ans = []
        m = len(nums)
        nums.sort()

        def recursion(idx,ds):

            ans.append(ds.copy())
            
            for i in range(idx,m):
                
                if i > idx and nums[i] == nums[i-1]:
                    continue
                    
                ds.append(nums[i])
                recursion(i+1,ds)
                ds.remove(nums[i])
                    
        recursion(0,[])
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        nums = list(map(int, input().split()))
        ob = Solution()
        res = ob.printUniqueSubset(nums)
        print('[ ', end = '')
        for subset in res:
            print('[ ', end = '')
            for val in subset:
                print(val, end = ' ')
            print(']', end = '')
        print(' ]')
# } Driver Code Ends