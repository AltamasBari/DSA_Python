class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high  = len(nums) 
        while low < high:
            mid = low + (high-low)//2
            if(nums[mid] == target):
                if(mid != 0 and nums[mid-1] == target):
                    high = mid -1
                else:
                    return mid
            elif target > nums[mid]:
                low = mid+1
            else:
                high = mid
        
        return low
        
        
        
"""     x = self.binary_search(nums,target,0,len(nums)-1) 
        return x
        
    def binary_search(self,arr,val,start,end):   
        if start == end:
            if arr[start] >= val:
                return start
            else:
                return start+1

        if start > end:
            return start

        mid = (start+end)//2
        if arr[mid] < val:
            return self.binary_search(arr, val, mid+1, end)
        elif arr[mid] > val:
            return self.binary_search(arr, val, start, mid-1)
        else:
            return mid
"""