class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        
        mapleJordan, wiggins = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                mapleJordan = wiggins + 1
            if nums[i] < nums[i-1]:
                wiggins = mapleJordan + 1
                
        return max(mapleJordan,wiggins)