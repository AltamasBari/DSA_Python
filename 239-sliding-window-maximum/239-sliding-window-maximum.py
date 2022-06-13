class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        q = collections.deque([])
        i = 0
        j = 0
        
        while j < n:
            
            while q and q[-1] < nums[j]: 
            # q in decreasing order [7 4 3 1] and now we encounter 5,
            # other value less than 5 or equal to , are of no use in future
                q.pop()
            q.append(nums[j])

            if (j-i+1) == k:
                ans.append(q[0])
                if q[0] == nums[i]:
                    q.popleft()
                i += 1
                
            j += 1
        
        return ans