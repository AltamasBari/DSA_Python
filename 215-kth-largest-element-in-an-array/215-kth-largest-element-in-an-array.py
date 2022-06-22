import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-x for x in nums]
        hq.heapify(nums)
        
        
        while k-1:
            hq.heappop(nums)
            k -= 1
        
        return -hq.heappop(nums)