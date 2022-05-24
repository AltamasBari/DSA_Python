# User function Template for Python3
import collections
class Solution:
    def leftSmaller(self, n, a):
        # code here
        stack = collections.deque([])
        ans = [-1 for _ in range(n)]
        
        for i in range(n):
            while stack and stack[-1] >= a[i]:
                stack.pop()
            
            if stack:
                ans[i] = stack[-1]
            
            stack.append(a[i])
        
        return ans

#{ 
#  Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        for i in range(n):
            a[i] = int(a[i])
        
        ob = Solution()
        ans = ob.leftSmaller(n, a)
        for u in(ans):
            print(u,end = " ")
        print()
# } Driver Code Ends