class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        q = []
        
        for i,(x,y) in enumerate(zip(heights,heights[1:])):
            
            d = y-x
            if d > 0:
                heappush(q,d)
                
            if len(q) > ladders:
                bricks -= heappop(q)
                if bricks < 0:
                    return i
                
        return len(heights)-1