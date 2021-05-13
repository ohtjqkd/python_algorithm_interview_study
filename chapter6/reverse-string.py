# leet no. 344

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]


# 일반적인 슬라이싱 방식으로는 해결할 수 없는 문제다. tricky한 방법이 필요함
# s[:] = s[::-1]

# pythonic solution
# s.reverse()