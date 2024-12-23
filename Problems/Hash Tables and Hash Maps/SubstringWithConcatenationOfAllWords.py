# You are given a string s and an array of strings words. All the strings of words are of the same length.

# A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

# For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
# Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.
    
class Solution(object):
  def findSubstring(self, s, words):
      if not s or not words:
          return []

      word_len = len(words[0])
      num_words = len(words)
      total_len = word_len * num_words

      # Counter for the words in words list
      word_count = Counter(words)

      result = []

      # Iterate through each possible starting index for the window
      for i in range(word_len):
          left = i
          right = i
          current_count = Counter()

          # Slide the window across the string
          while right + word_len <= len(s):
              word = s[right:right + word_len]
              right += word_len

              # If the word is in the words list, include it
              if word in word_count:
                  current_count[word] += 1

                  # If the count of the word exceeds the expected count, shift left pointer
                  while current_count[word] > word_count[word]:
                      current_count[s[left:left + word_len]] -= 1
                      left += word_len

                  # Check if the current window is valid
                  if right - left == total_len:
                      result.append(left)
              else:
                  # If the word is not in the list, reset the window
                  current_count.clear()
                  left = right

      return result
