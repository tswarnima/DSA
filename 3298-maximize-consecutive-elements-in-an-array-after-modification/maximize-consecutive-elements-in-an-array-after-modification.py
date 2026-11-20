class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:

        nums.sort()

        dp = {}
        ans = 0

        for x in nums:

            # Option 1: Increase x by 1
            if x in dp:
                length = dp[x] + 1
            else:
                length = 1

            if x + 1 in dp:
                if dp[x + 1] < length:
                    dp[x + 1] = length
            else:
                dp[x + 1] = length

            # Option 2: Keep x as it is
            if x - 1 in dp:
                length = dp[x - 1] + 1
            else:
                length = 1

            if x in dp:
                if dp[x] < length:
                    dp[x] = length
            else:
                dp[x] = length

            # Update maximum answer
            if dp[x] > ans:
                ans = dp[x]

            if dp[x + 1] > ans:
                ans = dp[x + 1]

        return ans