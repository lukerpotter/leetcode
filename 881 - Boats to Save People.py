"""
https://leetcode.com/problems/boats-to-save-people/

You are given an array people where people[i] is the weight of the ith
person, and an infinite number of boats where each boat can carry a maximum
weight of limit. Each boat carries at most two people at the same time,
provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

1 <= people.length <= 5 * 104
1 <= people[i] <= limit <= 3 * 104
"""
from typing import List, Optional
from math import ceil


class Solution:

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        idx_of_lightest_remaining_person = 0
        idx_of_heaviest_person_remaining = len(people) - 1
        num_boats = 0

        while idx_of_lightest_remaining_person <= \
                idx_of_heaviest_person_remaining:

            num_boats += 1

            # We're always going to throw the next-heaviest person into the
            # boat. We may or may not throw a light person in if that person
            # won't overload the boat.
            if people[idx_of_lightest_remaining_person] + \
                people[idx_of_heaviest_person_remaining] <= limit:
                idx_of_lightest_remaining_person += 1

            idx_of_heaviest_person_remaining -= 1

        return num_boats

test = Solution()
print(test.numRescueBoats(people=[1, 2, 4], limit=3))
print(test.numRescueBoats(people=[3, 2, 2, 1], limit=3))
print(test.numRescueBoats(people=[3, 5, 3, 4], limit=5))
print(test.numRescueBoats(people=[21, 40, 16, 24, 30], limit=50))
print(test.numRescueBoats(people=[3, 2, 3, 2, 2], limit=6))
