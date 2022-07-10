class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        dp[1] = 0
        
        for i in range(1,n+1):
            if i == 1:
                dp[i] = min(dp[i], nums[i-1] + dp[i-1])
            else:
                dp[i] = min(dp[i], nums[i-1] + dp[i-1], nums[i-2] + dp[i-2])
                
                
        return dp[n]