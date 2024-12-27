# Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

# Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

class Solution:
  def findContentChildren(self, g, s):
      """
      :type g: List[int]  # greed factors of children
      :type s: List[int]  # sizes of the cookies
      :rtype: int
      """
      # Sort the greed factors and cookie sizes
      g.sort()
      s.sort()

      # Initialize pointers for greed factors and cookies
      i, j = 0, 0
      content_children = 0

      # Iterate through both the greed factors and the cookies
      while i < len(g) and j < len(s):
          # If the current cookie can satisfy the current child's greed
          if s[j] >= g[i]:
              content_children += 1
              i += 1  # move to the next child
          # Move to the next cookie regardless
          j += 1

      return content_children