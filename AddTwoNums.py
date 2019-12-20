# You are given two non-empty linked lists representing two non-negative integers. The digits 
# are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    if l2 == None:
      l2 = ListNode(0)

    if l1 == None:
      l1 = ListNode(0)
    
    nextVar = ListNode(l1.val+l2.val)
    if nextVar.val >= 10:
      nextVar.val = nextVar.val-10
      if l2.next != None:
        l2.next.val = l2.next.val+1
      elif l1.next != None:
        l1.next.val = l1.next.val+1
      else:
        l1.next = ListNode(1)
    if l1.next != None or l2.next != None:
      # the remaining list is just equal to l2
      nextVar.next = self.addTwoNumbers(l1.next,l2.next)

    return nextVar
