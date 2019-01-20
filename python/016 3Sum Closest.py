'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


# Solution 1: O(N^2) 188ms top 60.53%
# double pointers
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        n = len(nums)
        for i in range(n - 2):
            L, R = i + 1, n - 1
            while L < R:
                temp = nums[i] + nums[L] + nums[R]
                if temp == target:
                    return target
                elif temp > target:
                    R -= 1
                else:
                    L += 1
 
                if abs(temp - target) < abs(result - target):
                    result = temp
        
        return result

        
