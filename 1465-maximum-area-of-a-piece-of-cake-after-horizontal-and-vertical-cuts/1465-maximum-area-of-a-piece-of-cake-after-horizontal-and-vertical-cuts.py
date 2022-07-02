class Solution:
    def maxArea(self, h: int, w: int, hori: List[int], vert: List[int]) -> int:
        hori.append(0)
        vert.append(0)
        hori.append(h)
        vert.append(w)
        
        hori.sort()
        vert.sort()
        
        maxH, maxV = 0,0
        for x,y in zip(hori,hori[1:]):
            maxH = max(maxH,y-x)
            
        for x,y in zip(vert,vert[1:]):
            maxV = max(maxV,y-x)
            
        return (maxH * maxV) % 1000000007