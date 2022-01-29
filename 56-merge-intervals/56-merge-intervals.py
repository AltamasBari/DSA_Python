class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if(len(intervals) <= 1):
            return intervals
        
        intervals.sort(key = lambda y:y[0])
        
        cur = intervals[0]
        out = []
        out.append(cur)
        
        for x in intervals:
            cur_beg = cur[0]
            cur_end = cur[1]
            nex_beg = x[0]
            nex_end = x[1]
            
            if(cur_end >= nex_beg):
                cur[1] = max(cur_end,nex_end)
            else:
                cur = x
                out.append(x)
        
        return out
            