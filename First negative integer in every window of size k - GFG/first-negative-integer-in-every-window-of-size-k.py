#User function Template for python3
import collections
def printFirstNegativeInteger( A, N, K):
    # code here
    i = 0
    j = 0
    
    q = collections.deque()
    ans = []
    
    while j < N:
        if A[j] < 0:
            q.append(A[j])
            
        if (j - i + 1) == K:
            if q:
                ans.append(q[0])
                if q[0] == A[i]:
                    q.popleft()
            else:
                ans.append(0)
            i += 1
        
        j += 1
    
    return ans
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends