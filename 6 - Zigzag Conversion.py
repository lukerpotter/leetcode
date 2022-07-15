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
Attempt 1: 2022-07-15. My solution works, but is rather slow (only faster than
16.88% of Pyton3 solutions submitted to Leetcode).
"""


class Solution:
	def convert(self, s: str, numRows: int) -> str:

		# If our number of rows is 1, we can just return the string; we don't
		# have to perform any processing
		if numRows == 1:
			return s

		# So the string can be broken into blocks of (numRows + (numrows - 2))
		# letters. The first numRows characters will be inserted into the
		# respective rows in order. The remaining numrows - 2 characters will
		# be inserted in reverse order. We'll then add everything up when
		# we are done.

		rows = [""] * numRows
		blockSize = numRows + numRows - 2

		# Break the string into chunks
		# https://pythonexamples.org/python-split-string-into-specific-length-chunks/
		chunks = [s[i:i + blockSize] for i in range(0, len(s), blockSize)]

		for chunk in chunks:
			for idx, val in enumerate(chunk):
				position_in_block = idx % blockSize

				# If the position in the block is one of the first x elements
				# (the "straight-down" part of the zigzag), add it in the
				# appropriate place:
				if position_in_block < numRows:
					rows[position_in_block] += val

				# Otherwise, we want to move that many elements back "up" the
				# diagonal:
				else:
					rows[numRows - position_in_block - 2] += val

		return_string = ""
		for idx, val in enumerate(rows):
			return_string += val

		return return_string

###############################################################################
test = Solution()
print(test.convert(s="PAYPALISHIRING", numRows=3))  # PAHNAPLSIIGYIR
print(test.convert(s="PAYPALISHIRING", numRows=4))  # PINALSIGYAHRPI
print(test.convert(s="A", numRows=1))  # A
