# leete no. 1

class Solution:
    def twoSum(self, nums, target: int):
        
        return use_two_pointer(nums, target)


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

def use_in(nums, target): # use 'in' operand
    for i, n in enumerate(nums):
        complement = target - n
        if complement in nums[i+1:]:
            return [i, nums[i+1:].index(complement)+(i+1)]

def use_dict(nums, target):
    num_dic = dict()
    # num_dic = {n: True for n in nums}
    for i, n in enumerate(nums):

        print(num_dic)
        print(target-n)
        print(num_dic.get(target-n))
        print(num_dic.get(2))
        if num_dic.get(target-n) != None:
            print(i)
            return [num_dic.get(target-n), i]
        num_dic[n] = i
        print()
    
def use_two_pointer(nums, target):
    left, right = 0, len(nums)-1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 작으면 오른쪽 포인터를 왼쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

nums = [3,2,4]
target = 6
nums = [2,7,11,15]
target = 9
nums = [3,2,4]
target = 6

print(Solution().twoSum(nums, target))
