class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        mp = {}
        n = len(arr)
        
        for x in arr:
            mp[x] = mp.get(x,0) + 1
        
        ans = 0
        freq = 0
        for key,val in (sorted(mp.items(), key = lambda x:(x[1], x[0]),reverse=True)):
            freq += val
            ans += 1
            if freq >= n//2:
                return ans
        
        