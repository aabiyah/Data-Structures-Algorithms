# Given the head of a linked list, rotate the list to the right by k places.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the linked list
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        # Step 2: Make the linked list circular
        current.next = head

        # Step 3: Find the new head position
        k = k % length
        steps_to_new_head = length - k

        # Step 4: Traverse to the new tail and break the loop
        new_tail = head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
