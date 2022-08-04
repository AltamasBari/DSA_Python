class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:        
        #Divide p,q by 2 until at least one odd.
        while ((p%2==0) and (q%2==0)):
            p/=2;
            q/=2;

        # both p qnd q cannot be even
        if((p%2)==0 and (q%2)!=0):
            return 2; #when p is even and q is odd
        
        if((p%2)!=0 and (q%2)!=0):
            return 1; # when p is odd and q is odd
        
        return 0;  # when p is odd and q is even