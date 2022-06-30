class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums.sort()
        median = nums[n // 2]
        median2 = nums[n // 2 - 1]
        
        ans = 0
        for x in nums:
            ans += abs(x-median)
            
        if n % 2:
            return ans
        
        ans2 = 0
        for x in nums:
            ans2 += abs(x-median2)
            
        return min(ans,ans2)