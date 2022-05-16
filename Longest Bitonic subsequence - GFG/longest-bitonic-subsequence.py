#User function Template for python3

class Solution:
	def LongestBitonicSequence(self, nums):
		# Code here
		'''
		    n = 5
		 1 2 5 3 2
		 0  1  2  3  4
            i    end		 
		'''
		
		n = len(nums)
        dp = [1 for _ in range(n)]
        dp_reverse = [1 for i in range(n)]
        for i in range(n):
            end = n - 1 - i
            for j in range(i):
                prev_end = n - 1 - j
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                
                if nums[end] > nums[prev_end] and dp_reverse[end] < dp_reverse[prev_end] + 1:
                    dp_reverse[end] = dp_reverse[prev_end] + 1
        
        maxm = -1
        for i in range(n):
            maxm = max(dp[i] + dp_reverse[i] - 1,maxm)
                
                
        return maxm

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution()
		ans = ob.LongestBitonicSequence(nums)
		print(ans)
# } Driver Code Ends