# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

class UnionFind:
  def __init__(self, n):
      self.parent = list(range(n))
      self.rank = [1] * n

  def find(self, x):
      if self.parent[x] != x:
          self.parent[x] = self.find(self.parent[x])  # Path compression
      return self.parent[x]

  def union(self, x, y):
      rootX = self.find(x)
      rootY = self.find(y)

      if rootX != rootY:
          # Union by rank
          if self.rank[rootX] > self.rank[rootY]:
              self.parent[rootY] = rootX
          elif self.rank[rootX] < self.rank[rootY]:
              self.parent[rootX] = rootY
          else:
              self.parent[rootY] = rootX
              self.rank[rootX] += 1
          return True
      return False

class Solution(object):
  def minCostConnectPoints(self, points):
      """
      :type points: List[List[int]]
      :rtype: int
      """
      n = len(points)

      # List to store all edges (distance, point1, point2)
      edges = []

      # Generate all possible edges with Manhattan distance as the weight
      for i in range(n):
          for j in range(i + 1, n):
              dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
              edges.append((dist, i, j))

      # Sort edges by their distance (ascending)
      edges.sort()

      # Kruskal's algorithm with Union-Find to find MST
      uf = UnionFind(n)
      mst_cost = 0
      edges_used = 0

      for dist, u, v in edges:
          if uf.union(u, v):  # If u and v are not connected, connect them
              mst_cost += dist
              edges_used += 1
              if edges_used == n - 1:  # We need exactly n-1 edges to connect all nodes
                  break

      return mst_cost
