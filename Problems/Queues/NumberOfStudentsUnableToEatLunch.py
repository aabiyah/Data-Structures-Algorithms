# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches.

# The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the ith sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the jth student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.

class Solution(object):
  def countStudents(self, students, sandwiches):
      """
      :type students: List[int]
      :type sandwiches: List[int]
      :rtype: int
      """
      # Count the number of students preferring each type of sandwich
      count0 = students.count(0)
      count1 = students.count(1)

      # Iterate through the sandwiches stack
      for sandwich in sandwiches:
          if sandwich == 0:
              if count0 > 0:
                  count0 -= 1  # Serve a circular sandwich
              else:
                  break  # No more students want circular sandwiches
          else:
              if count1 > 0:
                  count1 -= 1  # Serve a square sandwich
              else:
                  break  # No more students want square sandwiches

      # Remaining students are those who couldn't eat
      return count0 + count1
