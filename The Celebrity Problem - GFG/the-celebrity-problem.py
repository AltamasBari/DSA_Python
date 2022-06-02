#User function Template for python3

class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        row = len(M)
        col = len(M[0])
        inDegree = [0 for _ in range(n)]
        outDegree = [0 for _ in range(n)]
        
        for i in range(row):
            for j in range(col):
                if M[i][j] == 1:
                    inDegree[j] += 1
                    outDegree[i] += 1
        
        for i in range(n):
            if inDegree[i] == n-1 and outDegree[i] == 0:
                return i
        return -1


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k+=1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m,n))
# } Driver Code Ends