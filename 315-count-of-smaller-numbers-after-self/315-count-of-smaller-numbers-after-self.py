from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums):
        
        order = SortedList()
        res = []
        
        for num in nums[::-1]:
            
            idx = SortedList.bisect_left(order,num)
            res.append(idx)
            order.add(num)
        
        return res[::-1]