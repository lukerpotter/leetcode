"""
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
of rows like this: (you may want to display this pattern in a fixed font for
better legibility)

P A H N
APLSIIG
Y I R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number
of rows

Constraints:
- 1 <= s.length <= 1000
- s consists of English letters (lower-case and upper-case), ',' and '.'.
- 1 <= numRows <= 1000
###
Attempt 2: 2022-07-15. Solution works and runs in an acceptable amount of time.
A variation of the solution can be found at
https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43),
and is much faster. The concepts are the same between my solution and the
linked solution; the linked solution is optimized/better structured.
"""

class Solution:
	def convert(self, s: str, numRows: int) -> str:

		# 		# If our number of rows is 1, we can just return the string; we don't
		# 		# have to perform any processing
		if numRows == 1:
			return s

		# Idea: basically, we're switching directions from "down" to "up".
		# Pattern: we go numRows down, then numRows - 2 up

		# Note that the index in our array is going to be one less than the
		# number of rows.
		rows = [""] * numRows
		insertion_row = 0
		direction = ""

		for val in s:

			rows[insertion_row] += val

			# We switch directions when we hit the top and bottom of our rows.
			if insertion_row % (numRows - 1) == 0:
				if direction == "down":
					direction = "up"
				else:
					direction = "down"

			if direction == "down":
				insertion_row += 1
			else:
				insertion_row -= 1

		return_string = ""
		for val in rows:
			return_string += val
		return return_string

# class Solution:
# 	def convert(self, s: str, numRows: int) -> str:
#
# 		# If our number of rows is 1, we can just return the string; we don't
# 		# have to perform any processing
# 		if numRows == 1:
# 			return s
#
# 		# So the string can be broken into blocks of (numRows + (numrows - 2))
# 		# letters. The first numRows characters will be inserted into the
# 		# respective rows in order. The remaining numrows - 2 characters will
# 		# be inserted in reverse order. We'll then add everything up when
# 		# we are done.
#
# 		rows = [""] * numRows
# 		blockSize = numRows + numRows - 2
#
# 		# Break the string into chunks
# 		# https://pythonexamples.org/python-split-string-into-specific-length-chunks/
# 		chunks = [s[i:i + blockSize] for i in range(0, len(s), blockSize)]
#
# 		for chunk in chunks:
# 			for idx, val in enumerate(chunk):
# 				position_in_block = idx % blockSize
#
# 				# If the position in the block is one of the first x elements
# 				# (the "straight-down" part of the zigzag), add it in the
# 				# appropriate place:
# 				if position_in_block < numRows:
# 					rows[position_in_block] += val
#
# 				# Otherwise, we want to move that many elements back "up" the
# 				# diagonal:
# 				else:
# 					rows[numRows - position_in_block - 2] += val
#
# 		return_string = ""
# 		for idx, val in enumerate(rows):
# 			return_string += val
#
# 		return return_string

###############################################################################
test = Solution()
#print(test.convert(s="PAYPALISHIRING", numRows=3))  # PAHNAPLSIIGYIR
print(test.convert(s="PAYPALISHIRING", numRows=4))  # PINALSIGYAHRPI
print(test.convert(s="A", numRows=1))  # A
