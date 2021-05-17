# leete no. 1

class Solution:
    def twoSum(self, nums, target: int):
        return first(nums, target)


def first(nums, target): ## slow....
    nums = [(n, idx) for idx, n in enumerate(nums)]
    nums.sort()
    end_idx = len(nums)-1
    for idx, tup in enumerate(nums):
        n, origin_idx = tup
        left, right = idx+1, end_idx
        while left <= right:
            mid = (left + right) // 2
            if target - n < nums[mid][0]:
                right = mid-1
            elif target - n > nums[mid][0]:
                left = mid+1
            else:
                return [origin_idx, nums[mid][1]]

nums = [3,2,4]
target = 6

print(Solution().twoSum(nums, target))
