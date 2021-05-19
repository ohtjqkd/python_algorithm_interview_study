class Solution:
    def arrayPairSum(self, nums):
        return first(nums)

def first(nums):
    answer = 0
    nums.sort()
    for i in range(0, len(nums), 2):
        answer += nums[i]
    return answer

nums = [6,2,6,5,1,2]


print(Solution().arrayPairSum(nums))