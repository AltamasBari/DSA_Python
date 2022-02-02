class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m = len(num1) #2
        n = len(num2) #3
        res = ""
        if n > m:
            num1,num2 = num2,num1
            m,n = n,m
            #num1 = 123 , num2 = 11
            #m = 3, n = 2

        rem = 0
        i = m - 1
        j = n - 1

        while i >=0 or j >=0:
            sm = 0
            if i >= 0:
                sm += int(num1[i]) 
                i -= 1
            if j >= 0:
                sm += int(num2[j])
                j -= 1

            fin = sm + rem
            rem = (fin) // 10
            sm = (fin) % 10 
            

            res += str(sm)
        if rem:
            res += str(rem)
        
        return "".join(reversed(res))