"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating
# characters.

Constraints:

0 <= s.length <= 5 * 10^4
s consists of English letters, digits, symbols and spaces.

Attempts 1 and 2: attempt 1 is slower; I was not able to complete attempt 2
without reviewing that solution required hash table
"""

class Solution:

    @staticmethod
    def lengthOfLongestSubstring(s):
        word_length = len(s)
        if word_length <= 1:
            return word_length

        charcters_and_most_recent_idx = {}
        left_idx = 0
        #end_of_current_substring = 0
        max_length = 0
        length_of_current_substring = 0

        # 213412

        for right_idx, val in enumerate(s):
            # If we haven't already seen the particular character we are
            # currently sitting on, or we've seen it but it's outside the
            # boundaries of our word, carry on to the next letter
            if val not in charcters_and_most_recent_idx or \
                charcters_and_most_recent_idx[val] < left_idx:
                max_length = max(max_length, right_idx - left_idx + 1)

            # Otherwise, we need to jump the start of our current word to
            # one position AFTER the index at which we last saw this
            # character
            else:
                left_idx = charcters_and_most_recent_idx[val] + 1

            charcters_and_most_recent_idx[val] = right_idx

        return max_length

    # This works; not blazing fast but not super-slow either
    @staticmethod
    def lengthOfLongestSubstring_ver1(s):
        word_length = len(s)
        if word_length <= 1:
            return word_length

        left_idx = 0
        right_idx = 1
        max_length = 0

        while right_idx < word_length:
            if s[right_idx] in s[left_idx:right_idx]:
                length = right_idx - left_idx
                if length > max_length:
                    max_length = length
                left_idx += 1
            else:
                right_idx += 1

        length = right_idx - left_idx
        if length > max_length:
            max_length = length

        return max_length

print(Solution.lengthOfLongestSubstring(s="123415"))
print(Solution.lengthOfLongestSubstring(s="1221"))  # 2
print(Solution.lengthOfLongestSubstring(s="dvvd"))  # 2
print(Solution.lengthOfLongestSubstring(s="dvdf"))  # 3
print(Solution.lengthOfLongestSubstring(s="aab"))  # 2
print(Solution.lengthOfLongestSubstring(s="abcabcbb"))  # 3
print(Solution.lengthOfLongestSubstring(s="bbbbb"))  # 1
print(Solution.lengthOfLongestSubstring(s="pwwkew"))  # 3
print(Solution.lengthOfLongestSubstring(s="a"))  # 1
print(Solution.lengthOfLongestSubstring(s="abcdefghijklmnopqrstuvwxyz"))  # 26
print(Solution.lengthOfLongestSubstring(s=""))  # 0

