class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = s.split()
        words.reverse()
        return ' '.join(words)

sol = Solution()
print(sol.reverseWords("the sky is blue"))  # Output: "blue is sky the"
print(sol.reverseWords("  hello world  "))  # Output: "world hello"
print(sol.reverseWords("a good   example"))  # Output: "example good a"
