class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        if not intervals:
            return [newInterval]
        
        temp = []        
        n = len(intervals)
        merged = False
        for i in intervals:
            if not merged and newInterval[0] < i[0]:
                temp.append(newInterval)
                merged = True
            
            temp.append(i)
        
        if not merged:
            temp.append(newInterval)
                    
        cur = temp[0]
        out = []
        out.append(cur)
        
        for x in temp:
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
                