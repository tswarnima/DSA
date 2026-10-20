
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            possible = True
            prev_max = None

            for start in range(0, n, k):
                block = nums[start:start + k]

                drops = 0

                for i in range(k - 1):
                    if block[i] > block[i + 1]:
                        drops += 1

                if block[-1] > block[0]:
                    drops += 1

                if drops > 1:
                    possible = False
                    break

                block_min = min(block)
                block_max = max(block)

                if prev_max is not None and prev_max > block_min:
                    possible = False
                    break

                prev_max = block_max

            if possible:
                ans += k

        return ans
