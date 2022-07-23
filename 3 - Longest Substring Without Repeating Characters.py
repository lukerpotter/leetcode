# Given a string s, find the length of the longest substring without repeating
# characters.

# Example 1:
#
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.

class Solution:

    @staticmethod
    def lengthOfLongestSubstring(s):
        left_idx = max_length = 0
        characters_seen_and_idx = {}

        for right_idx, char in enumerate(s):

            # If we have not already seen the character, or the last time we
            # saw the character was at an index prior to our left boundary
            # (inclusive), we still have a unique string. As such, we can
            # update our maximum length:
            if char not in characters_seen_and_idx or \
                    characters_seen_and_idx[char] < left_idx:
                max_length = max(max_length, right_idx - left_idx + 1)

            # Otherwise, we set out left index to be the point at which we
            # last saw the character, plus 1. As such, we iterate over every
            # unique value in the string, but also don't revisit duplicates.
            # For example, if we have string "dvvd", we set our left index to
            # 2 instead of 1, thus never starting a substring with the first
            # v in the list.
            else:
                left_idx = characters_seen_and_idx[char] + 1

            characters_seen_and_idx[char] = right_idx

        return max_length

print(Solution.lengthOfLongestSubstring(s="dvvd"))  # 2
print(Solution.lengthOfLongestSubstring(s="dvdf"))  # 2
print(Solution.lengthOfLongestSubstring(s="aab"))  # 2
print(Solution.lengthOfLongestSubstring(s="abcabcbb"))  # 3
print(Solution.lengthOfLongestSubstring(s="bbbbb"))  # 1
print(Solution.lengthOfLongestSubstring(s="pwwkew"))  # 3
print(Solution.lengthOfLongestSubstring(s="a"))  # 1
print(Solution.lengthOfLongestSubstring(s="abcdefghijklmnopqrstuvwxyz"))  # 26
print(Solution.lengthOfLongestSubstring(s=""))  # 0
