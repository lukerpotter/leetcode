"""
https://leetcode.com/problems/first-bad-version/

You are a product manager and currently leading a team to develop a new
product. Unfortunately, the latest version of your product fails the quality
check. Since each version is developed based on the previous version, all the
versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first
bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion (version) which returns whether version
is bad. Implement a function to find the first bad version. You should
# minimize the number of calls to the API.

The isBadVersion API is already defined for you.

Constraints:

1 <= bad <= n <= 2^31 - 1

"""

# This particular implementation returns the minimum value that meets the
# condition
def isBadVersion(version: int) -> bool:
    if version >= 4:
        return True
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left_idx = 0
        right_idx = n

        # We basically want to search until we find a bad version.
        while left_idx <= right_idx:

            mid = left_idx + ((right_idx - left_idx) // 2)

            # If the value at the mid-point is a bad version,
            if isBadVersion(mid) is True:
                # If we're at the first element, or the next element to the
                # left is false, return this element. It's the first bad
                # version.
                if mid == 0 or isBadVersion(mid - 1) is False:
                    return mid

                # Otherwise, we want to continue searching to the left. As such
                # we narrow our right-most index:
                right_idx = mid - 1

            # Otherwise, if the mid is not a bad version, we need to continue
            # to check to the right:
            else:
                left_idx = mid + 1

test = Solution()
print(test.firstBadVersion(4))
for x in range(1, 10000000):
    if test.firstBadVersion(x) is not None:
        print("{0} - {1}".format(x, test.firstBadVersion(x)))
