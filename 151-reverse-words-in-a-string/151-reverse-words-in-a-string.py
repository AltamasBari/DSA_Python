class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")
        lst = lst[::-1]
        print(lst)
        temp = []
        for x in lst:
            if x != "":
                temp.append(x)
        s = " ".join(temp)        
        return s