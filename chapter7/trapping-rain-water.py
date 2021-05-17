# leete no.42

from collections import deque
class Solution:
    def trap(self, height):
        # return first(height)
        return second(height)

def first(height):
    answer = 0
    dq = deque(height)
    stack = []
    while dq:
        now = dq.popleft()
        if not stack:
            stack.append(now)
        elif stack[0] <= now:
            mid_area = stack[1:]
            print(stack[0], len(mid_area), sum(mid_area))
            answer += stack[0] * len(mid_area) - sum(mid_area)
            stack = [now]
        else:
            stack.append(now)
        print(stack, answer)
    return answer

def second(height): # I think it have good performance but is not pythonic
    longest_bar = max(height)
    longest_idx = []
    total_water = longest_bar * len(height)
    for idx, long in enumerate(height):
        if long == longest_bar:
            longest_idx.append(idx)
    middle_area = height[longest_idx[0]+1:longest_idx[-1]]
    left_side, right_side = deque(height[:longest_idx[0]]), height[longest_idx[-1]+1:]
    empty_space = 0
    if left_side:
        left_stand = left_side.popleft()
        empty_space += longest_bar - left_stand
        while left_side:
            now = left_side.popleft()
            if left_stand < now:
                left_stand = now
            empty_space += longest_bar - left_stand
    if right_side:
        right_stand = right_side.pop()
        empty_space += longest_bar - right_stand
        while right_side:
            now = right_side.pop()
            if right_stand < now:
                right_stand = now
            empty_space += longest_bar - right_stand
    return total_water - empty_space - sum(height)
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
print(Solution().trap(height))