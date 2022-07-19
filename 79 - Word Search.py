"""
https://leetcode.com/problems/word-search/

Given an m x n board of characters board and a string word, return true if word
exists in the board.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.

Attempt 2: July 18, 2022 - Studied
https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments
and attempted to replicate from memory. Stumbling blocks included exist
condition, as well as dealing with the "trail of breadcrumbs". Keep an eye on
this in future problems.
"""
from typing import List, Optional
from copy import deepcopy


class Solution:

    def exist(self, board, word):
        if not board:
            return False

        num_rows = len(board)
        num_cols = len(board[0])

        def search_for_word(word, start_row, start_col):

            if len(word) == 0:
                return True

            # Check for validity:
            if start_row < 0 or start_row >= num_rows or \
                    start_col < 0 or start_col >= num_cols or \
                    word[0] != board[start_row][start_col]:
                return False

            # We've found the value in the board; don't search for it again
            # in this iteration. However, upon returning, we want to include
            # it in future searches

            val_at_start_row_and_col = board[start_row][start_col]
            board[start_row][start_col] = "#"

            # Check in all directions from the starting position
            result = search_for_word(word[1:], start_row - 1, start_col) or \
                     search_for_word(word[1:], start_row + 1, start_col) or \
                     search_for_word(word[1:], start_row, start_col - 1) or \
                     search_for_word(word[1:], start_row, start_col + 1)

            # Reset the board for the next iteration through the array
            board[start_row][start_col] = val_at_start_row_and_col
            return result

        coordinates = [(x, y) for x in range(num_rows) for y in range(num_cols)
                       if board[x][y] == word[0]]

        for coord in coordinates:
            if search_for_word(word, coord[0], coord[1]):
                return True
        # for row in range(num_rows):
        #     for num in range(num_cols):

        return False


test = Solution()

import time

start_time = time.time()

# print(set("AAB"))
# Expect True
print(test.exist(board=[["C", "A", "A"],
                        ["A", "A", "A"],
                        ["B", "C", "D"]],
                 word="AAB"))

# Expect True
print(test.exist(board=[['a']], word="a"))

# Expect True
print(test.exist(board=[["A", "B", "C", "E"],
                        ["S", "F", "C", "S"],
                        ["A", "D", "E", "E"]],
                 word="ABCCED"))

# Expect True
print(test.exist(board=[["A", "B", "C", "E"],
                        ["S", "F", "C", "S"],
                        ["A", "D", "E", "E"]],
                 word="SEE"))

# Expect True
print(test.exist(board=[["a", "b"],
                        ["c", "d"]],
                 word="cdba"))
print("####################################")
# Expect False
print(test.exist(board=[['a']],
                 word="b"))
# Expect False
print(test.exist(board=[["A", "B", "C", "E"],
                        ["S", "F", "C", "S"],
                        ["A", "D", "E", "E"]],
                 word="ABCESEEFB"))

print("--- %s seconds ---" % (time.time() - start_time))
