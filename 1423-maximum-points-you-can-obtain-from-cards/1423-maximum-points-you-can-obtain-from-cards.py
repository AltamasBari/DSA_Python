class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        size = n - k if n - k != 0 else n
        
        i = 0
        j = 0
        sm = 0
        res = float('inf')
        
        while j < n:
            sm += cardPoints[j]  #calculation on j only
            
            if (j-i+1) == size: #window size achieved
                res = min(res,sm) 
                sm -= cardPoints[i] # calculations on i
                i += 1  #increment i  - slide the window : start postn
            
            j += 1  #increment j - slide the window : end postn
        
        return sum(cardPoints) - res if sum(cardPoints) - res != 0 else sum(cardPoints)