class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums = set(nums)
        count = 0
        ans = 0
        prev = None
        
        for x in nums:
            if x-1 not in nums:
                prev = x
                count = 1
                
                while prev+1 in nums:
                    count += 1
                    prev += 1
            ans = max(ans,count)
        
        return ans
                    