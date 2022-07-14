"""
https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Constraints:
- the number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading
zeros.

###
Attempt 1: 2022-07-13 - Tripped up by "and" vs "or" at line 53. May want to
revisit in future for potential faster solutions.
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def print_list(self):
		x = self

		while x.next is not None:
			print(x.val)
			x = x.next
		print(x.val)


class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

		# We have at least one value in one of the lists. The lists will not be
		# null nodes. i don't need to check for that. Just add their values
		# together.
		
		total = l1.val + l2.val
		carry, remainder = divmod(total, 10)
		x = newList = ListNode(remainder)

		l1_curr_node = l1
		l2_curr_node = l2
		while l1_curr_node.next is not None or l2_curr_node.next is not None:
			
			total = carry
			if l1_curr_node.next is not None:
				print(f"l1_curr_node.next.val: {l1_curr_node.next.val}")
				total += l1_curr_node.next.val
				l1_curr_node = l1_curr_node.next
			if l2_curr_node.next is not None:
				print(f"l2_curr_node.next.val: {l2_curr_node.next.val}")
				total += l2_curr_node.next.val
				l2_curr_node = l2_curr_node.next
			
			carry, remainder = divmod(total, 10)
			x.next = ListNode(remainder)
			x = x.next

		if carry != 0:
			x.next = ListNode(carry)
			
			

		# Run out our remaining nodes

		return newList
		# sum = 0
		# if l1_curr_node.next is not None:
		#     sum += l1_curr_node.val
		# if l2_curr_node.next is not None:
		#     sum += l2_curr_node.val
		# newList_curr_node.next = ListNode(sum)



l1 = ListNode(9) # 1
l1.next = ListNode(9) # 2
l1.next.next = ListNode(9) # 3
l1.next.next.next = ListNode(9) # 4
l1.next.next.next.next = ListNode(9) # 5
l1.next.next.next.next.next = ListNode(9) # 6
l1.next.next.next.next.next.next = ListNode(9) # 7

l2 = ListNode(9) # 1
l2.next = ListNode(9) # 2
l2.next.next = ListNode(9) # 3
l2.next.next.next = ListNode(9) # 4

test = Solution()
test.addTwoNumbers(l1, l2).print_list()

l1 = ListNode(2) # 1
l1.next = ListNode(4) # 2
l1.next.next = ListNode(9) # 3

l2 = ListNode(5) # 1
l2.next = ListNode(6) # 2
l2.next.next = ListNode(4) # 3
l2.next.next.next = ListNode(9) # 4

test = Solution()
#print(test.addTwoNumbers(l1=[2, 4, 3], l2=[5, 6, 4]))
test.addTwoNumbers(l1, l2).print_list()


