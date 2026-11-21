class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        ans = 0 
        n = len(nums)
        nums.sort()

        for i in range(0,n,2):
            ans+=nums[i]

        return ans    
        
