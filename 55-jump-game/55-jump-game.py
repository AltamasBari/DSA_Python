class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
         [2,3,1,  1,  4]
          0 1 2   3   4
          
                f(0)-->2
              f(1)          f(2)  
            f(2) f(3) f(4)
           f(3) 
           f(4)
           
           f(0):
            if num[i]==0:
                
            for 0 to num[i]:
               if( f(i+1) == true)
                return
            
            5
            0 1 2 3 4
            3
            0 1 2
            
            
            i + nums[i]
            4
            0 1 2 3
        
        '''
        '''
        n = len(nums) 
        dp = [-1 for _ in range(n)]
        #[-1 -1 -1  -1 -1]
        # 0   1  2   3  4
        def recursion(i):
            if i >= n - 1:
                dp[i] = True
                return True

            if dp[i] != -1:
                return dp[i]
            for j in range(i+1,i+nums[i]+1):
                dp[j] = recursion(j)
                if(dp[j]):
                    return True
            dp[i] = False
            return False
        
        return recursion(0)
        '''
        n = len(nums)
        dp = [-1 for _ in range(n)]
        dp[n-1] = True
        for i in reversed(range(len(nums)-1)):
            for j in range(i+1,i+nums[i]+1):
                if(dp[j]):
                    dp[i] = True
                    break
            else:
                dp[i] = False
        return dp[0]
        
        
        '''
        last = len(nums)-1
        for i in reversed(range(len(nums)-1)):
            if (i + nums[i]) >= last:
                    last = i
        return last == 0	
        '''