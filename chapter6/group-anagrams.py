# leete no. 49

from collections import deque
class Solution:
    def groupAnagrams(self, strs):
        pass

    def my_solution(self, strs): ## 해결은 가능했지만 너무 느리다. 해결방안은??
        result = []
        strs.sort(key = lambda x: len(x))
        sorted_str = deque([])
        for idx, s in enumerate(strs):
            sorted_str.append((sorted(s), idx))

        while sorted_str:
            std = sorted_str.popleft()
            group = [strs[std[1]]]
            no_match = deque([])
            while sorted_str:
                compare = sorted_str.popleft()
                if len(std[0]) != len(compare[0]):
                    no_match.append(compare)
                    break
                elif std[0] == compare[0]:
                    group.append(strs[compare[1]])
                else:
                    no_match.append(compare)
            result.append(group)
            sorted_str = no_match + sorted_str

        return result



strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["eat","tea","tan","ate","nat","bat","ac","bd","aac","bbd","aacc","bbdd","acc","bdd"]

sol = Solution()
print(sol.my_solution(strs))
