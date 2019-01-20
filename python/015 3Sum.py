'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''


# Solution 1: O(N^2) 1084ms top 91.6%
# change the 3sum problem to 2sum problem
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        result = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i-1]:
                continue
            hash_map = {}
            target = -v
            for x in nums[i+1:]:
                diff = target - x
                if diff in hash_map:
                    result.add((v,-v-diff,diff))
                hash_map[x] = 1 
                
        ans = []
        for res in result:
            ans.append(list(res))
            
        return ans
        

# Solution 2: O(N^2) 1388ms top 58.40%
# double pointers

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Sorted array can save a lot of time
        n = len(nums)
        nums.sort()
        ans = []
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            L,R = i+1,n-1
            target = -nums[i]
            
            while L < R :
                if nums[L] + nums[R] == target:
                    ans.append([nums[i],nums[L],nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L-1]:
                        L += 1
                    while L < R and nums[R] == nums[R+1]:
                        R -= 1
                elif nums[L] + nums[R] < target:
                    L += 1
                else:
                    R -= 1
        return ans




        