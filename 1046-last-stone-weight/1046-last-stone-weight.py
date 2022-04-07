class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones.sort()
        while stones:
            s1 = stones.pop()  # the heaviest stone
            if not stones:  # s1 is the remaining stone
                return s1
            s2 = stones.pop()  # the second-heaviest stone; s2 <= s1
            if s1 > s2:
                # the remaining stone will be s1-s2
                # binary-insert the remaining stone into stones
                insort_left(stones, s1-s2)
            # else s1 == s2; both stones are destroyed
        return 0  # if no more stones remain
        
        