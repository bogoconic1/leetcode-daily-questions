class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        if len(nums) <= 2:
            return True
        
        l,r = 0, len(nums)-1
                
        while r > 0:
            if nums[r] >= nums[r-1]:
                r -= 1
            else:
                break
                
        #strictly increasing
        #r = 1 can just modify first element
        if r == 0 or r == 1:
            return True
            
        while l < r-2:
            if nums[l] <= nums[l+1]:
                l += 1
            else:
                break
                
        if l != r-2:
            return False
                
        if nums[l] <= nums[r]:
            return True
        
        if r+1 < len(nums) and nums[l+1] <= nums[r+1] and nums[l] <= nums[l+1]:
            return True
        
        if nums[l] <= nums[l+1] and r == len(nums)-1:
            return True
        
        return False
            