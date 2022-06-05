class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1,n+1)]
        mp = [False for _ in range(n)]
        ans = []
        
        self.k = k
        def recursion(ds,mp):
            if len(ds) == n:
                self.k -= 1
                if self.k == 0:
                    ans.append(ds.copy())
                    return True
                return False
            for x in range(n):
                if mp[x] == False:
                    mp[x] = True
                    ds.append(nums[x])

                    if recursion(ds,mp):
                        return True

                    mp[x] = False
                    ds.pop()
            return False
        
        recursion([],mp)

        s = ""
        for num in ans[0]:
            s += str(num)
        return s
        