class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        dict = {}
        for x in nums:
            dict[x] = dict.get(x,0) + 1
            
        for x,v in dict.items():    
            if(v > len(nums)//2):
                return x
        '''
        count = 0
        elem = None
        
        for num in nums:
            if count == 0:
                elem =  num
            
            if elem == num:
                count += 1
            else:
                count -= 1
        
        return elem