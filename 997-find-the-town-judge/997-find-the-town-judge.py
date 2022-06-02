class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDegree = [0 for _ in range(n+1)]
        outDegree = [0 for _ in range(n+1)]
        
        for x,y in trust:
            inDegree[y] += 1
            outDegree[x] += 1
        
        for i in range(1,n+1):
            if inDegree[i] == n-1 and outDegree[i] == 0:
                return i
        return -1