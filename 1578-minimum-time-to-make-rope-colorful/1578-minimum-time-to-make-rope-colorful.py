class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        #https://leetcode.com/problems/minimum-time-to-make-rope-colorful/discuss/1044203/python3easy-understanding
        ans = 0
        for i in range(1,len(colors)):
            if colors[i] == colors[i-1]:
                ans += min(neededTime[i],neededTime[i-1])
				#when it meet more than two consecutive same numbers
				#ex: a,a,a cost, 12,9,13 when it chose to delect 9 it should move 12 to number 9's position
                neededTime[i] = max(neededTime[i],neededTime[i-1])
        return ans