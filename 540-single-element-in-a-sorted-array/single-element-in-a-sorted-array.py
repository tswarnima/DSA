class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[n-1] != nums[n-2]:
            return nums[n-1]

        for j in range(1, n-1):
            if nums[j-1] != nums[j] and nums[j] != nums[j+1]:
                return nums[j]