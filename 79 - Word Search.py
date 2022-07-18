"""
https://leetcode.com/problems/word-search/

Given an m x n board of characters board and a string word, return true if word
exists in the board.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell
may not be used more than once.

Attempt 1: July 17, 2022 - I was unable to solve this without timing out. I
believe my function operates as expected, but cannot get it to complete in
a timely fashion.
"""
from typing import List, Optional
from copy import deepcopy

class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        num_rows = len(board)
        num_cols = len(board[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def find_next_letter(starting_row,
                             starting_col,
                             coords_already_seen:List[List[str]],
                             idx_in_word = 1,
                             depth = 0):

            coords_already_seen[starting_row][starting_col] = True
            letter_to_find = word[idx_in_word]

            running_count = 0

            # We want to look in every direction from the spot we're standing
            # on.
            for d in directions:
                running_count += 1
                new_row = starting_row + d[0]
                new_col = starting_col + d[1]

                # At this point, we want to see if the
                if 0 <= new_col < num_cols and 0 <= new_row < num_rows:
                    if coords_already_seen[new_row][new_col] is False:

                        # If the letter at the coordinates is not in our
                        # word, add the coordinates to the list of those
                        # we want to ignore i.e. don't check it again
                        if board[new_row][new_col] not in set(word):
                            coords_already_seen[new_row][new_col] = True

                        #print(f"    We are looking for {letter_to_find} (at index"
                            # f" {idx_in_word} of {word}) at [{new_row}, {new_col}]")

                        # If we have found the letter:
                        if board[new_row][new_col] == letter_to_find:
                            ##print(f"{'          ' * (depth+1)} WE FOUND IT!")

                            # If we've found the last letter in the word,
                            # return true
                            if idx_in_word + 1 == len(word):
                                return True

                            # Otherwise, continue searching, passing a full
                            # copy of the "coords_already_seen" list to the
                            # next function
                            new_coords = deepcopy(coords_already_seen)
                            new_idx = idx_in_word + 1
                            new_depth = depth + 1
                            letter_found = find_next_letter(
                                starting_row=new_row, starting_col=new_col,
                                             coords_already_seen=new_coords,
                                             idx_in_word=new_idx,
                                             depth=new_depth)

                            if letter_found:
                                 return True
                # else:
                    #print(f"{'   ' * (depth+1)}Out of range")

            return False


            # Each time into the directional loop, we need to reset our
            # "letters we've found" list to everything up to and including
            # the current starting_row and starting_y
###############################################################################
        # First, find the coordinates where the first letter of the word is
        # found.
        #print(word[0])
        #print(range(num_rows))
        #print(range(num_cols))
        #print(board)
        vals_in_word = set(word)
        letters_in_board = set([board[x][y] for x in range(num_rows) for y in
                       range(num_cols) if board[x][y] in vals_in_word])

        print(vals_in_word)
        print(letters_in_board)

        if vals_in_word != letters_in_board:
            return False

        coordinates = [(x, y) for x in range(num_rows) for y in
                       range(num_cols) if board[x][y] in vals_in_word]

        #print(coordinates)
        # If the length of the word is 1 letter, and we have coordinates,
        # we've found our word and can short circuit by returning true:
        if len(coordinates) != 0 and len(word) == 1:
            return True

        # Otherwise, we need to say, "Okay, I've found the first letter in the
        # word. Now, I need to look at the NEXT letter in the word, which is
        # found at index 1.
        for coord in coordinates:
            # We pass in the coordinate at which we start looking. We ALSO
            # pass

            # #print(f"Starting: found first letter of word at [{coord[0]},"
            #       f" {coord[1]}]")

            #visited_so_far = [[False] * num_cols for i in range(num_rows)]
            string_found = find_next_letter(starting_row=coord[0],
                                            starting_col=coord[1],
                                            coords_already_seen=[
                                                [False] * num_cols for i in
                                                range(num_rows)]
                                            )

            # If we've found our string, short-circuit
            if string_found:
                return True

        return False

test = Solution()

import time
start_time = time.time()

#print(set("AAB"))
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
#print("####################################")
# Expect False
print(test.exist(board=[['a']],
                 word="b"))
# Expect False
print(test.exist(board=[["A", "B", "C", "E"],
                        ["S", "F", "C", "S"],
                        ["A", "D", "E", "E"]],
                 word="ABCESEEFB"))


print("--- %s seconds ---" % (time.time() - start_time))