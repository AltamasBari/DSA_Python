class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        idxs = [0 for _ in range(n)]
        dp = [1 for _ in range(n)]
        nums.sort()
        maxm = -1

        for i in range(n):
            idxs[i] = i
            for j in range(i):
                if nums[i] % nums[j] == 0 and 1 + dp[j] > dp[i]:
                    dp[i] = 1 + dp[j]
                    idxs[i] = j
            if dp[i] > maxm:
                maxm = dp[i]
                bestEnd = i
        ans = []
        ans.append(nums[bestEnd])
        
        while idxs[bestEnd] != bestEnd:
            bestEnd = idxs[bestEnd]
            ans.append(nums[bestEnd])
        
        return ans[::-1]