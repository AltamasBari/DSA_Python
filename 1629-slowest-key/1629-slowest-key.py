class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        n = len(releaseTimes)
        maxm = releaseTimes[0]
        c = keysPressed[0]
        
        for i in range(1,n):
            diff = releaseTimes[i] - releaseTimes[i-1]
            if diff > maxm:
                maxm = diff
                c = keysPressed[i]
            if diff == maxm:
                maxm = diff
                if keysPressed[i] > c:
                    c = keysPressed[i]
        
        return c