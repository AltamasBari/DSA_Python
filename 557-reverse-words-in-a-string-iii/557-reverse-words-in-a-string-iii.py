class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")

        for i,x in enumerate(lst):
            lst[i] = x[::-1]

        return " ".join(lst) 