#3010. Divide an Array Into Subarrays With Minimum Cost I

# Input: nums = [1,2,3,12]
# Output: 6
# Explanation: The best possible way to form 3 subarrays is: [1], [2], and [3,12] at a total cost of 1 + 2 + 3 = 6.
# The other possible ways to form 3 subarrays are:
# - [1], [2,3], and [12] at a total cost of 1 + 2 + 12 = 15.
# - [1,2], [3], and [12] at a total cost of 1 + 3 + 12 = 16.


class Solution(object):
    def minimumCost(self, nums):
        first = nums[0]

        rest = nums[1:]
        rest.sort()

        return first + rest[0] + rest[1]