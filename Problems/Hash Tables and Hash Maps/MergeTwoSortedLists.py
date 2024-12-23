# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to simplify the merging process
        dummy = ListNode(-1)
        current = dummy  # Pointer to build the new list

        # Traverse both lists and merge them
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1  # Attach list1 node to the merged list
                list1 = list1.next  # Move the list1 pointer
            else:
                current.next = list2  # Attach list2 node to the merged list
                list2 = list2.next  # Move the list2 pointer

            current = current.next  # Move the current pointer

        # If there are remaining nodes in list1, attach them
        if list1:
            current.next = list1
        # If there are remaining nodes in list2, attach them
        if list2:
            current.next = list2

        # Return the merged list starting from dummy.next
        return dummy.next