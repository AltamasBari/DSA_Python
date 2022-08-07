class Solution:
    def countVowelPermutation(self, n: int) -> int:
        M = 1000000007
        d =  {}
        
        def getcount(rem,c):
            
            if(rem == 0):
                return 1
            
            key = "" + str(rem) + str(c)

            if key in d:
                return d[key]

            sm = 0

            if c == 'a':
                sm += getcount(rem-1,'e') % M
            elif c == 'e':
                sm += (getcount(rem-1,'a') + getcount(rem-1,'i'))% M
            elif c == 'i':
                sm += (getcount(rem-1,'a') + getcount(rem-1,'e') + getcount(rem-1,'o') + getcount(rem-1,'u')) % M
            elif c  == 'o':
                sm += (getcount(rem-1,'i') + getcount(rem-1,'u')) % M
            elif c == 'u':
                sm += getcount(rem-1,'a') % M

            d[key] = sm
            return sm
        
        
        total = 0
        char_list = ['a','e','i','o','u']
        for char in char_list:
            total = (total + getcount(n-1,char)) % M
        return total
    
