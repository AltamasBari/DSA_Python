class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        R = bisect.bisect_left(arr, x)
        L = R - 1
        while k:
            if(R >= n or L >= 0 and x - arr[L] <= arr[R] - x):
                L -= 1
            else:
                R += 1
            k -= 1
        return arr[L + 1: R]