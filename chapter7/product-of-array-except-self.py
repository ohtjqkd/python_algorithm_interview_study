# leete no. 

class Solution:
    def productExceptSelf(self, nums):
        return first(nums)

def first(nums): ## 메모리를 너무 많이 사용해요..
    total = 1
    z_cnt = 0

    for i, n in enumerate(nums):
        if n != 0:
            total *= n
        elif z_cnt == 1:
            for i in range(len(nums)):
                nums[i] = 0
            return nums
        else:
            z_cnt += 1
            z_idx = i
    for i, n in enumerate(nums):
        if z_cnt == 1:
            if n == 0:
                nums[i] = total
            else:
                nums[i] = 0
        else:
            nums[i] = total//n
    return nums


nums = [1,2,3,4]
# nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))