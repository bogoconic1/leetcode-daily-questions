class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        products.sort()
        res = []
        
        search = ""
        for x in searchWord:
            search += x
            idx_left = bisect_left(products,search)
            idx_right = bisect_right(products,search+"{")
            rg = idx_right-idx_left
            if rg > 3:
                rg = 3
            res.append(products[idx_left:idx_left+rg])
            
        return res