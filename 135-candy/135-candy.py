class Solution:
    def candy(self, ratings: List[int]) -> int:
        
        n = len(ratings)
        
        fw = [1]*n
        bw = [1]*n
        res = [1]*n
        
        count = 1
        
        for i in range(1,n):
            
            if ratings[i] > ratings[i-1]:
                count += 1
                fw[i] = count
                
            else:
                count = 1
                
                
        count = 1
                
        for i in range(n-2,-1,-1):
            
            if ratings[i] > ratings[i+1]:
                count += 1
                bw[i] = count
                
            else:
                count = 1
                
        
        for i in range(n):
            res[i] = max(fw[i], bw[i])
            
        return sum(res)