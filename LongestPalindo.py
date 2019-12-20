# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
  def longestPali(self, s: str, start: int) -> int:
    i = start
    j = i
    lenth = len(s)
    curLen = 1
    while i-1 >= 0 and j+1 < lenth:
      i-=1
      j+=1
      if s[i] == s[j]:
        curLen+=2
      else:
        return curLen
    return curLen

  def longestPaliEven(self, s: str, start: int) -> int:
    i = start
    j = i+1
    lenth = len(s)
    curLen = 0
    while i >= 0 and j < lenth:
      if s[i] == s[j]:
        curLen+=2
      else:
        return curLen
      i-=1
      j+=1
    return curLen

  def longestPalindrome(self, s: str) -> str:
    longestPaliIndex = -1
    longestPaliSize = -1
    if s == "":
      return ""
    for i in range(len(s)):
      
      cursize2 = self.longestPaliEven(s,i)
      if longestPaliSize < cursize2:
        longestPaliSize = cursize2
        longestPaliIndex = i-cursize2//2+1
        print(longestPaliIndex,longestPaliSize,s[longestPaliIndex: longestPaliIndex+longestPaliSize])

      cursize = self.longestPali(s,i)
      if longestPaliSize < cursize:
        longestPaliSize = cursize
        longestPaliIndex = i-cursize//2
        print(longestPaliIndex,longestPaliSize,s[longestPaliIndex: longestPaliIndex+longestPaliSize])
      
    return s[longestPaliIndex: longestPaliIndex+longestPaliSize]
    

      
    
    
s = Solution()
print(s.longestPalindrome("tattarrattat"))