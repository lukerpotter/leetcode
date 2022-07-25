"""
https://leetcode.com/problems/binary-search/

Given an array of integers nums which is sorted in ascending order, and an
integer target, write a function to search target in nums. If target exists,
then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Constraints:

- 1 <= nums.length <= 104
- 10^4 < nums[i], target < 10^4
- all the integers in nums are unique
- nums is sorted in ascending order

Attempt 1: I had completed this exercise far prior to this, but wanted to see
if I could complete it properly from memory.
"""

from typing import List


class Solution:
    @staticmethod
    def search(nums: List[int], target: int) -> int:
        left_idx = 0
        right_idx = len(nums) - 1

        while left_idx <= right_idx:
            mid = left_idx + ((right_idx - left_idx) // 2)

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                right_idx = mid - 1
            else:
                left_idx = mid + 1

        return -1

print(Solution.search(nums=[-1,0,3,5,9,12], target=12))
print(Solution.search(nums=[-1,0,3,5,9,12], target=3))
