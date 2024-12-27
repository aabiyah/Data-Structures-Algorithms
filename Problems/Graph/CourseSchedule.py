# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

class Solution(object):
  def canFinish(self, numCourses, prerequisites):
      """
      :type numCourses: int
      :type prerequisites: List[List[int]]
      :rtype: bool
      """
      # Step 1: Build the graph (adjacency list)
      graph = {i: [] for i in range(numCourses)}
      for course, prereq in prerequisites:
          graph[course].append(prereq)

      # Step 2: Create a visited array to track state of each course
      visited = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = visited

      # Step 3: Define the DFS function to detect cycles
      def dfs(course):
          if visited[course] == 1:  # Cycle detected
              return False
          if visited[course] == 2:  # Already visited, no cycle
              return True

          # Mark the course as currently visiting
          visited[course] = 1

          # Visit all prerequisites (neighbors)
          for prereq in graph[course]:
              if not dfs(prereq):
                  return False

          # Mark the course as completely visited
          visited[course] = 2
          return True

      # Step 4: Perform DFS for each course
      for course in range(numCourses):
          if visited[course] == 0:  # Unvisited
              if not dfs(course):
                  return False

      # If no cycles are detected, return True
      return True