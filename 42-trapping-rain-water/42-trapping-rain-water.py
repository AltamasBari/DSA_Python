class Solution:
    def trap(self, height: List[int]) -> int:
        #using two pointers
        n = len(height)
        left = 0
        right = n - 1
        
        left_max, right_max = 0, 0
        ans = 0
        while (left <= right):
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += (left_max - height[left])
                left += 1
            else: 
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += (right_max - height[right]);
                right -= 1
        return ans
        
        '''
        #TC -> O(2N) , SC -> O(N)
        n = len(height)
        maxm = float('-inf')
        temp = [0 for _ in range(n)]
        
        for i in range(n):
            maxm = max(maxm,height[i])
            temp[i] = maxm
        
        ans = 0
        maxm = float('-inf')
        for i in reversed(range(n)):
            maxm = max(maxm,height[i])
            temp[i] = min(maxm,temp[i])
            ans += (temp[i] - height[i])
            
        return ans
        '''
        