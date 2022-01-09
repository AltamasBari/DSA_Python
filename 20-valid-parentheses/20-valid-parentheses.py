class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ch_opp = {')':'(', '}':'{', ']':'['}
        for ch in s:
            if ch in ch_opp:
                if not stack or stack[-1] != ch_opp[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack