class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        sett = set()
        maxx = 0
        while s and r<len(s):
            
    
            while s[r] in sett :
                sett.remove(s[l])
                l+=1

            sett.add(s[r])
            maxx = max(maxx,r-l+1)

            r+=1
        return maxx