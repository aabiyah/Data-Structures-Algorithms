# Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

# The steps of the insertion sort algorithm:

  # Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
  # At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
  # It repeats until no input elements remain.
# The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.

class Solution:
  def insertionSortList(self, head):
      """
      :type head: ListNode
      :rtype: ListNode
      """
      # Create a dummy node to serve as the start of the sorted list
      dummy = ListNode(0)
      current = head  # Pointer to traverse the original list

      while current:
          # At each step, extract the next node and insert it into the sorted list
          next_node = current.next  # Save the next node to process after insertion
          prev = dummy  # Start from the dummy node to find the correct position

          # Find the position to insert the current node
          while prev.next and prev.next.val < current.val:
              prev = prev.next

          # Insert current between prev and prev.next
          current.next = prev.next
          prev.next = current

          # Move to the next node in the original list
          current = next_node

      return dummy.next