class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: (x[0],-x[1]))
        prev = intervals[0]
        n = len(intervals)
        for i in range(1,len(intervals)):
            curr = intervals[i]
            a,b = prev[0],prev[1]
            c,d = curr[0],curr[1]
            if c >= a and b >= d:
                n -= 1
                prev = [a,b]
            else:
                prev = curr
        
        return n