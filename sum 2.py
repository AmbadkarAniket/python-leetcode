#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        seen = {} 

        for i, num in enumerate(nums):
            need = target - num  

            if need in seen:
                return [seen[need], i]

            seen[num] = i

        
# @lc code=end