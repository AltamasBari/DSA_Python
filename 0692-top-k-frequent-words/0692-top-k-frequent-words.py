class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        mp = {}
        ans = []
        
        for x in words:
            mp[x] = mp.get(x,0) + 1
            
        
        for key,val in sorted(mp.items(),key = lambda x: (-x[1],x[0])):
            if k:
                ans.append(key)
                k -= 1
            else:
                break
        
        return ans   