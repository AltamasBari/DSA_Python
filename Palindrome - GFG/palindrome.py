#User function Template for python3

class Solution:
	def is_palindrome(self, n):
		# Code here
        '''
        123 == 321 No
        
        555 == 555 Yes
        
        
        123 = 12*10 + 3 #     10 * remaining_num + last_digit
        '''
        
        original_number = n # 555
         
        rev = 0 # 0

        while (n != 0):  # 5
            last_digit = n % 10  # 5
            rev = rev * 10 + last_digit
            #rev = 55 * 10 + 5 # 555
            n = n // 10  #0
        
        if original_number == rev:
            return "Yes"
        else:
            return "No"
        
        
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_palindrome(n)
		print(ans)
# } Driver Code Ends