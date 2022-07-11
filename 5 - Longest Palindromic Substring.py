'''
https://leetcode.com/problems/longest-palindromic-substring/

Initial Attempt: 2022-07-10

First approach: start with the full string. If it is not a palindrome, check
all strings that are one position shorter on the next iteration. Eventually,
you will either find a palindrome or return any letter in the string (a "one-
character palindrome")
'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # What I'm trying to do here:
        # Pass 1: get all strings of length x
        # Pass 2: get all strings of length x -1
        # ...

        for str_length in range(len(s), 0, -1):

            num_possible_solutions_of_length = len(s) - str_length + 1

            for idx in range(0, num_possible_solutions_of_length):
                string_to_check = s[idx:idx+str_length]
                rev_string = string_to_check[::-1]
                if string_to_check == rev_string:
                    return string_to_check

test = Solution()
print(test.longestPalindrome(s = "abccbd"))

