class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        dp = [0] * (budget + 1)

        mn = float('inf')

        for factor, price in items:

            mn = min(mn, price)

            cnt = 0

            for f, p in items:
                if f % factor == 0:
                    cnt += 1

            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + cnt)

        ans = 0

        for i in range(budget + 1):
            ans = max(ans, dp[i] + (budget - i) // mn)

        return ans