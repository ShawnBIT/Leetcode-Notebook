'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''


# Solution 1: O(N^3) 144ms top 86.85%
# change the 4sum problem to 3sum problem
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        nums.sort()
        result = set()
        
        for i, v in enumerate(nums[:-3]):
            if i >= 1 and v == nums[i-1]:
                continue
            # reduce the compute time
            if v*4 > target or nums[-1]*4 < target:
                continue
            target_3 = target - v
            for j, x in enumerate(nums[i+1:-2]):
                # reduce the compute time
                if x*3 > target_3 or nums[-1]*3 < target_3:
                    continue
                target_2 = target_3 - x
                hash_map = {}
                for k, y in enumerate(nums[i+2+j:]):
                    diff = target_2 - y
                    if diff in hash_map:
                        result.add((v,x,target-diff-v-x,diff))
                    hash_map[y]  =1
                    
        ans = []
        for res in result:
            ans.append(list(res))
            
        return ans

# Attention:If you dont use the judgement to reduce the computation time, you will get 1320ms computation time.


