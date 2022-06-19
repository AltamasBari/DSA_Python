class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans = []
        
        products = sorted(products)
        
        prefix = ""
        for ch in searchWord:
            prefix += ch
            temp = []
            for product in products:
                if product.startswith(prefix) and len(temp) < 3:
                    temp.append(product)
                if len(temp) == 3:
                    break
            ans.append(temp)
        
        return ans