class Solution:
    def addDigits(self, num: int) -> int:
                
        n = num

        while(n > 9):
            sm = 0
            while (n):
                sm = sm + (n % 10)
                n = n // 10
            n = sm
        
        return n
                