class Solution:
    def minDeletions(self, s: str) -> int:
        
        freq = sorted([x for x in Counter(s).values()],reverse=True)
        prev = 10**10
        ans = 0
        for i in range(len(freq)):
            if freq[i] >= prev:
                ans += min(freq[i],freq[i]-prev+1)
                freq[i] = max(0,prev-1)
            prev = freq[i]
            
        #print(freq)
        return ans