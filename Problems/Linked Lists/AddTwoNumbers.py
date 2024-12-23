# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Solution:
  def addTwoNumbers(self, l1, l2):
      """
      :type l1: ListNode
      :type l2: ListNode
      :rtype: ListNode
      """
      # Initialize a dummy node and carry
      dummy = ListNode(0)
      current = dummy
      carry = 0

      # Traverse both linked lists
      while l1 or l2:
          # Get values from the current nodes (or 0 if the list is exhausted)
          val1 = l1.val if l1 else 0
          val2 = l2.val if l2 else 0

          # Compute the sum and carry
          total = val1 + val2 + carry
          carry = total // 10
          current.next = ListNode(total % 10)
          current = current.next

          # Move to the next nodes in both lists
          if l1:
              l1 = l1.next
          if l2:
              l2 = l2.next

      # If there's a carry left, add a new node for it
      if carry > 0:
          current.next = ListNode(carry)

      return dummy.next