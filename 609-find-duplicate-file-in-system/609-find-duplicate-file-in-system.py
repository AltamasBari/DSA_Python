class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        mp = defaultdict(list)
        
        for path in paths:
            files = path.split(" ")
            root = files[0]
            
            for i in range(1,len(files)):
                idx = files[i].index("(")
                
                key = files[i][idx:]
                value = files[i][:idx]
                

                mp[key].append(root+ "/" + value)
        
        ans = []
        for value in mp.values():
            if len(value) > 1:
                ans.append(value)
        
        return ans