"""

Given a signed 32-bit integer x, return x with its digits reversed. If
reversing x causes the value to go outside the signed 32-bit integer range
[-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or
unsigned).

Attempt 1: Solved by converting to list and performing two pointer work. This
executed far more slowly than I anticipated, and I am assuming this is
directly related to the number of conversions involved.
"""

class Solution:
    def reverse(self, x: int) -> int:
        back = 0
        abs_val = abs(x)

        while (abs_val > 0):
            back = (back * 10) + abs_val % 10
            if (back > (2 ** 31 - 1)):
                return 0
            abs_val = abs_val // 10

        if x < 0:
            return -1 * back
        else:
            return back

    def reverse(self, x: int) -> int:

        # Two pointer
        val_as_string = list(str(x))

        # need to screw with left index if negative
        left = 1 if val_as_string[0] is '-' else 0
        right = len(val_as_string) - 1

        while left <= right:
            val_as_string[left], val_as_string[right] = val_as_string[
                                                            right], \
                                                        val_as_string[left]
            left += 1
            right -= 1

        val_as_float = float(''.join(val_as_string))
        if (abs(val_as_float) > (2 ** 31 - 1)):
            return 0
        else:
            return int(val_as_float)


test = Solution()
print(test.reverse(-1234))
