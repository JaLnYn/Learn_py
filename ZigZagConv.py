# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution:
    def convert(self, s: str, numRows: int) -> str:
      if(numRows == 1):
        return s
      middleRows = numRows - 2
      sectionSize = 2 + middleRows*2
      i = 0
      zigzag=""
      #first add all the toprows
      while i*sectionSize < len(s):
        zigzag += s[i*sectionSize]
        i+=1
      #next do the middle rows
      curRow=0
      while curRow < middleRows:
        i=0
        while i*sectionSize+1+curRow < len(s):
          zigzag += s[i*sectionSize+1+curRow]
          if i*sectionSize+sectionSize-1-curRow < len(s):
            zigzag += s[i*sectionSize+sectionSize-1-curRow]
          
          i += 1
        curRow+=1
      i=0
      while (i)*sectionSize+sectionSize//2 < len(s):#bottom row
        zigzag += s[(i)*sectionSize+sectionSize//2]
        i+=1
      

      return zigzag

s = Solution()
print(s.convert("PAYPALISHIRING",3))
print(s.convert("PAYPALISHIRING",4))