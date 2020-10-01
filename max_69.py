# https://leetcode.com/problems/maximum-69-number/

class Solution:
  def maximum69Number(self, num):
        return int(str(num).replace('6', '9', 1))

if __name__ == "__main__":

    X = Solution()

    print( X.maximum69Number(9669) )
                