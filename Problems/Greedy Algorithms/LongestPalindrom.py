# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

from collections import Counter

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_counts = Counter(s)
        palindrome_length = 0
        has_odd = False

        for count in char_counts.values():
            if count % 2 == 0:
                palindrome_length += count
            else:
                palindrome_length += count - 1
                has_odd = True

        # Add one for the center character if there's any odd count
        if has_odd:
            palindrome_length += 1

        return palindrome_length