class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        data = []
        for i in range(n):
            data.append([efficiency[i],speed[i]])
            
        data.sort(key = lambda x: (-x[0],x[1]))
        minHeap = []
        totalSpeed = 0
        maxm = 0
        for eff, spd in data:
            heappush(minHeap, spd)
            if len(minHeap) <= k: 
                totalSpeed += spd
            else:
                totalSpeed += spd - heappop(minHeap)
                
            maxm = max(maxm, totalSpeed * eff)
        
        return maxm % 1000000007