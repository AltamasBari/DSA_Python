class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [0 for _ in range(n)]
        sm = 0
        for i in reversed(range(n)):
            sm += nums[i]
            temp[i] = sm
        
        sm = 0
        for i in range(n):
            if i != n-1 and sm == temp[i+1]:
                return i
            if i == n-1 and sm == 0:
                return i
            sm += nums[i]
        return -1