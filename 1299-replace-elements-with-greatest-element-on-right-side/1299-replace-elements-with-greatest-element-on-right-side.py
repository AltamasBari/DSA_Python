class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        minm = -1
        ans = [-1 for _ in range(n)]
        for i in reversed(range(n-1)):
            minm = max(arr[i+1],minm)
            ans[i] = minm
        return ans
            