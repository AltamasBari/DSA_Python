class Solution:
    def addDigits(self, num: int) -> int:
                
        n = num
        sm = 0
        while(n > 0):
            sm = sm + (n % 10)
            n = n // 10
            if (n == 0 and sm > 9):
                n = sm
                sm = 0
        
        return sm
                