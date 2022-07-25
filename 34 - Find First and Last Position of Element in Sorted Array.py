"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order, find the
starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Attempt 1: if this is to be 0(logn) complexity, we know it has to be a
variation of a binary search, but we have to keep going once we have found
the value. I have written a function that works, but I don't know if it
is actually what's expected, or if I am to continue to perform binary searches
to the left or right instead of running to the left and right.
"""

from typing import List


class Solution:
    @staticmethod
    def searchRange(nums: List[int], target: int) -> List[int]:
        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx <= right_idx:

            mid = left_idx + ((right_idx - left_idx) // 2)
            if nums[mid] == target:
                min_pointer = mid
                while min_pointer >= 0 and \
                        nums[min_pointer] == target:
                    min_pointer -= 1


                max_pointer = mid
                while max_pointer < len(nums) and \
                        nums[max_pointer] == target:
                    max_pointer += 1

                return [min_pointer + 1, max_pointer - 1]

            elif nums[mid] > target:
                right_idx = mid - 1
            else:
                left_idx = mid + 1

        return [-1, -1]



print(Solution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
print(Solution.searchRange(nums = [5,7,7,8,8,10], target = 6))
print(Solution.searchRange(nums = [], target = 0))

# @staticmethod
# def search(nums: List[int], target: int) -> int:
#     first_element = 0
#     last_element = len(nums) - 1
#
#     while first_element <= last_element:
#         mid = first_element + ((last_element - first_element) // 2)
#
#         # Element found at mid
#         element_at_mid = nums[mid]
#         if nums[mid] == target:
#             return mid
#
#         elif target < nums[mid]:
#             last_element = mid - 1
#
#         else:
#             first_element = mid + 1
#
#     return -1
