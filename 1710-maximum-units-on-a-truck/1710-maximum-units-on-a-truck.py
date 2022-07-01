class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: [-x[1],-x[0]])
        ans = 0
        
        for nBox, nUnit in boxTypes:            
            if truckSize <= 0:
                return ans
            
            if nBox <= truckSize:
                ans += (nBox * nUnit)
                truckSize -= nBox
            
            else:
                ans += (truckSize * nUnit)
                truckSize = 0
        
        return ans