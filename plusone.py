# # Intuition
# <!-- Describe your first thoughts on how to solve this problem. -->

# # Approach
# <!-- Describe your approach to solving the problem. -->

# # Complexity
# - Time complexity:
# <!-- Add your time complexity here, e.g. $$O(n)$$ -->

# - Space complexity:
# <!-- Add your space complexity here, e.g. $$O(n)$$ -->


class Solution(object):
    def plusOne(self, digits):
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits
