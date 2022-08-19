class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        # https://youtu.be/uJ8BAQ8lASE
        
        hypoMap = {}      # hypothetical map, how many new seqs can be ended with this key
        freqMap = {}        # key: number, val: how many of key are left unchecked
        
        for num in nums:
            freqMap[num] = freqMap.get(num,0) + 1
        
        for num in nums:
            if freqMap[num] == 0: 
                continue   # the number is already in seqs, we don't need to check again
            
            if (hypoMap.get(num,0) > 0):    # If there is chance of addition in the sequence, we add the number to the seq
                freqMap[num] -= 1 
                hypoMap[num+1] = hypoMap.get(num+1,0) + 1
                hypoMap[num] -= 1
                
            elif(freqMap.get(num,0) > 0 and freqMap.get(num+1,0) > 0 and freqMap.get(num+2,0) > 0):   # If not we create a new seq using the number
                freqMap[num] -= 1
                freqMap[num+1] -= 1
                freqMap[num+2] -= 1
                hypoMap[num+3] = hypoMap.get(num+3,0) + 1
            
            else:
                return False
        
        return True