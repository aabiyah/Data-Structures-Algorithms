# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Solution:
  def removeNthFromEnd(self, head, n):
      """
      :type head: ListNode
      :type n: int
      :rtype: ListNode
      """
      # Create a dummy node to handle edge cases, like removing the first node
      dummy = ListNode(0)
      dummy.next = head
      first = dummy
      second = dummy

      # Move the first pointer `n + 1` steps ahead
      for _ in range(n + 1):
          first = first.next

      # Move both pointers until the first pointer reaches the end
      while first:
          first = first.next
          second = second.next

      # Remove the nth node from the end
      second.next = second.next.next

      # Return the new head of the list
      return dummy.next