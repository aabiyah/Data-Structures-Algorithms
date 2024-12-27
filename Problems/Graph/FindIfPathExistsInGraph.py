# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise

class Solution(object):
  def validPath(self, n, edges, source, destination):
      """
      :type n: int
      :type edges: List[List[int]]
      :type source: int
      :type destination: int
      :rtype: bool
      """
      # Step 1: Build the adjacency list
      graph = [[] for _ in range(n)]
      for u, v in edges:
          graph[u].append(v)
          graph[v].append(u)

      # Step 2: BFS to check if we can reach destination from source
      visited = [False] * n
      queue = deque([source])
      visited[source] = True

      while queue:
          node = queue.popleft()
          if node == destination:
              return True
          for neighbor in graph[node]:
              if not visited[neighbor]:
                  visited[neighbor] = True
                  queue.append(neighbor)

      # If we finish BFS and did not find destination
      return False