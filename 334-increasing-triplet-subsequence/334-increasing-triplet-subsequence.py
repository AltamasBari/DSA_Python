class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = b = float('inf')
        for x in nums:
            if x <= a:
                a = x
            elif x <= b:
                b = x
            else:
                return True
        return False