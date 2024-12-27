# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

  # The town judge trusts nobody.
  # Everybody (except for the town judge) trusts the town judge.
  # There is exactly one person that satisfies properties 1 and 2.
  # You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

class Solution(object):
  def findJudge(self, n, trust):
      """
      :type n: int
      :type trust: List[List[int]]
      :rtype: int
      """
      # If there is only one person, that person is trivially the judge
      if n == 1:
          return 1

      # Initialize in-degree and out-degree arrays
      in_degree = [0] * (n + 1)
      out_degree = [0] * (n + 1)

      # Process each trust relationship
      for a, b in trust:
          out_degree[a] += 1  # a trusts b
          in_degree[b] += 1   # b is trusted by a

      # Find the person who is trusted by everyone but trusts no one
      for i in range(1, n + 1):
          if in_degree[i] == n - 1 and out_degree[i] == 0:
              return i

      return -1Fi