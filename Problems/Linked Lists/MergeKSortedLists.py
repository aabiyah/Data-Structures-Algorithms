# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None

        # Min-heap to keep track of the smallest element among the heads of the lists
        heap = []

        # Push the first node of each linked list into the heap
        for i, l in enumerate(lists):
            if l:
                heappush(heap, (l.val, i, l))

        # Dummy node to start the merged list
        dummy = ListNode()
        current = dummy

        while heap:
            # Pop the smallest node from the heap
            val, i, node = heappop(heap)

            # Add it to the merged list
            current.next = node
            current = current.next

            # If there are more nodes in the same list, push the next node into the heap
            if node.next:
                heappush(heap, (node.next.val, i, node.next))

        return dummy.next