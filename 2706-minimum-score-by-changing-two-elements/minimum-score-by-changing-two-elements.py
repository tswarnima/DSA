class Solution:
    def minimizeSum(self, nums: List[int]) -> int:



        nums.sort()
        n = len(nums)

        if n <= 3:
            return 0

        ans = float('inf')

        ans = min(ans, nums[n-1] - nums[2])
        ans = min(ans, nums[n-2] - nums[1])
        ans = min(ans, nums[n-3] - nums[0])

        return ans
