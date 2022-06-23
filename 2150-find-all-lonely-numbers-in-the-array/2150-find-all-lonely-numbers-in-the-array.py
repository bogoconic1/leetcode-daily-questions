class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        
        c = Counter(nums)
        ans = []
        for x in nums:
            if x-1 not in c and c[x] == 1 and x+1 not in c:
                ans.append(x)
                
        return ans