class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        pre = [0] + list(accumulate(cardPoints))
        suf = [0] + list(accumulate(cardPoints[::-1]))
        return max(pre[i] + suf[k-i] for i in range(k+1))
            