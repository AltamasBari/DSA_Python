class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        cnt = [1 for _ in range(n)]
        maxm = -1
        for i in range(n):
            for j in range(i):
                if(nums[i] > nums[j] and 1 + dp[j] > dp[i]):
                    dp[i] = 1 + dp[j]
                    cnt[i] = cnt[j]
                elif(nums[i] > nums[j] and 1 + dp[j] == dp[i]):
                    cnt[i] += cnt[j]
            if dp[i] > maxm:
                maxm = dp[i]
        
        ans = 0
        for i in range(n):
            if dp[i] == maxm:
                ans += cnt[i]
                    
        return ans