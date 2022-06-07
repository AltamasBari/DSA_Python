class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def sorted(self, s):
        # Code here
        if len(s) == 1:
            return
        
        temp = s.pop()
        self.sorted(s)
        self.insert(s,temp)
        
        return
    
    def insert(self,s,temp):
        if len(s) == 0 or s[-1] <= temp:
            s.append(temp)
            return
        v = s.pop()
        self.insert(s,temp)
        s.append(v)
        
    

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.sorted(arr)
        for e in range(len(arr)):
            print(arr.pop(), end=" ")
        print()


# } Driver Code Ends