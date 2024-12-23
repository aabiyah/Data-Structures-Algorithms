# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Create a dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Traverse the list in pairs
        while prev.next and prev.next.next:
            # Identify the two nodes to swap
            first = prev.next
            second = first.next

            # Perform the swap
            first.next = second.next
            second.next = first
            prev.next = second

            # Move the pointer to the next pair
            prev = first

        return dummy.next