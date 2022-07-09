class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        n = len(nums)
        q = deque()
        q.append((0,nums[0]))
        cur_val = nums[0]
        for i in range(1,n):
            cur_val = float("-inf")
            while q and q[0][0] < i-k:
                idx, val = q.popleft()
                #cur_val = max(cur_val, val)

            cur_val = q[0][1]
            cur_val += nums[i]
            
            while q and cur_val >= q[-1][1]:
                q.pop()
                
            q.append((i,cur_val))
                
            
        return cur_val