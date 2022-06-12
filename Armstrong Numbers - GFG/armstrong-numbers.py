#User function Template for python3

#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        # code here 
        
        # last_digit  = 153 % 10 = 3
         # x ** 3 : cube 
        # n = 153 // 10 = 15
         
        #last_digit = 5
        
        # n = 15 // 10 = 1
        # last_digit = 1
        
        # n = 1 // 10 = 0
        
        original_number  = n # original_number: 153
        sum_cube = 0

        while (n != 0): #1
            last_digit = n % 10 #1
            sum_cube = sum_cube + (last_digit ** 3) 
            n = n // 10 # 0
        
        if original_number == sum_cube:
            return "Yes"
        else:
            return "No"
            

        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends