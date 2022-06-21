class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        def check(mid):
            
            brem, lrem = bricks, ladders

            canTake = heights[:mid+1]
            diff = sorted([y-x for x,y in zip(canTake,canTake[1:])])
            for x in diff:
                if x <= 0:
                    continue
                elif brem >= x:
                    brem -= x
                else:
                    if lrem == 0:
                        return False
                    lrem -= 1
                    
            return True
        
        
        l,r = 0, len(heights)-1
        while l < r:
            mid = l+r >> 1
            if check(mid):
                l = mid+1
            else:
                r = mid
                
        if check(l):
            return l
        return l-1