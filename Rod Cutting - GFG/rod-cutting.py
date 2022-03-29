#User function Template for python3

class Solution:
    def cutRod(self, price, n):
        #code here
        def recursion(idx,n,mp):
            if idx == 0:
                return n * price[0]
            
            key = str(idx)+"_"+str(n)
            if key in mp:
                return mp[key]
            
            not_take = 0 + recursion(idx-1,n,mp)
            take = float('-inf')
            if idx+1 <= n:
                take = price[idx] + recursion(idx,n-(idx+1),mp)
            
            mp[key] = max(not_take,take)
            return mp[key]
            
        return recursion(n-1,n,{})
#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a, n))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends