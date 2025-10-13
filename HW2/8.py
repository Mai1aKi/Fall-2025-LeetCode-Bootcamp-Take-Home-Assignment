class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        # no spaces
        # no letters
        # no special characters except + and -

        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        if s[0] in ('-', '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]
        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)
        num *= sign
        num = max(-2**31, min(num, 2**31 - 1))
        return num
    
sol = Solution()
print(sol.myAtoi("42"))  # Output: 42
print(sol.myAtoi(" -042"))  # Output: -42
print(sol.myAtoi("1337c0d3"))  # Output: 1337
print(sol.myAtoi("0-1"))  # Output: 0
print(sol.myAtoi("words and 987"))  # Output: 0