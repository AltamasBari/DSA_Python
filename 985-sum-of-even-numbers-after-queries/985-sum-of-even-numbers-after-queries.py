class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        sm = 0
        
        for x in nums:
            if x % 2 == 0:
                sm += x
                
        ans = []
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                sm -= nums[idx]
            
            nums[idx] += val
            if nums[idx] % 2 == 0:
                sm += nums[idx]

            ans.append(sm)
        
        return ans