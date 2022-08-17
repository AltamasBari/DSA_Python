class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        mp = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        unique = set()
        for word in words:
            code = ""
            for char in word:
                code += mp[ord(char)-ord('a')]
            
            unique.add(code)
        
        return len(unique)