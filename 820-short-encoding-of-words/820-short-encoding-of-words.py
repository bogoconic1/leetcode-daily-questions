class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        
        trie = {}
        for word in words:
            word = word[::-1]
            cur = trie
            for x in word:
                if x not in cur:
                    cur[x] = {}
                cur = cur[x]
                
        cur = trie
        #print(trie)
        
        stack = []
        for x in cur:
            stack.append((cur[x],1))
            
        ans = 0
        
        while stack:
            node,dist = stack.pop()
            if node == {}:
                ans += dist+1
            for x in node:
                stack.append((node[x],dist+1))
                
        return ans