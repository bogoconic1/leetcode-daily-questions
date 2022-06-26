class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        pre = [0] + list(accumulate(cardPoints))
        suf = [0] + list(accumulate(cardPoints[::-1]))
        ans = 0
        for i in range(k+1):
            ans = max(ans, pre[i] + suf[k-i])
            
        return ans