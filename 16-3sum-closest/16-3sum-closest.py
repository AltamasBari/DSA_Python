class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() #Sort the array
        answer = nums[0] + nums[1] + nums[2] #initialise Answer
        n=len(nums)
        for i in range(n-2):
            j=i+1 #take 2 ptr
            k=n-1
            while(j<k):
                sum=nums[i]+nums[j]+nums[k] # count sum 
                if sum < target:  #if sum too small , inc j ptr
                    j=j+1
                elif sum > target:  #if sum too large, dec k ptr
                    k=k-1
                else:  #if sum == target 
                    return sum
                if abs(sum - target) < abs(answer - target):
                    answer = sum
        return answer