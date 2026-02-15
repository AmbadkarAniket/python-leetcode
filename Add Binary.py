# Given two binary strings a and b, return their sum as a binary string.


class Solution(object):
    def addBinary(self, a, b):
        pointer_a = len(a) - 1
        pointer_b = len(b) - 1
        carry = 0
        answer = ""

        while pointer_a >= 0 or pointer_b >= 0 or carry:
            digit_a = int(a[pointer_a]) if pointer_a >= 0 else 0
            digit_b = int(b[pointer_b]) if pointer_b >= 0 else 0

            total = digit_a + digit_b + carry
            answer = str(total % 2) + answer
            carry = total // 2

            pointer_a -= 1
            pointer_b -= 1

        return answer
