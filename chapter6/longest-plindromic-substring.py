# leete no. 5

import heapq

class Solution:
    def longestPalindrome(self, s: str) -> str:
        return first(s)
s = "babad"

def first(s: str): # slow..
    answer = []
    for i in range(len(s)):
        for j in range(len(s), i, -1):
            word = s[i:j]
            if word == word[::-1]:
                heapq.heappush(answer, (-len(word), word))
                break
    return heapq.heappop(answer)[1]

def second(s: str):
    pass

print(Solution().longestPalindrome(s))