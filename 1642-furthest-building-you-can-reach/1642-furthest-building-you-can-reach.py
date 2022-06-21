import heapq as hp
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        q = []
        hp.heapify(q)
        
        for i in range(n-1):
            diff = heights[i+1] - heights[i]
            if diff > 0:
                hp.heappush(q,diff)
            if len(q) > ladders:
                bricks -= hp.heappop(q)
            
            if bricks < 0:
                return i
        return n-1