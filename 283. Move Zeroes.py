"""

# https://leetcode.com/problems/move-zeroes/

# Given an integer array nums, move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]
"""
from typing import List


class Solution:

    # This one is SLOW, although I did calculate it out myself and I think
    # that's worth something.

    # def moveZeroes(self, nums: List[int]) -> None:
    #
    #     zero_positions = [x for x in range(len(nums)) if nums[x] == 0]
    #
    #     if len(zero_positions) != 0:
    #         for idx in range(len(zero_positions)):
    #             zero_position = zero_positions[idx]
    #             nums[zero_position:-1] = nums[zero_position+1:]
    #             zero_positions = [x - 1 for x in zero_positions]
    #
    #         nums[-len(zero_positions):] = [0] * len(zero_positions)

    """
    Do not return anything, modify nums in-place instead.
    """

    def moveZeroes(self, nums: List[int]) -> None:
        # Where we will move the next non-zero element TO
        spot_to_put_non_zero = 0

        # We want to put all the non-zero values at the start. So let's
        # say we got "01020304". So we start:

        # Idx 0 - 0: 01020304; non-zero spot 0. Go to the next step.
        # Idx 1 - 1: 10020304; non-zero spot 1. Swap arr[0] and arr[1].
        # Idx 2 - 0. 10020304; non-zero spot 1. Go to the next step.
        # Idx 3 - 2. 12000304; non-zero spot 2. Swap arr[1] and arr[3].
        # Idx 4 - 0. 12000304; non-zero spot 2. Go to the next step.
        # Idx 5 - 3. 12300004; non-zero spot 3. Swap arr[2] and arr[5].
        # Idx 6 - 0. 12300004; non-zero spot 3. Go to the next step.
        # Idx 7 - 0. 12340000; non-zero spot 3. Swap arr[3] and arr[7].

        # "12000304".
        # Idx 4 - 0. Go to the next step.
        # Idx 4 - 0. Go to the next step.

        # along and we get to a non-zero value. Say it's at index 2, right?
        # So we say "oh, we're supposed to put non zero
        for idx, num in enumerate(nums):
            print(f"Idx {idx} - {num}: {nums}, non-zero spot "
                  f"{spot_to_put_non_zero}")
            if num != 0:
                nums[idx], nums[spot_to_put_non_zero] = \
                    nums[spot_to_put_non_zero], num
                spot_to_put_non_zero += 1

test = Solution()
#
nums = [1,  0, 2, 2, 0, 3, 3, 3, 0, 4, 4, 4, 4]
#nums = [1]
test.moveZeroes(nums)
print(nums)

# nums = [0, 1, 0, 3, 12]
# test.moveZeroes(nums)
# print(nums)
#
# nums = [0]
# test.moveZeroes(nums)
# print(nums)
#
