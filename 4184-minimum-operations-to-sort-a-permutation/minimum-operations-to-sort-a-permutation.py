class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def check(arr):
            pos = arr.index(0)

            for i in range(n):
                if arr[(pos + i) % n] != i:
                    return -1

            return pos

        ans = float('inf')

        # Case 1: No reversal, or two reversals
        k = check(nums)
        if k != -1:
            ans = min(ans, k, n - k + 2)

        # Case 2: One reversal
        k = check(nums[::-1])
        if k != -1:
            ans = min(ans, min(k, n - k) + 1)

        return ans if ans != float('inf') else -1      