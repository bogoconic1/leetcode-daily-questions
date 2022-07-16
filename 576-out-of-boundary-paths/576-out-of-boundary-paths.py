class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        if m == 1 and n == 1:
            return 4
        
        @cache
        def dp(r,c,moves):
            
            if not 0 <= r < m or not 0 <= c < n:
                return 1
            
            ans = 0
            
            if moves > 0:
                for nr, nc in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
                    ans += dp(nr,nc,moves-1) % 1000000007
                    
            return ans % 1000000007
        
        return dp(startRow,startColumn,maxMove) % 1000000007