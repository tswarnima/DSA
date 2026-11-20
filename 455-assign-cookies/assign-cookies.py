class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        
        s.sort()
        g.sort()
        n = len(g)
        m = len(s)
        l , r = 0 , 0
        ans = 0

        while l<n and r<m :
            if g[l] <= s[r] :
                ans += 1 
                l+=1
            r+=1

        return ans 

