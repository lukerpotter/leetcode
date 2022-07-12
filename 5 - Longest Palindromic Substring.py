'''
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s. Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.

Second Attempt: 2022-07-11

Outer loop: iterates over the string as passed in. Finds strings of consecutive
letters, then passes this string, the index of the letter prior to it, and
the index of the letter after it, to the recursive function

Recursive function: using the indices passed in, checks if these two values
match. If so, add to each end of the string, then decrement the left index
and increment the right index, and call the function again.

Some comments and whatnot
'''

class Solution:

    def longestPalindrome(self, s: str) -> str:

        max_string = ""

        def recurse_thing(palindromic_string: str, left_idx: int,
                          right_idx: int):

            if left_idx >= 0 and right_idx < len(s):

                if s[left_idx] == s[right_idx]:
                    palindromic_string = s[left_idx] + palindromic_string + s[
                        right_idx]

                    palindromic_string = recurse_thing(palindromic_string,
                                                       left_idx - 1,
                                                       right_idx + 1)

            return palindromic_string

        #######################################################################
        running_idx = 0
        while running_idx < len(s):

            starting_idx = running_idx
            running_idx += 1

            palindrome_string = s[starting_idx]
            while running_idx < len(s) and \
                    s[starting_idx] == s[running_idx]:
                palindrome_string += s[running_idx]
                running_idx += 1
                #print(palindrome_string)

            word = recurse_thing(palindrome_string, left_idx=starting_idx - 1,
                                 right_idx=running_idx)

            if len(word) > len(max_string):
                max_string = word

        return max_string

test = Solution()
print(test.longestPalindrome(s="babad"))
print(test.longestPalindrome(s = "abcccccbd"))
print(test.longestPalindrome(s = "cbaaaaaaaabcd"))
