class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        c = 0
        i = 0
        while c<len(g) and i<len(s):
            if g[c]<=s[i]:
                c += 1
            i+=1
        return c
                       
