class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        #O(n*n)
        maxm = 0
        n = len(height)
        for i in range(n):
            temp = 0
            
            left = 0
            while(left >=0 and left < n and left < i and height[left] < height[i]):
                left += 1
            
            if left != i:
                temp += (i - left)*height[i]
                
            right = n - 1
            while (right >= 0 and right < n and right > i and height[right] < height[i]):
                right -= 1
            
            if right != i:
                temp += (right - i)*height[i]

            maxm = max(temp,maxm)
        return maxm
        '''
        maxm = 0
        n = len(height)
        i = 0
        j = n-1
        while i >= 0 and j < n and i < j:
            temp = (j-i) * min(height[i],height[j])
            maxm = max(temp,maxm)
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return maxm
            