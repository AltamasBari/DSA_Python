#User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        ans = []
        
        def dfs(i,j,temp):
        
            if i == n-1 and j == n-1 and m[i][j] == 1:
                ans.append("".join(temp))
                return
            
            if i < 0 or j < 0 or i >= n or j >= n or m[i][j] == 0 or m[i][j] == 2:
                return
            

            m[i][j] = 2
            temp += "D"
            dfs(i+1,j,temp)
            temp = temp[:-1]
            
            temp += "R"
            dfs(i,j+1,temp)
            temp = temp[:-1]
            
            temp += "U"
            dfs(i-1,j,temp)
            temp = temp[:-1]
            
            temp += "L"
            dfs(i,j-1,temp)
            temp = temp[:-1]
            
            m[i][j] = 1
            
            return
        
        dfs(0,0,"")
        return (ans)
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        ob = Solution()
        result = ob.findPath(matrix, n[0])
        result.sort()
        if len(result) == 0 :
            print(-1)
        else:
            for x in result:
                print(x,end = " ")
            print()
# } Driver Code Ends