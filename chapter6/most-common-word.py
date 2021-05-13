# leet no. 819

import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned) -> str:
        splited = list(map(str.lower, re.split('[\s!?\',;.]', paragraph)))
        banned = {ban: True for ban in banned}
        word_count = dict()
        for word in splited:
            if not word or banned.get(word):
                continue
            else:
                word_count[word] = word_count.get(word, 0) + 1
        return sorted(word_count.items(), key=lambda x: x[1])[-1][0]


## re 없이 풀고 싶은 경우는??

paragraph, banned = "a.", []
paragraph, banned = "Bob hit a ball, the hit BALL flew far after ?it was hit.", ["hit"]

print(Solution().mostCommonWord(paragraph, banned))