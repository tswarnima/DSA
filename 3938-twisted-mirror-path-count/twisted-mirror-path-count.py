
class Solution:
    def uniquePaths(self, grid):
        m = len(grid)
        n = len(grid[0])
        mod = 10**9 + 7

        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        right[0][0] = 1

        for i in range(m):
            for j in range(n):

                if grid[i][j] == 0:
                    if j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + right[i][j] + down[i][j]) % mod

                    if i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + right[i][j] + down[i][j]) % mod

                else:
                    if i + 1 < m:
                        down[i + 1][j] = (down[i + 1][j] + right[i][j]) % mod

                    if j + 1 < n:
                        right[i][j + 1] = (right[i][j + 1] + down[i][j]) % mod

        return (right[m - 1][n - 1] + down[m - 1][n - 1]) % mod
