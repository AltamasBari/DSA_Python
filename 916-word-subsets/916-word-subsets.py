class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        mapWord2 = {}
        
        for s in words2:
            temp = {}
            for ch in s:
                temp[ch] = temp.get(ch,0) + 1
                mapWord2[ch] = max(temp[ch],mapWord2.get(ch,0))
        
        def check(word1):
            mapWord1 = {}
            
            for ch in word1:
                mapWord1[ch] = mapWord1.get(ch,0) + 1
            
            for key,value in mapWord2.items():
                if key not in mapWord1:
                    return False
                else:
                    if mapWord1[key] < value:
                        return False
            return True
        
        
        ans = []
        for word1 in words1:
            if check(word1):
                ans.append(word1)
        
        return ans