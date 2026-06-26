class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        r = 0
        maxx = 0
        d = {}

        while r<len(fruits):
            d[fruits[r]] = d.get(fruits[r],0)+1

            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]]==0:
                    del d[fruits[l]]
                l+=1

            r+=1
            maxx = max(maxx,r-l)

        return maxx
            