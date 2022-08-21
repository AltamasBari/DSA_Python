class Solution:
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        stamp = list(stamp)
        target = list(target)
        
        m = len(stamp)
        n = len(target)
        
        self.starCount = 0
        vis = [0 for _ in range(n)]
        ans = []
        
        def checkAndReplace(start):
            for i in range(m):
                if target[i+start] != "?" and target[i+start] != stamp[i]:
                    return False
                
            for i in range(m):
                if target[i+start] != "?":
                    target[i+start] = '?'
                    self.starCount += 1
            
            return True
        
        while self.starCount != n:
            isReplaced = False
            
            for i in range(n-m+1):
                if vis[i] == 0 and checkAndReplace(i):
                    vis[i] = 1
                    isReplaced = True
                    ans.append(i)
                    
                if self.starCount == n:
                    break
        
            if not isReplaced:
                return []
        
        return ans[::-1]