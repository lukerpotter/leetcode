"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Attempt 2: if this is to be 0(logn) complexity, we know it has to be a
variation of a binary search, but we have to keep going once we have found
the value. I have written a function that works, but I don't know if it
is actually what's expected, or if I am to continue to perform binary searches
to the left or right instead of running to the left and right.
"""

from typing import List


class Solution:
    @staticmethod
    def getLeftPosition(nums, target):
        left_idx = 0
        right_idx = len(nums) - 1

        # Find smallest index that holds target
        while left_idx <= right_idx:

            mid = left_idx + ((right_idx - left_idx) // 2)

            # If it matches:
            if nums[mid] == target:
                # If we're at the very first index, or the previous element
                # does not match our target, return this index. This is the
                # left-most index that holds the target value.
                if mid == 0 or nums[mid - 1] != target:
                    return mid

                # Otherwise, our values match, but we aren't at the left-most
                # one. As such, we need to change our window so it ends at
                # one element to the left of mid.
                right_idx = mid - 1

            # If the value at the mid is greater than our target, we need to
            # narrow our window such that it ends to the left and eliminates
            # mid from the search range.
            elif nums[mid] > target:
                right_idx = mid - 1

            # If the value at the mid is less than our target, we need to
            # narrow our window such that it starts to the right of mid and
            # eliminates mid from the search range.
            else:
                left_idx = mid + 1

        return -1

    @staticmethod
    def getRightPosition(nums, target):
        left_idx = 0
        right_idx = len(nums) - 1

        # Find largest index that holds target
        while left_idx <= right_idx:

            mid = left_idx + ((right_idx - left_idx) // 2)

            # If it matches:
            if nums[mid] == target:
                # If we're at the very last index, or the next element
                # does not match our target, return this index. This is the
                # right-most index that holds the target value.
                if mid == len(nums) - 1 or nums[mid + 1] != target:
                    return mid

                left_idx = mid + 1

            # If the value at the mid is greater than our target, we need to
            # narrow our window such that it ends to the left and eliminates
            # mid from the search range.
            elif nums[mid] > target:
                right_idx = mid - 1
            else:
                left_idx = mid + 1

        return -1

    @staticmethod
    def searchRange(nums: List[int], target: int) -> List[int]:
        return [Solution.getLeftPosition(nums, target), \
                Solution.getRightPosition(nums, target)]

print(Solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(Solution.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(Solution.searchRange(nums = [], target = 0))