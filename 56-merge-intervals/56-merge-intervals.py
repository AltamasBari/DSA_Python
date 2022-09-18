class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if(len(intervals) <= 1):
            return intervals
        
        intervals.sort(key = lambda y:y[0])
        
        out = []
        out.append(intervals[0])
        
        for x in intervals:
            cur_beg = out[-1][0]
            cur_end = out[-1][1]
            nex_beg = x[0]
            nex_end = x[1]
            
            if(cur_end >= nex_beg):
                out[-1][1] = max(cur_end,nex_end)
            else:
                out.append(x)
        
        return out
            