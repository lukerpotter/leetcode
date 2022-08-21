"""
https://leetcode.com/problems/isomorphic-strings/

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to
get t.

All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character, but a character may map to itself.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t_map = {}
        for idx, val in enumerate(s):
            # If the given value in string s is not already in our mapping:
            if val not in s_to_t_map:
                # We need to make sure that the value in string t has not
                # already been mapped by another value in string s
                if t[idx] not in s_to_t_map.values():
                    s_to_t_map[val] = t[idx]
                else:
                    return False
            else:
                if t[idx] != s_to_t_map[val]:
                    return False

        return True

test = Solution()
print(test.isIsomorphic(s = "badc", t = "baba"))
#print(test.isIsomorphic(s = "foo", t = "bar"))
#print(test.isIsomorphic(s = "paper", t = "title"))
