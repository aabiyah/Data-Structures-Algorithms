# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# For example, the following two linked lists begin to intersect at node c1:
# The test cases are generated such that there are no cycles anywhere in the entire linked structure.

# Note that the linked lists must retain their original structure after the function returns.

# Custom Judge:

# The inputs to the judge are given as follows (your program is not given these inputs):

# intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
# listA - The first linked list.
# listB - The second linked list.
# skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
# skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
# The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

class Solution:
  def getIntersectionNode(self, headA, headB):
      """
      :type headA, headB: ListNode
      :rtype: ListNode
      """
      if not headA or not headB:
          return None

      # Initialize two pointers
      pointerA, pointerB = headA, headB

      # Traverse both lists
      while pointerA != pointerB:
          # Move pointerA and pointerB forward, or switch to the other list's head
          pointerA = pointerA.next if pointerA else headB
          pointerB = pointerB.next if pointerB else headA

      # Either both are None (no intersection) or both meet at the intersection node
      return pointerA
