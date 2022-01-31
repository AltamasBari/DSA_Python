class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
                
        if(len(intervals) <= 1):
            return 0
        
        intervals.sort(key = lambda y:y[1])
        
        end = float('-inf')
        count = 0
        for s,e in intervals:            
            if(s >= end):
                end = e
            else:
                count += 1
        return count