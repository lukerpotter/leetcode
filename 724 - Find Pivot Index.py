"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the
left of the index is equal to the sum of all the numbers strictly to the
index's right.

If the index is on the left edge of the array, then the left sum is 0 because
there are no elements to the left. This also applies to the right edge of the
array.

Return the leftmost pivot index. If no such index exists, return -1.

Constraints:
1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000

Attempt 1:

"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        max_idx = len(nums)  # Right-most index

        for running_pivot_idx in range(max_idx):
            left_sum = sum(nums[0:running_pivot_idx])
            right_sum = sum(nums[running_pivot_idx + 1:])
            if left_sum == right_sum:
                return running_pivot_idx

        # Nothing found
        return -1



test = Solution()
# nums = [1,7,3,6,5,6]
print(test.pivotIndex(nums=[1, 7, 3, 6, 5, 6]))
print(test.pivotIndex(nums=[2,1,-1]))

print(test.pivotIndex(nums=[-1,-1,-1,1,1,-1]))
