
class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        arr = []

        for i in range(m):
            row = []

            for j in range(n):
                if i == 0 or j == n - 1:
                    row.append('.')
                else:
                    row.append('#')

            arr.append(''.join(row))

        return arr
