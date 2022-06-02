class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sm = 0
        n = len(nums)
        ans = [0 for _ in range(n)]
        
        for i in range(n):
            sm += nums[i]
            ans[i] = sm
        
        return ans