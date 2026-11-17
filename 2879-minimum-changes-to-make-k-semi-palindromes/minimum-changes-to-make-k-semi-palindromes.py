class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # Step 1: Precompute cost of making each substring semi-palindrome
        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                ans = float('inf')

                # Find all proper divisors of length
                for d in range(1, length):
                    if length % d == 0:
                        changes = 0

                        # Compare corresponding characters in each group
                        for r in range(d):
                            left = i + r
                            right = i + r + ((length - 1 - r) // d) * d

                            while left < right:
                                if s[left] != s[right]:
                                    changes += 1

                                left += d
                                right -= d

                        ans = min(ans, changes)

                cost[i][j] = ans

        # Step 2: Dynamic Programming
        dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for parts in range(1, k + 1):
            for j in range(2 * parts, n + 1):
                for p in range(2 * (parts - 1), j - 1):

                    if dp[parts - 1][p] != float('inf'):
                        dp[parts][j] = min(
                            dp[parts][j],
                            dp[parts - 1][p] + cost[p][j - 1]
                        )

        return dp[k][n]