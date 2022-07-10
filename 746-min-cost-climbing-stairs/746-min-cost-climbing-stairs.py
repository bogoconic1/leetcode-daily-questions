class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        
        @cache
        def dp(i):
            
            if i >= len(nums):
                return 0
            
            return nums[i] + min(dp(i+1),dp(i+2))
        
        return min(dp(0),dp(1))