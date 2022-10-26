class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        mp = {}
        sm = 0
        mp[sm] = 0
        
        for i in range(n):
            sm += nums[i]
            
            if (sm % k) not in mp:
                mp[sm % k] = i + 1
            
            elif mp[sm % k] < i:
                return True
        
        return False