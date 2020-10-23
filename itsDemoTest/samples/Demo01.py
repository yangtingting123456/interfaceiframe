# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
import random
class Solution(object):
    def twoSum(self, nums, target):

        return nums+target

sum4 = Solution()
nums = [2, 7, 11, 15]
n = len(nums)
i=random.randint(0,n-1)
target = 9
print(sum4.twoSum(nums[i],target))
