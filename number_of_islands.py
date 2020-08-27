# https://leetcode.com/problems/number-of-islands/
# Using DFS (DFS uses recursion here)

class Solution:
    def isValid(self, A, row, col):
        if row < 0 or row >= len(A) or col < 0 or col >= len(A[0]):
            return False
        return True

    def dfs(self, A, i, j, vis):
        vis[i][j] = True

        row = [-1, 0, 1, 0]
        col = [0, -1, 0, 1]

        for r, c in zip(row, col):
            nRow = i + r
            nCol = j + c

            if self.isValid(A, nRow, nCol) and A[nRow][nCol] == '1' and not vis[nRow][nCol]:
                vis[nRow][nCol] = True
                self.dfs(A, nRow, nCol, vis)

    def numIslands(self,A):
        if not A: return 0
        m = len(A)
        n = len(A[0])
        vis = [[False] * n for _ in range(m)]

        count = 0
        for i in range(m):
            for j in range(n):
                if not vis[i][j] and A[i][j] == '1':
                    self.dfs(A,i,j,vis)
                    count += 1

        return count
    

if __name__ == "__main__":
    x = Solution()
    print( x.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]) ) # should be 1