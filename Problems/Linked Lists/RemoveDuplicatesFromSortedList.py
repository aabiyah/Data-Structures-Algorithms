# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

class Solution:
  def deleteDuplicates(self, head):
      """
      :type head: ListNode
      :rtype: ListNode
      """
      current = head

      while current and current.next:
          if current.val == current.next.val:
              # Skip the duplicate node
              current.next = current.next.next
          else:
              # Move to the next node
              current = current.next

      return head