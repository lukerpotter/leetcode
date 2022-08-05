"""
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image, rotate the image by
90  degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the
input  2D matrix directly. DO NOT allocate another 2D matrix and do the
rotation.

"""
from math import ceil
from typing import List, Tuple


class Solution:

    def get_landing_coords(self, coords: Tuple[int,int],
                           topRow: int,
                           bottomRow: int) -> Tuple[int, int]:

        # The index of the left column is always equal to the top row, and the
        # index of the right column is always equal to the bottom row.
        leftCol = topRow
        rightCol = bottomRow

        # There may be a better way to identify this, but I'm going to
        # start with corners.
        coord_row = coords[0]
        coord_col = coords[1]

        if coord_row == topRow:
            return (coord_col, rightCol)

        if coord_row == bottomRow:
            return (coord_col, leftCol)

        # When we're dealing with the num_cols, we care about the position of
        # the element relative to the rest of the matrix, not relative to
        # the actual matrix on the outside. As such, the coordinate row only
        # matters relative to the top and bottom rows.

        if coord_col == leftCol:
            return (topRow, rightCol - coord_row + leftCol)

        if coord_col == rightCol:
            return (bottomRow, rightCol - coord_row + leftCol)

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # To make this happen, we have to pick up an element, figure out
        # where to drop it, pick up THAT element, drop the first one,
        # and go forward.

        # The logic I'm using is that we move each "layer", or "ring" around
        # the array, then move to the next inner one. The other thought is
        # if there's any way to rotate column by column, but that's sketchy AF
        # considering we have to do it in place

        full_matrix_dims = len(matrix[0])
        num_layers = ceil(full_matrix_dims / 2)

        # Each layer is going to be an n*n layer, similar to an onion. When
        # we rotate the array ninety degrees, we only need to step through
        # the first n-1 elements. Via the loop shown below, taking n-1 steps
        # will actually trigger all elements in the layer to move.

        # starting_row = starting_col = 0
        num_elements_to_rotate = full_matrix_dims - 1
        # Rotate a "layer", then move to the next layer
        for row in range(num_layers):

            print(f"Starting with row {row}")
            cur_matrix_dims = full_matrix_dims - (2*row)
            print(f"Current matrix dimensions of  {cur_matrix_dims} * {cur_matrix_dims}")
            num_cols = cur_matrix_dims - 1

            for col in range(row, row + num_cols):
                print(f"Starting with column {col}")

                starting_row, starting_col = row, col
                val_to_move = matrix[starting_row][starting_col]

                landing_idx = self.get_landing_coords([row, col], topRow=row,
                                                      bottomRow=row + num_cols)

                landing_row = landing_idx[0]
                landing_col = landing_idx[1]



                while (landing_row != starting_row or landing_col !=
                                       starting_col):
                    print(
                        f"      Moving value {val_to_move} to index [{landing_row},"
                        f"{landing_col}]")

                    next_val_to_move = matrix[landing_row][landing_col]
                    print(
                        f"      Current value at index [{landing_row},"
                        f"{landing_col}] is "
                        f"{next_val_to_move}, which we will move next.")
                    matrix[landing_row][landing_col] = val_to_move
                    val_to_move = next_val_to_move

                    landing_idx = self.get_landing_coords([landing_row, landing_col],
                                                          topRow=row,
                                                          bottomRow=row + num_cols)

                    landing_row = landing_idx[0]
                    landing_col = landing_idx[1]

                matrix[landing_row][landing_col] = val_to_move

test = Solution()

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
test.rotate(matrix)
print(matrix)