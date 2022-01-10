class Solution:
    def fib(self, n: int) -> int:
        #0 1 2 3 4 5
        #0 1 1 2 3 5
        #x y cur
        if n == 0:
            return 0
        if n == 1:
            return 1
        x = 0
        y = 1
        for i in range(2,n+1):
            cur = x + y
            x = y
            y = cur
        return cur