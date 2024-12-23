# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

class Solution:
  def removeElements(self, head, val):
      """
      :type head: ListNode
      :type val: int
      :rtype: ListNode
      """
      # Create a dummy node to handle edge cases
      dummy = ListNode(0)
      dummy.next = head

      # Initialize current and previous pointers
      current = head
      prev = dummy

      # Traverse the list
      while current:
          if current.val == val:
              # Skip the current node
              prev.next = current.next
          else:
              # Move prev pointer
              prev = current
          # Move to the next node
          current = current.next

      # Return the new head
      return dummy.next