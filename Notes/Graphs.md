
# Graphs & Solving LeetCode Questions

## Basics of Graphs:
1. **Definition**: A collection of nodes (vertices) connected by edges.
2. **Types of Graphs**:
   - **Directed Graph**: Edges have a direction.
   - **Undirected Graph**: Edges have no direction.
   - **Weighted Graph**: Edges have weights.
   - **Unweighted Graph**: All edges are equal.
   - **Cyclic Graph**: Contains at least one cycle.
   - **Acyclic Graph**: No cycles (e.g., DAG - Directed Acyclic Graph).
3. **Representation**:
   - **Adjacency Matrix**: `O(V^2)` space, fast lookups.
   - **Adjacency List**: `O(V + E)` space, efficient for sparse graphs.

---

## Steps to Solve Graph Problems:
1. **Understand the Problem**:
   - Identify the graph type (directed/undirected, weighted/unweighted).
   - Determine what needs to be computed (shortest path, traversal, etc.).

2. **Choose a Representation**:
   - Use adjacency list for most problems.
   - Use adjacency matrix for dense graphs.

3. **Pick an Algorithm**:
   - **Traversal**: DFS, BFS.
   - **Shortest Path**: Dijkstra’s, Bellman-Ford, Floyd-Warshall.
   - **Connectivity**: Union-Find, Tarjan’s algorithm.
   - **Cycle Detection**: DFS-based cycle detection.

4. **Write Code**:
   - Use helper functions for modularity (e.g., traversal, path finding).
   - Handle edge cases (e.g., disconnected components, self-loops).

5. **Test**:
   - Test with provided examples.
   - Add edge cases (e.g., empty graph, single node, multiple components).

---

## Common Techniques:
1. **Breadth-First Search (BFS)**:
   - Use a queue to explore nodes level by level.
   - Example: Shortest path in an unweighted graph.

2. **Depth-First Search (DFS)**:
   - Use recursion or a stack to explore as far as possible.
   - Example: Detect cycles in a graph.

3. **Dijkstra's Algorithm**:
   - Use a priority queue to find the shortest path in weighted graphs.

4. **Union-Find**:
   - Use for connectivity problems (e.g., connected components, MST).
   - Example: Kruskal’s algorithm for MST.

5. **Topological Sort**:
   - Order vertices of a DAG using DFS or Kahn’s algorithm.
   - Example: Course schedule problem.

6. **Backtracking**:
   - Explore all paths in the graph.
   - Example: Hamiltonian path, word search.

7. **Dynamic Programming on Graphs**:
   - Use DP for shortest paths in DAGs or solving subproblems.
   - Example: Floyd-Warshall for all-pairs shortest paths.

---

## Example LeetCode Questions:
1. **Clone Graph**:
   - Use BFS or DFS to copy nodes and edges.

2. **Number of Islands**:
   - Use DFS/BFS for connected components in a grid.

3. **Course Schedule**:
   - Use topological sort to check for cycle and ordering.

4. **Shortest Path in Binary Matrix**:
   - Use BFS for unweighted shortest path.

5. **Minimum Spanning Tree**:
   - Use Kruskal’s or Prim’s algorithm.

6. **Network Delay Time**:
   - Use Dijkstra’s algorithm for single-source shortest path.

7. **Word Ladder**:
   - Use BFS to find the shortest transformation sequence.

---

## Tips:
- **Initialization**: Use clear graph representations (list, matrix, dictionary).
- **Edge Cases**: Handle disconnected graphs, cycles, and isolated nodes.
- **Time Complexity**: Analyze based on `O(V + E)` for most algorithms.
- **Debugging**: Visualize the graph structure and traversal order.

---

Master graph problems to excel in traversal, pathfinding, and connectivity challenges!
