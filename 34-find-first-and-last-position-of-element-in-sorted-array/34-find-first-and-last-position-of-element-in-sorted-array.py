class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        n = len(nums)
        l = 0
        h = n - 1
        
        while(l <= h):
            mid = (l + h)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                ans[0] = mid
                h = mid - 1
        l = 0
        h = n - 1
        while(l <= h):
            mid = (l + h)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                h = mid - 1
            else:
                ans[1] = mid
                l = mid + 1
        return ans