'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


# Solution 1: O(N) 36ms top 100%
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i,num in enumerate(nums):
            diff = target - num
            # judge the key
            if diff in hash_map:  
                return [hash_map[diff], i]
            hash_map[num] = i
        

# Solution 2: O(N) 56ms top 96.48%
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i,num in enumerate(nums):
            hash_map[num] = i
        for i,num in enumerate(nums):
            diff = target - num
            # Attention for repeated index
            if diff in hash_map and i != hash_map[diff]:
                return [i,hash_map[diff]]
