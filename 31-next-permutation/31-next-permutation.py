class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        peakIdx = 0
        n = len(nums)
        
        for i in reversed(range(1,n)):
            if nums[i-1] < nums[i]:
                peakIdx = i
                break
        
        if peakIdx:
            greaterIdx = peakIdx
            
            for i in reversed(range(peakIdx,n)):
                if nums[i] > nums[peakIdx - 1]:
                    greaterIdx = i
                    break
            
            nums[peakIdx-1],nums[greaterIdx] = nums[greaterIdx],nums[peakIdx-1]
        
        i = peakIdx
        j = n - 1
        while(i < j):
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        
        
        