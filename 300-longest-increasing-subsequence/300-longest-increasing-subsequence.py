class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(1,n):
            for idx in reversed(range(i)):
                if nums[idx] < nums[i]:
                    dp[i] = max(dp[i],dp[idx] + 1)

        return max(dp)