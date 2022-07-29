class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def recursion(idx):
            if idx == n:
                res.append(nums.copy())
                return
            s = set()
            for i in range(idx,n):
                if nums[i] not in s:
                    nums[idx],nums[i] = nums[i],nums[idx]
                    recursion(idx+1)
                    nums[idx],nums[i] = nums[i],nums[idx]
                    s.add(nums[i])
                    
        recursion(0)
        return res