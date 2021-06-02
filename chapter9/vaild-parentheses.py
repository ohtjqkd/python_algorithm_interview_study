class Solution:
    def isValid(self, s: str) -> bool:
        couple = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        if s[0] not in couple.keys():
            return False
        stack = []
        for b in s:
            if len(stack) == 0 or b in couple.keys():
                stack.append(b)
            else:
                if couple.get(stack[-1]) == b:
                    stack.pop()
                else:
                    return False
            

        return True if len(stack) == 0 else False


s = "()"
print(Solution().isValid(s))