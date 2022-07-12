"""
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target. You may assume that each input
would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
###
Attempt 1: 2022-07-11. I had attempted this before, and in this version, I
initially made the mistake of putting my "return" condition first. As this
had to be evaluated each time through the loop, but would only return once,
I elected to put it in the "else" clause, only triggering it once.
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Using this example: twoSum(nums=[2, 7, 11, 15], target=18)

        # I have a target sum, and I know that two of the values in the list
        # will add to that sum. In our example, those values are 7 and 11
        # adding up to 18.

        vals_and_indices = {}

        for idx, val in enumerate(nums):

            # If the value is not already in our dictionary, add it. What
            # we're doing is saying "at this particular index (a), you will
            # find another index (b). Index a plus the value held at index
            # b will totally to our target.

            # Loop 1: vals_and_indices[18 - 2] = 0 -> vals_and_indices[16] = 0
            # Loop2: vals_and_indices[18 - 7] = 1 -> vals_and_indices[11] = 1

            if val not in vals_and_indices.keys():
                vals_and_indices[target - val] = idx

            # Loop 3: At this point, we have key 11 in our dictionary. Key 11
            # contains the index at which we will find the value that, when
            # added to 11, totals to 18. As such, we return the two indices.
            else:
                return [vals_and_indices[val], idx]


test = Solution()
print(test.twoSum(nums=[2, 7, 11, 15], target=18))
