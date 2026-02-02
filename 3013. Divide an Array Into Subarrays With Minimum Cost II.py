#3013. Divide an Array Into Subarrays With Minimum Cost II

# Input: nums = [1,3,2,6,4,2], k = 3, dist = 3
# Output: 5
# Explanation: The best possible way to divide nums into 3 subarrays is:
#  [1,3], [2,6,4], and [2]. This choice is valid because ik-1 - i1 is 5 - 2 = 3 which is equal to dist.
#  The total cost is nums[0] + nums[2] + nums[5] which is 1 + 2 + 2 = 5.
# It can be shown that there is no possible way to divide nums into 3 subarrays at a cost lower than 5.


import bisect

class Solution:
    def minimumCost(self, nums, k, dist):
        n = len(nums)
        base = nums[0]

        window = []
        small_sum = 0

        # Initialize window
        for i in range(1, dist + 2):
            bisect.insort(window, nums[i])

        small_sum = sum(window[:k-1])
        ans = base + small_sum

        for i in range(dist + 2, n):
            out = nums[i - (dist + 1)]
            in_ = nums[i]

            # Remove outgoing
            idx = bisect.bisect_left(window, out)
            if idx < k - 1:
                small_sum -= out
            window.pop(idx)

            # Add incoming
            idx = bisect.bisect_left(window, in_)
            if idx < k - 1:
                small_sum += in_
                if len(window) >= k - 1:
                    small_sum -= window[k - 2]
            window.insert(idx, in_)

            ans = min(ans, base + small_sum)

        return ans
