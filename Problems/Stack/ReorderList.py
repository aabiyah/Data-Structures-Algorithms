# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
# You may not modify the values in the list's nodes. Only nodes themselves may be changed.

class ListNode(object):
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution(object):
  def reorderList(self, head):
      """
      :type head: ListNode
      :rtype: None Do not return anything, modify head in-place instead.
      """
      if not head or not head.next or not head.next.next:
          return

      # Step 1: Find the middle of the list
      slow, fast = head, head
      while fast and fast.next:
          slow = slow.next
          fast = fast.next.next

      # Step 2: Reverse the second half of the list
      prev, curr = None, slow.next
      slow.next = None  # Split the list into two halves
      while curr:
          temp = curr.next
          curr.next = prev
          prev = curr
          curr = temp

      # Step 3: Merge the two halves
      first, second = head, prev
      while second:
          temp1, temp2 = first.next, second.next
          first.next = second
          second.next = temp1
          first, second = temp1, temp2
