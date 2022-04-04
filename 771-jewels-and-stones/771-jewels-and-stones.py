class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        cnt = 0
        mp = {}
        
        for ch in jewels:
            mp[ch] = mp.get(ch,0) + 1      
        
        for ch in stones:
            if ch in mp:
                cnt += 1
        
        return cnt