class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        q = []
        for n in nums:
            if len(q) == k:
                #check if n is larger than the top element of the heap
                if n > q[0]:
                    heapq.heappop(q)
                    heapq.heappush(q,n)
                else:
                    continue
            else:
                heapq.heappush(q,n)
                
        return q[0]