# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x: int) -> int:
      
      s = str(x)
      s = s[::-1]
      if s[len(s)-1] == '-':
        s = '-' + s[0:len(s)-1]
      x = int(s)
      if x > (2 ** 31) or x < (-2**31-1):
        return 0
      return x


s = Solution()
print(s.reverse(123))