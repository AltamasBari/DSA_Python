class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        #https://medium.com/@roperluo.me/leetcode-1996-the-number-of-weak-characters-in-the-game-python-56db58aa833e
        properties.sort(key= lambda x: (-x[0], x[1]))
        result = max_defense =  0
        
        for _, defense  in properties:
            if defense < max_defense:
                result +=  1

            max_defense = max(max_defense, defense)
        
        return result