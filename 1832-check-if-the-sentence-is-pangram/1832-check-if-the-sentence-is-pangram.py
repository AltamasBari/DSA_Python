class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        d = set()
        
        for x in sentence:
            d.add(x)
        
        if len(d) == 26:
            return True
        else:
            return False