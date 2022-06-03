class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = [-1 * n for n in nums]
        heapq.heapify(nums)
        ds = [-1,-1]
        ds[0] = ds[-1] = heapq.heappop(nums)
        count = 2
        while(nums and count):
            x = heapq.heappop(nums)
            if ds[-1] != x:
                ds[-1] = x
                count -= 1
        
        if count:
            return -ds[0]
        else:
            return -ds[-1]